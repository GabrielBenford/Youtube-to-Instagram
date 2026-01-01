import webbrowser

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
class Login:
    usernames=['locked_out_user','standard_user','problem_user','performance_glitch_user','error_user','visual_user']
    passwords=['secret_sauce','Eva']
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def open_website(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
    def username_password(self,):
        random_usernames=random.choice(self.usernames)
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(random_usernames)
        random_passwords=random.choice(self.passwords)
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(random_passwords)
    def making_login(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".submit-button.btn_action"))).click()
    def adding_cart(self):
        shop=self.wait.until(EC.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",shop)

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        login = Login(driver)
        login.open_website()
        login.username_password()
        login.making_login()
        login.adding_cart()
    finally:
        driver.quit()
if __name__ == '__main__':
    main()



