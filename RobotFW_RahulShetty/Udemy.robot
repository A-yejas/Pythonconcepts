*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}  https://example.com

*** Test Cases ***
Open Browser and Verify Title
    Open Browser  ${URL}  Chrome
    Title Should Be  Example Domain
    Close Browser
