import pymongo
import pandas as pd
import csv
import json
import sys, getopt, pprint
from config import MONGO_URI

myclient = pymongo.MongoClient(MONGO_URI)



dblist = myclient.list_database_names()
if "data" in dblist:
  print("The database exists.")

mydb = myclient["data"]
mycol = mydb["data"]




print(dblist)




#CSV to JSON Conversion
csvfile = open('battles.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=pymongo.MongoClient(MONGO_URI)
db=mongo_client.data
db.segment.drop()
header= ["name","year","battle_number","attacker_king","defender_king","attacker_1","attacker_2","attacker_3","attacker_4","defender_1","defender_2","defender_3","defender_4","attacker_outcome","battle_type","major_death","major_capture","attacker_size","defender_size","attacker_commander","defender_commander","summer","location","region","note"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.segment.insert(row)