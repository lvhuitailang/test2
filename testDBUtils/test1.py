import time
import  pymysql

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_DATABASE = 'test'
DB_CHARSET = 'utf8'

if '__main__' == __name__:
    db_params = {
        'host':DB_HOST,
        'user':DB_USER,
        'password':DB_PASSWORD,
        'port':DB_PORT,
        'charset':DB_CHARSET,
        'database':DB_DATABASE
    }


    startTime = time.time()

    conn = pymysql.connect(**db_params)
    cursor = conn.cursor()
    for x in range(100):
        sql = r'insert into user(name) values(%s)  '
        cursor.execute(sql,'wolfie')
        conn.commit()
    cursor.close()
    conn.close()




    endTime = time.time()
    print(endTime-startTime)


