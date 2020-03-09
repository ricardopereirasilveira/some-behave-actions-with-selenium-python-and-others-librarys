Feature: Automate demo 'About Me' form using Selenium
  Scenario: You must complet the form sucessfully with all informations
    Given Open this link - https://www.techlistic.com/p/selenium-practice-form.html
    When Enter first and last name (textbox).
    When Select gender (radio button).
    When Select years of experience (radio button).
    When Enter date.
    When Select Profession (Checkbox).
    When Select Automation tools you are familiar with (multiple checkboxes).
    When Select Continent (Select box).
    When Select multiple commands from a multi select box.
    When If you can handle Upload image then try it or leave this step.
    When Click on Download file link and handle the download file pop-up (leave it if you are beginner).
    When Click on Submit button.
    Then close the browser and the session