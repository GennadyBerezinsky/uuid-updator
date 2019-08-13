import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## users
cur = conn.cursor();
cur.execute("select * from temp_uuid.users")
res = cur.fetchall();
rows = 0
for str in res:
    uuid = str[4]    
    login = str[1]
    passw = str[2]
    name = str[3]
    

    ins = "insert into probirka_uuid.users(id, login, password, name) values (%s, %s, %s, %s);"
    val = (uuid, login, passw, name);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('users inserted, affected rows: ')
print(rows)
print("########")

## users history
cur = conn.cursor();
cur.execute("select users_history.uuid, users.uuid as user_id, login_date from temp_uuid.users_history join temp_uuid.users on users_history.user_id = users.id")
res = cur.fetchall();
rows = 0
for str in res:  

    ins = "insert into probirka_uuid.users_history(id, user_id, login_date) values (%s, %s, %s);"
    val = (str[0], str[1], str[2]);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('users history inserted, affected rows: ')
print(rows)
print("########")