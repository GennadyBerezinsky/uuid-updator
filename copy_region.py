import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## region
cur = conn.cursor();
cur.execute("select * from temp_uuid.region")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.region(id, name) values (%s, %s);"
    val = (str[2], str[1]);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('city inserted, affected rows: ')
print(rows)
print("########")