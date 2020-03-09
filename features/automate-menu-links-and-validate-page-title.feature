Feature: Automate Menu Links and Validate Page Titles using Selenium
  Scenario: Automate Menu Links and Validate Page Titles to verify that when clicking on menu links then users are landing on correct pages.
    Given Open this link  https://www.techlistic.com/
    When Launch Firefox browser. (You can choose browser of your choice).
    When Maximize or set size of browser window.
    When Click on Java Tutorial link and validate page title.
    When Navigate back to Home Page.
    When Click on Selenium Blogs link and validate page title.
    When Navigate back to Home Page.
    When Click on TestNG Blogs link and validate page title.
    Then Close the browser.