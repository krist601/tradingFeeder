symbol="MSFT"
classification="TECH"
python3 /Users/kscortesp/Documents/Other\ Projects/tradingProject/tradingFeeder/dropDatabase.py
python3 /Users/kscortesp/Documents/Other\ Projects/tradingProject/tradingFeeder/main.py $symbol $classification
mongodump -d tradingFeeder -o output/$symbol/dump