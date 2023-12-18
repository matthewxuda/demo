# demo
This is a demo for automation api test and mobile ui test with python and appium

demo
- api_automation
  - tests
    - test_create_user.py
    - test_get_user.py
- testdata
  - test_data.yaml
- ui_automation
  - base
    - base_page.py
  - page_objects
  - tests
    - features
    - step_definition
    - test_chrome.py
- run_all_cases.py
- reports
  - html
- screenshots

![Test Report Screen](https://github.com/matthewxuda/demo/blob/main/reports/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202023-12-18%2023.29.23.png)
![Test Report Screen](https://github.com/matthewxuda/demo/blob/main/reports/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202023-12-18%2023.29.52.png)

## Features 
 
- The api_automation directory stores API automation test cases. 
- The testdata directory stores parameterized test data. 
- The ui_automation directory stores UI automation test cases. 
- The run_all_cases.py script is the project entry point, which is used to execute all test cases. 
- The reports directory stores test reports. 
 
## Usage 
 
1. Install the Python environment. 
2. Install the dependency library. 
3. Modify the testdata/test_data.yaml file to configure the test data. 
4. Run the run_all_cases.py script to execute all test cases. 
5. View the test report in the reports/html directory.