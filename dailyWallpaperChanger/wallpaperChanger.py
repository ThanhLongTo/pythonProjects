import ctypes
import datetime
import time
import os
import json
import urllib.request
import requests
from bs4 import BeautifulSoup



class ChangeWallpaper():
	global default_datetime
	global time_now
	global photo_select
	global data

	#open text.json for photo_select number
	with open("C:/Users/PC/Pictures/dailyWallpaperChanger/log.json") as f:
		data = json.load(f)
		photo_select = data['number']
	default_datetime = datetime.datetime(data["datetime"][0], data["datetime"][1], data["datetime"][2], 
											 data["datetime"][3], data["datetime"][4], data["datetime"][5])
	time_now = datetime.datetime.now()
	
	

	def unplash_wallpaper(self):
		# Check if a day is passed or not, to set daily wallpaper
		if (time_now-default_datetime).days >= 1:

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
			#print(a)

			detailedURL = "https://unsplash.com{}/download?".format(str(a))
			#print(detailedURL)
			detailedName = str(datetime.datetime.now()).replace('.','-').replace(':', '-').replace(" ", '-')
			urllib.request.urlretrieve(detailedURL, "{}.jpg".format(detailedName))
			ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/PC/Pictures/dailyWallpaperChanger/{}.jpg".format(detailedName) , 0)


			tomorrow = time_now + datetime.timedelta(days=1)
			data["datetime"][0] = tomorrow.year
			data["datetime"][1] = tomorrow.month
			data["datetime"][2] = tomorrow.day
			data["datetime"][3] = tomorrow.hour
			data["datetime"][4] = tomorrow.minute
			data["datetime"][5] = tomorrow.second

			
			#change the data in json file (+1)
			data['number'] = data['number'] + 1

			with open("C:/Users/PC/Pictures/dailyWallpaperChanger/log.json", "w") as f:
				json.dump(data, f)

			# remove previous photo
			listdir = os.listdir("C:/Users/PC/Pictures/dailyWallpaperChanger")
			if len(listdir) >= 7:
				os.remove(listdir[0])

			print("Successfully changed wallpaper!\nClosing program...")
			time.sleep(1.5)

		else:
			print("A day hasn't passed yet!\nClosing program...")
			time.sleep(1.5)


	def wallpaperCraft_wallpaper(self):
		

		if (time_now-default_datetime).days >= 1:

			url = "https://wallpaperscraft.com/catalog/city/2048x1152"
			headers = {
			    'Connection': 'keep-alive',
			    'Cache-Control': 'max-age=0',
			    'sec-ch-ua-mobile': '?0',
			    'Upgrade-Insecure-Requests': '1',
			    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
			    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			    'Sec-Fetch-Site': 'same-origin',
			    'Sec-Fetch-Mode': 'navigate',
			    'Sec-Fetch-User': '?1',
			    'Sec-Fetch-Dest': 'document',
			    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8'}

			html = requests.get(url, headers=headers)
			soup = BeautifulSoup(html.content, 'html.parser')
			a = soup.find_all('a', class_='wallpapers__link')[1]['href']


			detailedUrl = "https://wallpaperscraft.com{}".format(str(a))
			print(detailedUrl)
			html2 = requests.get(detailedUrl)
			soup2 = BeautifulSoup(html2.content, 'html.parser')
			downloadUrl = soup2.find_all('a', class_='JS-Popup')[0]['href']
			

			detailedName = str(datetime.datetime.now()).replace('.','-').replace(':', '-').replace(" ", '-')
			urllib.request.urlretrieve(downloadUrl, "{}.jpg".format(detailedName))
			ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/PC/Pictures/dailyWallpaperChanger/{}.jpg".format(detailedName) , 0)


			tomorrow = time_now + datetime.timedelta(days=1)
			data["datetime"][0] = tomorrow.year
			data["datetime"][1] = tomorrow.month
			data["datetime"][2] = tomorrow.day
			data["datetime"][3] = tomorrow.hour
			data["datetime"][4] = tomorrow.minute
			data["datetime"][5] = tomorrow.second

			
			#change the data in json file (+1)
			data['number'] = data['number'] + 1
				
			with open("C:/Users/PC/Pictures/dailyWallpaperChanger/log.json", "w") as f:
				json.dump(data, f)

			# remove previous photo
			listdir = os.listdir("C:/Users/PC/Pictures/dailyWallpaperChanger")
			if len(listdir) >= 7:
				os.remove(listdir[0])

			print("Successfully changed wallpaper!\nClosing program...")
			time.sleep(1.5)


		else:
			print("A day hasn't passed yet!\nClosing program...")
			time.sleep(1.5)



if __name__ == '__main__':
	ChangeWallpaper().wallpaperCraft_wallpaper()