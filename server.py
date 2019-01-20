from flask import Flask
from flask import request

import os

app = Flask(__name__)

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
        f.close()
        mid()
        return str(getc()) + ": Sent " + send

@app.route("/latest/")
def returnboi():
    return getc()


app.run(host='0.0.0.0',port=6969)
