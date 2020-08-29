from secrets import username,password
from selenium import webdriver
import time

def posttimeline(username,password,message):
    try:
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        browser = webdriver.Chrome(options=options)
        browser.get('https://www.facebook.com/')
        browser.find_element_by_name("email").send_keys(username)
        browser.find_element_by_name("pass").send_keys(password)
        browser.find_element_by_name('login').click()
        time.sleep(20)        
        browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div').click()
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').send_keys(message)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div').click()
        time.sleep(12)
        browser.close()
        browser.quit()
    except Exception as e:
        print("Error occured : ",e)


message="Hello world <3"
posttimeline(username,password,message)