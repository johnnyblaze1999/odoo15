*** Settings ***
Library           SeleniumLibrary


*** Variables ***
${LOGIN_URL}      http://localhost:8069/web/login
${BROWSER}        Firefox
${DELAY}          1
${USERNAME}       johnnyblaze1999.sg@gmail.com
${PASSWORD}       student

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    ${USERNAME}
    Input Password    ${PASSWORD}
    Submit Credentials
    Welcome Page Should Be Open
Create Robot Patient
    Go To Patients Page
    Create New Patient
    Verify Patient Creation
Delete Robot Patient
    Remove Patient
Create Patient Without Name
    Go To Patients Page
    Create Empty Name Patient
    Verify Field Error
    Discard
Create Patient With Invalid Age
    Go To Patients Page
    Create Invalid Age Patient
    Verify Field Error
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Set Selenium Speed    ${DELAY}
    Title Should Be    Login | My Website

Input Username
    [Arguments]    ${username}
    Input Text    id=login    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    id=password    ${password}

Submit Credentials
    Click Button    css=.btn-primary

Welcome Page Should Be Open
    Title Should Be    Odoo - Discuss

Go To Patients Page
    Go To     http://localhost:8069/web#cids=1&menu_id=285&action=395&model=hospital.patient&view_type=list

Create New Patient
    Click Button    xpath=//button[@data-original-title="Create record"]
    Input Text    name    Robot Patient
    Input Text    age    30
    Click Button    xpath=//button[@title='Save record']

Verify Patient Creation
    Page Should Contain    Robot Patient

Remove Patient
    Click Button    xpath=//button[@data-original-title="Additional actions"]
    Execute JavaScript    document.evaluate("//*[contains(text(), 'Delete')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
    Click Button    xpath=//button[@class='btn btn-primary']

Verify Patient Removal
    Page Should Not Contain    Robot Patient

Create Empty Name Patient
    Click Button    xpath=//button[@data-original-title="Create record"]
    Input Text    age    30
    Click Button    xpath=//button[@title='Save record']

Create Invalid Age Patient
    Click Button    xpath=//button[@data-original-title="Create record"]
    Input Text    name    Robot Patient
    Input Text    age    invalid
    Click Button    xpath=//button[@title='Save record']

Discard 
    Click Button    xpath=//button[@title='Discard record']

Verify Field Error
    Page Should Contain    Invalid fields: