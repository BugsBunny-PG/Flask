from flask import Flask,render_template,url_for,request,redirect,abort,flash
app=Flask(__name__)
app.secret_key='login64655r5'  #for flashing the message

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        file_n=request.files['file']
        file_n.save(file_n.filename)      #if we wnt to store at perticular folder gives path like ('static/'+file_n.filename)
        return "success"
    else:
        return redirect('/')
    #login route
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
       u_name=request.form['uname']
       pwd=request.form['pass']
       if u_name=="Pragya" and pwd=="123":
           flash("You are succesfully Login")
           return render_template('message.html',name=u_name)
       else:
            abort(401)       #handle bad requested from client side
            return "try again"
    
    else:
        return redirect('/')


if __name__=='__main__':
    app.run(debug=True)
