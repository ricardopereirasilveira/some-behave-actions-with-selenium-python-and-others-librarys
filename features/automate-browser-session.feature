Feature: Automate Browser Actions - Launch Browser, maximize window, validate title & close browser
  Scenario: Automate using Browser Selenium Commands - Launch browser, maximize, validate page title and close browser. It should be your first webdriver script.
    Given Open this link - https://www.techlistic.com/
    When Launch Firefox browser. (You can choose browser of your choice).
    When Maximize or set size of browser window.
    When Get Title of page and validate it with expected value.
    When Get URL of current page and validate it with expected value.
    When Get Page source of web page.
    When And Validate that page title is present in page source.
    Then Close browser.