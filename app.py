from flask import Flask, request

app = Flask(__name__)

@app.route('/id/<int:id>',methods=['GET'])
def home(id):
    value = id
    print(value)
    if value >= 5000: return "{ ‘result’: true }"
    else: return "{ ‘result’: false }"
    
@app.route('/id',methods = ['POST'])
def function():
    data = request.get_json()
    return data['name']

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)