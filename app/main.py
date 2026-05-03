"""
Filename:   main.py
Author:     Piyaphat Jaiboon
Data:       2026-05-03 (03/05/2026)
Version:    0.1.0
Description: Entry point for FastAPI  App
             Used to bind URL paths to function
"""

from fastapi import FastAPI, Request, HTTPException, Header

from  line_api import *

from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()


# ==== FastAPI Section ====
@app.post("/callback")
async def callback(request : Request, x_line_signature : str = Header(None)) :
    body = await  request.body()
    body_str = body.decode('utf-8')
    try :
        handler.handle(body_str, x_line_signature)
    except :
        print("Invalid Signature. please check your access tokne / channel secret.")
        raise   HTTPException(status_code=400,detail="Invalid Signature.")

