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
cur.execute("select address.address_key from probirka_uuid.address")
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
    ins = "update probirka_uuid.address set temp_address_key_uuid = %s where address_key = %s";
    val = (users[i], i );
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    

    

print('customer inserted, affected rows: ')
print(rows)
print("########")