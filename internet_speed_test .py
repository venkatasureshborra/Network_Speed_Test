from speed_bot import InternetSpeedTwitterBot
from selenium.webdriver.chrome.service import Service
from time import sleep
driver_path=Service("your selenium driver location")

bot=InternetSpeedTwitterBot(driver_path)
bot.get_internet_speed()
sleep(2)
bot.tweet_at_provider()