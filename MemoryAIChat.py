import _thread as thread
import base64
import datetime
import hashlib
import hmac
import json
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import websocket  # 使用websocket_client

answer = ""


class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, Spark_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(Spark_url).netloc
        self.path = urlparse(Spark_url).path
        self.Spark_url = Spark_url

    # 生成url
    def create_url(self):
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = self.Spark_url + '?' + urlencode(v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        return url


class AIChat:
    def __init__(self):
        # 以下密钥信息从控制台获取
        self.appid = "fe2c4a11"  # 填写控制台中获取的 APPID 信息
        self.api_secret = "NDk3Njk2OGIwYTFlZDZiNWVlMWM1ZjVh"  # 填写控制台中获取的 APISecret 信息
        self.api_key = "2523e8f0d30b56fe0ce00f7d2b8e3099"  # 填写控制台中获取的 APIKey 信息

        # 用于配置大模型版本，默认“general/generalv2”
        # domain = "general"   # v1.5版本
        self.domain = "generalv2"  # v2.0版本
        # 云端环境的服务地址
        # Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
        self.Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址

        self.text = []

    @staticmethod
    # 收到websocket错误的处理
    def on_error(ws, error):
        print("### error:", error)

    @staticmethod
    # 收到websocket关闭的处理
    def on_close(ws, one, two):
        print(" ")

    # 收到websocket连接建立的处理
    def on_open(self, ws):
        thread.start_new_thread(self.run, (ws,))

    def run(self, ws, *args):
        data = json.dumps(self.gen_params(appid=ws.appid, domain=ws.domain, question=ws.question))
        ws.send(data)

    @staticmethod
    # 收到websocket消息的处理
    def on_message(ws, message):
        # print(message)
        data = json.loads(message)
        code = data['header']['code']
        if code != 0:
            print(f'请求错误: {code}, {data}')
            ws.close()
        else:
            choices = data["payload"]["choices"]
            status = choices["status"]
            content = choices["text"][0]["content"]
            print(content, end="")
            global answer
            answer += content
            # print(1)
            if status == 2:
                ws.close()

    @staticmethod
    def gen_params(appid, domain, question):
        """
        通过appid和用户的提问来生成请参数
        """
        data = {
            "header": {
                "app_id": appid,
                "uid": "1234"
            },
            "parameter": {
                "chat": {
                    "domain": domain,
                    "random_threshold": 0.5,
                    "max_tokens": 2048,
                    "auditing": "default"
                }
            },
            "payload": {
                "message": {
                    "text": question
                }
            }
        }
        return data

    def main(self, appid, api_key, api_secret, Spark_url, domain, question):
        # print("星火:")
        wsParam = Ws_Param(appid, api_key, api_secret, Spark_url)
        # websocket.enableTrace(False)
        wsUrl = wsParam.create_url()
        ws = websocket.WebSocketApp(wsUrl, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close,
                                    on_open=self.on_open)
        ws.appid = appid
        ws.question = question
        ws.domain = domain
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def getText(self, role, content):
        jsoncon = {}
        jsoncon["role"] = role
        jsoncon["content"] = content
        self.text.append(jsoncon)
        return self.text

    @staticmethod
    def getlength(text):
        length = 0
        for content in text:
            temp = content["content"]
            leng = len(temp)
            length += leng
        return length

    def checklen(self, text):
        while (self.getlength(text) > 8000):
            del text[0]
        return text

    def init(self):
        self.text.clear
        print("-------------------------------------------")
        print("作者: @Memory ")
        print("欢迎使用讯飞星火API接口，实现防伪验证！")
        print("-------------------------------------------")

        input("开始对话吧！(单击Enter键开始)")
        while (1):
            Input = input(">>> User: ")
            self.question = self.checklen(self.getText("user", Input))
            answer = ""
            print(">>> AI: ", end="")
            self.main(self.appid, self.api_key, self.api_secret, self.Spark_url, self.domain, self.question)
            self.getText("assistant", answer)
            # print(str(text))
