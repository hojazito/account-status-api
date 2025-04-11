from flask import Flask, request, jsonify

app = Flask(__name__)

# Example account database
accounts = {
    "1026297289": {"Estado": "Suspendido", "Saldo": "-250.000"},
    "1056726846": {"Estado": "Activa", "Saldo": "450.000"},
    "1025386467": {"Estado": "En Revisión", "Saldo": "0"}
}

# API route to get account status
@app.route("/status", methods=["GET"])
def get_status():
    account = request.args.get("account")
    if account in accounts:
        return jsonify(accounts[account])
    else:
        return jsonify({"Estado": "No encontrado", "Saldo": "N/A"}), 200
