# http://www.pythonchallenge.com/pc/def/channel.html
import zipfile, re

def nextNothing(text):
    filter = re.compile("\d+$")
    findtext = re.findall(filter, text)
    if len(findtext) == 1:
        return findtext[0]
    else:
        return ""

zipFile = zipfile.ZipFile("channel.zip", "r")

nothing = "90052"
result = ""
while True:
    filename = str(nothing) + ".txt"
    text = zipFile.read(filename)
    # answer is in zip
    result += zipFile.getinfo(filename).comment
    # next nothing is:
    nothing = nextNothing(text)
    if nothing == "":
        break

print result
