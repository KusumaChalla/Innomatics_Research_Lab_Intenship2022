import os
import pyshorteners
import requests
import pyautogui
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.secret_key = "abc"
###################Sql Alchemy onfiguration ###################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

#### Creating a model ####
class Urlshortener(db.Model):
    __tablename__ = "urlshortener"
    id = db.Column(db.Integer, primary_key=True)
    baseurl = db.Column(db.String(500), nullable=False)
    shorten_url = db.Column(db.String(50),nullable=False)

    def __init__(self,baseurl,shorten_url):
        self.baseurl = baseurl
        self.shorten_url = shorten_url

    def __repr__(self):
        return "Base url - {}  and  Shortened Url - {}".format(self.baseurl,self.shorten_url)


@app.route('/', methods = ["POST","GET"])
def shortUrl():
    short_url=""
    url_name=""
    if request.method == "POST":
        url_name = request.form.get('input_1')
        s = pyshorteners.Shortener()
        try:
            short_url = s.tinyurl.short(url_name)
        # short1 = url_name = request.form['input_2']
        except requests.exceptions.ReadTimeout:
            pyautogui.alert("URL timedout. Please enter again!!!")
            short_url = ""
            url_name = ""
        except pyshorteners.exceptions.BadURLException:
            pyautogui.alert("Input URL not entered . Please enter again!!!")
            short_url = ""
            url_name = ""

    if url_name != "" and short_url != "":
        new_ob = Urlshortener(baseurl = url_name ,shorten_url= short_url )
        db.session.add(new_ob)
        db.session.commit()
    return render_template("HomePage.html",url_name=url_name,short_url=short_url)
@app.route('/HistoryPage')
def history_page():
    data_table = Urlshortener.query.all()
    return render_template("HistoryPage.html",data_table = data_table )


if __name__ == "__main__":
    app.run(debug = True)