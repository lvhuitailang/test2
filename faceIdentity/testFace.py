
import requests
import json
import base64
API_KEY = 'YHwHt9pGSXRCtmm8CBoGka6n'
SECRET_KEY = '4lvSGf6sac11XSxpiGvU0zSxDGkGvwWF'

TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

FACE_DETECT = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
def fetch_token():
    '''
    获得token
    :return:
    '''
    param = {
        'grant_type' : 'client_credentials',
        'client_id':API_KEY,
        'client_secret':SECRET_KEY

    }
    response = requests.post(url=TOKEN_URL,data=param)
    if response.status_code == requests.codes.ok:
        result = json.loads(response.text)
        return result['access_token']
    else:
        return None


def read_file(filePath):
    '''
    读取图片
    :return:
    '''

    with open(filePath,'rb') as f:
        return f.read()


def get_request(url,headers,data):
    response = requests.request(method='post',url=url,headers=headers,data=data)
    if response.status_code == requests.codes.ok:
        resultJson = json.loads(response.text)
        return resultJson





if '__main__' == __name__:
    access_token = fetch_token()
    file = read_file('img/test.jpg')
    headers = {'Content-Type':'application/json'}
    data = {
        'access_token':access_token,
        'image':base64.b64encode(file),
        'image_type':'BASE64',
        'face_field':'age,gender',
        'max_face_num':'2'
    }
    result = get_request(FACE_DETECT,headers,data)['result']
    print('人脸数目:'+str(result['face_num']))
    if result['face_num'] > 0:
        for face in result['face_list']:
            print('===========')
            print('年龄:'+str(face['age']))
            print('性别:'+str(face['gender']['type']))

    pass