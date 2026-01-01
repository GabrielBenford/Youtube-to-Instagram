import os
import pytest
import datetime
import pytest_html.extras
from selenium import webdriver

from Login import Login
@pytest.fixture
def test_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
#Screenshot
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when=='call' and report.failed:
     driver=item.funcargs.get("test_driver")
     if driver:
         os.makedirs('screenshots', exist_ok=True)
         timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
         file_name=f'{item.name}_{timestamp}.png'
         file_path=os.path.join('screenshots', file_name)
         driver.save_screenshot(file_path)
         #HTML Report
         extra=getattr(report, 'extra', [])
         extra.append(pytest_html.extras.image(file_path))
         report.extra=extra

def test_login(test_driver):
        login = Login(test_driver)
        login.open_website()
        login.username_password()
        login.making_login()
        login.adding_cart()


