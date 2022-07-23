from twitter_bot import InternetSpeedTwitterBot
import os

#speed being paid for:
PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 10

TWITTER_ACCOUNT = os.getenv("TWITTER_ACCOUNT")  #your Twitter account
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")  #your password
DRIVER_PATH = os.getenv('DRIVER_PATH')  #your driver path

#using bot to check internet speed and tweet at provider
bot = InternetSpeedTwitterBot(driver_path=DRIVER_PATH,
                              promised_download=PROMISED_DOWNLOAD,
                              promised_upload=PROMISED_UPLOAD
                              )
bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_ACCOUNT, TWITTER_PASSWORD)
