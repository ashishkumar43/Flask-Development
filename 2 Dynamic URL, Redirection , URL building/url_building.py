import time
from flask import Flask,redirect ,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return f"<h1>Hi, Welcome to Home Page!!!</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>Congrats {sname.title()}, you are passed with {marks} marks!!!</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>Sorry {sname.title()}, you are failed with {marks} marks!!!</h1>"


@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        #redirect user to page "fail"
        # we can do it manually but it will take more time to do instead of doing manually we will do it with the help of url_for method.
        return redirect(url_for("failed",sname=name , marks=num))   #url_for gives us the endpoint (function) so that i will generate the url to reach to that endpoint.
        # pass
    else:
        #redirect user to page "pass"
        return redirect(url_for("passed" , sname=name , marks=num))
        # pass
 
if __name__=="__main__":
    app.run(debug=True)