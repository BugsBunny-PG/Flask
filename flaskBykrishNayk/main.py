#integrate html page 
# use HTTP verb GET and POST 
'''here we see more jinja2 templates which can we use in html page
like
{%....%}  statements like if ,else, for etc
{{ }}   expressions to print output
{#  #} this is for comments'''
from flask import Flask,render_template,redirect ,url_for,request

app=Flask(__name__)

@app.route('/')
def home():          #this is a home page must return html page by render template (Jinja2 technique)
    return render_template('index.html')
    
@app.route('/succes/<int:marks>')
def succes(marks):
    return render_template('result.html',sc=marks)     # here also pass html file and send marks by jinja2 template

@app.route('/fail/<int:marks>')
def fail(marks):
    return 'student fail with '+str(marks)+' marks'
@app.route('/result/<int:score>')
def result(score):
    # print(score)
    ans=""
    if(score>50):
        ans='succes'
    else:
       ans='fail'
    return redirect(url_for(ans,marks=score))

@app.route('/submit',methods=['POST','GET'])     #index.html page hit this url the how we read all the entries by request
def submit():
    total_score=0
    if request.method=='POST':   #in html form method gives post then take entries
        science=float(request.form['science'])   #inside form take a name of that field and convert it into float
        Data_science=float(request.form['datascience'])
        # print(Data_science)
        maths=float(request.form['maths'])  #name must be same as in html file input feild
        c=float(request.form['c'])
        total_score=(science+Data_science+maths+c)/4
        print(total_score)
    return redirect(url_for('result',score=total_score))     #redirect  to result route
        
if __name__=='__main__':
    app.run(debug=True)