LINKEDIN_URL = 'https://www.linkedin.com/login'
NAUKRI_URL = "https://www.naukri.com/"

USERNAME = "harshal.shinde1075@gmail.com"
PASSWORD = "Harsh@555"

JOB_SEARCH_TITLES = 'SDET, python test automation, Software testing, Automation testing, software developer engineer in test, python automation test engineer, '
JOB_SEARCH_LOCATIONS = 'Pune, Bengaluru, Indore, India, Hyderabad, '

LINKEDIN_JOB_SEARCH_TITLES = 'SDET'
LINKEDIN_JOB_SEARCH_LOCATIONS = 'India'

USER_FULL_NAME = "Harshal Suryakant Shinde"

YEARS_OF_EXPERIENCE_IN_CORE = '4'
YEARS_OF_EXPERIENCE_IN_NON_CORE = '2'

EXPECTED_CTC = '15 LPA'
CURRENT_CTC = '7 LPA'
EXPECTED_CTC_FULL_NUMERIC = '1500000'
CURRENT_CTC_FULL_NUMERIC = '700000'

EXPECTED_CTC_NUMERIC = '15'
CURRENT_CTC_NUMERIC = '7'

ANSWER_YES = 'YES'
ANSWER_NO = 'NO'
ANSWER_NOT_APPLICABLE = 'NA'
ANSWER_ALL = 'ALL'

PROGRAMMING_LANGUAGE = 'Python'

FIRST_NAME = 'Harshal'
LAST_NAME = 'Shinde'
DATE_OF_BIRTH = '29/12/1998'
GENDER = 'Male'
COUNTRY_CODE = '+91'

CURRENT_LOCATION = 'Bengaluru, Karnataka, India'
CURRENT_LOCATION_IS_BANGALORE = 'Currently staying in bengaluru'
NOTICE_PERIOD = 'Immediately Available'

ROLE_CATEGORY_SECTION = 'Quality Assurance and Testing'  ## Dev 'Software Development'

question_answer_map = {
    "How many years of experience do you have in test engineering?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of work experience do you have with VectorCAST?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of work experience do you have with Karate?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of work experience do you have with Jira?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "What is your current annual compensation?": CURRENT_CTC,
    "How many years of work experience do you have with Java 8+?": ANSWER_YES,
    "Your ECTC ?": EXPECTED_CTC,
    "What is your expected CTC from Airtel?": EXPECTED_CTC,
    "Have you received any mail for Recruit.AI@ltts.com ?": ANSWER_NO,
    "Hi Harshal, companies value diversity and want to build inclusive teams. Share your career status to proceed with this job application. Are you on a career break?": ANSWER_NO,
    "How many years of experience do you have in Storage?":YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "We are committed to Thriving Together! Are you able to work in the office at least twice a week?": ANSWER_YES,
    "How many years of work experience do you have with Automation Testing?": YEARS_OF_EXPERIENCE_IN_CORE,
    "Please share your Annual Expected Compensation in INR": EXPECTED_CTC_FULL_NUMERIC,
    "What is your Expected CTC?": EXPECTED_CTC_FULL_NUMERIC,
    "How many years of work experience do you have with REST / SOAP services, KAFKA / MQ event-based applications": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of work experience do you have with JUnit?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of work experience do you have with data validation and analysis?": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your Notice Period ?": NOTICE_PERIOD,
    "How many years of experience do you have with Selenium with Java?": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your total years of experience": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Rest Assured Framework?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of work experience do you have with Playwright?": YEARS_OF_EXPERIENCE_IN_CORE,
    "Years of experience in software testing?": YEARS_OF_EXPERIENCE_IN_CORE,
    "Do you have hands-on experience with Robot Framework?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "ow many years of experience do you have in Robot?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "Have you ever worked on CI/CD pipelines?": ANSWER_YES,
    "What types of testing have you performed (e.g., functional, regression, smoke)?": ANSWER_ALL,
    "Have you ever used Git or any version control systems?": ANSWER_YES,
    "Are you comfortable writing test cases from scratch?": ANSWER_YES,
    "Do you have experience with API testing?": ANSWER_YES,
    "Have you used any cloud-based testing tools or platforms?": ANSWER_YES,
    "Are you familiar with any test management tools like JIRA, TestRail, or Zephyr?": ANSWER_YES,
    "Can you write scripts in any programming language? If so, which ones?": PROGRAMMING_LANGUAGE,
    "Have you worked in an Agile environment?": ANSWER_YES,
    "Do you have experience in mobile testing (Android/iOS)?": ANSWER_YES,
    "Are you familiar with any performance testing tools?": ANSWER_YES,
    "Have you ever contributed to framework development or enhancement?": ANSWER_YES,
    "How many years of work experience in Appium testing": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How much experience do you have with automation frameworks?": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your current CTC?": CURRENT_CTC,
    "What is your current CTC? (Fixed + Variable)": CURRENT_CTC,
    "What is your overall years of experience?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of work experience do you have with Functional Testing?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of Investment Banking experience do you currently have?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "What is your Experience in C#": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many Years of Experience you have with Cypress E2E?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "What is your exp in automation testing ?": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your notice period ?": NOTICE_PERIOD,
    "How many days notice period you have ?": NOTICE_PERIOD,
    "How many years of experience do you have in software testing?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have with SQL?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of work experience do you have with QA Engineering?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Selenium and Selenium WebDriver": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your Total year of Experience": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in QA?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in QA Automation?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of work experience do you have with Appium?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "What are your years of experience?": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your official notice period ?": NOTICE_PERIOD,
    "Location (city)": CURRENT_LOCATION,
    "How many years of experience do you have as an Python Automation Engineer?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of work experience do you have with Cypress/javascript/playwright? MUST REFLECT IN RESUME.": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of work experience do you have with VBScript?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of Information Technology and Services experience do you currently have?": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your current annual salary in INR?": CURRENT_CTC_FULL_NUMERIC,
    "How many years of work experience do you have with AWS Lambda?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "What is your expected CTC salary in Lakh Per Annum (that will have PF and TDS deductions)?": EXPECTED_CTC_NUMERIC,
    "How many years of work experience do you have with Embedded Systems?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in Robot Framework?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in GitLab?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in AWS?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of work experience do you have with Python (Programming Language)?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Android Testing?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in Mainframe Testing?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in Java?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in python automation?": YEARS_OF_EXPERIENCE_IN_CORE,
    "Total Experience?": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your Total years of experience?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience you have in quality engineering": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you with Quality Assurance?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Rest Assured?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in embedded software development and testing for aerospace products?": YEARS_OF_EXPERIENCE_IN_CORE,
    "Notice Period (In Days)": NOTICE_PERIOD,
    "What is your notice period? How soon can you take up this role ?": NOTICE_PERIOD,
    "How many years of experience do you have in Java Selenium?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in cypress?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have working in the aerospace domain?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have as a Software Tester?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Mainframes?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in Ui Automation?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in playwright?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Automation?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Selenium?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience you have in API?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Automation Test Framework?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience you have Postman?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience you have in Selenium?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Api Automation?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of exp in python coding": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Manual Testing?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Salesforce Testing?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in Selenium Automation?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of experience do you have in Javascript?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "What is your last working day?": NOTICE_PERIOD,
    "How many years of experience do you have in Python?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of Exp in Automation Python testing?": YEARS_OF_EXPERIENCE_IN_CORE,
    "How many years of total experience you have?": YEARS_OF_EXPERIENCE_IN_CORE,
    "What is your expected CTC in Lakhs per annum?": EXPECTED_CTC,
    "Please confirm your availability for Virtual interview on 17th May 2025?": ANSWER_YES,
    "Current CTC": CURRENT_CTC,
    "How many years of experience do you have in Application Engineering?": YEARS_OF_EXPERIENCE_IN_CORE,
    "Are you open to work on contract?": ANSWER_YES,
    "Are you currently residing in Hyderabad, Telangana or willing to relocate to Hyderabad, Telangana?": ANSWER_YES,
    "Are you currently residing in Ahmedabad or willing to relocate to Ahmedabad?": ANSWER_YES,
    "do you have good experience in python?": ANSWER_YES,
    "Are you open to work in 10:00 AM To 07:00 PM for this job?": ANSWER_YES,
    "Are you willing to relocate to Pune to work in Hybrid mode on direct payroll with my client ?": ANSWER_YES,
    "Are you currently residing in Bengaluru or willing to relocate to Bengaluru?": ANSWER_YES,
    "This is a work from office opportunity. Are you willing to work full-time out of our office in Hebbal, Bangalore?": ANSWER_YES,
    "Do you have PF in your current company?": ANSWER_YES,
    "Are you currently residing in Hyderabad or willing to relocate to Hyderabad?": ANSWER_YES,
    "Are you currently residing in Gurugram, Haryana or willing to relocate to Gurugram, Haryana?": ANSWER_YES,
    "Are you willing to work 4 days a week from Office?": ANSWER_YES,
    "Are you ready to work on C2H Role?": ANSWER_YES,
    "Are you okay to relocate to bangalore": CURRENT_LOCATION_IS_BANGALORE,
    "How Many Years of exp you have in Data Engineering?": YEARS_OF_EXPERIENCE_IN_CORE,
    "Expected CTC (Numeric Input Only)": EXPECTED_CTC_FULL_NUMERIC,
    "Expected CTC (Numeric Inputs Only)": EXPECTED_CTC_FULL_NUMERIC,
    "What is your expected annual CTC in INR ?": EXPECTED_CTC_FULL_NUMERIC,
    "Current CTC (Numeric Input Only)": CURRENT_CTC_FULL_NUMERIC,
    "Current CTC (Numeric Inputs Only)": CURRENT_CTC_FULL_NUMERIC,
    "What is your expected CTC per annum in lakhs? (Mention Only Number) (For e.g. 10)": EXPECTED_CTC_NUMERIC,
    "What is your expected cost to company? (Please mention in LPA)": EXPECTED_CTC_NUMERIC,
    "What is your current CTC per annum in lakhs? (Mention Only Number) (For e.g. 10)": CURRENT_CTC_NUMERIC,
    "What is your current CTC in LPA?": CURRENT_CTC_NUMERIC,
    "What is your current cost to company? (Please mention in LPA)": CURRENT_CTC_NUMERIC,
    "What is your current CTC in Lakhs per annum?": CURRENT_CTC_NUMERIC,
    "What is your current annual CTC in INR ?": CURRENT_CTC_FULL_NUMERIC,
    "Notice Period": NOTICE_PERIOD,
    "What is your notice period?": NOTICE_PERIOD,
    "What is your current Notice Period?": NOTICE_PERIOD,
    "First Name": FIRST_NAME,
    "Date of Birth": DATE_OF_BIRTH,
    "Gender": GENDER,
    "Country Code": COUNTRY_CODE,
    "Last Name": LAST_NAME,
    "Current Location": CURRENT_LOCATION,
    "Preferred Location": CURRENT_LOCATION,
    "How many years of Experience do you have in ETL resting?": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many years of experience do you have in Mobile Testing?  ": YEARS_OF_EXPERIENCE_IN_NON_CORE,
    "How many relevant years of experience into Python development?": YEARS_OF_EXPERIENCE_IN_NON_CORE
}
