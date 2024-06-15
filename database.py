import mysql.connector, csv
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5888",
    database="stock_market_predictor"
)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("DROP TABLE stocks")
mycursor.execute("CREATE TABLE stocks (ticker VARCHAR(255), day DATE, open DOUBLE(20, 10), high DOUBLE(20, 10), low DOUBLE(20, 10), close DOUBLE(20, 10), adj_close DOUBLE(20, 10), volume INT(255))")

file = open("all500.csv", "r")
reader = csv.reader(file)
for r in reader:
    ticker = r[0]
    data = open(f"data/{ticker}.csv")
    data_reader = csv.reader(data)
    next(data_reader)
    for row in data_reader:
        mycursor.execute(f"INSERT INTO stocks VALUES (\"{ticker}\", \"{row[0]}\", {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]})")
file.close()

mydb.commit()