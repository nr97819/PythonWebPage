from flask import Flask, render_template, request
import pymysql

KEY = 'SKshieldusKEY'
app = Flask(__name__)

MYSQL_HOST = 'test-1.cpoaafcf6ree.ap-northeast-2.rds.amazonaws.com'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='admin',
    passwd='tkrwp911',
    db='db_test',
    charset='utf8'
)

def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN

def SQL_SELECT():
	db_cursor = conn_mysqldb().cursor()
	sql = """SELECT id, email, passwd
	FROM flask_table"""
	db_cursor.execute(sql)
	user = db_cursor.fetchall()
	if not user:
		db_cursor.close()

	for e in user:
		print(e)
	db_cursor.close()

def SQL_SELECT_LOGIN(email, passwd):
	db_cursor = conn_mysqldb().cursor()
	sql = """SELECT CONVERT(AES_DECRYPT(email, SHA2('key',256)) using UTF8)
	FROM flask_table
	WHERE email=%s and passwd=%s"""
	db_cursor.execute(sql, email, passwd)
	user = db_cursor.fetchall()
	if not user:
		db_cursor.close()

	for e in user:
		print(e)
	db_cursor.close()

def SQL_INSERT(username, password):
	db = conn_mysqldb()
	db_cursor = db.cursor()
	sql = """insert into flask_table(email, passwd)
     		values (SHA2(%s,'256'), AES_ENCRYPT(%s, SHA2(%s,256)))"""
	"""
	INSERT INTO db_test.flask_table (email, passwd, bloodsugar, bloodtype, height, weight)
	VALUES (AES_ENCRYPT('testEmail', SHA2('SALT',256)), 
			SHA2('testPasswd',256), 
			AES_ENCRYPT('testbloodsugar', SHA2('SALT',256)),
			AES_ENCRYPT('testbloodtype', SHA2('SALT',256)), 
			AES_ENCRYPT('testheight', SHA2('SALT',256)), 
			AES_ENCRYPT('testweight', SHA2('SALT',256)));"""
	db_cursor.execute(sql, (username, password, KEY))
	db.commit()
	db_cursor.close()

@app.route('/', methods=['GET','POST']) # 접속할 URL
def main():
	return render_template('index.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
	if request.method =='GET':
		return render_template('index.html')
		
	elif request.method =='POST':
		SQL_SELECT_LOGIN()


		return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method =='GET':
		return render_template('register.html')
		
	elif request.method =='POST':
		username = request.form['username']
		password = request.form['password']
		# print(username)
		# print(password)
		SQL_INSERT(username, password)
		return render_template('complete.html')

# @app.route('/complete', methods=['GET','POST'])
# def complete():
# 	if request.method =='GET':
# 		return render_template('complete.html')

@app.route('/agreement', methods=['GET','POST']) # 개인 정보 동의 페이지
def agree():
	if request.method =='GET':
		return render_template('agreement.html')
		
	elif request.method =='POST':
		return render_template('index.html')

@app.route('/uploading', methods=['GET','POST']) # 진단서 업로드 페이지
def upload():
	if request.method =='GET':
		return render_template('uploading.html')
		
	elif request.method =='POST':
		return render_template('index.html')

@app.route('/products', methods=['GET','POST']) # 상품 목록 페이지
def product():
	if request.method =='GET':
		return render_template('products.html')
		
	elif request.method =='POST':
		return render_template('index.html')

if __name__ == '__main__':
	SQL_SELECT()
	# SQL_INSERT()
	app.run(host='0.0.0.0', debug=True)