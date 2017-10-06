# The Moon Man knows all. He eats all.

# from bs4 import BeautifulSoup as bs
# import lxml
import requests
import re

page = requests.get('https://www.walmart.com/c/kp/microwave-meals')

# regex = "[0-9]+\.\d\d"
# prices = re.findall(regex,str(page.content))

# print(str(page.content))
# for price in prices:
	# print(prices.index(price),price)

# Find the URLy things based on the pattern we see. 
regex = "/ip/[A-Za-z0-9\-]+/[A-Za-z0-9\-]+"
urls = re.findall(regex,str(page.content))

# Iterate through the links to see the first instance of each link. Reduce index size to all unique links.
maximum = -1 # maximum index 
for urli in range(0,len(urls)-1):
	url = urls[urli]
	if urls.index(url) > maximum:
		maximum = urls.index(url)

url_branches = []

# Iterate through unique links and add to new list.
for i in range(0,maximum):
	subdir = 'https://www.walmart.com'+urls[i]
	print(subdir)
	url_branches.append(subdir)

# Once we are on the item page, otherwise known as the subdirectory, let's get the real info.
def subdirscrape_walmart(url):
	cost_cals_url = []
	page = requests.get(url)

	# Find the price
	regex = "title\=\"\$[0-9]+\.\d\d\""
	price = re.findall(regex,str(page.content)) # catch
	regex = "[0-9]+\.\d\d"
	price = re.findall(regex,price) # specify

	# Find the cals
	regex = "values\"\:\[\"[0-9]+ Calories" # catch
	cals = re.findall(regex,str(page.content))
	regex = "[0-9]+" # specify
	cals = re.findall(regex,cals)


subdirscrape_walmart("https://www.walmart.com/ip/Hormel-Compleats-Chicken-Breast-Mashed-Potatoes-13-oz-Tray/177829320")

