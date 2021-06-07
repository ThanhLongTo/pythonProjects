# This is the script that autoplay yt video in loop
# Also, the volumn is turn off because many videos play in the same time cause a mixture of sound

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


TIMES = 2               #change to yours
TABS = 3                #changes to yours
TIMES_PER_VIDEO = 40    #change to yours
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"  #change to yours
CHROME_DRIVER_PATH = "C:\\Users\\PC\\Documents\\Coding workplace\\chromedriver_win32 (1)\\chromedriver.exe"  #change to yours
YOUTUBE_URL = "https://www.youtube.com/watch?v=xSkSL3nxJwc&"


for times in range(TIMES):

    user_agent = USER_AGENT
    options = webdriver.ChromeOptions()
    options.headless = False   # or "True" if you dont want the browser to open
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(
        executable_path=CHROME_DRIVER_PATH,
        options=options)
    
    driver.get(YOUTUBE_URL)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='ytp-mute-button ytp-button']")))
    element.click()

    for i in range(TABS):
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[i+1])
        driver.get(YOUTUBE_URL)
        print(driver.current_window_handle)   

    time.sleep(TIMES_PER_VIDEO)
    driver.quit()
    time.sleep(1)
    
    

    