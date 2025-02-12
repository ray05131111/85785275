from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os


app = Flask(__name__)



@app.route("/")
def home():
    return f"LINE Bot is running on Vercel!"


# if __name__ == "__main__":
#     app.run(port=8080)
