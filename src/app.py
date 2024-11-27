from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello, Marshall!"

@app.route('/add')
def add():  
    a = 5
    b = 10
    return str(a + b)
    

SECRET_API_KEY = "12345-abcdef-6789"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)