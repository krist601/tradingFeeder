from pymongo import  MongoClient

######### DATABASE CONFIGURATION #########

client = MongoClient('localhost')
db = client['tradingFeeder']
col = db['StockPrice']

col.delete_many({})
print("DATABASE DROPPED")