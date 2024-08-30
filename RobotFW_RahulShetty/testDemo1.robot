#http://www.rahulshettyacademy.com/loginpagePractise/
# Setting, test Cases, Keywords, these are optional, but which helps us to categorize your test case.
*** Settings ***
#lot of things you can do in settings Also.
Test Teardown    Close Browser

Documentation    To Validate the Login form
Library    SeleniumLibrary
# setup methods, teardown methods like what should be your pre-request script cleanup script.
#And if this file depends upon any other external files like reusable utilities, page objects, which
##we will do later, all those files related details you will pass here in terms of resource.
###Resource
*** Variables ***
#And if you declare any variable on this level, then that variable is called global variable and that
#scope is applied to the entire file.You can use it anywhere.
#I'm just showing you how the variable helps.It's just not only locators.
#Whatever you think can be reused in your test cases multiple times, then you can declare that as a variable on
#global level and you can reuse it value wherever you want.So that's how this variables module is used.

${error_message_login}    css:.alert-danger

*** Test Cases ***
Validate UnSuccesful Login
    open the browser with the Mortage payment url
    Fill the login details
    wait until it checks and display the error message
    verify error is message is collect

*** Keywords ***
open the browser with the Mortage payment url
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/
Fill the login details
    Input Text    username    rahulshettyacademy
    Input Text    password    12345678
    Click Button    signInBtn
wait until it checks and display the error message
    Wait Until Element Is Visible    ${error_message_login}
    verify error is message is collect
verify error is message is collect
    ${result}=    Get Text    ${error_message_login}
    #Should Be Equal As Strings    ${result}    Incorrect username/password.
    Element Text Should Be    ${error_message_login}    Incorrect username/password.
