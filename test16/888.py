from xiaoai import *
import random
import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def outputJson(toSpeakText, is_session_end, openMic=True):
    xiaoAIResponse=XiaoAIResponse(to_speak=XiaoAIToSpeak(type_=0, text=toSpeakText), open_mic=openMic)
    response = xiaoai_response(XiaoAIOpenResponse(version="1.0",
                                                  is_session_end=is_session_end,
                                                  response=xiaoAIResponse))
    return response


def main(event):
    req = xiaoai_request(event)
    if req.request.type == 0:
        return outputJson('欢迎来到随机数，请说来一个随机数，或者返回一个100以内的随机数。', False)
    elif req.request.type == 1:
        if ((not hasattr(req.request, "slot_info")) or (not hasattr(req.request.slot_info, "intent_name"))):
            return outputJson("抱歉，我没有听懂", False)
        else:
            if req.request.slot_info.intent_name == 'random_any':
                return outputJson('您所要的随机数是：'+str(random.randint(0,1000)), False)
            elif req.request.slot_info.intent_name == 'random_in':
                slotlist = req.request.slot_info.slots
                maxValue = [item for item in slotlist if item['name']=='numberMax'][0]['value']
                return outputJson('您所要的随机数是：'+str(random.randint(0,int(maxValue))), False)
            else: return outputJson("抱歉，我没有听懂", False)
    else:
        return outputJson("感谢使用随机数，下次再见", True, False)

