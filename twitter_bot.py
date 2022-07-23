from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self, driver_path, promised_upload, promised_download):
        ser = Service(driver_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.down = 0
        self.up = 0
        self.driver.implicitly_wait(30)
        self.promised_download = promised_download
        self.promised_upload = promised_upload

    def get_internet_speed(self):

        speedtest_link = "https://www.speedtest.net/"
        self.driver.get(speedtest_link)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        values_not_available = True

        while values_not_available:
            download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
            upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            try:
                self.down = float(download.text)
                self.up = float(upload.text)
                values_not_available = False
            except ValueError:
                time.sleep(2)

    def tweet_at_provider(self, username: str, password: str):

        if self.down < self.promised_download or self.up < self.promised_upload:

            message = f"Hey internet provider! Why am I only receiving {self.down}Down/{self.up}UP when I " \
                  f"am paying for {self.promised_download}Down/{self.promised_upload}UP"

            #pulls up site
            twitter_link = "https://twitter.com/"
            self.driver.get(twitter_link)

            #logging in
            go_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
            go_button.click()
            time.sleep(1)

            enter_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            time.sleep(1)
            enter_username.send_keys(f"{username}{Keys.ENTER}")
            time.sleep(1)

            enter_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            time.sleep(1)
            enter_password.send_keys(f"{password}{Keys.ENTER}")
            time.sleep(1)

            #tweets
            start_tweet = self.driver.find_element(By. XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            start_tweet.click()
            time.sleep(1)

            type_message = self.driver.find_element(By. XPATH, f'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div/div/div/div')
            time.sleep(1)
            type_message.send_keys(f"{message}")
            time.sleep(1)

            send_tweet = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
            send_tweet.click()
            print("tweet posted")

        #ends program
        input('click ENTER when ready to quit program: ')  #allows user to delete/view tweets or view internet speed if line 43 is false
        self.driver.quit()
