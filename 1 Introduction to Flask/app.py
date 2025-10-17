from flask import Flask
app=Flask(__name__)  

@app.route("/")   # create an endpoint
@app.route("/home")  # we can create multiple endpoints for the same function.
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>Welcome to the about page!</h1>"

@app.route("/welcome/<name>")  # add a path parameter (/<name>) as a string with the endpoint.
def welcome(name):
    # return f"<h1>Hi {name},you are Welcome to this page!</h1>"
    return f"<h1>Hi {name.title()},you are Welcome to this page!</h1>"  # {name.title()} string function to capitalize the first letter of the name.

# for numeric path parameter we can use <int>
@app.route("/addition/<int:num>")
def addition(num):
    return f"Input is {num},Output is {num+10}"


# for numeric path parameter we can use <int> 
# can we add multiple path parameters in a single endpoint?
@app.route("/addition_two/<int:num1>/<int:num2>")   # we can give by adding / between two path parameters.
def addition_two(num1,num2):     # if we have multiple endpoints we cannot give the same name to the function.
    return f"Input is {num1} + {num2} is {num1+num2}"

if __name__=="__main__":
    app.run(debug=True)   # It will generate the log file.