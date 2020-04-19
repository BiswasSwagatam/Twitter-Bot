from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class twitterbot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')   
        time.sleep(8)
        # bot.find_element_by_data-testid("loginButton").click()
        # time.sleep()
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        time.sleep(3)
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_tweet(self,hashtag):
        # time.sleep(3)
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')  
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            # links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            tweetLinks = [i.get_attribute('href') for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x,tweetLinks))
            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath("//div[@data-testid='like']").click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(10)    

        

sw = twitterbot('swagatamrocks01@gmail.com','sb7063187787')
sw.login()  
sw.like_tweet('ArtificialIntelligence')     