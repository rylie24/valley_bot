import mysql.connector

conn = mysql.connector.connect(
    host="db-mfl-01.sparkedhost.us",
    port=3306,
    user="u174976_5ULhqRPzsW",
    passwd="4n+0pw+D45fJmG2Y^3u2ZXU+",
)

cursor = conn.cursor()
