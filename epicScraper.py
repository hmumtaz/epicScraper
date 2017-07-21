import requests
import os
import sys
import json
import datetime
import urllib
from dateutil import parser




"""
Pulls the latest published images of Earth from NASA's EPIC project.
"""
def main():
	localDir = "" #Local directory you want to save images to
	try:
		files = [f for f in os.listdir(localDir)]
	except (WindowsError):
		print ("Please edit line 16 to include your local directory")
		sys.exit(0)
	#Uncomment line below if you wish to remove old files when fetching new ones
	#deleteOldFiles(localDir)
	fetched = requests.get(
		"https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY")
	data = json.loads(fetched.content)
	date = parser.parse(data[0]["date"])
	formattedDate = dateFormatter(date)
	for item in data:
		name = item['image'] + ".jpg"
		url = "https://epic.gsfc.nasa.gov/archive/natural/" \
			+ formattedDate + "/jpg/" + name
		localName = localDir + name
		urllib.urlretrieve(url, localName)


"""
Helper method for formatting date properly

Parameters
------------
date : dateTime
	the date being formatted
"""
def dateFormatter(date):
	year = str(date.year)
	month = str(date.month)
	day = str(date.day)
	if len(month) == 1:
		month = '0' + month
	if len(day) == 1:
		day = '0' + day
	formattedDate = year + '/' + month + '/' + day
	return formattedDate

"""
Helper method for removing old files from a directory

Parameters
-----------
directory : string
	the directory we are emptying

"""
def deleteOldFiles(directory):
	files = [f for f in os.listdir(directory)]
	for file in files:
		localFile = directory + file
		os.remove(localFile)

main()
