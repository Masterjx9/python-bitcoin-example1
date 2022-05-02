from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    # Flask creates an html with the string "Hello World!"
    return 'Hello, World!'


@app.route('/welcome')
def welcome():
    # return a static html webpage
    bitcoindata = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return render_template("index.html", bitcoindata=bitcoindata)

# @app.route('/bitcoin', methods=['GET'])
# def bitcoin():
#     bitcoindata = requests.get(
#         "https://api.coindesk.com/v1/bpi/currentprice.json").json()
#     return bitcoindata

    # If this file is being ran directly, then the app will run.
if __name__ == "__main__":
    app.run()
