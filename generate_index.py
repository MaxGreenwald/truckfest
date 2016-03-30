import re
import csv
import requests
from jinja2 import Template

			


def downloadFBPicture(fburl):
	access_token = "EAACEdEose0cBAJM0ZC7XajULVgH1ZBvhYIXLoCKnYeJVl1ccZCPV42WbzAzfTZC2QoK7RLT0bgUhHLfu5yBl6weNZAlFnFQlm8qrv62zV8BnZBrMkX0IQxoazzwX5jWZC7kTrCvZAVhVIljGXvzZB8crNINZBtMKKXmM9m9bB7MSNI6QZDZD"
	pagename = fburl.strip().replace("https://www.facebook.com/", "").replace("/", "")
	if "-" in pagename:
		pagename = pagename.split("-")[-1]

	with open("img/portfolio/" + pagename + ".png", "w") as imagefile:
		r = requests.get("https://graph.facebook.com/v2.5/" + pagename + "/picture?height=500&access_token=" + access_token)
		imagefile.write(r.content)

	return pagename + ".png"



def getTrucksInfo():
	with open("Truck Information - SOCIAL MEDIA.csv") as f1:
		with open("Truck Information - MENUS.csv") as f2:
			socialMedia = list(csv.reader(f1))[1:]
			menus = list(csv.reader(f2))[1:]
			allTrucks = []


			# Get Social Media Data
			for s in socialMedia:

				truck = {
							'name': 	s[0], 
							'picture': 	"", 
							'url':		s[4], 
							'facebook':	s[3], 
							'menu': []
						}
				if truck['name'] == "Bombay Local Pizza":
					truck['picture'] = "BombayLocalPizza.png"
				else:
					truck['picture'] = downloadFBPicture(s[3])

				if truck['name'] == "Princeton University Food Truck":
					truck['picture'] = "princetonfoodtruck.png"
				allTrucks.append(truck)


			# Get Menu Data
			for i, menu in enumerate(menus):
				assert allTrucks[i]['name'] == menu[0]				# assert that names are accurate
				price_re = re.compile("\(.*(\$|\?).*?\)")
				
				for item in menu[1:-1]:								# last item is "utensils"
					price = ""
					match = re.match(price_re, item)
					if match != None:
						price = match.group(0)
						item = item.replace(price, "")
					allTrucks[i]['menu'].append({'name': item, 'price': price})



			return allTrucks








# Main
with open("template.html", "r") as t:
	template = Template(t.read())
	index = template.render(trucks=getTrucksInfo())

	with open("index.html", "w") as generated:
		generated.write(index)




