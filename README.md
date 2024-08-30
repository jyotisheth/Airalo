# Airalo Coding Exercise

This project contains code for below assignments:

- UI Test: Open Airalo website and verify eSIM package for Japan
- API Test: Obtain OAuth2 token and verify POST, GET eSIM package endpoints

##### Prerequisites
- Python 3.7.2 (installed and configured)
```pip install -r requirements.txt```
- ChromeDriver is setup on and added to PATH variable on machine
    How to Setup ChromeDriver [Mac](https://medium.com/@tripleaceme/setting-up-chrome-driver-on-mac-0f32580912c3)  [Windows](https://medium.com/@patrick.yoho11/installing-selenium-and-chromedriver-on-windows-e02202ac2b08).

##### Running the tests
Mac: ```./run_tests.sh```
Windows: 
Installing Cygwin or Git Bash on Windows and adding the path where it is installed to the Environment variables will allow us to run “.sh” files on Windows from Command Prompt.

##### Overview of Test Automation approach
1. Setup required packages for the automation 
    pytest - Test execution framework
    requests - package for API Automation  
    Selenium - package for UI Automation
2. API Automation: 
   Get OAuth2 Token
   Use token in GET and POST endpoint
3. UI Automation: 
   Setup chromedriver object
   Navigate to Airalo website
   Search for Japan >> Select an eSIM package
   Verify package details 

##### Open Issues/ Observation 
1. GET endpoint:  always throws 401 error if include : order.status,order,order.user,share however passing only order.status,order,order.user works
2. GET endpoint: filter Y-m-d - Y-m-d appears not working, never returned data based on data 
3. Since there is no explicit way to filter GET result based on package slug (package_id), to make sure data correctness have used limit:6 and verified only first 6 records returned by endpoint