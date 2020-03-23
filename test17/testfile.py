import json
if __name__ == '__main__':
    with open('./userInfo.json',encoding='utf8',mode='r') as f:
            print(json.loads(f.read()))





