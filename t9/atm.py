import tkinter as tk
import pymysql
from  hashlib import sha1
import hashlib
import time
import faker
import datetime
import os, sys
import time
import wmi,zlib

class MysqlHelper:
    def __init__(self, host='locahhost', port=3306, db='test', user='root', passwd='123456', charset='utf8'):
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

            return rows
        except Exception as e:
            print("None", e)

conn = MysqlHelper('192.168.0.105', port=3306, db='test', user='root', passwd='123456', charset='utf8')

f = faker.Faker(locale='zh-CN')   #获取注册码函数
def code1():
    code = f.password(15)
    sql = 'INSERT into code(recode) VALUES(%s)'
    conn.conn.cursor().execute(sql, code)
    conn.conn.commit()


def code2():
    list=[]
    for i in range(1,4):
        code = f.password(15)
        list.append(code)
    sql = 'INSERT into registercode(paycode) VALUES(%s)'
    for i in list:
        conn.conn.cursor().execute(sql, i)
        conn.conn.commit()


def now():   #获取当前时间
    nowTime=datetime.datetime.now()#现在
    return nowTime

def dqtime(a,b,c): #获取到期时间
    t = datetime.datetime.now()
    s=t+datetime.timedelta(hours=a,minutes=b,seconds=c)
    return s

def get_cpu():   #获取电脑cpuid
          c = wmi.WMI ()
          for cpu in c.Win32_Processor():
#cpu 序列号
            cid=cpu.ProcessorId.strip()
            return cid

windows = tk.Tk()
#photo=tk.PhotoImage(file=r"C:\Users\Administrator\Desktop\1.gif")

label=tk.Label(windows)  #图片
label.pack()
windows.title('登陆')
windows.geometry('922x267')
windows.resizable(0, 0)

Label1 = tk.Label(windows, text='username',bg='black',fg='red')
Label1.place(height=22, width=62, x=526, y=70)

Label2 = tk.Label(windows, text='password',bg='black',fg='red')
Label2.place(height=22, width=62, x=524, y=120)

Label3 = tk.Label(windows, text='信息查询',bg='black',fg='white')
Label3.place(height=22, width=62, x=526, y=20)


u = tk.StringVar()
p = tk.StringVar()
cxx = tk.StringVar()
u1 = tk.StringVar()
p2 = tk.StringVar()
p3 = tk.StringVar()
m  = tk.StringVar()
zid=tk.StringVar()
zmoney=tk.StringVar()
td = tk.StringVar()

#修改密码的参数
xguser = tk.StringVar()
superpassword = tk.StringVar()
newpassword = tk.StringVar()

Entry1 = tk.Entry(windows, textvariable=u)
Entry1.place(height=34, width=171, x=620, y=65)

Entry2 = tk.Entry(windows, textvariable=p)
Entry2['show']='*'
Entry2.place(height=36, width=172, x=620, y=110)

Entry3 = tk.Entry(windows, textvariable=cxx)
Entry3.place(height=34, width=171, x=620, y=17)


u1.set('输入注册账号')
p2.set('输入注册密码')
p3.set('再次输入密码')
cxx.set('请输入要查询的账号')
td.set('1')

def xxcx():   #信息查询方法
    cx1=cxx.get()
    sql1 = 'select username from user where username = %s '
    sql2 = 'SELECT overtime from user where username= %s'
    res=conn.conn.cursor().execute(sql1,cx1)
    if res == 0 :
        windows.title('当前用户不存在!!')
    else:
        t=conn.fetchone(sql2,cx1)
        windows.title('当前用户到期时间：'+str(t[0]))

def mmxg():   #修改密码编辑框
    global windows4
    windows4 = tk.Tk()
    windows4.title('修改密码')
    windows4.geometry('295x230')
    windows4.resizable(0, 0)
    Label1 = tk.Label(windows4, text='用户名:')
    Label1.place(height=31, width=92, x=20, y=24)
    Entry1 = tk.Entry(windows4, textvariable=xguser)
    Entry1.place(height=25, width=100, x=120, y=26)

    Label2 = tk.Label(windows4, text='超级密码:')
    Label2.place(height=31, width=92, x=20, y=74)
    Entry2 = tk.Entry(windows4, textvariable=superpassword)
    Entry2.place(height=25, width=100, x=120, y=76)
    Entry2['show'] = '*'

    Label3 = tk.Label(windows4, text='新密码:')
    Label3.place(height=31, width=92, x=20, y=124)
    Entry3 = tk.Entry(windows4, textvariable=newpassword)
    Entry3.place(height=25, width=100, x=120, y=126)
    Entry3['show'] = '*'

    Button1 = tk.Button(windows4, text='确认修改',command= lambda: xgmmfun(Entry1,Entry2,Entry3,windows4))
    Button1.place(height=40, width=80, x=110, y=170)
    tk.mainloop()

def xgmmfun(Entry1,Entry2,Entry3,windows4):  #修改密码方法
    xuser=Entry1.get()
    superpw = Entry2.get()
    newpw = Entry3.get()
    s1 = sha1()
    s1.update(newpw.encode())  #对输入的密码进行处理
    upwd2 = s1.hexdigest()      #加密
    sql1 = 'select username from user where username = %s '
    sql2 = 'select superpass from user where username = %s '
    sql3 = 'update user set password=%s  where username=%s'
    sql4 = "SELECT password from user where username = %s "
    result = conn.conn.cursor().execute(sql1,xuser)
    if result == 0:
        windows4.title('用户名不存在!!')
    else:
        result1 = conn.fetchone(sql2,xuser)
        if result1[0] != superpw:
            windows4.title('超级密码错误!!')
        else:
            if len(newpw)<5:
                windows4.title('密码低于5位，请重新设置!!')
            else:
                res2 = conn.fetchone(sql4,xuser)
                if res2[0] == upwd2 :
                    windows4.title('新密码和原密码相同!!')
                else:
                    conn.conn.cursor().execute(sql3,(upwd2,xuser))
                    conn.conn.commit()
                    windows4.title('修改密码成功!!')
                    time.sleep(1)
                    windows4.destroy()

def get():   #登陆函数
    global usname
    usname = u.get()
    upwd = p.get()
    s1 = sha1()
    s1.update(upwd.encode())  #对输入的密码进行处理
    upwd2 = s1.hexdigest()      #加密
    sql = "SELECT password from user where username = %s "
    sql1 = 'SELECT overtime from user where username= %s'
    sql2 ='update user set cid=%s  where username=%s'
    sql3= 'SELECT cid from user where username= %s'
    sql4='SELECT username from user where username= %s'
    params = usname
    result = conn.fetchone(sql, params)
    result1 =conn.fetchone(sql1,params)
    result2 =conn.fetchone(sql3,usname)
    result3 = conn.conn.cursor().execute(sql4,params)
    t1 = datetime.datetime.now().strftime("%Y-%m-%d %X")  # 当前时间
    if result1 != None:
        t = str(result1[0]) < str(t1)   #判断时间是否到期
    else:
        windows.title('User Error!')
    if result3 == 0 :
        windows.title('Username is not in cool!')
    elif result[0] == upwd2 and t == False and result2[0] =='' :
        windows.title('Login Success!')
        id1=conn.fetchone(sql3,usname)
        if id1[0] == None:   #第一次登陆成功把机器码存进数据库
            id=get_cpu()
            conn.conn.cursor().execute(sql2,(id,usname))
            conn.conn.commit()
        else:
            print('cid is  already')
        time.sleep(1)
        windows.destroy()
        g()
    elif result[0] == upwd2 and t == False and result2[0] != '' :  #第二次登陆验证机器码是否正确
        newid=get_cpu()
        if result2[0] == newid:
            windows.title('Login success!')
            time.sleep(1)
            windows.destroy()
            g()
        else:
            windows.title('Computer machine is error!')
    elif result[0] == upwd2 and t == True:
        windows.title('Time is over,Please pay it!!')
    else:
        windows.title('password error!')
        return

def g():   #调用登陆成功的界面

    global usre
    global windows
    usre = u.get()
    windows = tk.Tk()
    windows.geometry('383x258')
    windows.resizable(0, 0)
    sql='SELECT overtime from user where username= %s'
    res = conn.fetchone(sql,usre)
    windows.title('到期时间：'+ str(res[0]))
    t1 = datetime.datetime.now().strftime("%Y-%m-%d %X") #当前时间
    Label1 = tk.Label(windows, text='尊敬的'+ usre+ ',欢迎使用ATM自助机', font=("华文彩云",10),fg="red")
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
    Button5 = tk.Button(windows, text='解绑',command=lambda:unbundling())
    Button5.place(height=50, width=60, x=140, y=180)
    Button6 = tk.Button(windows, text='退出系统',command=lambda:clos() )
    Button6.place(height=50, width=60, x=240, y=180)
    tk.mainloop()

def cx():  #查询函数
    uname = u.get()
    sql = "SELECT money from user where username = %s "
    result = conn.fetchone(sql, uname)
    money = list(result)
    windows.title('当前余额为：' + str(money[0])+'元!')
    return money[0]

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
    sql = "SELECT username from user where username = %s "
    result = conn.fetchone(sql, uname1)
    print(result)
    if result == None :
        windows3.title('该用户不存在!')
        print(type(str3))
    elif result[0] == usname:
        windows3.title('禁止给自己转账!')
    else:
        money = str(a - str3)  # 转账后账户实际余额
        if str3 > a:
            windows3.title('当前余额不足!')
        else :
            sql2 = r'update user set money=' + money + '  where username=\'' + usname + '\''  #更新自己的余额
            sql4 = 'SELECT money FROM user WHERE username= %s'
            m2 = conn.fetchone(sql4, uname1)
            conn.conn.commit()
            q = list(m2)[0]
            m3 = str(q + str3)
            sql3 = r'update user set money=' + m3 + '  where username=\'' + uname1 + '\''
            conn.conn.cursor().execute(sql3)
            conn.conn.commit()
            windows3.title('转账成功!')
            windows.title('当前余额为：' + str(money)+'元!')
            conn.conn.cursor().execute(sql2)
            conn.conn.commit()
            windows3.destroy()



def cunqian():   #调用存钱方法
    bian()

def quqian():  #调用取钱方法
    qu()

def registFun(e1, e2, e3,u1,sp, windows1):    #注册函数
    reguser = e1.get()  # 用户名
    regpass = e2.get()  # 第一次输入密码
    repassagin = e3.get()  # 第二次输入密码
    recode = u1.get() # 获取注册码
    superpass = sp.get() # 获取超级密码
    s1 = sha1()
    s1.update(superpass.encode())
    superpass2 = s1.hexdigest()
    conn1 = MysqlHelper(host='192.168.0.105', port=3306, db='test', user='root', passwd='123456', charset='utf8')
    sql2 = 'select recode from code where recode = %s '
    code1=conn1.conn.cursor().execute(sql2,recode)
    conn1.conn.commit()
    if code1 == 1:
        cus1 = conn1.conn.cursor()
        sql = 'INSERT into user(username,password,superpass) VALUES(%s,%s,%s)'
        sql1 = 'select username from user where username = %s '
        sql3 = r'update user set money=%s  where username=%s'
        sql4 = 'DELETE FROM code where recode=%s'
        sql5 =  r'update user set overtime=%s  where username=%s'
        s = cus1.execute(sql1, reguser)
        if s == 0 and regpass == repassagin and len(regpass)>6 and len(superpass)>6 :
            windows1.title('注册成功,欢迎使用!!')
            ti=dqtime(24,0,0)
            pwd = hashlib.sha1(regpass.encode('utf-8')).hexdigest()
            res = (reguser, pwd,superpass)
            cus1.execute(sql, res)
            conn1.conn.commit()
            conn1.conn.cursor().execute(sql3,(0,reguser))
            conn1.conn.cursor().execute(sql5,(ti,reguser))
            conn1.conn.cursor().execute(sql4,recode)
            conn1.conn.commit()
            conn1.conn.close()
            time.sleep(1)
            windows1.destroy()
        elif s == 0 and regpass == repassagin and len(regpass)<=6 :
            windows1.title('密码太短，请重新设置一个大于6位数的密码!!')
        elif s == 0 and regpass == repassagin and len(superpass)<=6 :
            windows1.title('超级密码太短，请重新设置一个大于6位数的密码!!')
        elif regpass != repassagin:
            windows1.title('密码不一致!')
            return
        else:
            windows1.title('用户名已存在!')
    else:
        windows1.title('无效的注册码!')
        return
        '设置密码,commit过后，数据库里面才会有注册的user，之后才能设置金额'

def clos():   #关闭界面窗口
    windows.destroy()


def unbundling():  #解绑
    sql='update user set cid='' where username=%s'

    MysqlHelper('192.168.0.105', port=3306, db='test', user='root', passwd='123456', charset='utf8').update(r'update user set cid="" where username=%s',usname)


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
    uname = u.get()  # 获取用户名
    a = cx()
    s1 = str(int(m.get()) + a)
    sql = r'update user set money=' + s1 + '  where username=\'' + uname + '\''
    conn.conn.cursor().execute(sql)
    # windows1.title('成功！余额为：'+s1)
    windows.title('存钱成功! 当前余额：'+s1)
    conn.conn.commit()


def outmoeny(m):  #取钱方法
    uname = u.get()  # 获取用户名
    a = cx()
    moneyString = m.get()
    if  m.get()=='' or ((m.get()).isdigit()==False):
        windows.title('金额无效!!')
        return
    b = int(moneyString)
    if a - b >= 0:
        s1 = str(a - b)
        sql = r'update user set money=' + s1 + '  where username=\'' + uname + '\''
        conn.conn.cursor().execute(sql)
        windows.title('' '取钱成功!当前余额为' + s1 + '元!')
        conn.conn.commit()

    else:
         windows.title('当前余额不足以取这么多钱!')

def regist():   #注册编辑框
    windows1 = tk.Tk()
    windows1.title('注册')
    windows1.geometry('461x284')
    windows1.resizable(0, 0)
    Label1 = tk.Label(windows1, text='用户名：')
    Label1.place(height=20, width=75, x=32, y=23)
    Label2 = tk.Label(windows1, text='密码：')
    Label2.place(height=20, width=75, x=27, y=60)
    Label3 = tk.Label(windows1, text='再次输入密码：')
    code1()
    Label3.place(height=20, width=85, x=35, y=105)
    Label4 = tk.Label(windows1, text='注册码：')
    Label4.place(height=25, width=85, x=30, y=145)
    Label5 = tk.Label(windows1, text='超级密码：')
    Label5.place(height=25, width=85, x=30, y=190)

    u1 = tk.StringVar()
    p2 = tk.StringVar()
    p3 = tk.StringVar()
    c1 = tk.StringVar()
    sp = tk.StringVar()

    Entry1 = tk.Entry(windows1, textvariable=u1)
    Entry1.place(height=20, width=130, x=152, y=24)
    Entry2 = tk.Entry(windows1, textvariable=p2)
    Entry2['show']='*'
    Entry2.place(height=20, width=130, x=152, y=60)
    Entry3 = tk.Entry(windows1, textvariable=p3)
    Entry3['show']='*'
    Entry3.place(height=20, width=130, x=152, y=105)
    Entry4 = tk.Entry(windows1, textvariable=c1)
    Entry4.place(height=20, width=130, x=152, y=145)
    Entry5 = tk.Entry(windows1, textvariable=sp)
    Entry5.place(height=20, width=130, x=152, y=185)
    Button4 = tk.Button(windows1, text='注册', command=lambda: registFun(Entry1, Entry2, Entry3,Entry4, Entry5,windows1))
    Button4.place(height=48, width=127, x=152, y=220)

def pay():   #充值编辑框
    code2()
    windows1 = tk.Tk()
    windows1.title('充值')
    windows1.geometry('461x350')
    windows1.resizable(0, 0)
    Label1 = tk.Label(windows1, text='用户名：')
    Label1.place(height=33, width=75, x=32, y=23)
    Label2 = tk.Label(windows1, text='卡号1：')
    Label2.place(height=33, width=75, x=27, y=84)
    Label3 = tk.Label(windows1, text='卡号2：')
    Label3.place(height=33, width=75, x=27, y=145)
    Label5 = tk.Label(windows1, text='卡号3：')
    Label5.place(height=25, width=75, x=27, y=190)
    Label4 = tk.Label(windows1, text='推广人：')
    Label4.place(height=25, width=75, x=27, y=230)

    user1 = tk.StringVar()
    num1 = tk.StringVar()
    num2 = tk.StringVar()
    num3 = tk.StringVar()
    person= tk.StringVar()

    Entry1 = tk.Entry(windows1, textvariable=user1)
    Entry1.place(height=30, width=130, x=152, y=24)
    Entry2 = tk.Entry(windows1, textvariable=num1)
    Entry2.place(height=30, width=130, x=152, y=85)
    Entry3 = tk.Entry(windows1, textvariable=num2)
    Entry3.place(height=30, width=130, x=152, y=146)
    Entry4 = tk.Entry(windows1, textvariable=num3)
    Entry4.place(height=30, width=130, x=152, y=195)
    Entry5 = tk.Entry(windows1, textvariable=person)
    Entry5.place(height=30, width=130, x=152, y=230)
    Button4 = tk.Button(windows1, text='充值', command=lambda: up(Entry1, Entry2, Entry3,Entry4,Entry5, windows1))
    Button4.place(height=48, width=127, x=152, y=280)

def up(user1,num1,num2,num3,person,windows1):   #充值函数判断
    sql1='select username from user where username = %s'
    sql2='select paycode from registercode where paycode = %s'
    sql3 = 'SELECT overtime from user where username= %s'
    sql4 = r'update user set overtime=%s  where username=%s'
    sql5 = 'delete from registercode where paycode = %s'
    user=user1.get()  #用户名
    nu1=num1.get()   #卡1
    nu2=num2.get()  #卡2
    nu3=num3.get()  #卡3
    pers=person.get()  #推广人
    RES = conn.fetchone(sql1,user)
    res=conn.conn.cursor().execute(sql1,user)
    isuser=conn.conn.cursor().execute(sql1,pers)   #查询推广人是否存在
    resisuser=conn.fetchone(sql1,pers)   #查询推广人
    isovertime=conn.fetchone(sql3,pers)
    res1=conn.conn.cursor().execute(sql2,nu1)       #返回值为1证明该注册码为真
    res2=conn.conn.cursor().execute(sql2,nu2)
    res3=conn.conn.cursor().execute(sql2,nu3)
    result = conn.fetchone(sql3,user)   #用户剩余时间
    if (res == 0 or len(user)== 0 or RES[0] != user) == True:
        windows1.title('用户名不存在或为空!!')
        return
    if (nu1 == nu2 or nu1 == nu3 or nu2 ==nu3) and (len(nu1+nu2+nu3))>15 :
        windows1.title('一张注册卡只能使用一次!!')
        return
    if res1+res2+res3 == 3 :  #全部正确
        if len(pers) == 0:  #推广人为空
            t1=result[0]+datetime.timedelta(days=31)   #增加后的时间
            conn.conn.cursor().execute(sql4,(t1,user))
            conn.conn.commit()
            windows1.title('充值成功，当前账户加时31天!!')
            conn.conn.cursor().execute(sql5,nu1)  #注册成功删除注册卡
            conn.conn.cursor().execute(sql5,nu2)
            conn.conn.cursor().execute(sql5,nu3)
            conn.conn.commit()
        elif isuser == 0 :
            windows1.title('推广人账号未找到!!')
        elif isuser ==1  :
            if  (nu1 == nu2 or nu1 == nu3 or nu2 ==nu3) == True:
                windows1.title('禁止重复使用注册卡!!')
            else:
                t1=result[0]+datetime.timedelta(days=32)   #填写推广人后的时间在双方基础上多加一天
                t2=isovertime[0]+datetime.timedelta(days=1) #被推广人时间加一天
                conn.conn.cursor().execute(sql4,(t1,user))
                conn.conn.cursor().execute(sql4,(t2,pers))
                conn.conn.commit()
                windows1.title('充值成功，当前账户加时32天!!')
                conn.conn.cursor().execute(sql5,nu1)
                conn.conn.cursor().execute(sql5,nu2)
                conn.conn.cursor().execute(sql5,nu3)
                conn.conn.commit()
        else:
            windows1.title('未知错误,请关闭软重新充值!!')
    elif res1+res2+res3 ==2:   #正确2个
        if len(pers) == 0:  #推广人为空
            t1=result[0]+datetime.timedelta(days=14)   #增加后的时间
            conn.conn.cursor().execute(sql4,(t1,user))
            conn.conn.cursor().execute(sql5,nu1)
            conn.conn.cursor().execute(sql5,nu2)
            conn.conn.cursor().execute(sql5,nu3)
            conn.conn.commit()
            windows1.title('充值成功，当前账户加时14天!!')
            conn.conn.cursor().execute(sql5,nu1)
            conn.conn.cursor().execute(sql5,nu2)
            conn.conn.cursor().execute(sql5,nu3)
            conn.conn.commit()
        elif isuser == 0:
            windows1.title('推广人账号未找到!!')
        else:
            t1=result[0]+datetime.timedelta(days=15)   #填写推广人后的时间在双方基础上多加一天
            t2=isovertime[0]+datetime.timedelta(days=1)
            conn.conn.cursor().execute(sql4,(t1,user))
            conn.conn.cursor().execute(sql4,(t2,pers))
            conn.conn.cursor().execute(sql5,nu1)
            conn.conn.cursor().execute(sql5,nu2)
            conn.conn.cursor().execute(sql5,nu3)
            conn.conn.commit()
            windows1.title('充值成功，当前账户加时15天!!')

    elif res1+res2+res3 ==1:   #正确1个
        if len(pers) == 0:  #推广人为空
            t1=result[0]+datetime.timedelta(days=7)   #增加后的时间
            conn.conn.cursor().execute(sql4,(t1,user))
            conn.conn.commit()
            windows1.title('充值成功，当前账户加时7天!!')
            conn.conn.cursor().execute(sql5,nu1)
            conn.conn.cursor().execute(sql5,nu2)
            conn.conn.cursor().execute(sql5,nu3)
            conn.conn.commit()
        elif isuser == 0:
            windows1.title('推广人账号未找到!!')
        else:
            t1=result[0]+datetime.timedelta(days=8)   #填写推广人后的时间在双方基础上多加一天
            t2=isovertime[0]+datetime.timedelta(days=1)
            conn.conn.cursor().execute(sql4,(t1,user))
            conn.conn.cursor().execute(sql4,(t2,pers))
            conn.conn.commit()
            windows1.title('充值成功，当前账户加时8天!!')
            conn.conn.cursor().execute(sql5,nu1)
            conn.conn.cursor().execute(sql5,nu2)
            conn.conn.cursor().execute(sql5,nu3)
            conn.conn.commit()
    else:                       #正确0个
            windows1.title('请输入正确的注册码!!')

Button1 = tk.Button(windows, text='登陆',bg='black',fg='white', command=get)
Button1.place(height=30, width=60, x=850, y=65)

Button2 = tk.Button(windows, text='注册',bg='black',fg='white', command =regist)
Button2.place(height=32, width=60, x=850, y=110)

Button3 = tk.Button(windows, text='充值',bg='black',fg='white', command =pay)
Button3.place(height=32, width=60, x=850, y=155)

Button3 = tk.Button(windows, text='查询',bg='black',fg='white', command =xxcx)
Button3.place(height=32, width=60, x=850, y=20)

Button4 = tk.Button(windows, text='修改密码',bg='black',fg='white', command =mmxg)
Button4.place(height=32, width=60, x=850, y=200)

tk.mainloop()
