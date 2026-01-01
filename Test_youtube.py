from Youtube import Youtube
from selenium import webdriver
import pytest
@pytest.fixture
def test_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
def test_youtube_chanel_to_instagram(test_driver):
    try:
        automation = Youtube(test_driver)
        automation.open_youtube()
        automation.search_youtube('Video name')
        automation.click_on_video()
        automation.open_chanel()
        automation.open_chanel_description()
        automation.open_instagram()
    finally:
        test_driver.quit()


