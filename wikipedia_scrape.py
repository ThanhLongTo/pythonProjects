import requests
from bs4 import BeautifulSoup
import re


class Wiki:
    def __init__(self, input_search, sentence=None):
        self.input_search = input_search
        self.sentence = sentence
    
    def wiki(self):
        try:
            search = requests.get(f"https://en.wikipedia.org/w/index.php?search={'+'.join((self.input_search).split(' '))}&title=Special:Search&profile=advanced&fulltext=1&ns0=1", timeout=10)
            result = BeautifulSoup(search.content, 'html.parser')
            link = "https://en.wikipedia.org"+ str((result.find("div", {"class":"mw-search-result-heading"}).find("a")).get_attribute_list("href")[0])
        
        
            page = requests.get(link,timeout=10)
            html = BeautifulSoup(page.content, 'html.parser')

            content = html.find_all("div", {"class":"mw-parser-output"})

            data = ""

            for i in content:
                for j in i.find_all("p"):
                    if re.sub("\[.*\]","",j.text) != "\n" or re.sub("\[.*\]","",j.text) != "":
                        data += re.sub("\[.*\]","",j.text)
            
            if self.sentence==None:
                return data
            else:
                return "".join(data.split(".")[:self.sentence]).replace("(listen)","")
        
        except AttributeError:
            return "Cannot find anything"
        except Exception as E:
            return E


if __name__ == "__main__":
    # Remove "sentence" for full page
    search = Wiki(input_search="Google", sentence=5)
    print(search.wiki())
