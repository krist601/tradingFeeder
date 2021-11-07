import http.client

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "a821b6def6msheed4829d62c0f7cp1f22f2jsne456f4e55f9d"
    }

conn.request("GET", "/query?interval=5min&function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&datatype=json&output_size=compact&slice=year1month1", headers=headers)

res = conn.getresponse()
dataString = res.read().decode("utf-8")

for line in dataString.splitlines() :
    dataSlipted = line.split(sep=",")
    print("date: "+dataSlipted[0])
    print("open: "+dataSlipted[1])
    print("high: "+dataSlipted[2])
    print("low: "+dataSlipted[3])
    print("close: "+dataSlipted[4])
    print("volume: "+dataSlipted[5])