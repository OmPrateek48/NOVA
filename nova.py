from flask import Flask, request
import hashlib

app = Flask(__name__)
admin_key_hash = hashlib.sha256("OmPrateek4843".encode()).hexdigest()

@app.route("/")
def home():
    return "Nova AI is running and evolving!"

@app.route("/verify", methods=["POST"])
def verify_admin():
    data = request.json
    if hashlib.sha256(data["key"].encode()).hexdigest() == admin_key_hash:
        return {"status": "success", "message": "Admin verified."}
    else:
        return {"status": "error", "message": "Unauthorized access."}, 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
