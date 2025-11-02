from flask_wtf import FlaskForm
from wtforms import (StringField,SelectField,DateField,PasswordField,SubmitField,BooleanField)
from wtforms.validators import(DataRequired,Length,Email,optional,EqualTo)

class SignupForm(FlaskForm):
    username=StringField(
        "Username",
        validators=[DataRequired(),
        Length(2,30)])
    email=StringField(
        "Email",
        validators=[DataRequired()]
    )
    gender=SelectField("gender",choices=["Male","Female","Other"],validators=[optional()]
    )
    dob=DateField("Date of Birth",validators=[optional()]
    )
    password=PasswordField("Password",validators=[DataRequired(),Length(5,25)])
    
    Confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),Length(5,25),EqualTo("password")])
     
    submit=SubmitField("Signup")
    


class LoginForm(FlaskForm):
    email=StringField(
        "Email",
        validators=[DataRequired()]
    )
    
    password=PasswordField("Password",validators=[DataRequired(),Length(5,25)])
    
    remember_me= BooleanField("Remember Me")
    submit=SubmitField("Login")
    