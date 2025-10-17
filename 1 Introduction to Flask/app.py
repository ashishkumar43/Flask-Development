from flask import Flask
app=Flask(__name__)  

@app.route("/")   # create an endpoint
@app.route("/home")  # we can create multiple endpoints for the same function.
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>Welcome to the about page!</h1>"

if __name__=="__main__":
    app.run(debug=True)   # It will generate the log file.