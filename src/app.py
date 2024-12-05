from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello, Everyone!"

@app.route('/add')
def add():  
    a = 5
    b = 10
    return str(a + b)

API_ACCESS_KEY= 'abcd-12345-5678'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)