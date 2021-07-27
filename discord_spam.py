import requests
import datetime
import random
import time


while True:
    payload = {
        "content" : f'```diff\n- Nautilus is powerful at {datetime.datetime.utcnow()}\n- {random.random()}```'
    }

    headers = {
        "authorization" : "###"
    }
    r = requests.post("https://discord.com/api/v9/channels/864877068499550228/messages", data=payload, headers=headers)
    time.sleep(2)
