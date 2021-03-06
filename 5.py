import tkinter as tk
import pymysql
from  hashlib import sha1
import hashlib

class MysqlHelper:
    def __init__(self,host='localhost',port=3306,db='test',user='root',passwd='root',charset='utf8'):
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

Label1=tk.Label(windows,text='username')
Label1.place(height = 48,width = 62,x = 26,y = 60)

Label2=tk.Label(windows,text='pwd')
Label2.place(height = 48,width = 54,x = 24,y = 105)

checkbutton1=tk.Checkbutton(windows)
checkbutton1.place(height = 40,width = 30,x = 80,y = 175)


Label3=tk.Label(windows,text='记住用户名和密码')
Label3.place(height = 48,width = 120,x = 100,y = 170)

u=tk.StringVar()
p=tk.StringVar()
u1=tk.StringVar()
p2=tk.StringVar()
p3=tk.StringVar()

Entry1=tk.Entry(windows,textvariable=u)
Entry1.place(height = 34,width = 171,x = 119,y = 65)

Entry2=tk.Entry(windows,textvariable=p)
Entry2.place(height = 36,width = 172,x = 118,y = 110)

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
u1.set('输入注册账号')
p2.set('输入注册密码')
p3.set('再次输入密码')

def get():
    uname=u.get()
    upwd=p.get()
    s1=sha1()
    s1.update(upwd.encode())
    upwd2=s1.hexdigest()
    conn = MysqlHelper(host='118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    sql = "SELECT password from user where username = %s "
    params=[uname]
    result = conn.fetchall(sql, params)
    if result == None:
        windows.title('用户名错误！')

    elif not result:
        windows.title('用户名错误！')

    elif result[0][0] == upwd2:
        print(result[0][0])
        windows.title('登陆成功！')
    else:
        windows.title('密码错误！')

def registFun(e1,e2,e3):


    reguser=e1.get()    #用户名
    regpass=e2.get()    #第一次输入密码
    repassagin=e3.get() #第二次输入密码

    conn = MysqlHelper(host='118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8').conn
    cus1=conn.cursor()
    sql='INSERT into user(username,password) VALUES(%s,%s)'
    pwd=hashlib.sha1(regpass.encode('utf-8')).hexdigest()
    print(pwd)
    res=(reguser,pwd)
    print(res)
    cus1.execute(sql,res)
    conn.commit()
    cus1.close()
    conn.close()

def regist():

    windows = tk.Tk()
    windows.geometry('461x284')
    windows.resizable(0,0)
    Label1=tk.Label(windows,text='用户名：')
    Label1.place(height = 33,width = 75,x = 32,y = 23)
    Label2=tk.Label(windows,text='密码：')
    Label2.place(height = 33,width = 75,x = 27,y = 84)
    Label3=tk.Label(windows,text='再次输入密码：')
    Label3.place(height = 33,width = 85,x = 35,y = 145)

    u1 = tk.StringVar()
    p2 = tk.StringVar()
    p3 = tk.StringVar()

    Entry1=tk.Entry(windows,textvariable=u1)
    Entry1.place(height = 36,width = 130,x = 152,y = 24)
    Entry2=tk.Entry(windows,textvariable=p2)
    Entry2.place(height = 36,width =130,x = 152,y = 85)
    Entry3=tk.Entry(windows,textvariable=p3)
    Entry3.place(height = 36,width = 130,x = 152,y = 146)
    Button4=tk.Button(windows,text='注册',command=lambda:registFun(Entry1,Entry2,Entry3))
    Button4.place(height = 48,width = 127,x = 152,y = 215)



Button1=tk.Button(windows,text='登陆',command=get)
Button1.place(height = 30,width = 60,x = 60,y = 218)


Button2=tk.Button(windows,text='注册',command=regist)
Button2.place(height = 32,width =60,x = 220,y = 215)


tk.mainloop()