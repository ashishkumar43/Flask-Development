from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ipl.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]= False

db=SQLAlchemy(app) 

class Team(db.Model):
    __tablename__="teams"   # if we want to give our own name then this is the code.
    id=db.Column(db.Integer,primary_key=True)
    team=db.Column(db.String(50),nullable=False,unique=True)
    state=db.Column(db.String(50),nullable=False)
    members=db.relationship("Player",backref="team")  # members is a attributes of the table teams to established the relationship b/w the table and backref="team" gives us the fake column for the sqlalchemy we have done. 
    
    def __repr__(self):
        return f"Team('{self.team}','{self.state}')"
    
class Player(db.Model):
    __tablename__="players"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    nationality=db.Column(db.String(50),nullable=False) 
    team_id=db.Column(db.Integer,db.ForeignKey("teams.id"))   # this is the foreign key for teams table
    
    def __repr__(self):
        return f"Player('{self.name}','{self.nationality}')"
    
    
if __name__=="__main__":
    app.run(debug=True)