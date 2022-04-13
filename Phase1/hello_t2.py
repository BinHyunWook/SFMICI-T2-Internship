from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Since Flask is WSGI Engine, Hosted Server's IP address will get by shell script
    hostip = subprocess.check_output(
        "hostname -I", shell=True
    ).decode('utf-8')
    

    return 'Hello SFMICI-T2 Internship  ' + 'serviced from  >>>>      ' +  hostip

if __name__ == '__main__':
    app.run(host='0.0.0.0')