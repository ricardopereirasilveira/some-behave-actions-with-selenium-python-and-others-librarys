from behave import given, when, then, step
from selenium import webdriver


@given('Open this link - https://www.techlistic.com/')
def index(context):
    context.url = 'https://www.techlistic.com/'
    context.drive = webdriver.Firefox()

@when('Launch Firefox browser. (You can choose browser of your choice).')
def index(context):
    context.drive.get(context.url)

@when('Maximize or set size of browser window.')
def index(context):
    context.drive.maximize_window()

@when('Get Title of page and validate it with expected value.')
def index(context):
    context.titulo = context.drive.title
    assert 'Techlistic' in context.titulo

@when('Get URL of current page and validate it with expected value.')
def index(context):
    assert context.url in context.drive.current_url

@when('Get Page source of web page.')
def index(context):
    context.pageSource = context.drive.page_source

@when('And Validate that page title is present in page source.')
def index(context):
    assert context.titulo in context.drive.page_source

@then('Close browser.')
def index(context):
    context.drive.close()
    context.drive.quit()

