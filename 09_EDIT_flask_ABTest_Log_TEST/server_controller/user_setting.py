from flask_login import UserMixin
from pymysql import NULL
from server_model.mysql import conn_mysqldb

MY_SALT_VALUE = 'SKSHIELDUS'

class User(UserMixin):
    
    def __init__(self, id, username, passwd):
        self.id = id
        self.username = username
        self.passwd = passwd

    def get_id(self):
        return str(self.id)
 
    @staticmethod
    def get(id):
        mysql_db = conn_mysqldb()
        mysql_db_cursor = mysql_db.cursor()
        sql = "SELECT * \
                FROM user_data_table \
                WHERE id = %s" % (id)
        mysql_db_cursor.execute(sql)
        user = mysql_db_cursor.fetchone()
        if not user:
            return None

        user = User(id=user[0], username=user[1], passwd=user[2])
        return user
    
    @staticmethod
    def find(username, passwd):
        mysql_db = conn_mysqldb()
        mysql_db_cursor = mysql_db.cursor()
        sql = "SELECT * \
                FROM user_data_table \
                WHERE user = '%s' \
                    and pw = '%s'" % (str(username), str(passwd))
        mysql_db_cursor.execute(sql)
        user = mysql_db_cursor.fetchone()
        if not user:
            return None
        
        user = User(id=user[0], username=user[1], passwd=user[2])
        return user
    
    @staticmethod
    def examine(username, password):
        print(username, password)
        mysql_db = conn_mysqldb()
        mysql_db_cursor = mysql_db.cursor()
        sql = """SELECT AES_DECRYPT(%s, 'SKSHIELDUS'), AES_DECRYPT(%s, SHA2('SKSHIELDUS',256))
                FROM user_data_table;""" % (str(username), str(password))
        print(sql)
        mysql_db_cursor.execute(sql)
        user = mysql_db_cursor.fetchone()
        if not user:
            return None
        print(user[0], user[1])
        print(user)
        user = User(id=NULL, username=user[0], password=user[1])
        return user
    
    # @staticmethod
    # def examine(username, passwd):
    #     mysql_db = conn_mysqldb()
    #     mysql_db_cursor = mysql_db.cursor()
    #     sql = "SELECT * \
    #             FROM user_info_table \
    #             WHERE username = '%s' \
    #                 and passwd = '%s'" % (str(username), str(passwd))
    #     mysql_db_cursor.execute(sql)
    #     user = mysql_db_cursor.fetchone()
    #     if not user:
    #         return None
        
    #     user = User(id=user[0], username=user[1], passwd=user[2])
    #     return user
    
        "INSERT INTO db_test.flask_table (email, passwd, bloodsugar, bloodtype, height, weight)\
        VALUES (AES_ENCRYPT('testEmail', SHA2('SALT',256)), \
                SHA2('testPasswd',256), \
                AES_ENCRYPT('testbloodsugar', SHA2('SALT',256)),\
                AES_ENCRYPT('testbloodtype', SHA2('SALT',256)), \
                AES_ENCRYPT('testheight', SHA2('SALT',256)), \
                AES_ENCRYPT('testweight', SHA2('SALT',256)));"
   
    @staticmethod
    def create(username, password):
        mysql_db = conn_mysqldb()
        mysql_db_cursor = mysql_db.cursor()
        sql = """INSERT INTO user_data_table (user, pw) \
                VALUES (AES_ENCRYPT("%s", "%s"), AES_ENCRYPT("%s", SHA2("%s",256)) )""" % (str(username), MY_SALT_VALUE, str(password), MY_SALT_VALUE)
        mysql_db_cursor.execute(sql)
        mysql_db.commit()
        
        # 생성된 정보에 대해 find(정보) 전달
        return User.find(username, password)
    
        # user = User.find(username)
        # if user == None:
        #     mysql_db = conn_mysqldb()
        #     mysql_db_cursor = mysql_db.cursor()
        #     sql = "INSERT INTO user_info_table (username) \
        #             VALUES ('%s')" % str(username)
        #     mysql_db_cursor.execute(sql)
        #     mysql_db.commit()
        #     return User.find(username)
        # else:
        #     return user # 이미 있던 것 return
            
    # mysql_db_cursor.close()