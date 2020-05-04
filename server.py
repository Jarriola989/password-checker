from flask import Flask, request
import checkpass

app = Flask(__name__)

@app.route("/check-pass", methods=['POST'])
def process_pass():
    pass_request = request.get_json()
    password = pass_request.get('password')
    return checkpass.check_password(password)