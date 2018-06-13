#coding: UTF-8
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Este é o primeiro site python da aluna: Sonia Nalli"
	