"""
Filename:   main.py
Author:     Piyaphat Jaiboon
Data:       2026-05-03 (03/05/2026)
Version:    0.1.0
Description: Entry point for FastAPI  App
             Used to bind URL paths to function
"""

from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from  line_api import *
from linebot.v3.exceptions import InvalidSignatureError

from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

class LineSignatureMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/callback":
            signature = request.headers.get("x-line-signature")
            if not signature:
                return JSONResponse(
                    content={"detail": "Missing X-Line-Signature header"},
                    status_code=400
                )

            body = await request.body()
            request.state.body = body

            try:
                # We call handle once here just to validate the signature.
                # The actual event processing will happen again in the route,
                # but since we are just validating, this is the most reliable way
                # as handler.handle does the HMAC check internally.
                handler.handle(body.decode('utf-8'), signature)
            except InvalidSignatureError:
                return JSONResponse(
                    content={"detail": "Invalid Signature"},
                    status_code=400
                )

        return await call_next(request)

app.add_middleware(LineSignatureMiddleware)

# ==== FastAPI Section ====
@app.post("/callback")
async def callback(request : Request):
    body_str = request.state.body.decode('utf-8')
    x_line_signature = request.headers.get("x-line-signature")

    # The middleware already validated the signature,
    # but we call handle again to actually trigger the @handler.add decorated functions.
    handler.handle(body_str, x_line_signature)

    return {"status": "ok"}

