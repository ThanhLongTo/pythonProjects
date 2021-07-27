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

    
    
    
    
    
# SCRAPE ĐIỂM THPT 2021


import requests
from bs4 import BeautifulSoup
import json
import time

def fetch_data(sbd):
    headers = {
        'authority': 'diemthi.tuoitre.vn',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'referer': 'https://diemthi.tuoitre.vn/thpt-2021',

    }
    payload = {"data": str(sbd), "code": ""}

    page = requests.post("https://diemthi.tuoitre.vn/search-thpt-score", headers=headers, data=payload)
    print(page.status_code)

    html = BeautifulSoup(page.content, "html.parser")

    a = json.loads(str(html))

    return a


# Sample response form : data = {"data":[{"_id":"S9D33noBrZdVKVdyg4Fk","_index":"student_thpt","_score":0,"_source":{"examination_id":1,"name":"","sbd":"01000020","school_id":49,"score":"Toán:8.80;Văn:6.25;Lí:5.50;Hóa:8.25;Sinh:4.50;Sử:;Địa:;GDCD:;Ngoại Ngữ:8.40;"},"_type":"_doc"}],"message":"Suscess!","status":200}

def analyse(data):
    # pretty = json.dumps(data, indent=4,ensure_ascii=False)

    sbd = data["data"][0]["_source"]["sbd"]
    score_list = data["data"][0]["_source"]["score"].split(";")

    score_extract = {}
    for i in score_list:
        score_extract[i[:i.find(":")]] = i[i.find(":")+1:]

    return [sbd,score_extract]

if __name__ == "__main__" :

    RANGE_SEARCH = 100
    main_data = {}
    sbd_error = []

    for i in range(1,RANGE_SEARCH):
        sbd = "0" + str(1000000+i)

        try:
            data = fetch_data(sbd=sbd)
            result = analyse(data)
            print("pass")
            main_data[str(result[0])] = result[1]
            # print(result)
            time.sleep(0.2)
        except Exception:
            print(sbd + " error")
            sbd_error.append(sbd)
    
    print(main_data)
    print(sbd_error)
