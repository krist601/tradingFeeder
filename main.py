import http.client
from pymongo import  MongoClient
import sys
import time

######### INPUTS #########

symbol = sys.argv[1]
classification = sys.argv[2]

######### API CONNECTION CONFIGURATION #########

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "a821b6def6msheed4829d62c0f7cp1f22f2jsne456f4e55f9d"
    }

######### DATABASE CONFIGURATION #########

client = MongoClient('localhost')
db = client['tradingFeeder']
col = db['StockPrice']

######### YEAR-MONTH LOOP #########

for year in ["1", "2"]:
    for month in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:

        ######### REQUEST #########

        conn.request("GET", "/query?interval=5min&function=TIME_SERIES_INTRADAY_EXTENDED&symbol="+symbol+"&datatype=json&output_size=compact&slice=year"+year+"month"+month, headers=headers)
        res = conn.getresponse()
        dataString = res.read().decode("utf-8")

        ######### INSERT INTO DATABASE #########

        for line in dataString.splitlines()[1:10] :
            dataSlipted = line.split(sep=",")
            col.insert_one({
                "symbol": symbol,
                "classification": classification,
                "date": dataSlipted[0],
                "open": dataSlipted[1],
                "high": dataSlipted[2],
                "low": dataSlipted[3],
                "close": dataSlipted[4],
                "volume": dataSlipted[5]
            })
        
        print("DONE: "+symbol+" year " + year + " - month " + month)
        time.sleep(15)
    
print("DATABASE INSERTIONS DONE")
#print(client.list_database_names())
#print(db.list_collection_names())
cursor = col.find({})
for document in cursor:
    print(document)