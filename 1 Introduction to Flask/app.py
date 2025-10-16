from flask import Flask
app=Flask(__name__)

@app.route("/")   #create an endpoint
def home():
    return "<h1>Welcome to the Home Page!</h1>"

if __name__=="__main__":
    app.run(debug=True)   # It will generate the log file.