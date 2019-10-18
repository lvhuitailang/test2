import tkinter as tk
import pymysql
from  hashlib import sha1
import hashlib
import _thread
import time
import faker

f = faker.Faker(locale='zh-CN')
def code1():
    code = f.password(15)
    conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    sql = 'INSERT into code(recode) VALUES(%s)'
    conn.conn.cursor().execute(sql, code)
    conn.conn.commit()
    conn.conn.close()


class MysqlHelper:
    def __init__(self, host='locahhost', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)

    def insert(self, sql, params):
        return self.__cud(sql, params)

    def update(self, sql, params):
        return self.__cud(sql, params)

    def delete(self, sql, params):
        return self.__cud(sql, params)

    def my_md5(self, pwd):
        my_md5 = hashlib.md5()
        my_md5.update(pwd.encode('utf-8'))
        return my_md5.hexdigest()

    def __cud(self, sql, params=[]):
        try:
            # 用来获得python执行Mysql命令的方法
            cs1 = self.conn.cursor()
            # 真正执行MySQL语句
            rows = cs1.execute(sql, params)
            self.conn.commit()
            cs1.close()
            self.conn.close()
            return rows  # 影响到了哪行
        except Exception as e:
            print(e)
            self.conn.rollback()

    def fetchone(self, sql, params=[]):
        # 一次只返回一行查询到的数据
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            row = cs1.fetchone()
            # 把查询的结果集中的下一行保存为序列
            # print(row)
            # row是查询的值
            cs1.close()
            self.conn.close()
            return row
        except Exception as e:
            print("None", e)

    def fetchall(self, sql, params):
        # 接收全部的返回结果行
        # 返回查询到的全部结果值
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            rows = cs1.fetchall()
            cs1.close()
            self.conn.close()

            return rows
        except Exception as e:
            print("None", e)


windows = tk.Tk()
windows.title('登陆')
windows.geometry('355x275')
windows.resizable(0, 0)

#background
bgImg = tk.PhotoImage(file=r"./bg.png")
imgLabel = tk.Label(windows,image=bgImg)
imgLabel.pack(side=tk.RIGHT)


Label1 = tk.Label(windows, text='username')
Label1.place(height=48, width=62, x=26, y=60)

Label2 = tk.Label(windows, text='pwd')
Label2.place(height=48, width=54, x=24, y=105)

checkbutton1 = tk.Checkbutton(windows)
checkbutton1.place(height=40, width=30, x=80, y=175)

Label3 = tk.Label(windows, text='记住用户名和密码')
Label3.place(height=48, width=120, x=100, y=170)

u = tk.StringVar()
p = tk.StringVar()
u1 = tk.StringVar()
p2 = tk.StringVar()
p3 = tk.StringVar()
m  = tk.StringVar()
zid=tk.StringVar()
zmoney=tk.StringVar()

Entry1 = tk.Entry(windows, textvariable=u)
Entry1.place(height=34, width=171, x=119, y=65)

Entry2 = tk.Entry(windows, textvariable=p)
Entry2.place(height=36, width=172, x=118, y=110)


def succes():
    import tkinter as tk
    windows = tk.Tk()
    windows.geometry('86x55')
    windows.resizable(0, 0)
    var = tk.StringVar()
    e = tk.Entry(windows, textvariable=var, state='readonly')
    var.set('success')
    e.pack()
    tk.mainloop()


def flas():
    import tkinter as tk
    windows = tk.Tk()
    windows.geometry('86x55')
    windows.resizable(0, 0)
    var = tk.StringVar()
    e = tk.Entry(windows, textvariable=var, state='readonly')
    var.set('flase')
    e.pack()
    tk.mainloop()


u.set('输入账号')
p.set('输入密码')
u1.set('输入注册账号')
p2.set('输入注册密码')
p3.set('再次输入密码')
m.set('money')


def get():
    global usname
    usname = u.get()
    upwd = p.get()
    s1 = sha1()
    s1.update(upwd.encode())
    upwd2 = s1.hexdigest()
    conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    sql = "SELECT password from user where username = %s "
    params = usname
    result = conn.fetchone(sql, params)
    if result == None:
        windows.title('用户名为空!')
    elif not result:
        windows.title('用户名错误!')
    elif result[0] == upwd2:
        windows.title('登陆成功!')
        time.sleep(1)
        windows.destroy()
        g()
    else:
        windows.title('密码错误!')




def g():
    import tkinter as tk
    usre=u.get()
    global windows
    windows = tk.Tk()
    windows.title('ATM')
    windows.geometry('383x258')
    windows.resizable(0, 0)
    Label1 = tk.Label(windows, text='尊敬的'+ usre+ ',欢迎使用ATM自助机')
    Label1.place(height=16, width=200, x=80, y=18)
    Button1 = tk.Button(windows, text='查询',command=lambda:cx())
    Button1.place(height=50, width=60, x=40, y=60)
    Button2 = tk.Button(windows, text='转账',command=lambda:zhuanzhang())
    Button2.place(height=50, width=60, x=140, y=60)
    Button3 = tk.Button(windows, text='存钱',command=lambda:cunqian())
    Button3.place(height=50, width=60, x=240, y=60)
    Label2 = tk.Label(windows, text='ʚΐɞʚΐɞ请点击按钮选择功能ʚΐɞʚΐɞ')
    Label2.place(height=60, width=180, x=80, y=120)
    Button4 = tk.Button(windows, text='取钱',command=lambda:qu())
    Button4.place(height=50, width=60, x=40, y=180)
    Button5 = tk.Button(windows, text='注册码',command=lambda:code1())
    Button5.place(height=50, width=60, x=140, y=180)
    Button6 = tk.Button(windows, text='退出系统',command=lambda:clos() )
    Button6.place(height=50, width=60, x=240, y=180)
    tk.mainloop()




def cx():
    uname = u.get()
    conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    sql = "SELECT money from user where username = %s "
    result = conn.fetchone(sql, uname)
    money = list(result)
    windows.title('当前余额为：' + str(money[0])+'元!')
    return money[0]


def zz():
    a = cx()
    uname = u.get()  # 获取用户名
    str1 = input('输入转账账号：')
    conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    myconn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8').conn
    myconn1 = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    myconn2 = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    sql = "SELECT username from user where username = %s "
    result = conn.fetchone(sql, str1)
    print(result)
    if result == None:
        print('账户不存在!')
    elif result == uname:
        print('不能给自己转账!')
    else:
        str2 = int(input('输入转账金额：'))
        money = str(a - str2)  # 转账后账户实际余额
        if str2 > a:
            print('当前余额不足！')
        else:
            sql2 = r'update user set money=' + money + '  where username=\'' + uname + '\''

            sql4 = 'SELECT money FROM user WHERE username= %s'
            m2 = myconn1.fetchone(sql4, str1)
            myconn.commit()
            q = list(m2)[0]
            m3 = str(q + str2)
            sql3 = r'update user set money=' + m3 + '  where username=\'' + str1 + '\''
            myconn2.conn.cursor().execute(sql3)
            myconn2.conn.commit()
            print('转账成功!')
            myconn.cursor().execute(sql2)
            myconn.commit()
            myconn.close()

            # money=list(result)
            # print(money)

def zhuanzhang():#转账编辑框
    import tkinter as tk
    global windows3
    windows3 = tk.Tk()
    windows3.title('转账')
    windows3.geometry('304x144')
    windows3.resizable(0,0)
    Label1=tk.Label(windows3,text='账号：')
    Label1.place(height = 26,width = 55,x = 20,y = 18)
    Label2=tk.Label(windows3,text='金额：')
    Label2.place(height = 26,width = 55,x = 20,y = 58)
    Entry1=tk.Entry(windows3)
    Entry1.place(height = 22,width = 140,x = 98,y = 20)
    Entry2=tk.Entry(windows3)
    Entry2.place(height = 22,width = 140,x = 98,y = 60)
    Button1=tk.Button(windows3,text='确认',command=lambda : zhuanzhangfc(Entry1,Entry2))
    Button1.place(height = 25,width = 60,x =110,y = 100)
    windows3.mainloop()

def  zhuanzhangfc(Entry1,Entry2):  #转账方法
    a = cx()
    uname1 = Entry1.get()  # 获取用户名
    str3 = int(Entry2.get())   # 获取金额
    conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    myconn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8').conn
    myconn1 = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    myconn2 = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    sql = "SELECT username from user where username = %s "
    result = conn.fetchone(sql, uname1)
    print(result)
    if result == None :
        windows3.title('该用户不存在!')
    elif result[0] == usname:
        windows3.title('禁止给自己转账!')
    else:
        money = str(a - str3)  # 转账后账户实际余额
        if str3 > a:
            windows3.title('当前余额不足!')
        else:
            sql2 = r'update user set money=' + money + '  where username=\'' + usname + '\''  #更新自己的余额

            sql4 = 'SELECT money FROM user WHERE username= %s'
            m2 = myconn1.fetchone(sql4, uname1)
            myconn.commit()
            q = list(m2)[0]
            m3 = str(q + str3)
            sql3 = r'update user set money=' + m3 + '  where username=\'' + uname1 + '\''
            myconn2.conn.cursor().execute(sql3)
            myconn2.conn.commit()
            windows3.title('转账成功!')
            windows.title('当前余额为：' + str(money)+'元!')
            myconn.cursor().execute(sql2)
            myconn.commit()
            myconn.close()

def cunqian():
    bian()
    # s = int(input('请输入存款金额：'))
    # conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    # uname = u.get()  # 获取用户名
    # a = cx()
    # s1 = str(s + a)
    # sql = r'update user set money=' + s1 + '  where username=\'' + uname + '\''
    # conn.conn.cursor().execute(sql)
    # print('' '存钱成功！当前余额为' + s1 + '元！')
    # conn.conn.commit()
    # conn.conn.close()

def quqian():
    qu()
    # s = int(input('请输入取款金额：'))
    # conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    # uname = u.get()  # 获取用户名
    # a = cx()
    # if a - s >= 0:
    #     s1 = str(a - s)
    #     sql = r'update user set money=' + s1 + '  where username=\'' + uname + '\''
    #     conn.conn.cursor().execute(sql)
    #     print('' '取钱成功！当前余额为' + s1 + '元！')
    #     conn.conn.commit()
    #     conn.conn.close()
    # else:
    #     print('当前余额不足以取这么多钱！')



        # webbrowser.open('http://www.iqiyi.com')


def registFun(e1, e2, e3,u1, windows1):
    reguser = e1.get()  # 用户名
    regpass = e2.get()  # 第一次输入密码
    repassagin = e3.get()  # 第二次输入密码

    if regpass != repassagin:
        windows1.title('密码不一致!')
        return

    recode = u1.get() # 获取注册码
    conn1 = MysqlHelper(host='118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8').conn
    sql2 = 'select recode from code where recode = %s '
    code1=conn1.cursor().execute(sql2,recode)
    conn1.commit()
    if code1 == 1:
        conn = MysqlHelper(host='118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8').conn
        cus1 = conn.cursor()
        sql = 'INSERT into user(username,password) VALUES(%s,%s)'
        sql1 = 'select username from user where username = %s '
        sql3 = r'update user set money=%s  where username=%s'
        sql4 = 'DELETE FROM code where recode=%s'
        s = cus1.execute(sql1, reguser)
        ''' 
        设置密码,commit过后，数据库里面才会有注册的user，之后才能设置金额
        '''
        pwd = hashlib.sha1(regpass.encode('utf-8')).hexdigest()
        res = (reguser, pwd)
        cus1.execute(sql, res)
        conn.commit()
        cus1.close()
        conn.close()



        if s == 0 and regpass == repassagin:
            windows1.title('注册成功!')
            conn2 = MysqlHelper(host='118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8').conn
            conn2.cursor().execute(sql3,(0,reguser))
            conn2.cursor().execute(sql4,recode)
            conn2.commit()
            conn2.close()
        elif regpass != repassagin:
            windows1.title('密码不一致!')
            return
        else:
            windows1.title('用户名已存在!')
    else:
        windows1.title('无效的注册码!')
        return




def clos():
    windows.destroy()

def bian():  #存钱编辑框
    import tkinter as tk
    global windows1
    windows1 = tk.Tk()
    windows1.title('存钱')
    windows1.geometry('259x86')
    windows1.resizable(0,0)
    Label1=tk.Label(windows1,text='存钱金额：')
    Label1.place(height = 27,width = 62,x = 10,y = 20)
    Entry1=tk.Entry(windows1, textvariable=m)
    Entry1.place(height = 20,width = 123,x = 76,y = 25)
    Button4 = tk.Button(windows1,text='确认',command= lambda: getmoeny(Entry1) )
    Button4.place(height = 20,width = 40,x = 210,y = 25)
    windows.mainloop()

def qu():  #取钱编辑框
    import tkinter as tk
    global windows1
    windows1 = tk.Tk()
    windows1.title('取钱')
    windows1.geometry('259x86')
    windows1.resizable(0,0)
    Label1=tk.Label(windows1,text='取钱金额：')
    Label1.place(height = 27,width = 62,x = 10,y = 20)
    Entry1=tk.Entry(windows1, textvariable=m)
    Entry1.place(height = 20,width = 123,x = 76,y = 25)
    Button4 = tk.Button(windows1,text='确认',command= lambda: outmoeny(Entry1) )
    Button4.place(height = 20,width = 40,x = 210,y = 25)
    windows.mainloop()

def getmoeny(m):  #存钱方法
    conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    uname = u.get()  # 获取用户名
    a = cx()
    s1 = str(int(m.get()) + a)
    sql = r'update user set money=' + s1 + '  where username=\'' + uname + '\''
    conn.conn.cursor().execute(sql)
    # windows1.title('成功！余额为：'+s1)
    windows.title('存钱成功! 当前余额：'+s1)
    conn.conn.commit()
    conn.conn.close()

def outmoeny(m):  #取钱方法
    conn = MysqlHelper('118.25.217.90', port=3306, db='test', user='xhh', passwd='flzx_3QC', charset='utf8')
    uname = u.get()  # 获取用户名
    a = cx()
    b=int(m.get())
    if a - b >= 0:
        s1 = str(a - b)
        sql = r'update user set money=' + s1 + '  where username=\'' + uname + '\''
        conn.conn.cursor().execute(sql)
        windows.title('' '取钱成功!当前余额为' + s1 + '元!')
        conn.conn.commit()
        conn.conn.close()
    else:
         windows.title('当前余额不足以取这么多钱!')


def regist():

    code1()

    windows1 = tk.Tk()
    windows1.title('注册')
    windows1.geometry('461x284')
    windows1.resizable(0, 0)
    Label1 = tk.Label(windows1, text='用户名：')
    Label1.place(height=33, width=75, x=32, y=23)
    Label2 = tk.Label(windows1, text='密码：')
    Label2.place(height=33, width=75, x=27, y=84)
    Label3 = tk.Label(windows1, text='再次输入密码：')
    Label3.place(height=33, width=85, x=35, y=145)
    Label4 = tk.Label(windows1, text='注册码：')
    Label4.place(height=25, width=85, x=30, y=190)

    u1 = tk.StringVar()
    p2 = tk.StringVar()
    p3 = tk.StringVar()
    c1 = tk.StringVar()

    Entry1 = tk.Entry(windows1, textvariable=u1)
    Entry1.place(height=36, width=130, x=152, y=24)


    '''
    输入框变星号
    '''
    Entry2 = tk.Entry(windows1, textvariable=p2)
    Entry2['show'] = '*'
    Entry2.place(height=36, width=130, x=152, y=85)


    Entry3 = tk.Entry(windows1, textvariable=p3)
    Entry3['show'] = '*'
    Entry3.place(height=36, width=130, x=152, y=146)


    Entry4 = tk.Entry(windows1, textvariable=c1)
    Entry4.place(height=30, width=130, x=152, y=185)
    Button4 = tk.Button(windows1, text='注册', command=lambda: registFun(Entry1, Entry2, Entry3,Entry4, windows1))
    Button4.place(height=48, width=127, x=152, y=220)


Button1 = tk.Button(windows, text='登陆', command=get)
Button1.place(height=30, width=60, x=60, y=218)

Button2 = tk.Button(windows, text='注册', command=lambda : regist())
Button2.place(height=32, width=60, x=220, y=215)

tk.mainloop()
