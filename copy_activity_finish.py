import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)



## act finish
cur = conn.cursor();
cur.execute("select activity_finish.uuid, customer.uuid, registration_date, customer.registration_code from temp_uuid.activity_finish join temp_uuid.customer on customer.id = activity_finish.customer_id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.activity_finish values (%s, %s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('act finish inserted, affected rows: ')
print(rows)
print("########")
   
    

