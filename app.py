from flask import Flask,render_template,request
import spacy

from spaci import run_model
from database_handler import load_database
from configs import model_name_pt

nlp = spacy.load(model_name_pt)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sobre')
def about():
    return render_template("about.html")

@app.route('/traducao',methods=["POST"])
def process():
    if request.method == 'POST':
        text = request.form['rawtext']
        database = load_database()
        nb_text = run_model(database, nlp, text)
        print('*****ORIGINAL TEXT*****')
        print(text)
        print('********NB TEXT********')
        print(nb_text)
        print('***********************')
    return render_template("index.html",results=nb_text,rawtext=text)

if __name__ == '__main__':
    app.run()