import os,sys
from flask import Flask,request
from pymessenger import Bot



app=Flask(__name__)
bot=Bot("EAACkXEqdZAksBAGR6urSN4r2O3PCuJXvKngAO8ZADVWyMs9cWFCOWyr4ek4A1ZCsv8Kw4U9GMrrHoBl7p1VvxhoLGz8ePRUXTDYONdchgfhfhghfOFtfQcZBXt01kaLZA7Gks6k10nUPTQZCfgjgjyygjgfxfgxgfxgx")

dic={"how are you?":"I'm fine,what about you","who are you?":"I'm a BOT,I assist people","what is your name?":"My name is PeaceBot","hello":"hello, how are you?","I'm fine":"Any work that I can do for you"}

@app.route("/",methods=['GET'])
def ver():
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "Verification token mismatch",403
        return request.args["hub.challenge"],200
    return "hello",200

@app.route("/",methods=['POST'])
def webhook():
    data=request.get_json()
    log(data)
    

    if data["object"]=="page":
        for entry in data["entry"]:
            for mess in entry["messaging"]:
                m=mess["message"]["text"]
                sid=mess["sender"]["id"]
                try:
                    s=dic[m]
                except:
                    s="Sorry, I am not trained well enough to answer yuor query.YOU CAN VISIT http://peacehai.com" 
                bot.send_text_message(sid,s)
              

 
    return "ok", 200  


def log(mess):
    print(mess)
    sys.stdout.flush()


if __name__=="__main__":
    app.run(debug=True)
