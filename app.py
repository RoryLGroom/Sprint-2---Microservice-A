from flask import Flask, jsonify, request
import uuid
import datetime

from controller import create_hold, retrieveHold, removeHold


app = Flask(__name__)


@app.route("/api/v1/transactions/holds", methods=["POST"])
def create_hold_endpoint():
    request_body = request.get_json()
    return jsonify(create_hold(request_body))


@app.route("/api/v1/transactions/holds", methods=["GET"])
def getHold():
    request_body = request.get_json()
    book_id = request_body["book_id"]


    return jsonify(retrieveHold(book_id))

@app.route("/api/v1/transactions/holds", methods=["DELETE"])
def deleteHold():
    request_body = request.get_json()
    book_id = request_body["book_id"]
    user_id = request_body["user_id"]

    return jsonify(removeHold(book_id, user_id))


if __name__ == "__main__":
    app.run(port=8000)

# 2025-MM-DD
