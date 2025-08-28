import mysql.connector

cnx = mysql.connector.connect(user='root', password='rootd1n',
                              host='192.168.1.124',
                              database='gestorpbf')

mycursor = cnx.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

mycursor = cnx.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM G_finales")
for x in mycursor:
  print(x)


mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM G_finales")
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
mycursor.execute("SELECT * FROM G_finales where valor=5")
for x in mycursor:
  print(x)


print("-----------------------------------")
mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM G_finales where nombre='Agendado'")
for x in mycursor:
  print(x)

print("-----------------------------------")
mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM G_finales where nombre like '%feren%'")
for x in mycursor:
  print(x)

# Print results in comma delimited format
print("-----------------------------------")
mycursor.execute("SELECT * FROM G_finales")
rows = mycursor.fetchall()
for row in rows:
    for col in row:
        print("%s," % col)
    print("\n")


cnx.close()
