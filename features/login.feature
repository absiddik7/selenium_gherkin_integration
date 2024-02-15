Feature: Login to Test Website

    Scenario: Successful login with valid credentials
        Given I am on the test website login page
        When I enter the valid username "student" and password "Password123"
        And I click the submit button
        Then I should successfull logged in message "Logged In Successfully"

# Scenario: Unsuccessful login with invalid credentials
#     Given I am on the test website login page
#     When I enter an invalid username "student120" and password "Password1234"
#     And I click the submit button
#     Then I should see an error message "Your username is invalid!"