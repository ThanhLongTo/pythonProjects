import requests
from bs4 import BeautifulSoup
import re


input_search = input("Anything: ")


search = requests.get(f"https://en.wikipedia.org/w/index.php?search={'+'.join(input_search.split(' '))}&title=Special:Search&profile=advanced&fulltext=1&ns0=1", timeout=10)
result = BeautifulSoup(search.content, 'html.parser')
link = "https://en.wikipedia.org"+ str((result.find("div", {"class":"mw-search-result-heading"}).find("a")).get_attribute_list("href")[0])


page = requests.get(link,timeout=10)
html = BeautifulSoup(page.content, 'html.parser')

content = html.find_all("div", {"class":"mw-parser-output"})

for i in content:
    for j in i.find_all("p"):
        print(re.sub("\[\d+\]","",j.text))
