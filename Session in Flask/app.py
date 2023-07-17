from flask import *
app=Flask(__name__)
app.secret_key='login64655r5dg'  #for flashing the message   all data will be in encypted form

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
       u_name=request.form['uname']
       pwd=request.form['pass']
       if u_name=="Pragya" and pwd=="123":
           session['username']=u_name
           flash("You are succesfully Login")
           return render_template('succes.html',name=u_name)
       else:
            abort(401)       #handle bad requested from client side
            return "try again"
    
    else:
        return redirect('/')
    
@app.route('/logout')
def logout():
    session.pop('username',None)   #session popup end krr denge
    return redirect('/')

@app.route('/profile')
def profile():
    if 'username' in session:     # if user exist in session store data of that user and till user not logout session will be countinue
        username=session['username']
        return render_template("profile.html",name=username)
    else:
        return redirect('/')
    


if __name__=='__main__':
    app.run(debug=True)