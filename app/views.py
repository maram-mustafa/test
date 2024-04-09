from flask import jsonify
from app import app

@app.route('/api/data', methods=['GET'])
def get_data():
     return "Hello, World!"
