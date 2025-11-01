from flask import (Flask,render_template,redirect,url_for)

from forms import SignupForm, LoginForm   # classes SignupForm and LoginForm 

app=Flask(__name__)
app.config["SECRET_KEY"]="THIS_IS_THE_SECRET_KEY"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html" , title="Home")

@app.route("/signup", methods=["GET","POST"])
def signup():  
    form=SignupForm()   # create an object of that class
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("signup.html" , title="Signup",form=form)


@app.route("/login")
def login():
    form=LoginForm()    # create an object of that class
    return render_template("login.html" , title="login",form=form)

if __name__=="__main__":
    app.run(debug=True)
 