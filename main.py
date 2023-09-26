import psycopg2
import pandas as pd

conn = psycopg2.connect(database="jeremysingh",
                        host="localhost",
                        user="jeremysingh",
                        password="",
                        port="5432")

cursor = conn.cursor()

cursor.execute("SELECT * FROM spending")

#print(cursor.fetchone())
#print(cursor.fetchall())
#print(cursor.fetchmany(size=5))

sql_query = cursor.fetchall()

df = pd.DataFrame(sql_query, columns = ['id','date', 'city','cartype','exptype','gender','amount'])
print (df)