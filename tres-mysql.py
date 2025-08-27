import mysql.connector

cnx = mysql.connector.connect(user='root', password='rootd1n',
                              host='localhost',
                              database='prueba')

mycursor = cnx.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

mycursor = cnx.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM employees")
for x in mycursor:
  print(x)


mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM employees")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


#mycursor = cnx.cursor()
#mycursor.execute("SELECT * FROM G_finales")
#myresult = mycursor.fetchone()
#print(myresult)


#print("-----------------------------------")
print("-----------------------------------")
mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM employees where name='Roger Federer'")
for x in mycursor:
  print(x)


print("-----------------------------------")
mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM employees where name='Roger Federer'")
for x in mycursor:
  print(x)

print("-----------------------------------")
mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM employees where name like '%oger%'")
for x in mycursor:
  print(x)

# Print results in comma delimited format
print("-----------------------------------")
mycursor.execute("SELECT * FROM employees")
rows = mycursor.fetchall()
for row in rows:
    for col in row:
        print("%s," % col)
    print("\n")


cnx.close()
