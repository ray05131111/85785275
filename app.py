from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 使用你的 Channel Secret 和 Channel Access Token
CHANNEL_SECRET = 'YOUR_CHANNEL_SECRET'
CHANNEL_ACCESS_TOKEN = 'YOUR_CHANNEL_ACCESS_TOKEN'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # 获取请求的签名
    signature = request.headers['X-Line-Signature']

    # 获取请求的内容
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 回复用户发送的消息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Hello, {}'.format(event.message.text))
    )

if __name__ == "__main__":
    app.run(debug=True)
