import ctypes
import datetime
import time
import os
import json
import urllib.request
import requests
from bs4 import BeautifulSoup

def skip_wallpaper():
	with open("C:/Users/PC/Pictures/dailyWallpaperChanger/log.json") as f:
		data = json.load(f)
		photo_select = data['number'] + 1


	url = "https://unsplash.com/s/photos/nature?orientation=landscape"
	headers = {
		    'authority': 'unsplash.com',
		    'cache-control': 'max-age=0',
		    'sec-ch-ua-mobile': '?0',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-user': '?1',
		    'sec-fetch-dest': 'document',
		    'referer': 'https://www.google.com/',
		    'accept-language': 'en-US,en;q=0.9,vi;q=0.8'}

	html = requests.get(url)
	soup = BeautifulSoup(html.content, 'html.parser')
	a = soup.find_all('a', class_="_2Mc8_")[photo_select]['href']

	detailedURL = "https://unsplash.com{}/download?".format(str(a))
	
	detailedName = str(datetime.datetime.now()).replace('.','-').replace(':', '-').replace(" ", '-')
	urllib.request.urlretrieve(detailedURL, "{}.jpg".format(detailedName))
	ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/PC/Pictures/dailyWallpaperChanger/{}.jpg".format(detailedName) , 0)


	data['number'] = data['number'] + 1
	
	with open("C:/Users/PC/Pictures/dailyWallpaperChanger/log.json", "w") as f:
		json.dump(data, f)

		# remove previous photo
	listdir = os.listdir("C:/Users/PC/Pictures/dailyWallpaperChanger")
	if len(listdir) >= 7:
		os.remove(listdir[0])

	print("Successfully changed wallpaper!\nClosing program...")
	time.sleep(1.5)


if __name__ == "__main__":
	skip_wallpaper()
