from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello, Marshall!")


@app.route('/add')
def add():  
     a = 5
     b = 10
     sum = a + b  
     return jsonify(result=a + b)

if __name__ == '__main__':
    app.run(debug=True)