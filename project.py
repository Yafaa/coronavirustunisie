import os
import sys
from flask import (
    Flask,
    render_template,
    request,
    make_response,
    redirect,
    jsonify,
    url_for,
    flash,
    session as login_session
)
from functools import wraps

from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
import random
import string
import httplib2
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from dbSetup import Cases,Admins
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, PROJECT_ROOT)

app = Flask(__name__)
app.secret_key = 'super_secret_key'
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(PROJECT_ROOT, 'database.db'))
db = SQLAlchemy(app)
session = db.session
loged = False

###############################################################################










@app.route('/')
def main():
    Casess = session.query(Cases).order_by(Cases.totalcases.desc())
    loged = False
    return render_template('main.html', Cases=Casess)


@app.route('/update/', methods=['GET', 'POST'])
def update():
    global loged
    if request.method == 'POST' and loged == False :
    	pasw = request.form['password']
    	user = request.form['username']
    	print(user,pasw)
    	adm = session.query(Admins).filter(Admins.username == user) 
    	res = adm.first()
    	if res and res.password == pasw : 
    	    loged = True
    	    Casess = session.query(Cases).order_by(Cases.totalcases.desc())
    	    return render_template('update.html', Cases=Casess)
    	else :
    	    return render_template('password.html')
    elif request.method == 'POST' and loged == True :
    	li = [ "Tunis", "Ariana" , "Béja", "Ben Arous", "Bizerte", "Gabés", "Gafsa", "Jendouba", "Kairouan", "Kasserine", "Kébili", "Le kef", "Mahdia", "La manouba", "Monastir", "Médenine", "Nabeul", "Sfax", "Sidi Bouzid", "Siliana", "Sousse", "Tataouine", "Tozeur", "Zaghouan", ]
    	for i in li:
    	    print(i)
    	    totalcases1 = request.form['1'+i]
    	    newcases1 = request.form['2'+i]
    	    totaldeath1 = request.form['3'+i]
    	    newdeath1 = request.form['4'+i]
    	    totalrecovered1 = request.form['5'+i]
    	    serious1 = request.form['6'+i]
    	    print
    	    session.query(Cases).filter(Cases.state == i ).update({"totalcases" : totalcases1  , "newcases" : newcases1 , "totaldeath" : totaldeath1 , "newdeath" : newdeath1 , "totalrecovered" : totalrecovered1 , "serious" : serious1})
    	    session.commit()
    	    
    	    
    	Casess = session.query(Cases).order_by(Cases.totalcases.desc())
    	return render_template('update.html', Cases=Casess)



    else :
    	print("vide")
    	loged = False
    	return render_template('password.html')
    












##########################################################


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
