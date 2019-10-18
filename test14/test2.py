import tkinter as tk
import urllib.request
import urllib.parse
import json



windows = tk.Tk()

res=tk.StringVar()
cont=tk.StringVar()

windows.title('翻译')
windows.geometry('281x209')
windows.resizable(0,0)


Label1=tk.Label(windows,text='翻译内容:')
Label1.place(height = 25,width = 89,x = 5,y = 10)
Entry1=tk.Entry(windows, textvariable=cont)
Entry1.place(height = 38,width = 271,x = 5,y = 43)
Button1=tk.Button(windows,text='翻译',command= lambda:fy())
Button1.place(height = 30,width = 50,x = 100,y = 93)
Label2=tk.Label(windows,text='翻译结果:')
Label2.place(height = 29,width = 89,x = 6,y = 124)
Entry2=tk.Entry(windows, textvariable=res)
Entry2.place(height = 38,width = 271,x = 5,y = 156)

def fy():
    line = cont.get()
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
    data={}
    data['i'] = line
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1517799189818'
    data['sign'] = '8682192c0707c52ecdffbc98f77a17ac'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'true'


    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')


    translate_results = json.loads(html)
    #找到翻译结果，load函数能将str转换成dict类型
    translate_results = translate_results['translateResult'][0][0]['tgt']
    res.set(translate_results)

windows.mainloop()
