import tkinter as tk
import pymysql
from  hashlib import sha1
import hashlib

class MysqlHelper:
    def __init__(self,host='118.25.217.90',port=3306,db='test',user='root',passwd='djyiL%;j.3:4_',charset='utf8'):
        self.conn=pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset=charset)

    def insert(self,sql,params):
        return self.__cud(sql,params)

    def update(self,sql,params):
        return self.__cud(sql,params)

    def delete(self,sql,params):
        return self.__cud(sql,params)

    def my_md5(self, pwd):
        my_md5 = hashlib.md5()
        my_md5.update(pwd.encode('utf-8'))
        return my_md5.hexdigest()

    def __cud(self,sql,params=[]):
        try:
            #用来获得python执行Mysql命令的方法,也就是我们所说的操作游标
            #cursor 方法将我们引入另外一个主题：游标对象。通过游标扫行SQL 查询并检查结果。
            #游标连接支持更多的方法，而且可能在程序中更好用。
            cs1 = self.conn.cursor()
            #真正执行MySQL语句
            rows=cs1.execute(sql, params)
            self.conn.commit()
            #完成插入并且做出某些更改后确保已经进行了提交，这样才可以将这些修改真正地保存到文件中。
            cs1.close()
            self.conn.close()
            return rows #影响到了哪行
        except Exception as e:
            print (e)
            self.conn.rollback()

    def fetchone(self, sql, params=[] ):
        #一次只返回一行查询到的数据
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql , params)
            row = cs1.fetchone()
            #把查询的结果集中的下一行保存为序列
            #print(row)
            #row是查询的值
            cs1.close()
            self.conn.close()
            return row
        except Exception as e:
            print("None", e)

    def fetchall(self,sql,params):
        #接收全部的返回结果行
        #返回查询到的全部结果值
        try:
            cs1=self.conn.cursor()
            cs1.execute(sql,params)
            rows=cs1.fetchall()
            cs1.close()
            self.conn.close()

            return rows
        except Exception as e:
            print("None",e)


windows = tk.Tk()
windows.title('ly')
windows.geometry('355x275')
windows.resizable(0,0)

Label1=tk.Label(windows,text='     username:')
Label1.place(height = 48,width = 62,x = 26,y = 60)

Label2=tk.Label(windows,text='key:')
Label2.place(height = 48,width = 54,x = 24,y = 154)

u=tk.StringVar()
p=tk.StringVar()

Entry1=tk.Entry(windows,textvariable=u)
Entry1.place(height = 34,width = 171,x = 119,y = 65)

Entry2=tk.Entry(windows,textvariable=p)
Entry2.place(height = 36,width = 172,x = 118,y = 161)

def succes():
    import tkinter as tk
    windows = tk.Tk()
    windows.geometry('86x55')
    windows.resizable(0,0)
    var=tk.StringVar()
    e =tk.Entry(windows, textvariable = var,state='readonly')
    var.set('success')
    e.pack()
    tk.mainloop()

def flas():
    import tkinter as tk
    windows = tk.Tk()
    windows.geometry('86x55')
    windows.resizable(0,0)
    var=tk.StringVar()
    e =tk.Entry(windows, textvariable = var,state='readonly')
    var.set('flase')
    e.pack()
    tk.mainloop()

u.set('输入账号')
p.set('输入密码')
def get():
    uname=u.get()
    upwd=p.get()
    s1=sha1()
    s1.update(upwd.encode())
    upwd2=s1.hexdigest()


    conn=MysqlHelper(host='118.25.217.90',port=3306,db='test',user='root',passwd='djyiL%;j.3:4_',charset='utf8')
    sql = "SELECT upwd from user where username = %s "
    params=[uname]
    result = conn.fetchall(sql, params)
    if result == None:
        windows.title('用户名错误！')
        return

    pwd = result[0][0]
    s2=sha1()
    s2.update(pwd.encode())
    encodedPwd = s2.hexdigest()

    if encodedPwd == upwd2:
        windows.title('登陆成功！')
    else:
        windows.title('密码错误！')


Button1=tk.Button(windows,text='login',command=get)
Button1.place(height = 30,width = 108,x = 104,y = 218)
tk.mainloop()