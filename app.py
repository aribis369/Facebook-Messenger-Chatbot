import os,sys
from flask import Flask,request
from pymessenger import Bot


# initializing the flask app
app=Flask(__name__)
# initializing the pymessenger bot
# get yourself a access token and initialize using this
# the access token below has been tampered and will not work
bot=Bot("EAACkXEqdZAksBAGR6urSN4r2O3PCuJXvKngAO8ZADVWyMs9cWFCOWyr4ek4A1ZCsv8Kw4U9GMrrHoBl7p1VvxhoLGz8ePRUXTDYONdchgfhfhghfOFtfQcZBXt01kaLZA7Gks6k10nUPTQZCfgjgjyygjgfxfgxgfxgx")

# defining a dictionary for queries and their corresponding answers
# A LOT OF WORK IS TO BE DONE IN THIS SECTION
dic={"how are you?":"I'm fine,what about you","who are you?":"I'm a BOT,I assist people","what is your name?":"My name is PeaceBot","hello":"hello, how are you?","I'm fine":"Any work that I can do for you"}

@app.route("/",methods=['GET'])
# this entire function is the used to setup the webhook with the api
# the "hello" word you find is the verification token there
# this part is required to verify whether the bot is run on a server having https configuration
# other things in this part is just following steps to setup webhook.(found in messenger api documentation)
def ver():
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "Verification token mismatch",403
        return request.args["hub.challenge"],200
    return "hello",200


# this part is to be used when webhook is setup and our bot is connected to our server
# the messenges it recieves is sent to our server, the entire info is give in json format with many thinhgs like sender_id, message etc.(P.S. the api doc)
@app.route("/",methods=['POST'])
def webhook():
    # collecting the json data sent by the api
    data=request.get_json()
    #this part is for printing the message and checking for any errors in recieving the json object sent by messenger api
    log(data)
    
    # after message is recieved the message sent is read and the corresponding answer is generated from the dictionary dic
    if data["object"]=="page":
        for entry in data["entry"]:
            for mess in entry["messaging"]:
                m=mess["message"]["text"]
                sid=mess["sender"]["id"]
                try:
                    s=dic[m]
                except:
                    # if no query matches anything in dic then this message is sent to the user
                    s="Sorry, I am not trained well enough to answer yuor query.YOU CAN VISIT http://peacehai.com" 
                # sending message to the user
                bot.send_text_message(sid,s)
              

 
    return "ok", 200  


def log(mess):
    print(mess)
    sys.stdout.flush()


if __name__=="__main__":
    app.run(debug=True)
