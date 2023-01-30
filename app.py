from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/id/<int:id>', methods=['GET'])
def get(id):
    if(id >=5000):
        return {"result": "true"}
    else:
        return {"result": "false"}

@app.route('/id', methods=['POST'])
def post():
    param = request.get_json()
    name = param['name']
    return name
    #return jsonify(param)

"""{
    "name":"bowon",
    "value": 23
}
"""
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)