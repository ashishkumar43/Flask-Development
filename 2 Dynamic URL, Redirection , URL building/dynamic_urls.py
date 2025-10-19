from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"
# This will generate the static endpoint to make it dynamic we can use path parameters.
@app.route("/welcome/ashish")
def welcome_ashish():
    return "<h1>Welcome to Ashish's Page!</h1>" 

@app.route("/welcome/rohan")
def welcome_rohan():
    return "<h1>Welcome to rohan's Page!</h1>" 

#we can make it dynamic by using path parameters.
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hi {name.title()},you are Welcome to this page!</h1>"

#we can make it dynamic by using path parameters.
@app.route("/welcome/<gender>")
def gender(gender):
    return f"<h1>Hi,Your gender is {gender} and you are Welcome to this page!</h1>"


#we can make it dynamic by using path parameters.
@app.route("/welcome/<Age>")
def age(age):
    return f"<h1>Hi,Your age is {age} and you are Welcome to this page!</h1>"


if __name__=="__main__":
    app.run(debug=True)   #It will generate the log file.
    
   



 
    
