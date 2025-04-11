from flask import Flask, request, jsonify

app = Flask(__name__)


accounts = {
    "1026297289": {"Estado de cuenta": "Suspendido", "Saldo": "-250.000", "code": 403},
    "1056726846": {"Estado de cuenta": "Activa", "Saldo": "450.000", "code": 200},
    "1025386467": {"Estado de cuenta": "En Revisión", "Saldo": "0", "code": 102}
}

@app.route("/status", methods=["GET"])
def get_status():
    account = request.args.get("account")
    if account in accounts:
        response = accounts[account].copy()
        response.pop("code", None)  
        return jsonify(response)
    else:
        return jsonify({"error": "Account not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

