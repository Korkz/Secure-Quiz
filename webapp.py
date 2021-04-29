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
    if 'q1' not in session:
        session["q1"]=request.form['q1']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if 'q2' not in session:
        session["q2"]=request.form['q2']
    return render_template('page3.html')
	
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if 'q3' not in session:
        session["q3"]=request.form['q3']
    return render_template('page4.html')
	
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    if 'q4' not in session:
        session["q4"]=request.form['q4']
    return render_template('page5.html')

@app.route('/answer',methods=['GET','POST'])
def renderAnswer():
    correct=0
    if 'q5' not in session:
        session["q5"]=request.form['q5']
    #---------Question 1----------------
    if session['q1'] == 'q1a2':
        score=score+1
        correct1="Question 1 was correct"
    if session['q1'] != 'q1a2':
	correct1="Question 1 was incorrect"
    #---------Question 2----------------
    if session['q2'] == 'q2a4':
        score=score+1
        correct2="Question 2 was correct"
    if session['q2'] != 'q2a4':
	correct2="Question 2 was incorrect"	
    #---------Question 3----------------
    if session['q3'] == 'q3a1':
        score=score+1
        correct3="Question 3 was correct"
    if session['q3'] != 'q3a1':
	correct3="Question 3 was incorrect"
    #---------Question 4----------------	
    if session['q4'] == 'q4a1':
        score=score+1
        correct4="Question 4 was correct"
    if session['q4'] != 'q4a1':
	correct4="Question 4 was incorrect"
    #---------Question 3----------------
    if session['q5'] == 'q5a3':
        score=score+1
        correct5="Question 5 was correct"
    if session['q5'] != 'q5a3':
	correct5="Question 5 was incorrect"
	
    return render_template('answer.html', scoretxt = score, correct1txt = correct1, correct2txt = correct2, correct3txt = correct3, correct4txt = correct4, correct5txt = correct5)			   
if __name__=="__main__":
    app.run(debug=False)
