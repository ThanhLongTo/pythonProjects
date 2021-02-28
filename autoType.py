from pynput.keyboard import Controller
import time

keyboard = Controller()

# Insert your string here
string = """
"""

time.sleep(1)

for i in string:
	keyboard.type(i)
	keyboard.release(i)
	time.sleep(0.02)   # choose type speed



