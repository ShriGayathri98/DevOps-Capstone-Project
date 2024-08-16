from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
CORS(app)
Talisman(app, content_security_policy=None, force_https=False)

@app.route('/')
def hello_world():
    return 'Hello, World!'

accounts = {}

@app.route('/accounts', methods=['GET'])
def list_accounts():
    return jsonify(accounts), 200

@app.route('/accounts/<account_id>', methods=['GET'])
def get_account(account_id):
    account = accounts.get(account_id)
    if not account:
        return jsonify({'error': 'Account not found'}), 404
    return jsonify(account), 200

@app.route('/accounts', methods=['POST'])
def create_account():
    account = request.json
    account_id = account.get('id')
    accounts[account_id] = account
    return jsonify(account), 201

@app.route('/accounts/<account_id>', methods=['PUT'])
def update_account(account_id):
    account = request.json
    if account_id not in accounts:
        return jsonify({'error': 'Account not found'}), 404
    accounts[account_id] = account
    return jsonify(account), 200

@app.route('/accounts/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    if account_id not in accounts:
        return jsonify({'error': 'Account not found'}), 404
    del accounts[account_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
