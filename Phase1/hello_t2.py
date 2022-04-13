from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    #Flask의 경우 WSGI 엔진이여서 Shell Script 사용하여 서버의 주소 추출
    hostip = subprocess.check_output(
        "hostname -I", shell=True
    ).decode('utf-8')
    

    return 'Hello SFMICI-T2 Internship  ' + 'serviced from  >>>>' +  hostip

if __name__ == '__main__':
    app.run(host='0.0.0.0')