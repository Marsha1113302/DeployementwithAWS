from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")

def home():
    return jsonify(message="Hello, Marshall!")

@app.route('/add')
def add():  
     a = 5
     b = 10
     return jsonify(result=a + b)
     


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)