from flask import Flask, request, jsonify

app = Flask(__name__)

accounts = {
    "12345": {"status": "suspended", "code": 403},
    "67890": {"status": "active", "code": 200},
    "99999": {"status": "pending", "code": 102}
}

@app.route("/status", methods=["GET"])
def get_status():
    account = request.args.get("account")
    if account in accounts:
        return jsonify(accounts[account])
    else:
        return jsonify({"error": "Account not found"}), 404