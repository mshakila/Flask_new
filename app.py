from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
     return "This is Home page"

@app.route("/greet")
def greet():
     return "<p>Hello World !!! </p>"   # using html tags   -- paragraph tags


@app.route("/index")
def index():
     return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
     return "The candidate has passed and the score is "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
     return "The candidate has failed and the score is "+str(score)

@app.route("/welcome")
def welcome():
     return "<h1>Hello World !!!</h1> \n<h2>Hello India !!</h2> \n<b>Hello Goldie !</b> \n<p>Hello</p>"

@app.route("/calculate", methods=['POST',"GET"])
def calculate():
     if request.method =="GET":
          return render_template("calculate.html")
     else:
          maths = float(request.form['maths'])
          science = float(request.form['science'])
          social = float(request.form['social'])
          kannada = float(request.form['kannada'])

          average_marks = (maths+science+social+kannada)/4

          result = ""
          if average_marks >=50:
               result = "success"
          else:
               result = "fail"
     
          #return redirect(url_for(result, score=average_marks))


     return render_template('result.html', results=average_marks)
        

if __name__ == "__main__":
    app.run(debug=True)  
