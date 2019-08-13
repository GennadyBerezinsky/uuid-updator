import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## city
cur = conn.cursor();
cur.execute("select document.uuid, customer_key, document.name, path, u.uuid, state from temp_uuid.document join temp_uuid.users u on document.user_edit_id = u.id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.document values (%s, %s, %s, %s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('reg inserted, affected rows: ')
print(rows)
print("########")