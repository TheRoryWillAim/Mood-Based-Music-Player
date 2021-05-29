from flask import Flask, request, render_template,redirect,url_for,jsonify
import pandas as pd
import sys
import subprocess
import flask_excel as excel



app = Flask(__name__)
excel.init_excel(app)
@app.route('/')
def my_form():
    return render_template('templates.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['song']
    subprocess.call(["python", "old_dd.py",'{}'.format(text)])
    return redirect('/upload')



@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    data = pd.read_excel('temp.xlsx')
    return render_template('view.html',tables=[data.to_html(classes='name')],
    titles = ['Songs'])

if __name__=='__main__':
    app.debug = True
    app.run()
    
