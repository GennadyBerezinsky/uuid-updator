import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## city
cur = conn.cursor();
cur.execute("select address_work_type_list.uuid, wt.uuid, a.uuid from temp_uuid.address_work_type_list join temp_uuid.address a on address_work_type_list.address_id = a.id join temp_uuid.work_type wt on address_work_type_list.work_type_id = wt.id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.address_work_type_list values (%s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('awtl inserted, affected rows: ')
print(rows)
print("########")