import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## address
cur = conn.cursor();
cur.execute("select address.uuid, address_key, version, customer_key, address_type, r.uuid, c.uuid, d.uuid, address_name, income_date, income_number, u.uuid, start_date, end_date, state from temp_uuid.address join temp_uuid.city c on address.city_id = c.id join temp_uuid.region r on address.region_id = r.id join temp_uuid.district d on address.district_id = d.id join temp_uuid.users u on address.user_edit_id = u.id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.address values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('address inserted, affected rows: ')
print(rows)
print("########")