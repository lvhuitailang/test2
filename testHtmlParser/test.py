from pyquery import PyQuery as pq

htmlString = '''

      <strong style="font-weight: bold;color: #EE1B2E">xxx压缩软件的注册算法</strong><br>
版块：『脱壳破解区』<br>
       作者：doublesine<br>
       时间：2019-07-03 21:28:24<br>

'''
doc = pq(htmlString)
str2 = doc.text()
print('===================')
print(str2)

pass