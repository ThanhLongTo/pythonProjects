import requests
from bs4 import BeautifulSoup
import re


class Wiki:
    def __init__(self, input_search, language, sentence=None):
        self.language = language
        self.input_search = input_search
        self.sentence = sentence

        try:
            self.search = requests.get(f"https://{self.language}.wikipedia.org/w/index.php?search={'+'.join((self.input_search).split(' '))}&title=Special:Search&profile=advanced&fulltext=1&ns0=1")
            self.result = BeautifulSoup((self.search).content, 'html.parser')
            self.link = f"https://{self.language}.wikipedia.org"+ str(((self.result).find("div", {"class":"mw-search-result-heading"}).find("a")).get_attribute_list("href")[0])

            self.page = requests.get(self.link)
            self.html = BeautifulSoup((self.page).content, 'html.parser')

        except AttributeError:
            return "Cannot find anything"
        except Exception as E:
            return E


    def content(self):

        content = (self.html).find_all("div", {"class":"mw-parser-output"})

        data = ""

        for i in content:
            for j in i.find_all("p"):
                if re.sub("\[.*\]","",j.text) != "\n" or re.sub("\[.*\]","",j.text) != "":
                    data += re.sub("\[.*\]","",j.text)
        
        if self.sentence==None:
            return data
        else:
            return "".join(data.split(".")[:self.sentence]).replace("(listen)","")
        
    
    def links(self, _title=None):

        content = (self.html).find_all("a",href=True, title=True)

        links_data = ""
        if _title == True:
            for i in content:
                links_data += f"{i['title']} , https://{self.language}.m.wikipedia.org{i['href']}\n" if ("https://" not in i["href"]) else f"{i['title']} , {i['href']}"
        else:
            for i in content:
                links_data += f"https://{self.language}.m.wikipedia.org" + i["href"] + "\n" if ("https://" not in i["href"]) else i["href"] + "\n"
            
        return links_data
    
    def thumbnails(self, _title=None):
        content = (self.html).find_all("img", src=True, alt=True)

        links_data = ""
        
        if _title==True:
            for i in content:
                links_data += f"{i['alt']} , https:{i['src']}\n"
        else:
            for i in content:
                links_data += f"https:{i['src']}\n"
        
        return links_data
    
    def url(self):
        return self.link

    def title(self):
        return (self.link).replace("_"," ").replace(f"https://{self.language}.wikipedia.org/wiki/","")
    
    def pageHTML(self):
        return (self.html).prettify()


# if __name__ == "__main__":
#     # Remove "sentence" for full page
#     search = Wiki(input_search="Google", sentence=5)
#     print(search.content())
