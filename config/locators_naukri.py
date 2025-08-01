class NaukriLoginLocators:
    LOGIN_BUTTON = '[id="login_Layer"]'
    USERNAME_INPUT = '[placeholder="Enter your active Email ID / Username"]'
    PASSWORD_INPUT = '[placeholder="Enter your password"]'
    SUBMIT_BUTTON = '//button[@type="submit" and text()="Login"]'


class NaukriProfileLocators:
    VIEW_PROFILE = '//div[@class="view-profile-wrapper"]/a'
    PROFILE_NAME = '//span[@class="fullname"]'
    PROFILE_PERCENTAGE_VALUE = '//div[contains(@class, "user-percentage")]'
    EDIT_GENERAL_PROFILE = '//em[@class="icon edit " and text()="editOneTheme"]'
    SAVE_GENERAL_PROFILE_SECTION = '[id="saveBasicDetailsBtn"]'
    LAST_UPDATED_PROFILE_TODAY = '//span[text()="Today"]'


class NaukriJobSearchLocators:
    JOB_SEARCH_START = '//span[text()="Search jobs here"]'
    JOB_SEARCH_KEYWORD = '[placeholder="Enter keyword / designation / companies"]'
    JOB_SEARCH_LOCATION = '[placeholder="Enter location"]'
    JOB_SEARCH_EXPERIENCE = '[id="experienceDD"]'
    YEARS_OF_EXPERIENCE = '//span[text()="{total_years_of_experience} years"]'
    ROLE_CATEGORY = '//div[contains(@class, "swiper-wrapper")]//label[@for="chk-{role_category}-glbl_qcrc-expanded"]'
    ROLE_CATEGORY_VIEW_MORE  = '//span[text()="Role category"]/ancestor::div[@data-type="checkbox"]//a[contains(@class, "read-more-link")]'
    APPLY_ROLE_CATEGORY_FILTER = '//div[text()="Apply"]'
    B_TECH_EDUCATION = '//span[text()="B.Tech/B.E."]'
    ANY_GRADUATION_EDUCATION = '//span[text()="Any Graduate"]'
    SEARCH_BUTTON = '//span[text()="Search"]'
    FILTER_FRESHNESS = '#filter-freshness'
    FILTER_FRESHNESS_LAST_1_DAY = '//span[text()="Last 1 day"]'
    FILTER_FRESHNESS_LAST_3_DAYS = '//span[text()="Last 3 days"]'
    NO_OF_JOBS = '#jobs-list-header .styles_count-string__DlPaZ'
    APPLIED_FILTERS = '//a[contains(@class, "styles_appliedTxt__UmIjs") and normalize-space(.)="Applied ({number_of_filters_applied})"]'


class NaukriJobApplicationLocators:
    JOB_POSTS = '[class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]'
    APPLY_ON_COMPANY_SITE_BUTTON = '[id="company-site-button"]'
    NAUKRI_INTERNAL_APPLY_BUTTON = '//button[@id="apply-button"]'
    JOB_ALREADY_APPLIED = '[id="already-applied"]'
    JOB_APPLY_PAGINATION = 'div.styles_pages__v1rAK a'
    JOB_APPLY_SUCCESS = '[class="apply-message"]'
    I_AM_INTERESTED = '[id="walkin-button"]'
    ANSWER_PLACEHOLDER = 'div.textArea[contenteditable="true"]'
    QUESTION_PLACEHOLDER = 'li.botItem .botMsg.msg span'
    RADIO_BUTTON_ANSWER = '[name="radio-button"]'
    RADIO_OPTION_SELECTION = '//label[text()="{answer_value}"]'
    SAVE_BUTTON = '//div[@class="sendMsg" and text()="Save"]'
    RADIO_OPTIONS = '.ssrc__radio-btn-container label'
