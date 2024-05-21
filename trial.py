from flask import Flask , render_template, request, url_for
app = Flask(__name__)

@app.route("/calculate1", methods=["POST" ,"GET"])
def calculate():
    if request.method == "GET":
        return render_template("calculate1.html")
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        social = float(request.form['social'])

        average_marks = (maths + science + social)/3

    return render_template("result1.html")    

if __name__ == "__main__":
    app.run(debug=True)