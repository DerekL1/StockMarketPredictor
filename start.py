# import required modules
from bs4 import BeautifulSoup
import requests, csv
 
# scrape S&P500 list from Wikipedia
page = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
soup = BeautifulSoup(page.content, 'html.parser')

# find location in HTML of current S&P500 companies
object = soup.find(id="constituents")
items = object.find_all(class_="external text")

# add all the current S&P500 companies
current500 = set()
for result in items:
    current500.add(result.text)

# find location in HTML of removed S&P500 companies
object = soup.find(id="changes")
items = object.find_all("td")

# add all removed S&P500 companies
removed500 = set()
counter = 3
for result in items:
    if counter == 6:
        counter = 0
        removed500.add(result.text.replace("\n", ""))
    counter = counter + 1
removed500.remove("")

# combine both sets to create a history of companies in the S&P500
all500 = current500.union(removed500)

#retrieve the list of tickers that are no longer valid
deprecated = set()
file = open("deprecated.csv", "r")
reader = csv.reader(file)
for row in reader:
    deprecated.add(row[0])

#create an alphabetical list of all active tickers in the history of the S&P500
allActive500 = all500 - deprecated
sorted500 = sorted(allActive500)

#write this list to a file
file = open("all500.csv", "w")
writer = csv.writer(file, lineterminator="\n")
for ticker in sorted500:
    writer.writerow([ticker])

file.close()