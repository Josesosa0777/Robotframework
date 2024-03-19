*** Settings ***
Library  SeleniumLibrary
Library     ../python_library/main.py
# Library    ../.venv/lib/python3.11/site-packages/robot/libraries/XML.py

*** Test Cases ***
This is a test case
    My custom Keywords
    # Open Browser  http:/google.com  edge
    Open Browser         http://google.com  edge  alias=MyBrowser
    Sleep                1s
    ${content}=          main.Open File
    Log                  File content: ${content}
    # Set Window Size      1300    1080
    Sleep                1s


*** Keywords ***
My custom Keywords
    Log                  This is a Robot Framework test step!
    Log To Console       Loggin to Console
