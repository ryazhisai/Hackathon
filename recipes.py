import requests
import json
import sqlite3 as sl

url = "http://www.recipepuppy.com/api/."

querystring = {"url":"http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3"}


response = requests.request("GET", url,params=querystring)

json_obj=json.loads(response.text)

data_list= []
n=1
for data in (json_obj['results']):
    #print (data['regionName'])
    #print (data['casesCount'])
    #print (data['recoveredCount'])
    # print (data['deceasedCount'])
    rec= (n, data['title'], data['ingredients'])
    n= n+1
    data_list.append(rec)

con = sl.connect('recipe.db')

try:
    with con:
        con.execute("""
        CREATE TABLE RECIPES (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            ingredients TEXT
            );
    """)
except:
    print  ('This table already exists')

    sql = 'INSERT INTO RECIPES (id, title, ingredients) values(?, ?, ?)'

with con:
    con.executemany(sql, data_list)
with con:
        data = con.execute("SELECT * FROM RECIPES")
for row in data:
        print(row)