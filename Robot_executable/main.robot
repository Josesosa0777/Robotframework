*** Settings ***
Library  SeleniumLibrary
# Library     ../python_library/main.py

# https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
# https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Set%20Window%20Size
# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#if-else-syntax
# 3.9.18
*** Variables ***
${URL}                            https://cvsplm.corp.knorr-bremse.com:14432/#/showHome
${BROWSER}                        edge

*** Test Cases ***
This is a test case
    Log                           ${VARIABLE1}
    Open Browser                  ${URL}  ${BROWSER}
    # Maximize Browser Window
    Bendix Webpage                # Calling the Keyword `Bendix Webpage`
    Sleep                         3s
    # Open Excel File
    Close All Browsers

*** Keywords ***
Bendix Webpage
    log to console                Logging to console
    Wait Until Page Contains      CVS PLM (PRODUCTION)    timeout=30s
    # Maximize Browser Window
    Sleep    1s
    Click Element                 xpath=//*[@id="main-view"]/div/div[2]/div[1]/div/div/div/div/div[1]/header/div[2]/div[1]   # Haz clic en el elemento del botón de búsqueda
    Input Text                    xpath=//*[@id="aw_navigation"]/div[2]/form/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/input      K286348
    Sleep    3s
    Click Element                 xpath=//*[@id="aw_navigation"]/div[2]/form/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]
    Sleep    5s
    # Input Text                    name:searchBox                        K286348
    # Press Keys                    name:searchBox                        RETURN
    # Wait For Condition            return document.readystate == "complete"
    
    # Click Element    xpath=//*[@id="main-view"]/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div[1]/nav/div/div[1]/div[6]/button
    Click Element    css:button[button-id="Awp0NewGroup"]
    Sleep    5s
    Click Element    css:li[button-id="Awp0InContextReports"]
    Sleep    5s
    Click Element    xpath=//*[@id="aw_toolsAndInfo"]/div[2]/form/div[2]/div/div/div[2]/div/div[1]/div/ul/li[1]
    Sleep    8s
    Click Element    //button[contains(., 'Generate')]
    Sleep    5s

Open Excel File
    ${content}=          main.Open File
    Log                  File content: ${content}
# robot -d Results Tests

# python 3.9.18 initially, but edge 122 is not compatible
# conda install -c conda-forge webdriver-manager
# pip install webdriver-manager
# Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))) - skipping


# 1.- Close teams completely
# 2.- Go to Directoty c:\sers\<youruser>\appdata\local\Packages\MSTeams_8wekyb3d8bbwe
# 3.- Delete everything on this directory4.- run teams again</youruser>


