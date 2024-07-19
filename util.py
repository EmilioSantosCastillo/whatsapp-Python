def GetTextUser(message):
    text=""
    typeMessage=message["type"]

    if typeMessage=="text":
        text=(message["text"])["body"]
    elif typeMessage=="interactive":
        interactiveObject=message["interactive"]
        typeInteractive=interactiveObject["type"]
        if typeInteractive=="button_reply":
            text=(interactiveObject["button_reply"])["title"]
        elif typeInteractive=="list_reply":
            text=(interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")


    else:
        print("sin mensaje")

    return text

def TextMessage(text,number):
    data={
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": text
            }
        }
    return data

def TextFormatoMessage(text,number):
    
    data={
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "text",
            "text": {
                "body": "*body_text*"
            }
        }
    return data

def ImageMessage(number):
    
    data={
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "image",
            "image": {
                "link": "https://www.cdc.gov/coronavirus/2019-ncov/images/symptoms-testing/pcr-test.png?_=15023"
            }
        }
    return data

def AudioMessage(number):
    
    data={
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "audio",
            "audio": {
                "link": "https://www.cdc.gov/coronavirus/2019-ncov/images/symptoms-testing/pcr-test.png?_=15023"
            }
        }
    return data

def VideoMessage(number):
    
    data={
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "video",
            "video": {
                "link": "https://www.cdc.gov/coronavirus/2019-ncov/images/symptoms-testing/pcr-test.png?_=15023"
            }
        }
    return data

def DocumentMessage(number):
    
    data={
            "messaging_product": "whatsapp",    
            "to": number,
            "type": "document",
            "document": {
                "link": "https://www.cdc.gov/coronavirus/2019-ncov/images/symptoms-testing/pcr-test.png?_=15023"
            }
        }
    return data

def LocationMessage(number):
    
    data={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "location",
            "location": {
                "latitude": "-29.97365336281068",
                "longitude": " -71.25937594232917",
                "name": "casa",
                "address": "los ruiles 691"
            }
        }
    return data

def ButtonMessage(number):
    
    data={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "<BUTTON_TEXT>😁"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_1>",
                                "title": "<BUTTON_TITLE_1>"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_2>",
                                "title": "<BUTTON_TITLE_2>"
                            }
                        }
                    ]
                }
            }
        }
    return data

def ListMessage(number):
    
    data={
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": "✅ I have these options"
                },
                "footer": {
                    "text": "Select an option"
                },
                "action": {
                    "button": "See options",
                    "sections": [
                        {
                            "title": "Buy and sell products",
                            "rows": [
                                {
                                    "id": "main-buy",
                                    "title": "Buy",
                                    "description": "Buy the best product your home"
                                },
                                {
                                    "id": "main-sell",
                                    "title": "Sell",
                                    "description": "Sell your products"
                                }
                            ]
                        },
                        {
                            "title": "📍center of attention",
                            "rows": [
                                {
                                    "id": "main-agency",
                                    "title": "Agency",
                                    "description": "Your can visit our agency"
                                },
                                {
                                    "id": "main-contact",
                                    "title": "Contact center",
                                    "description": "One of our agents will assist you"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    return data