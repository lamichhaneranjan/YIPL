from selenium.webdriver.common.by import  By
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()
    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_css_selector"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        return element

        def click_on_element(self, locator_type, locator_value):
            element = self.get_element(locator_type, locator_value)
            element.click()

    def type_into_element(self, locator_type, locator_value, text_to_be_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_be_entered)

    def verify_page_url(self, expected_url):
        time.sleep(2)
        return self.driver.current_url.__contains__(expected_url)

    def verify_alert_message(self, expected_message):
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            # Switch to the alert
            alert_text = alert.text
            print("Alert text:", alert_text)
        except:
            print("Alert did not appear within the timeout.")
        return alert_text.__contains__(expected_message)