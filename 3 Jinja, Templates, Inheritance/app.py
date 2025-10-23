from flask import Flask,render_template

# create the flask app 
app=Flask(__name__)  # this have also one more parameter called templates it gives us the name templates that why i have made this folder name templates.

#home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")  # invoke the template like home.html and all and then i will show on screen.
#about page 
@app.route("/about")
def about():
    return render_template("about.html")


#start the app
if __name__=="__main__":
    app.run(debug=True)    