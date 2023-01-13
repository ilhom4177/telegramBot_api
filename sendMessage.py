import os
import requests

TOKEN = os.environ['TOKEN']

def sendMessage(chat_id:str, text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    
    
