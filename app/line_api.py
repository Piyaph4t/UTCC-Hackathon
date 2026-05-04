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
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    FileMessageContent,
    ImageMessageContent,
    AudioMessageContent,
    VideoMessageContent
)


from dotenv import load_dotenv
import json
import os
import asyncio
import logging
from scanners.file_scanner import scan_file

load_dotenv()
configuration = Configuration(access_token=os.getenv("LINE_ACCESS_TOKEN"))
handler = WebhookHandler(channel_secret=os.getenv("LINE_CHANNEL_SECRET"))
logger = logging.getLogger(__name__)


# ==== Line Webhook =====

async def download_message_content(message_id: str) -> bytes:
    """Downloads the binary content of a message from LINE API."""
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        content = line_bot_api.get_message_content(message_id)
        return content.read()

@handler.add(MessageEvent)
async def handle_message(event):
    # Log the event
    event_data = str(dict(event))
    with open("Meassage.log", "a") as log:
        log.write(event_data + "\n")

        # Check if message is a file/media
    if isinstance(event.message, (FileMessageContent, ImageMessageContent, AudioMessageContent, VideoMessageContent)):
        try:
            # 1. Download content
            content = await download_message_content(event.message.id)


        except Exception as e:
            logger.error(f"Error processing file scan: {e}")
