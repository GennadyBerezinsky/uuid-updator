import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## oft
cur = conn.cursor();
cur.execute("select uuid, name, allias from temp_uuid.organisation_form_type")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.organisation_form_type(id, name, allias) values (%s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('oft inserted, affected rows: ')
print(rows)
print("########")