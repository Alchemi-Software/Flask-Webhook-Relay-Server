import requests

ip = "127.0.0.1"
port = "6969"

while True:
    r = requests.get("http://"+ip+":"+port+"/message/?t="+input("Message: "))
    print(r.text)
