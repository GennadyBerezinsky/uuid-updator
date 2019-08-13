import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## city
cur = conn.cursor();
cur.execute("select marked_address_list.uuid, a.uuid from temp_uuid.marked_address_list join temp_uuid.address a on marked_address_list.address_id = a.id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.marked_address_list values (%s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('reg inserted, affected rows: ')
print(rows)
print("########")