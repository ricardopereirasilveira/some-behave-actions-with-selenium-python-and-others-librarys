Feature: Do a Login and a secure purchase on the Mercury Tours website.
  Scenario: You must be able to sucessfully make a purchase on the Mercury Tours.
    Given open the browser with the indicated URL
    When insert the true username and password to access the restricted page
    When on the first page after login, select the dates of the round trip flights as requested and click on continue
    When on the next screen, select the outbound and return flights and click on continue
    When on this screen, validate the company's information and insert the required fields and click on secure purchase
    When on this last screen, check if the Flight Confirmation Number has been generated
    Then close the browser and finish the selenium session