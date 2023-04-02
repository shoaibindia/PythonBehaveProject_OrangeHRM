Feature: OrangeHRM logo
  Scenario: Logo presence on OrangeHRM Home page
    Given launch chrome browser
    When  open orangehrm home page
    Then verify that the logo present on page
    And close the browser