from flask import Flask, request
from flask_cors import CORS
import checkpass

app = Flask(__name__)

cors = CORS(app)


@app.route("/check-pass", methods=['POST'])
def process_pass():
    pass_request = request.get_json()
    password = pass_request.get('password')
    return checkpass.check_password(password)
