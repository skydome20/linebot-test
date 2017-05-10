
"""
git add .
git commit -am "make it better"
git push heroku master

"""
 
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from random import choice




app = Flask(__name__)

# 設定linebot的基本資訊
line_bot_api = LineBotApi('xxxxxxxxxxxxxxxxHio3aN15PTUu2isIxcxfwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('xxxxxxxxxxxxxxx4547d2304')


# 設定route 和 webhook
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

# 貼圖handle
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):

    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(sticker_id = choice(['146','145','140','170','507']),
						   package_id = '2'))
	





# 文字handle
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
	text = event.message.text

	
	if ("掰" in text) or ("滾" == text) or ("討厭你" in text):
		line_bot_api.reply_message(
			event.reply_token, 
			StickerSendMessage(sticker_id = choice(['507', '27', '32']),
							   package_id = '2'))

		
		
	elif "終極密碼" == text:
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="""這個功能還在開發中哦～"""))
		
			
	elif "ㄉ一ㄨˊ" in text:
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="""ㄉ一ㄨˊㄉ一ㄨˊ的"""))	
			
			
	elif "加油" == text:
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="""加油～加油～"""))
			
			
	elif "功能" == text:
		buttons_template = TemplateSendMessage(
			alt_text='Buttons template',
			template=ButtonsTemplate(
				title='笨笨的我有笨笨的功能：',
				text='小想要哪一個呢？',
				actions=[
					MessageTemplateAction(
						label='我想看小說',
						text='我想看小說'
					)
				]
			)
		)
		
		line_bot_api.reply_message(event.reply_token, buttons_template)
			
	# 其他
	else:
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="""我笨笨的，聽不懂妳在說什麼\n"""))
		
		
	

if __name__ == "__main__":
    app.run()
	
	
	
	
	
	
	
	
