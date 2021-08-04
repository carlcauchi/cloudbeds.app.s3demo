import os
import json
 
from flask import Flask, jsonify
 
from s3demo import list_files, health_check
 
app = Flask(__name__)
 
# pre-requisites -
# 1. application configuration details set as environment variables to be consumed by app
# 2. aws iam cli user is already created and have s3 full access policy attached
# 3. aws s3 bucket is already created
 
 
# creating the endpoints

# healthcheck
@app.route('/healthcheck', methods=['GET'])
def health():

    return jsonify(health_check())
 
# index
@app.route('/', methods=['GET'])
def index():

    return jsonify(contents=list_files())

if __name__ == '__main__':
    app.run(
        host=os.environ.get('SERVER_ADDRESS', '0.0.0.0'),
        port=os.environ.get('SERVER_PORT', '5000'),
        debug=os.environ.get('DEBUG_MODE', False)
        )