from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    return "Hello bro"


@app.route("/")
def main():
    return "Welcome1"

if __name__ == "__main__":
   #app.run() ##Replaced with below code to run it using waitress 
   serve(app, host='0.0.0.0', port=8000)