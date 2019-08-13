import mysql.connector
import uuid

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

users = dict()
## customer
cur = conn.cursor();
cur.execute("select customer.customer_key from probirka_uuid.customer")
res = cur.fetchall();
rows = 0
for str in res:  
     
    key = str[0];  
    if key not in users:
        uuid_str = uuid.uuid4().hex
        f = uuid_str[:8] + '-' + uuid_str[8:12] + '-' + uuid_str[12:16] + '-' + uuid_str[16:20] + '-' + uuid_str[20:]
        users[key] = f

        

print(users.values)

for i in users:
    print(i)    
    ins = "update probirka_uuid.customer set temp_customer_key_uuid = %s where customer_key = %s";
    val = (users[i], i );
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    

    

print('customer inserted, affected rows: ')
print(rows)
print("########")