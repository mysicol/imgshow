import os
from PIL import Image

# -- ADJUST CHARSET HERE!!! --
charset = ['0', '*', 'o', '.', ' ']

# determine brightness interval based on charset
brightness_interval = int(255 / len(charset)) + 1

# get input and wipe terminal
filename = input("Enter image filepath: ")
os.system('clear')

# get terminal dimensions
width = os.get_terminal_size().columns
height = os.get_terminal_size().lines - 1

# open image
try:
    im = Image.open(filename)
except(FileNotFoundError):
    for _ in range(height - 1):
        for _ in range(int(width/6)):
            print("ALERT!", end="")
        print()
    print("why did you enter an image that doesnt exist")
    quit()

# set image dimensions to scale if we can in the terminal window
scaled_height = round(im.size[1] * (width / im.size[0]))
if scaled_height < height:
    height = scaled_height

# resize and grayscale the image
im = im.resize((width, height)).convert('L').load()

# print image
for i in range(height):
    for j in range(width):
        pix = im[j, i]
        
        # choose character based on pixel brightness
        repr_char = charset[len(charset) - 1]

        for n in range(len(charset)):
            if pix < brightness_interval * (n+1):
                repr_char = charset[n]
                break

        print(repr_char, end="")
    print()