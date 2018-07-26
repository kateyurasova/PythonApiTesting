## For running tests use the following command
py.test --alluredir=allure-results -s -q

## Note: Before running tests it makes sense to clear allure-results folder if it is not empty
rmdir allure-results /s /q

## For report generation
allure serve allure-results

