from page_objects.linkedin.job_apply_page import LinkedinJobApplyPage
from page_objects.linkedin.profile_page import LinkedinProfilePage
from page_objects.linkedin.login_page import LinkedinLoginPage
import time


class TestLinkedinApply:

    def test_linkedin_profile_random_edit(self, browser_page):
        linkedin_login_page = LinkedinLoginPage(browser_page)
        linkedin_profile_page = LinkedinProfilePage(browser_page)

        linkedin_login_page.login_to_linkedin_application()
        linkedin_profile_page.view_linkedin_profile()
        linkedin_profile_page.edit_linkedin_profile()
        time.sleep(5)

    def test_linkedin_job_apply(self, browser_page):
        linkedin_login_page = LinkedinLoginPage(browser_page)
        linkedin_profile_page = LinkedinProfilePage(browser_page)
        linkedin_apply_page = LinkedinJobApplyPage(browser_page)

        linkedin_login_page.login_to_linkedin_application()
        linkedin_profile_page.view_linkedin_profile()
        linkedin_apply_page.navigate_to_job_section()
        linkedin_apply_page.provide_job_search_input()
        linkedin_apply_page.apply_filter_date_posted()
        linkedin_apply_page.apply_filter_easy_apply()
        for page in range(1, 21):
            linkedin_apply_page.change_page(page)
            for job in range(25):
                linkedin_apply_page.apply_linkedin_jobs(job)
            time.sleep(5)
