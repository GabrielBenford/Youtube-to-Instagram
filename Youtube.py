from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class Youtube:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(self.driver)
    def open_youtube(self):
        self.driver.get("https://www.youtube.com")
    def search_youtube(self,text):
        searching=self.wait.until(EC.visibility_of_element_located((By.NAME, "search_query"))
        )
        searching.send_keys(text,Keys.ENTER)
    def click_on_video(self):
        videos=self.wait.until(EC.element_to_be_clickable((By.ID,"video-title"))
        )
        self.actions.move_to_element(videos).pause(1).click().perform()
    def open_chanel(self):
        chanel=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".yt-simple-endpoint.style-scope.yt-formatted-string"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", chanel
        )
        self.actions.move_to_element(chanel).pause(3).click().perform()
    def open_chanel_description(self):
        description=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"yt-truncated-text__absolute-button"))
        )
        self.driver.execute_script("arguments[0].click();", description
        )
    def open_instagram(self):
      try:
         instagram=self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"instagram.com"))
         )
         self.driver.execute_script("arguments[0].click();", instagram)
      except (TimeoutException,NoSuchElementException):
         print("Instagram not found.")
def youtube_chanel_to_instagram():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        automation = Youtube(driver)
        automation.open_youtube()
        automation.search_youtube('Video Name')
        automation.click_on_video()
        automation.open_chanel()
        automation.open_chanel_description()
        automation.open_instagram()
    finally:
        driver.quit()
if __name__ == "__main__":
    youtube_chanel_to_instagram()

