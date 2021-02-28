from pynput.keyboard import Controller
import time

keyboard = Controller()

string = """If he needs a million acres to make him feel rich, seems to me he needs it 'cause he feels awful poor inside hisself, and if he's poor in hisself, there ain't no million acres gonna make him feel rich, an' maybe he's disappointed that nothin' he can do'll make him feel rich.
"""

time.sleep(1)

for i in string:
	keyboard.type(i)
	keyboard.release(i)
	time.sleep(0.02)



