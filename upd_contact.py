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
cur.execute("select contact.contact_key from probirka_uuid.contact")
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
    ins = "update probirka_uuid.contact set contact_key_uuid = %s where contact_key = %s ";
    val = (users[i], i );
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    

    

print('customer inserted, affected rows: ')
print(rows)
print("########")