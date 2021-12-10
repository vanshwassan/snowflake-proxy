import os
from flask import Flask, jsonify, request
import json
import snowflake_conn

app = Flask(__name__)
app.secret_key = "snowflake-test"

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

## ENDPOINT ROUTES ##

@app.route('/get')
def resp():
    resp = snowflake_conn.getCases()
    return jsonify({"cases": int(resp)})


@app.route('/post', methods=["POST"])
def send():
    sql = request.json['sql']
    resp = snowflake_conn.sendSQL(sql)
    return jsonify({"value": int(resp)})

if __name__ == "__main__":
    app.run(debug=True)