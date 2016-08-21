import urllib2
from HTMLParser import HTMLParser
import sys
import subprocess
import os
import json
import urllib
import playlistdown

def hmsToSec(hms):
	#Works for HH:MM:SS and MM:SS
	split = hms.split(":")
	rate = 1
	total = 0
	for part in reversed(split):
		total = total + rate * int(part)
		rate = rate * 60
	return total

def main(argv):
	video = ""
	if len(argv) == 0:
		video = raw_input("Enter Funimation URL: ")
	else:
		video = argv[0]
	
	try:
		page = urllib2.urlopen(video).read()
	except:
		print "Error getting video. Please confirm video ID"
		return
	
	id = page[page.find("FUNImationID")+15:page.find("FUNImationID")+31]
	token = page[page.find("authToken")+12:]
	token = token[:token.find("\"")]
	url = "http://wpc.8c48.edgecastcdn.net/038C48/SV/480/" + id + "/" + id + "-480-750K.mp4.m3u8" + token
	title = video[video.rfind("/")+1:]
	if "?" in title:
		title = title[:title.find("?")]
	
	try:
		playlistdown.main([url, title])
	except urllib2.HTTPError as e:
		#Ahahaha fuck handling errors
		if e.code != 403:
			raise e
	return
			

if __name__ == "__main__":
	main(sys.argv[1:])