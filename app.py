from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = './gdmm.db'
db = SQLAlchemy(app)

db.create_all()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    text = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get("name")
        text = request.form.get("text")
        db.session.add(Message(name=name, text=text))
        db.session.commit()
    messages = Message.query.all()
    return render_template("index.html", messages=messages)


if __name__ == '__main__':
    app.run()
