# This program wraps inputted text into the shape of the map.png image.
# Any non-white pixel
# Try editing the png file pixel by pixel! (using paint or something)
# I wonder why you are here

from PIL import Image

img_map = Image.open("map.png")
img_pixelarr = list(img_map.getdata())
img_pixels = img_map.load()#image[x,y] => (r,g,b,a)

width, height = img_map.size
MAP = """"""

def myround(num, base): #round down to the nearest base (for calculating the current row of given pixel index)
    return base * int(num/base)

for y in range(height):
    for x in range(width): 
        distance_from_next_row = (myround(x,width) + width - x)
        if img_pixelarr[x:myround(x,width)][0:3] == ((255,255,255),)* distance_from_next_row:
            #skip this row if the remaining pixels in it are all white
            break

        if img_pixels[x,y] == (255,255,255,255):#all white
            MAP += ' '
        else:
            MAP += '#'

    MAP += '\n'


text = input("Enter some text: ")
i = 0 #counter to keep track of what is selected

def place(char):#don't want to say end = '' everytime
    print(char, end = '')
  
for c in MAP:
    i %= len(text)
    if c == '#':
        place(text[i])
        i += 1
    else:
        place(c)

input("Press enter to exit!")
