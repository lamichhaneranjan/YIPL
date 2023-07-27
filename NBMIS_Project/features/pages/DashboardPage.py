class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    user_xpath = "//a[contains(text(),'प्रयोगकर्ता')]"
    agency_xpath = "//a[contains(text(),'कार्यालय')]"
    profile_icon_xpath="//div[@class='ant-dropdown-trigger']"
    logout_xpath="//span[normalize-space()='Logout']"
    profile_link_xpath="//span[normalize-space()='Logout']"
    search_field_xpath="//input[contains(@placeholder,'प्रोजेक्ट आईडी वा प्रोजेक्ट शीर्षक वा बजेट कोड टाइप गरेर खोज्नुहोस् ...')]"
    search_field_button_xpath="//span[contains(text(),'खोजी गर्नुहोस्')]"
    project_development_xpath="//li[normalize-space()='Project Development']"
    detailed_project_report_xpath="//li[normalize - space() = 'Detailed Project Report']"
    project_readiness_xpath="//li[normalize-space()='Project Readiness']"
    passed_project_xpath="//li[normalize-space()='Passed Projects']"
    first_project_details_xpath="//body[1]/div[1]/main[1]/main[1]/div[1]/main[1]/section[3]/div[3]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/a[1]/span[2]"
    first_project_edit_xpath="//body[1]/div[1]/main[1]/main[1]/div[1]/main[1]/section[3]/div[3]/table[1]/tbody[1]/tr[1]/td[4]/div[2]/div[1]/a[1]/span[2]"
    first_project_evaluation_xpath="//body[1]/div[1]/main[1]/main[1]/div[1]/main[1]/section[3]/div[3]/table[1]/tbody[1]/tr[1]/td[4]/div[3]/div[1]/a[1]/span[2]"
    first_page_button_xpath="//div[normalize-space()='first']"
    second_page_button_xpath="//a[normalize-space()='2']"
    next_page_button_xpath="//a[normalize-space()='Next']"
    last_page_button_xpath="//div[normalize-space()='last']"