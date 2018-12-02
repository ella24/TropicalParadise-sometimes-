from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beaches.db'
db = SQLAlchemy(app)

class Beach(db.Model):
  __tablename__ = 'PRbeaches'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  index = db.Column(db.Integer, primary_key=True)

@app.route("/beaches/")
def list():
  beaches = Beach.query.all()
  return render_template ("list.html", beaches=beaches)

@app.route("/beaches/<index>")
def show(index):
  beach = Beach.query.filter_by(index=index).first()
  return render_template("show.html", beach=beach)

if __name__ == "__main__":
  app.run(debug=True)