import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## customer
cur = conn.cursor();
cur.execute("select customer.uuid, customer.customer_key, customer.version, customer.name, registry_number, customer_type, taxpayer_code, registration_code, registration_date, users.uuid, start_date, end_date, state from temp_uuid.customer join temp_uuid.users on users.id = user_edit_id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.customer(id, customer_key, version, name, registry_number, customer_type, taxpayer_code, registration_code, registration_date, user_edit_id, start_date, end_date, state) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('customer inserted, affected rows: ')
print(rows)
print("########")