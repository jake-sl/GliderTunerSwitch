import time
from flask import Flask, render_template, jsonify, request
import RPi.GPIO as GPIO
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Define GPIO pins
TUNE_PIN = 17
ANT_A_PIN = 27
ANT_B_PIN = 22
DISCONNECT_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(TUNE_PIN, GPIO.OUT)
GPIO.setup(ANT_A_PIN, GPIO.OUT)
GPIO.setup(ANT_B_PIN, GPIO.OUT)
GPIO.setup(DISCONNECT_PIN, GPIO.OUT)

GPIO.output(TUNE_PIN, GPIO.LOW)
GPIO.output(ANT_A_PIN, GPIO.LOW)
GPIO.output(ANT_B_PIN, GPIO.LOW)
GPIO.output(DISCONNECT_PIN, GPIO.LOW)

def trigger_pin(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)
    return "success"

# Replace these with your own credentials
PASSWORD = "devanoogaishammy"

API_KEYS = {
    "api_user1": "bFc9gvadVgjH",
    "api_user2": "gZBUYUCAQnCM"
}

users = {
    "web_user": PASSWORD,
    **API_KEYS
}


@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route("/")
@auth.login_required
def index():
    return render_template("index.html")

@app.route("/api/<button>", methods=["GET", "POST"])
@auth.login_required
def api(button):
    if button == "tune":
        trigger_pin(TUNE_PIN)
    elif button == "ant_a":
        trigger_pin(ANT_A_PIN)
    elif button == "ant_b":
        trigger_pin(ANT_B_PIN)
    elif button == "disconnect":
        trigger_pin(DISCONNECT_PIN)
    else:
        return jsonify({"error": "Invalid button"}), 400

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
