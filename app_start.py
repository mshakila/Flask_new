# create a simple Flask application

from flask import Flask, redirect , url_for, request
# for webpage, import redirect and url_for
# redirect will redirect to the given url
# request - whether post or get

## create flask app

app = Flask(__name__) # entry point of the program

@app.route("/")  # / is home page    # to create url, use decorators
def home():
    return "Hello World !!!"

# this is the local host ip address
# http://127.0.0.1:5000

app.route("/index")
def index():
    return redirect(url_for("index")) # to return webpage


if __name__ == "__main__":  #this is entry point
    app.run(debug = True)  # use debug only in development env  not in production env


