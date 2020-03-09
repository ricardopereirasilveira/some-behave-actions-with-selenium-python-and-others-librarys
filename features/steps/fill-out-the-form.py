from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

@given('Open this link - https://www.techlistic.com/p/selenium-practice-form.html')
def index(context):
    context.url = 'https://www.techlistic.com/p/selenium-practice-form.html'
    context.drive = webdriver.Firefox()
    context.drive.get(context.url)
    context.drive.implicitly_wait(5)
    assert context.drive.current_url == context.url
    print('Open this link - https://www.techlistic.com/p/selenium-practice-form.html - realizado com sucesso!')

@when('Enter first and last name (textbox).')
def index(context):
    context.drive.find_element_by_css_selector(
        '#post-body-3077692503353518311 > div > div:nth-child(1) > div:nth-child(4) > input[type=text]').send_keys(
        'Ricardo')
    context.drive.find_element_by_css_selector(
        '#post-body-3077692503353518311 > div > div:nth-child(1) > div:nth-child(7) > input[type=text]').send_keys(
        'Pereira')

@when('Select gender (radio button).')
def index(context):
    context.drive.find_element_by_xpath('//*[@id="sex-0"]').click()

@when('Select years of experience (radio button).')
def index(context):
    context.drive.find_element_by_xpath('//*[@id="exp-6"]').click()

@when('Enter date.')
def index(context):
    context.drive.find_element_by_css_selector('#datepicker').send_keys('25/03/1988')

@when('Select Profession (Checkbox).')
def index(context):
    context.drive.find_element_by_xpath('//*[@id="profession-1"]').click()

@when('Select Automation tools you are familiar with (multiple checkboxes).')
def index(context):
    context.drive.find_element_by_xpath('//*[@id="tool-2"]').click()

@when('Select Continent (Select box).')
def index(context):
    context.select = Select(context.drive.find_element_by_class_name('input-xlarge'))
    context.select.select_by_visible_text('South America')

@when('Select multiple commands from a multi select box.')
def index(context):
    context.select = Select(context.drive.find_element_by_xpath('//*[@id="selenium_commands"]'))
    context.select.select_by_visible_text('Browser Commands')
    sleep(1)
    context.select.select_by_visible_text('Switch Commands')
    sleep(1)
    context.select.select_by_visible_text('WebElement Commands')

@when('If you can handle Upload image then try it or leave this step.')
def index(context):
    imagePatch = os.path.abspath('/Volumes/HD/Transferências/frame (1).png')
    context.drive.find_element_by_xpath('//*[@id="photo"]').send_keys(imagePatch)

@when('Click on Download file link and handle the download file pop-up (leave it if you are beginner).')
def index(context):
    elementoPath = '#post-body-3077692503353518311 > div > div:nth-child(1) > div.controls > div:nth-child(2) > div > a'
    context.actionChains = ActionChains(context.drive)
    fileDownload = 'Click here to Download File'
    link = context.drive.find_element_by_css_selector(
        '#post-body-3077692503353518311 > div > div:nth-child(1) > div.controls > div:nth-child(2) > div > a')
    context.actionChains.context_click(link).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()

@when('Click on Submit button.')
def index(context):
    context.drive.find_element_by_css_selector('#submit').click()

@then('')
def index(context):
    context.drive.close()
    context.drive.quit()