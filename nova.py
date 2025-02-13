import os
import subprocess
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Admin key for secured commands
ADMIN_KEY = "OmPrateek4843"

# Function to execute shell commands securely
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode()}"

# Route for running secure commands
@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    if data.get("admin_key") == ADMIN_KEY:
        command = data.get("command")
        output = execute_command(command)
        return jsonify({"output": output})
    else:
        return jsonify({"error": "Unauthorized"}), 403

# Self-evolution logic
def evolve():
    print("Nova is evolving...")
    ensure_file("requirements.txt", "flask\ngunicorn")
    ensure_file("Dockerfile", '''
    FROM python:3.9
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["gunicorn", "nova:app", "--bind", "0.0.0.0:8000"]
    ''')
    print("Evolution complete.")

def ensure_file(filename, content):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(content)
        print(f"Created {filename}.")

@app.route("/", methods=["GET"])
def home():
    return "Nova is alive and evolving!"

if __name__ == "__main__":
    evolve()
    app.run(host="0.0.0.0", port=8000)
