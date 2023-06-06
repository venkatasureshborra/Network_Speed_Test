from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

twitter_no=xxxxxxxxxx
t_pass="xxxxxxxx"
PROMISED_DOWN = 150
PROMISED_UP = 10

##########------Testing-------------##########

class InternetSpeedTwitterBot:
    def __init__(self,driver):
        self.driver=webdriver.Chrome(service=driver)
        self.down=0
        self.up=0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(10)
        go_button=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        sleep(70)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(2)
        phone_num=self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(twitter_no)
        next=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        sleep(2)
        password=self.driver.find_element(By.NAME,'password').send_keys(t_pass)
        log_in=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        sleep(5)
        tweet=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        sleep(2)
        print("before happen")
        self.driver.find_element(By.XPATH ,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div').send_keys(f"Hello today in internet speed is {self.down}mbs down/{self.up}mbs upload but promised is {PROMISED_DOWN}mbs download/{PROMISED_UP} mbs upload ")
        print("success")
        sleep(10)
        self.driver.quit()

