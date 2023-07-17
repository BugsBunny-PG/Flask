#simple flask skeleton
from flask import Flask,redirect,url_for

#WSGI applications
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to flask tutorial'

@app.route('/home')
def home():             #binding function with url
    return 'Welcom to Home Page'

#binding url dynamically
@app.route('/sucess/<int:score>')   #with url gives integer value as input 
def sucess(score):
    return 'person is pass with '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'person fail with '+str(score)+'marks'

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if(marks<=50):
      result='fail'
    else:
        result='sucess'
    return redirect(url_for(result,score=marks))  #it redirect form sucess or fail route //redirect function redirect
#on different route and score send then it make url if it is fail it go to fail route

#when we show person fail or pass or results in another page so import library redirect(this library is used building
# the url dynamicaly)
      
if __name__=='__main___':
    app.run(debug=True)


#for run type python -m flask run 
#if debug mode not on then type $env:FLASK_DEBUG="1"