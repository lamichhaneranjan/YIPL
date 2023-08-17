from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
@pytest.mark.usefixtures("setup_and_teardown")
class TestForgotPassword:
    def test_forgot_password_link_visible(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://npbmis-stage.yipl.com.np/login")
        wait = WebDriverWait(driver, 5, poll_frequency=2)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.whitespace-nowrap")))
        print(element)
        assert element.is_displayed()

    def test_forgot_password_link_redirecting(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://npbmis-stage.yipl.com.np/login")
        wait = WebDriverWait(driver, 7, poll_frequency=1)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.whitespace-nowrap")))
        element.click()
        time.sleep(2)
        assert "Forgot Password | NPBMIS" in driver.title
