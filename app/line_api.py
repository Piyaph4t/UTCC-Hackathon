"""
Author: Piyaphat Jaiboon
Filename: line_api.py
Date: 2026-05-04 (04/05/2026)
Description: Handle Line chatbot api and webhook
"""

from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent


from dotenv import load_dotenv
import os

load_dotenv()
configuration = Configuration(access_token=os.getenv("LINE_ACCESS_TOKEN"))
handler = WebhookHandler(channel_secret=os.getenv("LINE_CHANNEL_SECRET"))


# ==== Line Webhook =====
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        test_reply_massage = "Hello from Fast/Line API"
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=test_reply_massage)],
            )
        )
