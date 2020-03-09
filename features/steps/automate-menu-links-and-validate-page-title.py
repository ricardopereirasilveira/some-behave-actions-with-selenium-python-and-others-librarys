from behave import then, when, given
from selenium import webdriver

@given('Open this link  https://www.techlistic.com/')
def index(context):
    context.url = 'https://www.techlistic.com/'
    context.drive = webdriver.Firefox()

@when('Launch Firefox browser. (You can choose browser of your choice).')
def index(context):
    context.drive.get(context.url)
    context.drive.implicitly_wait(5)

@when('Maximize or set size of browser window.')
def index(context):
    context.drive.maximize_window()

@when('Click on Java Tutorial link and validate page title.')
def index(context):
    context.drive.find_element_by_css_selector(
        '#PageList1 > div > div.overflowable-container.overflowable-2 > div.overflowable-contents > div > ul > li:nth-child(3) > a').click()
    assert 'Java Tutorials Series - Java For Selenium' in context.drive.title

@when('Navigate back to Home Page.')
def index(context):
    context.drive.find_element_by_css_selector('#PageList1 > div > div.overflowable-container.overflowable-2 > div.overflowable-contents > div > ul > li:nth-child(1) > a').click()

@when('Click on Selenium Blogs link and validate page title.')
def index(context):
    context.drive.find_element_by_class_name('overflow-button').click()
    context.drive.find_element_by_css_selector(
        '#PageList1 > div > div.overflow-popup > div > ul > li:nth-child(14) > a').click()

@when('Navigate back to Home Page.')
def index(context):
    context.drive.find_element_by_css_selector('#PageList1 > div > div.overflowable-container.overflowable-2 > div.overflowable-contents > div > ul > li:nth-child(1) > a').click()

@when('Click on TestNG Blogs link and validate page title.')
def index(context):
    assert 'Top Selenium Blogs' in context.drive.title

@then('Close the browser.')
def index(context):
    context.drive.close()
    context.drive.quit()