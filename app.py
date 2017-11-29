from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('NhK1NYrKfK8zknlm9aJlYlxWDbwAqmYbo2nAsYaQ44B0IZp2s98JO1bpgyuoiDXSV8ezdrvaRvzyA3zZYlFLCj2LBSXeEvvZqPoieOgIust/e7M33Vcr/1qdaGeEz0yR1wCbaMgfaT5nSALJmpHUXQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5a4d548b5cb54cac295af2ea9ce2032d')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='hi'))


if __name__ == "__main__":
    app.run()