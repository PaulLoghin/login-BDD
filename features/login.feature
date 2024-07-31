Feature: Test the login functionality of the internet heroku app

  @valid_login
  Scenario: Check valid credential
    Given I am login page
    When I introduce the valid username
    And I introduce the valid password
    And I clicked the login button
    Then I am in secure area
    And I am on a new page

  Scenario Outline: Test invalid credential for username and password
    Given I am login page
    When I use an invalid "<username>" and "<password>"
    And I clicked the login button
    Then I should remain on the login page
    Examples:
      | username | password             |
      | username | password             |
      | tomsmith | password             |
      | username | SuperSecretPassword! |







