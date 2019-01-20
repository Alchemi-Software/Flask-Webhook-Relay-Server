from flask import Flask
from flask import request,render_template,url_for
from gmail import *
import requests

import os

def getfile(name):
    f = open(name)
    t = f.read()
    f.close()
    return t

app = Flask(__name__)
app.config['TRAP_HTTP_EXCEPTIONS']=True

display = "Auto Mailer"

fwdheader = "Listserv Test"

address = "cattmompton@gmail.com"

password = getfile("emailpass")

# If = "OFF", then no webhook
discord = getfile("discord")

fromad = display + "<" + address + ">"
mailer = GMail(fromad,password)

def addemail(email):
    if os.path.exists("emails.txt"):
        f = open("emails.txt","a+")
        f.write("\n"+email)
        f.close()

def getemails():
    if os.path.exists("emails.txt"):
        f = open("emails.txt")
        t = f.read()
        f.close()
        return t


def mid():
    if not os.path.exists("c"):
        f = open("c","w")
        f.write("1")
        f.close()
    f = open("c")
    c = int(f.read())
    f.close()
    os.remove("c")
    c += 1
    f = open("c","w")
    f.write(str(c))
    f.close()
    return c

def getc():
    f = open("c")
    c = f.read()
    f.close()
    return c

def latest():
    f = open("msg")
    t = f.read()
    f.close()
    return t

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        address = request.form.get("email")
        addemail(address)
        return render_template('notification.html', type="success", text="Added " + address + " to the list")

    return render_template('index.html', message=str(latest()))


@app.route("/message/")
def handlemessage():
    send = request.args.get("t")
    if send == None:
        if os.path.exists("msg"):
            f = open("msg")
            c = f.read()
            f.close()
            return c
        else:
            return "No message"
    else:
        if os.path.exists("msg"):
            os.remove("msg")
        f = open("msg","w")
        f.write(send)
        # Email list
        #emails = str(getemails()).split("\n")
        #for email in emails:
            #if email != "\n":
                #forward = Message(fwdheader,to=email,text="Forward: " + send)
                #mailer.send(forward)

        if discord != "OFF":
            r = requests.post(discord, data={"username":"Relay Doggo","avatar_url":"https://i.ytimg.com/vi/4PDQ1gziLL8/maxresdefault.jpg","content":send})

        f.close()
        mid()
        return str(getc()) + ": Sent " + send



@app.errorhandler(Exception)
def http_error_handler(e):
    return render_template("notification.html",type="danger",text=str(e))

@app.route("/latest/")
def returnboi():
    return getc()

app.run(host='0.0.0.0',port=6969,debug=True)
