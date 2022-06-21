import urllib2
import sys
import os

def main(argv):
	video = ""
	name = ""
	if len(argv) < 2:
		video = raw_input("Enter Playlist URL: ")
		name = raw_input("Enter output name: ")
	else:
		video = argv[0]
		name = argv[1]
	playlist = urllib2.urlopen(video).read()
	parts = playlist.split("\n")
	segments = []
	for part in parts:
		if not "#" in part:
			segments.append(part)
	
	base_url = video[:video.rfind("/")] + "/"
	
	filename = name + ".ts"
	i = 1
	while os.path.exists(filename) and os.path.isfile(filename):
		filename = name + "-" + str(i) + ".ts"
		i = i + 1
	vid = open(filename, "wb")
	
	for segment in segments:
		part = urllib2.urlopen(base_url + segment).read()
		vid.write(part)
	vid.close()

if __name__ == "__main__":
	main(sys.argv[1:])