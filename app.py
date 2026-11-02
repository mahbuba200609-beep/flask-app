from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Mening PaaS ishlayapti!"

@app.route("/haqida")
def haqida():
    return "Bu mening birinchi Flask ilovam."
