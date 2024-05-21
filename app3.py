# return a web page  
# also import redirect and url
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
     return 

@app.route("/index")
def index():
     return render_template("index.html")
    
#@app.route("/index")
#def index():
#     return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)  