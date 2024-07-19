import requests
import json
from dotenv import load_dotenv
import os

def SendMessageWhatsapp(textUser,number):
    try:
        token = os.getenv("WHATSAPP_API_TOKEN")
        api_url="https://graph.facebook.com/v19.0/370015532861574/messages"
        data={
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "preview_url": False,
                    "body": textUser
                }
            }
        headers={"Content-Type":"application/json","Authorization":"Bearer " + token}
        response=requests.post(api_url,data=json.dumps(data), headers=headers)

        if response.status_code==200:
            return True
        
        return False
    
    except Exception as exception:
        print(exception)
        return False
    
