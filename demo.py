import mysql.connector

print("建立資料庫連線中")

# 若要連線至別人資料庫, 須請對方幫忙建立使用者與設定權限, 並提供Database的IP位置
cnx = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "dbuser",
    password = "1234",
    database = "world"
)

print("透過連線取得cursor物件")

dbcursor = cnx.cursor()

# 執行 select name from city
dbcursor.execute("select name from world.city")
for cityname in dbcursor:
    print(cityname)

print()

# 執行 select name, population from country
dbcursor.execute("select name, population from country")
for (c, p) in dbcursor:
    print(c, p)

dbcursor.close()
cnx.close()