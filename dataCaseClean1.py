import json
import pandas as pd
from pymongo import MongoClient 

with open('datacase.json', encoding= 'UTF-8') as f :
    s = f.read()
data = json.loads(s)

df = pd.DataFrame(columns= ['Case'] )

at = data['Data']

new_column = pd.Series([at], index=df.columns)
df = df.append(new_column,ignore_index=True)

df.to_json('dataCaseClean1.json')
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["DBCaseC"] 
Collection = db["dataCase"] 
with open('dataCaseClean1'+'.json') as file: 
    file_data = json.load(file)
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data)