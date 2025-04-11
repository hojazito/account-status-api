from flask import Flask, request, jsonify

app = Flask(__name__)

accounts = {
    "1026297289": {"Estado de cuenta": "Suspendido", "Saldo":"-250.000", "code": 403},
    "1056726846": {"Estado de cuenta": "Activa","Saldo";"450.000", "code": 200},
    "1025386467": {"Estado de cuenta": "En Revisión","Saldo";"0", "code": 102}
}

@app.route("/status", methods=["GET"])
def get_status():
    account = request.args.get("account")
    if account in accounts:
        return jsonify(accounts[account])
    else:
        return jsonify({"error": "Account not found"}), 404
