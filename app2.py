# html tags 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
     return "<h1>Hello World !!!</h1> \n<h2>Hello India !!</h2> \n<b>Hello Goldie !</b> \n<p>Hello</p>"
    

if __name__ == "__main__":
    app.run(debug=True)  
