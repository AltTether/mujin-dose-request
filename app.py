import json
from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['post'])
def main():
    hoge = request.json
    return json.dumps(hoge)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
