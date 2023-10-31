*** Settings ***
Documentation       Playwright template.

Library             RPA.Browser.Playwright
Library             SeleniumLibrary

Suite Setup    New Browser    browser=${BROWSER}    headless=${False}
Test Setup    New Context
Test Teardown    Close Context
Suite Teardown    Close Browser

*** Variables ***
${URL}            https://www.instagram.com/
${USERNAME}       mahendraneie45@gmail.com
${PASSWORD}       gojuryu45
${BROWSER}        chromium


*** Tasks ***
UnFollow Instragram Profiles
    New Browser     headless=${False}  # starts in headless in Control Room
    New Page    ${URL}
    # Wait For Page To Load
    Click Element    xpath=//a[text()='Log in']
    # Wait For Page To Load
    Input Text    name=username    ${USERNAME}
    Input Text    name=password    ${PASSWORD}
    Click Element    xpath=//button[@type='submit']
    # Wait For Page To Load
