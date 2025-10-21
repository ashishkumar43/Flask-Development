from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return f"<h1>Hi, Welcome to Home Page!!!</h1>"

@app.route("/passed")
def passed():
    return "<h1>Congrats, you are passed !!!</h1>"

@app.route("/failed")
def failed():
    return "<h1>Sorry , you are failed !!!</h1>"


@app.route("/score/<name>/<marks>")
def score(name,marks):
    if score < 30:
        #redirect user to page "fail"
        pass
    else:
        #redirect user to page "pass"
        pass
 




if __name__=="__main__":
    app.run(debug=True)