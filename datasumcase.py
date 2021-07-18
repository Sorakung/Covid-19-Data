import json
import pandas as pd


with open('datasumcase.json', encoding= 'UTF-8') as f :
    s = f.read()
data = json.loads(s)#เปลี่ยนเป็น dict เพื่อให้เข้าถึงข้อมูลภายในได้


df = pd.DataFrame(columns= ['Province', 'SumP','Level'] )
for x in data['Province'].items():
     
    Province = x[0]
    if Province == 'Unknown':
        Province = 'Bueng Kan'
    SumP = x[1]
    if SumP == 0:#  0 คน
        level = 1
    elif SumP <=10:# 1-10
        level = 2
    elif SumP <=50:#11-50
        level = 3
    elif SumP > 51:#   >51
        level = 4 
    new_column = pd.Series([Province,SumP,level], index=df.columns)
    df = df.append(new_column,ignore_index=True)

df.to_excel('datasumcase.xlsx')