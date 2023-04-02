Feature: OrangeHRM login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When  I open orangeHRM homePage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to Dashboard page

    Scenario Outline: Login to OrangeHRM with multiple parameters
      Given I launch chrome browser
      When  I open orangeHRM homePage
      And Enter username "<username>" and password "<password>"
      And Click on login button
      Then User must successfully login to Dashboard page

      Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin |
      | adminxyz | admin123 |
      | admin    | adminxyz |
