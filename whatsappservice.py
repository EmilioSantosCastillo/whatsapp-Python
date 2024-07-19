import requests
import json
from dotenv import load_dotenv
import os

def SendMessageWhatsapp(data):
    try:
        token = os.getenv("WHATSAPP_API_TOKEN")
        api_url="https://graph.facebook.com/v19.0/370015532861574/messages"
        
        headers={"Content-Type":"application/json","Authorization":"Bearer " + token}
        response=requests.post(api_url,data=json.dumps(data), headers=headers)

        if response.status_code==200:
            return True
        
        return False
    
    except Exception as exception:
        print(exception)
        return False
    
