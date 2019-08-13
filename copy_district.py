import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## district
cur = conn.cursor();
cur.execute("select district.uuid, city.uuid, district.name from temp_uuid.district join temp_uuid.city on city.id = city_id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.district(id, city_id, name) values (%s, %s, %s);"
    val = (str[0], str[1], str[2]);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('dictrict inserted, affected rows: ')
print(rows)
print("########")