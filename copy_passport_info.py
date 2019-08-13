import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## passport 
cur = conn.cursor();
cur.execute("select passport_info.uuid, c.uuid, info from temp_uuid.passport_info join temp_uuid.customer c on passport_info.custimer_id = c.id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.passport_info values (%s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('passport inserted, affected rows: ')
print(rows)
print("########")