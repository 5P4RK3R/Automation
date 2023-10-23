*** Settings ***
Documentation       Playwright template.

Library             RPA.Browser.Playwright


*** Variables ***
${URL}            https://www.instagram.com/
${USERNAME}       mahendraneie45@gmail.com
${PASSWORD}       gojuryu45


*** Tasks ***
Minimal task
    New Browser     headless=${False}  # starts in headless in Control Room
    New Page    ${URL}
    Wait For Page To Load
    # Click Element    xpath=//a[text()='Log in']
    # Wait For Page To Load
    # Input Text    name=username    ${USERNAME}
    # Input Text    name=password    ${PASSWORD}
    # Click Element    xpath=//button[@type='submit']
    # Wait For Page To Load
