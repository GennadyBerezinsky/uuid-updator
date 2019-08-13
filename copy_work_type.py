import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## city
cur = conn.cursor();
cur.execute("select uuid, name from temp_uuid.work_type")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.work_type(id, name) values (%s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('work type  inserted, affected rows: ')
print(rows)
print("########")