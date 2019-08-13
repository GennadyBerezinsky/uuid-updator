import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## contact
cur = conn.cursor();
cur.execute("select uuid, contact_key, version, customer_key, phone_number, email, start_date, end_date from temp_uuid.contact")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.contact(id, contact_key, version, customer_key, phone_number, email, start_date, end_date) values (%s, %s, %s, %s, %s, %s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('contact inserted, affected rows: ')
print(rows)
print("########")