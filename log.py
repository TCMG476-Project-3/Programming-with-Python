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

#2
Month_Jan = re.findall(r'Jan', response)
Month_Feb = re.findall(r'Feb', response)
Month_Mar = re.findall(r'Mar', response)
Month_Apr = re.findall(r'Apr', response)
Month_May = re.findall(r'May', response)
Month_Jun = re.findall(r'Jun', response)
Month_Jul = re.findall(r'Jul', response)
Month_Aug = re.findall(r'Aug', response)
Month_Sep = re.findall(r'Sep', response)
Month_Oct = re.findall(r'Oct', response)
Month_Nov = re.findall(r'Nov', response)
Month_Dec = re.findall(r'Dec', response) 

Jan = len(Month_Jan)
Feb = len(Month_Feb)
Mar = len(Month_Mar)
Apr = len(Month_Apr)
May = len(Month_May)
Jun = len(Month_Jun)
Jul = len(Month_Jul)
Aug = len(Month_Aug)
Sep = len(Month_Sep)
Oct = len(Month_Oct)
Nov = len(Month_Nov)
Dec = len(Month_Dec)

month = {"January" : Jan, "February" : Feb, "March" : Mar, "April" : Apr, "May" : May, "Jun" : Jun, "July" : Jul, "August" : Aug, "September" : Sep, "October" : Oct, "November" : Nov, "December" : Dec}

days = ()
days = re.findall(r'[0-9][0-9]\W[A-Z][a-z]\W[0-9][0-9][0-9][0-9]', response)

individual_days = set(days)

day_length = len(individual_days)

daydict = {}

for everyday in individual_days: 
    count = 0
    x = everyday
    for i in days: 
        if i == x:
            count = count + 1 
        daydict[x] = count

print ("\nDays:")
for a, b in daydict.items():
    print(a, b)

'''print (week)'''
print ("\nMonths:")

for x, y in month.items():
    print(x, y)