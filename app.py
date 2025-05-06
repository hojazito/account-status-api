from flask import Flask, request, jsonify

app = Flask(__name__)

accounts = {
    "1026297289": {"Estado": "Suspendido","Nombre":"Johan Cortes", "Saldo": "-250.000"},
    "1056726846": {"Estado": "Activa","Nombre":"Chris Nuñez", "Saldo": "451.000"},
    "1025386467": {"Estado": "En Revisión","Nombre":"Camilo Giraldo", "Saldo": "0"}
}

@app.route("/status", methods=["GET"])
def get_status():
    account = request.args.get("account")
    if account in accounts:
        return jsonify(accounts[account])
    else:
        return jsonify({"error": "Account not found"}), 404
