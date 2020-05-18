from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import checkpass

app = Flask(__name__)

cors = CORS(app)


@app.route("/check-pass", methods=['POST'])
def process_pass():
    pass_request = request.json
    password = pass_request.get('password')
    return jsonify({'result': checkpass.check_password(password)})
