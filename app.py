import json

from flask import Flask, request, jsonify
from src import Pool


app = Flask(__name__)
pool = Pool()

@app.route('/', methods=['GET','POST'])
def main():
    response = None
    if request.method == 'GET':
        response = pool.pop()
    elif request.method == 'POST':
        body_json = request.json
        pool.push(body_json)
        response = {'result': 'success'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
