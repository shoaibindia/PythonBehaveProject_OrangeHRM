import time

from behave import *
from selenium import webdriver


@given(u'launch chrome browser')
def launchBrowser(context):
    #context.driver = webdriver.Chrome(executable_path="F:\ProgramPractice\Drivers\chromedriver.exe") set the chromedriver in python script folder
    context.driver = webdriver.Chrome()


@when(u'open orangehrm home page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


@then(u'verify that the logo present on page')
def verifyLogo(context):
    time.sleep(3)
    status = context.driver.find_element("xpath", '(//img)[1]').is_displayed()
    assert status is True


@then(u'close the browser')
def closeBrowser(context):
    context.driver.close()
