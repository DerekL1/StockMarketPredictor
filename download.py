import urllib.request, urllib.error, csv

# access the list of all active and deprecated companies in the history of the S&P500
downloads = open("all500.csv", "r")
reader = csv.reader(downloads)
deprecated = open("deprecated.csv", "w")
writer = csv.writer(deprecated, lineterminator="\n")

for row in reader:
    #get the ticker and download link for the company
    ticker = row[0]
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=0&period2=2000000000&interval=1d&events=history&includeAdjustedClose=true"
    try: # try retrieving the download
        urllib.request.urlretrieve(url, f'/Users/derek/Projects/StockMarketPredictor/data/{ticker}.csv')
    except urllib.error.HTTPError as e: #if it doesn't work, add the ticker to the deprecated file
        writer.writerow([ticker])

downloads.close()
deprecated.close()