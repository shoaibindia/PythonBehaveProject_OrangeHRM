from behave import *
from selenium import webdriver
import time


@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open orangeHRM homePage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    time.sleep(3)
    context.driver.find_element("name", 'username').send_keys(user)
    context.driver.find_element("name", 'password').send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element("xpath", "//button[@type='submit']").click()


@then('User must successfully login to Dashboard page')
def step_impl(context):
    time.sleep(3)
    try:
        text = context.driver.find_element("xpath", "//h6[text() = 'Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        assert True, "Test Passed"
