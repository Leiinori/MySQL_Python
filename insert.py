import mysql.connector

print("建立資料庫連線中")

# 若要連線至別人資料庫, 須請對方幫忙建立使用者與設定權限, 並提供Database的IP位置
cnx = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "dbuser",
    password = "1234",
    database = "prize"
)

print("透過連線取得cursor物件")

dbcursor = cnx.cursor()

# 執行 insert into lottery(n1, n2, n3, n4, n5, n6) value(%s, %s, %s, %s, %s, %s)
print("執行insert")

insertSQL = "insert into lottery(n1, n2, n3, n4, n5, n6) value(%s, %s, %s, %s, %s, %s)"
parserdata = (11, 3, 19, 42, 37, 20)

dbcursor.execute(insertSQL, parserdata)
print("完成交易 確定要寫入資料庫")
cnx.commit()    #沒commit就不寫入

dbcursor.close()
cnx.close()