# -*- coding: utf-8 -*-

# This is the script that take data of TS10

from selenium import webdriver
import time

user_agent =\
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
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
    executable_path="C:\\Users\\PC\\Documents\\Coding workplace\\chromedriver_win32 (1)\\chromedriver.exe",
    options=options)

driver.get("https://thanhnien.vn/giao-duc/tuyen-sinh/2020/tra-cuu-diem-thi-lop-10.html")

final_list = {}
resList = []
i = 0
START_KEY = 100000
RANGE_SEARCH = 1000

for i in range(RANGE_SEARCH):
    search = driver.find_element_by_id("txtkeyword")
    search.send_keys(str(START_KEY + i))

    submit = driver.find_element_by_id("btnresult")
    submit.click()

    res = driver.find_elements_by_xpath(
        "//table[@class='table ptnk-tab-container-2']//tbody[@id='resultcontainer']")

    final = res[0].text
    # print(final)
    # idx1 = final.find("TPHCM") + 6
    idx2 = final.find("1") - 1
    resList = [final[:idx2]] + final[(idx2 + 1):].split(" ")
    final_list["Number {}".format(i)] = resList
    print(final_list)
    search.clear()
    time.sleep(0.4)
    i += 1
    continue
