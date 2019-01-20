import requests,time

ip = "127.0.0.1"
port = "6969"

init = requests.get("http://"+ip+":"+port+"/latest/")
mm = int(init.text)
print(str(mm))

while True:
    time.sleep(0.5)
    ct = requests.get("http://"+ip+":"+port+"/latest/")
    cm = int(ct.text)
    if cm > mm:
        message = requests.get("http://"+ip+":"+port+"/message/")
        print(message.text)
        mm = cm
