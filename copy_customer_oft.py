import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

## city
cur = conn.cursor();
cur.execute("select customer_organisation_form_info.uuid, customer.uuid, oft.uuid from temp_uuid.customer_organisation_form_info join temp_uuid.customer on customer.id = customer_id join temp_uuid.organisation_form_type oft on customer_organisation_form_info.organisation_form_id = oft.id")
res = cur.fetchall();
rows = 0
for str in res:    
    

    ins = "insert into probirka_uuid.customer_organisation_form_info(id, customer_id, organisation_form_id) values (%s, %s, %s);"
    val = (str);
    insCur = conn.cursor();
    insCur.execute(ins, val)
    conn.commit()
    rows += insCur.rowcount

print('reg inserted, affected rows: ')
print(rows)
print("########")