### Prerequisites:
Before running test use should install python 3.6 at you environments

Instructions for Windows:
The perform the set of command for installing libraries and components:
```
pip install -U pytest
pip install allure-pytest
pip install requests
pip install StringGenerator
pip install pytest-xdist
pip install pytest-logg
```
or perform the command to install all components based on configuration:
```
pip install -r requirements.txt
```
###  For running tests use the following command
```
py.test --alluredir=allure-results -s -q
```

###  For parallel run use parameters -n
```
py.test --alluredir=allure-results -s -q -n 10
```

###  For report generation
```
allure serve allure-results
```

Note: Before running tests it makes sense to clear allure-results folder if it is not empty
```
rmdir allure-results /s /q
```

