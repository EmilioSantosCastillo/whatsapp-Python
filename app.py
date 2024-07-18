from flask import Flask,request
import util
import whatsappservice

app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def index():
    return "welcome developer"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():
   
    try:
        accessToken="7SDAAS456ASD"
        token=request.args.get("hub.verify_token")
        challenge=request.args.get("hub.challenge")

        if token != None and challenge != None and token==accessToken:
            return challenge
        else:
            return "",400
    except:
         return "",400
    
@app.route('/whatsapp', methods=['POST'])
def ReceiveMessage():
    try:
        body=request.get_json()
        entry=(body["entry"])[0]
        changes=(entry["changes"])[0]
        value=changes["value"]
        message=(value["messages"])[0]
        number=message["from"]
        text=util.GetTextUser(message)
        print(text)
        GenerateMessage(text,number)
        
        return "EVENT_RECEIVED"

    except:
        return "EVENT_RECEIVED"


def GenerateMessage(text,number):
    text="El usuario dijo :" +text + number
    whatsappservice.SendMessageWhatsapp(text,number)


if __name__ == "__main__":
    app.run(debug=True)
