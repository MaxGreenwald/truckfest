import csv
import re


def createtable(truck):
    price_re = re.compile("""\(.*(\$|\?).*?\)""")
    table = """
  <h3 style="text-align:center">%s</h3>         
  <table class="table">
    <thead>
        <tr>
        <th style="text-align:center">Item(s)</th>
        <th style="text-align:center">Price</th>
        </tr>
    </thead>
    <tbody>
    """ % (truck[0])
    truck = truck[1:]

    for t in truck:
        if t == "":
            continue
        match = re.match(price_re, t)
        price = ""
        item = t
        if match != None:
            price = match.group(0)
            item = t.replace(price, "")

        table += """
      <tr>
        <td>%s</td>
        <td>%s</td>
      </tr>
      """ % (item, price)


    table += """
        </tbody>
  </table>
    """
    return table.replace("&", "&amp;")



tobeReplaced = "<p>Use this area of the page to describe your project. The icon above is part of a free icon set by <a href=\"https://sellfy.com/p/8Q9P/jV3VZ/\">Flat Icons</a>. On their website, you can download their free set with 16 icons, or you can purchase the entire set with 146 icons for only $12!</p>"

with open("Truck Information - MENUS.csv", "r") as csvfile:
    with open("index.html", "r+") as index:
    	with open("index_new.html", "w") as new_index:
	        webpage = index.read()
	        menus = list(csv.reader(csvfile))
	        for truck in menus[1:]:
	            webpage = webpage.replace(tobeReplaced, createtable(truck), 1)
	        new_index.write(webpage)




