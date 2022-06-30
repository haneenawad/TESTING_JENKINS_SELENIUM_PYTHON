import time
import warnings
from threading import Thread

import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():

    dc = {
        "browserName": "chrome",
        "platformName": "Windows 10"
    }

    # selenium grid standAlone
    driver = webdriver.Remote("http://localhost:4444",dc)

    yield driver
    driver.close()

def test_google_page_title(driver):
    driver.get('https://www.google.com')
    title = driver.title
    assert title == str.title("google")

def test_youtube_page_title(driver):
    driver.get('https://www.youtube.com')
    title = driver.title
    assert title == "Home - YouTube"

def test_addition_of_2_and_5_simple(driver):
    driver.get('https://www.google.com')
    # css_selector, xpath
    search_field = driver.find_element(By.NAME, "q")
    search_field.click()
    search_field.send_keys("2 + 5")
    search_field.send_keys(Keys.ENTER)

    ans_selector = "#cwos"

    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,ans_selector)))
    # actual_field = driver.find_element(By.CSS_SELECTOR,ans_selector)

    actual_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ans_selector)))

    assert actual_field.text == str(7)

