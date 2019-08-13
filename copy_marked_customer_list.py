import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## marced customer list
cur = conn.cursor();
cur.execute("select marked_customer_list.uuid, c.uuid from temp_uuid.marked_customer_list join temp_uuid.customer c on marked_customer_list.customer_id = c.id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.marked_customer_list(id, customer_id) values (%s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('marked customer list inserted, affected rows: ')
print(rows)
print("########")