import pymysql

MYSQL_HOST = 'test-1.cpoaafcf6ree.ap-northeast-2.rds.amazonaws.com'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='admin',
    passwd='tkrwp911',
    db='db_test',
    charset='utf8'
)

status='GOOD'
def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
        print(status)
    return MYSQL_CONN

user_id='1111'

db_cursor = conn_mysqldb().cursor()
sql = "SELECT * FROM my_test_table"
db_cursor.execute(sql)
user = db_cursor.fetchall()
if not user:
    db_cursor.close()

for e in user:
    print(e)
db_cursor.close()