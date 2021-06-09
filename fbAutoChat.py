# This is the script that autoplay yt video in loop
# Also, the volumn is turn off because many videos play in the same time cause a mixture of sound

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import pickle


PATH = "C:\\Users\\PC\\Documents\\Coding workplace\\my_cookies.pkl"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"  #change to yours
CHROME_DRIVER_PATH = "C:\\Users\\PC\\Documents\\Coding workplace\\chromedriver_win32 (1)\\chromedriver.exe"  #change to yours
MAIN_URL = "https://www.facebook.com/"
CONVERSATION_URL = "https://www.facebook.com/messages/t/100014827696661"
EMAIL = "###"
PASSWORD = "###"


def main():

    def save_cookies(driver, location):
        pickle.dump(driver.get_cookies(), open(location, "wb"))

    def load_cookies(driver, location, url=None):
        cookies = pickle.load(open(location, "rb"))
        print(cookies)
        driver.get(MAIN_URL)           
        for cookie in cookies:
            driver.add_cookie(cookie)
    
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,options=options)


    if (os.path.getsize(PATH)) > 0:

        load_cookies(driver,PATH)
        
        driver.get(CONVERSATION_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_1mf _1mj']"))).send_keys("Hii", Keys.ENTER)
        first_send = driver.find_element_by_xpath("//div[@class='_1mf _1mj']")
        time.sleep(5)
        first_send.send_keys("nani ", Keys.ENTER)
        time.sleep(3)

    else:

        driver.find_element_by_xpath("//input[@id='email']").send_keys(EMAIL)
        driver.find_element_by_xpath("//input[@id='pass']").send_keys(PASSWORD)
        driver.find_element_by_xpath("//button[@name='login']").click()
        time.sleep(2)

        save_cookies(driver,PATH)
    

if __name__ == "__main__":
    main()
    
    
    

    