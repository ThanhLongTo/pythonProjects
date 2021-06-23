from PIL import Image
import os
from pynput.mouse import Listener

'''
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
'''

print(os.listdir("C:\\Users\\PC\\Pictures\\everglowTab"))

original_dir = os.listdir("C:\\Users\\PC\\Pictures\\everglowTab")

i = 0 
for i in range(len(original_dir)):
    test_image = "C:\\Users\\PC\\Pictures\\everglowTab\\" + str(original_dir[i])
    original = Image.open(test_image)

    left = 0
    top = 556
    right = 1180
    bottom = 770
    cropped_example = original.crop((left, top, right, bottom))
    cropped_example = cropped_example.convert('RGB')
    cropped_example.save("C:\\Users\\PC\\Pictures\\Images\\tab{}.pdf".format(i))
    print("Image {} saved".format(i))
    i += 1


#(126, 532)
#(1082, 705)