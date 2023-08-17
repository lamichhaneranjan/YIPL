Feature:

  @login
  Scenario Outline:Login with valid credentials
    Given I navigated to Login page
    When I enter valid email as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      |email                 |password     |
      |superadmin@admin.com  |super@admin  |

  @login @check
  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email and valid password say "super@admin" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email say "superadmin@admin.com" and invalid password say "super@super" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario:Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email and invalid password say "super@Super" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I dont enter anything into email and password fields
    And I click on Login button
    Then I should get a proper warning message