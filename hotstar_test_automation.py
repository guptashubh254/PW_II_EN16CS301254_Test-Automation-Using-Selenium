# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
path=""
try:
    driver = webdriver.Chrome(path)
    driver.get("https://www.hotstar.com")
    driver.set_window_size(1382, 744)
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .nav-link > div").click()
    element = driver.find_element(By.LINK_TEXT, "Sports")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 5 | mouseOut | linkText=Sports |
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 6 | mouseOver | linkText=Sports |
    element = driver.find_element(By.LINK_TEXT, "Sports")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 7 | mouseOut | linkText=Sports |
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 8 | click | css=li:nth-child(2) .nav-link > div |
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .nav-link > div").click()
    # 9 | mouseOver | linkText=Movies |
    element = driver.find_element(By.LINK_TEXT, "Movies")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 10 | mouseOver | linkText=Sports |
    element = driver.find_element(By.LINK_TEXT, "Sports")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 11 | mouseOut | linkText=Sports |
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 12 | click | css=li:nth-child(3) .nav-link > div |
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) .nav-link > div").click()
    # 13 | mouseOver | linkText=Sports |
    element = driver.find_element(By.LINK_TEXT, "Sports")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 14 | mouseOut | linkText=Sports |
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 15 | click | css=.active > .nav-link > div |
    driver.find_element(By.CSS_SELECTOR, ".active > .nav-link > div").click()
    # 16 | mouseOver | css=.active > .nav-link > div |
    element = driver.find_element(By.CSS_SELECTOR, ".active > .nav-link > div")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 17 | mouseOut | css=.active > .nav-link > div |
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 18 | mouseOver | linkText=Premium |
    element = driver.find_element(By.LINK_TEXT, "Premium")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 19 | mouseOut | linkText=Premium |
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 20 | mouseOver | linkText=News |
    element = driver.find_element(By.LINK_TEXT, "News")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 21 | mouseOut | linkText=News |
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 22 | click | css=li:nth-child(4) > .dropdown-container div |
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .dropdown-container div").click()
    # 23 | click | css=li:nth-child(5) > .dropdown-container div |
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > .dropdown-container div").click()
    # 24 | mouseOver | linkText=Premium |
    element = driver.find_element(By.LINK_TEXT, "Premium")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 25 | click | id=searchField |
    driver.find_element(By.ID, "searchField").click()
    # 26 | type | id=searchField | news
    driver.find_element(By.ID, "searchField").send_keys("news")
    # 27 | sendKeys | id=searchField | ${KEY_ENTER}
    driver.find_element(By.ID, "searchField").send_keys(Keys.ENTER)
    # 28 | click | css=li:nth-child(1) .nav-link > div |
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .nav-link > div").click()

except Exception as e:
    print(e)
driver.close()
driver.quit()