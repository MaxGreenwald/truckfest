import requests


access_token = "CAACEdEose0cBAO52Np88l71ePUD3mbQJ2VqebkZCgnAZApd2B8uTpBHulZA1V7PXjGwQpbayZBQJaSCcccNOjZB47q4XZAoGORWX16U9yOid3aKvLX1GYm2NOH83IoKHkKZAEWBtbHmzld8Uun26jswINmSZCw4ZBh3Q6FouLZCUoa0bpJMkaZCesvDdFRf2A56P8WjkXksUpuwYAZDZD"
with open("urls.txt", "r") as f:
	for url in f.readlines():
		pagename = url.strip().replace("https://www.facebook.com/", "").replace("/", "")
		with open(pagename + ".png", "w") as imagefile:
			r = requests.get("https://graph.facebook.com/v2.5/" + pagename + "/picture?height=500&access_token=" + access_token)
			print r.headers['content-type']
			if r.headers['content-type'] == "application/json; charset=UTF-8":
				print r.json()
			imagefile.write(r.content)


