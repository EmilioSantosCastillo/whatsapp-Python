import requests
import json

def SendMessageWhatsapp(textUser,number):
    try:
        token="EAAQgVrW8ObgBO67hnFMP1pBKW3kHGp9ZBHyFBCJVEIZAeH8cncr5vFg2losUZB9JZCj7TS69vffKQTellYON1KasqtrSZAEKzMCrQZCHqrWe9seOYRh4BfCO1VZAK7kTYPy9raovxSt084NQ7bvK62Qgs7WmNRznXDvW5Y3eYWOEWOfJ6Np6tuh7uLminS0R7KxpbMSmZB2KaFkEh1K8rvmwsAzGbuN9egZC8nVLpc80ZD"
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
    
