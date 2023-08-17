from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    user_profile_avatar_css = "img.cursor-pointer"

    def presence_of_user_icon_avatar(self):
        wait = WebDriverWait(self.driver, 7, poll_frequency=1)
        e1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.user_profile_avatar_css)))
        print(e1.is_displayed())
        return e1.is_displayed()

    def get_current_url(self):
        return self.driver.current_url
