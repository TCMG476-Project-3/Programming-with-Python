import urllib.request
import urllib.parse
import re

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
response = str(urllib.request.urlopen(url).read())

file = open("file.txt,", "w")
file.write(response)


#1
total = ()
total = re.findall(r' - - ', response)

print (len(total))
