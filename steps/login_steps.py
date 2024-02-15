from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from environment import BASE_URL, BROWSER
from utils.driver_utils import setup_driver, teardown_driver

@given('I am on the test website login page')
def step_impl():
    driver = setup_driver(browser = BROWSER)
    driver.get(BASE_URL)

@when('I enter the username "{username}" and password "{password}"')
def step_impl(driver, username, password):
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

@when('I click the submit button')
def step_impl(driver):
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

@then('I should successfull logged in message "{message}"')
def step_impl(driver, message):
    success_message = driver.find_element(By.CLASS_NAME, "post-title")
    assert success_message.text == message


