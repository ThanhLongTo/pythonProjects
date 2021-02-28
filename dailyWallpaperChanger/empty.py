import json

with open("C:/Users/PC/Pictures/dailyWallpaperChanger/test.json") as f:
	data = json.load(f)
	print(data['number'])

data['number'] = data['number'] + 1
	
with open("C:/Users/PC/Pictures/dailyWallpaperChanger/test.json", "w") as f:
	json.dump(data, f)

