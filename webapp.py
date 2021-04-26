import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)


# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"];
@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["q1a1"]=request.form['q1a1']
    #print(session['q1a1'])
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    #session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page3.html')
	
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    return render_template('page4.html')
	
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    return render_template('page5.html')

if __name__=="__main__":
    app.run(debug=True)
