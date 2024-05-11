from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

def wait_click(driver, wait, locator):
    wait.until(ec.element_to_be_clickable(locator))
    driver.find_element(*locator).click()

driver = webdriver.Firefox()
driver.get('http://localhost:8069/web/database/selector')

wait = WebDriverWait(driver, 5)

server = (By.XPATH, '/html/body/div/div[1]/div/div[1]/div[1]/a')
wait_click(driver, wait, server)

email_box = (By.NAME, "login")
wait_click(driver, wait, email_box)
driver.find_element(*email_box).send_keys("johnnyblaze1999.sg@gmail.com")

pass_box = (By.NAME, "password")
wait_click(driver, wait, pass_box)
driver.find_element(*pass_box).send_keys("student")

login_btn = (By.XPATH, '/html/body/div[1]/main/div/form/div[4]/button[1]')
wait_click(driver, wait, login_btn)

profile_btn = (By.XPATH, '/html/body/header/nav/div[2]/div[4]/button')
wait_click(driver, wait, profile_btn)

logout_btn = (By.XPATH, '/html/body/header/nav/div[2]/div[4]/div/a[3]')
wait_click(driver, wait, logout_btn)

time.sleep(5)
driver.quit()