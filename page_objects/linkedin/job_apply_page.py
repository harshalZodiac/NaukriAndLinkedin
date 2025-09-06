from tests.to_skip_job_titles import skip_titles
from utils.helpers import save_external_link
from playwright.sync_api import Page
from config.locators_linkedin import *
import settings
import time


class LinkedinJobApplyPage:
    def __init__(self, page:Page):
        self.page = page
        self.job_apply_section = LinkedInJobSearchLocators.JOB_SECTION
        self.job_search_input = LinkedInJobSearchLocators.JOB_SEARCH_INPUT
        self.job_section_side_bar = LinkedInJobSearchLocators.JOB_SECTION_SIDE_BAR
        self.date_posted_filter = LinkedInJobSearchLocators.DATE_POSTED_FILTER_OPTIONS
        self.date_posted_last_one_day = LinkedInJobSearchLocators.DATE_POSTED_LAST_ONE_DAY
        self.easy_apply_filter = LinkedInJobSearchLocators.EASY_APPLY_FILTER
        self.apply_date_filter = LinkedInJobSearchLocators.APPLY_DATE_POSTED_FILTER
        self.linkedin_job_post = LinkedInApplicationLocators.JOB_POST
        self.linkedin_job_apply = LinkedInApplicationLocators.APPLY_BUTTON
        self.linkedin_external_job_apply = LinkedInApplicationLocators.EXTERNAL_APPLY_BUTTON
        self.limit_exceeded = LinkedInApplicationLocators.LIMIT_EXCEEDED
        self.next_button = LinkedInApplicationLocators.NEXT_BUTTON
        self.review_button = LinkedInApplicationLocators.REVIEW_BUTTON
        self.mandatory_not_filled_error = LinkedInApplicationLocators.MANDATORY_NOT_FILLED_ERROR
        self.submit_application_button = LinkedInApplicationLocators.SUBMIT_APPLICATION
        self.close_application_process = LinkedInApplicationLocators.CLOSE_APPLICATION
        self.done_with_application = LinkedInApplicationLocators.DONE_WITH_APPLICATION
        self.save_application = LinkedInApplicationLocators.SAVE_JOB
        self.already_applied = LinkedInApplicationLocators.ALREADY_APPLIED
        self.terms_and_conditions = LinkedInApplicationLocators.TERMS_AND_CONDITIONS
        self.pagination = LinkedInApplicationLocators.PAGINATION
        self.job_title = LinkedInApplicationLocators.JOB_TITLE

    def navigate_to_job_section(self):
        self.page.locator(self.job_apply_section).click()

    def provide_job_search_input(self):
        self.page.locator('//span[text()="My jobs"]').first.wait_for(state="visible")
        job_search_bar= self.page.locator(self.job_search_input).first
        job_search_bar.wait_for(state="visible")
        job_search_bar.fill(settings.LINKEDIN_JOB_SEARCH_INPUT)
        self.page.keyboard.press("Enter")

    def apply_filter_date_posted(self):
        self.page.locator(self.date_posted_filter).wait_for(state="visible")
        self.page.locator(self.date_posted_filter).click()
        self.page.locator(self.date_posted_last_one_day).click()
        self.page.locator(self.apply_date_filter).first.click()

    def apply_filter_easy_apply(self):
        self.page.locator(self.easy_apply_filter).wait_for(state="visible")
        self.page.locator(self.easy_apply_filter).click()

    def apply_linkedin_jobs(self, job_post):
        try:
            self.page.locator(self.linkedin_job_post).nth(job_post).wait_for(state="visible", timeout=5000)
        except Exception as e:
            print(f"[Warning] Job post #{job_post} not visible or blocked: {e}")
            try:
                self.page.mouse.click(0, 0)
                self.page.keyboard.press("Escape")
                time.sleep(1)
            except Exception as e:
                print(f" Need to update this statement {e}")
            return

        self.page.locator(self.linkedin_job_post).nth(job_post).click()
        time.sleep(2)

        job_title_element = self.page.locator(self.job_title).first
        if job_title_element.is_visible():
            job_title = job_title_element.inner_text().strip()
            print(f"[Info] Job Title: {job_title}")

            if job_title in skip_titles:
                print(f"[Info] Skipping job: {job_title}")
                return

        if self.page.locator(self.linkedin_external_job_apply).first.is_visible():
            with self.page.context.expect_page() as new_page_info:
                self.page.locator(self.linkedin_external_job_apply).first.click()

            new_tab = new_page_info.value
            external_url = new_tab.url

            if external_url:
                save_external_link(external_url, "linkedin_external_links.txt")
            new_tab.close()
            return

        if self.page.locator(self.limit_exceeded).first.is_visible():
            return

        if self.page.locator(self.linkedin_job_apply).first.is_visible():
            self.page.locator(self.linkedin_job_apply).first.click()

        if self.page.locator(self.already_applied).first.is_visible():
            self.page.locator(self.already_applied).first.click()
            return


        time.sleep(1.5)
        while True:
            try:
                if self.page.locator(self.review_button).is_visible():
                    self.page.locator(self.review_button).click()
                    time.sleep(2)
                if self.page.locator(self.terms_and_conditions).is_visible():
                    self.page.locator(self.terms_and_conditions).click()
                    time.sleep(2)
                if self.page.locator(self.submit_application_button).is_visible():
                    self.page.locator(self.submit_application_button).click()
                    time.sleep(2)
                    self.page.locator(self.done_with_application).wait_for(state="visible")
                    self.page.locator(self.done_with_application).first.click()
                    break

                error_icons_locators = self.page.locator(self.mandatory_not_filled_error)
                error_icons_count = error_icons_locators.count()
                if error_icons_count > 0:
                    unmapped_questions = []
                    for i in range(error_icons_count):
                        icon = error_icons_locators.nth(i)
                        container = icon.locator("xpath=ancestor::div[contains(@class, 'fb-dash-form-element')]")

                        label = container.locator("label").first  # pick the first label safely
                        input_field = container.locator("input, textarea").first

                        if not label.is_visible() or not input_field.is_visible():
                            continue

                        question = label.inner_text().strip()
                        answer = settings.question_answer_map.get(question)

                        if answer:
                            input_field.fill(answer)

                        elif "location (city)" in question.lower():
                            location_value = "Bengaluru, Karnataka, India"
                            input_field.fill(location_value)
                            time.sleep(1)
                            self.page.keyboard.press("Enter")
                            time.sleep(1)

                        else:
                            unmapped_questions.append(question)

                    if unmapped_questions:
                        for q in unmapped_questions:
                            print(f"[Unmapped Question]: {q}")
                        self.page.locator(self.close_application_process).first.click()
                        time.sleep(1)
                        self.page.locator(self.save_application).first.click()
                        return

                elif self.page.locator(self.next_button).count() > 0:
                    next_btn = self.page.locator(self.next_button).first
                    next_btn.wait_for(state="visible")
                    if next_btn.is_enabled():
                        next_btn.click()
                        time.sleep(1.5)
            except Exception as e:
                print(f"[Error] Exception during application process: {e}")
                break

    def change_page(self, page_no):
        self.page.locator(self.pagination.format(page_number=page_no)).wait_for(state="visible")
        self.page.locator(self.pagination.format(page_number=page_no)).click()


