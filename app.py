import json

from jsonschema import validate
from flask import Flask, request, jsonify
from src import Pool
from flask_cors import CORS


app = Flask(__name__)
pool = Pool()
CORS(app)

request_schema = {
    "type": "object",
    "definitions": {
        "item": {
            "type": "object",
            "properties": {
                "item_id": {"type": "number"},
                "volume": {"type": "number"}
            },
            "required": ["item_id", "volume"]
        }
    },
    "properties": {
        "user_id": {"type": "number"},
        "items": {
            "type": "array",
            "items": {"$ref": "#/definitions/item"}
        }
    },
    "required": ["user_id", "items"]
}

@app.route('/', methods=['GET','POST'])
def main():
    response = None
    if request.method == 'GET':
        response = pool.pop()

    elif request.method == 'POST':
        body_json = request.json
        validate(body_json, request_schema)
        pool.push(body_json)
        response = {'result': 'success'}

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
