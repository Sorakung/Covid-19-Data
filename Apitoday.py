import requests
import pandas as pd
import json
from pymongo import MongoClient 

url = 'https://covid19.th-stat.com/api/open/today'
response = requests.get(url)
data = response.text

data = pd.io.json.loads(response.text)
print(data)


with open('datatoday'+'.json', 'w') as outfile:
        json.dump(data, outfile)# save เป็นไฟล์ json



myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["todayTimeline"] 
Collection = db["datatoday"] 
with open('datatoday'+'.json') as file: 
    file_data = json.load(file)
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data)
    #เอาข้อมูลลง mongodb