# http://www.pythonchallenge.com/pc/def/hockey.html
# http://www.pythonchallenge.com/pc/def/oxygen.html
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
from PIL import Image, ImageDraw

# get image text
img = Image.open("oxygen.png")
y = (height/2)
result = ""
for x in range (0, width, 7):
    pixel = img.getpixel((x,y))
    result += chr(pixel[0])
print (result)
img.close()

# get key word from hint
array = [105, 110, 116, 101, 103, 114, 105, 116, 121]
nextWord = ""
for item in array:
    nextWord += chr(item)
print (nextWord)
