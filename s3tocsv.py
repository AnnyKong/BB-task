from os import listdir
from os.path import isfile,join
import re
import csv

jpgs = [f for f in listdir('comp100/') if re.match(r'[0-9]+.*\.jpg', f)]

s3jpgs = ["https://s3-us-west-2.amazonaws.com/slowglass-testamk/comp100/" + str(f) for f in jpgs]
s3jpgs = sorted(s3jpgs)
jpgcsv = [[] for i in range(11)]

# initialize header
#jpgcsv.append([])
for i in range(10):
	jpgcsv[0].append('image_url'+str(i+1))

# fill in lines
for i in range(len(s3jpgs)):
  f = s3jpgs[i]
  line = jpgcsv[i%10+1]
  print(f)
  line = line.append(f)

print("Total: " + str(len(jpgs)));

with open('comp100.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(jpgcsv)

