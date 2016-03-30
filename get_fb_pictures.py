import requests


with open("urls.txt", "r") as f:
	for url in f.readlines():
		pagename = url.strip().replace("https://www.facebook.com/", "").replace("/", "")
		if "-" in pagename:
			pagename = pagename.split("-")[-1]
			
		with open(pagename + ".png", "w") as imagefile:
			r = requests.get("https://graph.facebook.com/v2.5/" + pagename + "/picture?height=500")
			if r.headers['content-type'] == "application/json; charset=UTF-8":
				print r.json()
			imagefile.write(r.content)


