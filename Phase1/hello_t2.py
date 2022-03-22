
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    host = request.host
    return 'Hello SFMICI-T2 Internship  ' +'serviced from  ' +  host

if __name__ == '__main__':
    app.run(host='0.0.0.0')