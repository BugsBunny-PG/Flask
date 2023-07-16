from flask import Flask,render_template,request,url_for
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='mydb'
mysql=MySQL(app)
@app.route('/')
def home():
 return render_template('signUppage.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    name=request.form['name']
    pas=request.form['password']
    cur=mysql.connection.cursor()      #create mysql cursor
    cur.execute('INSERT INTO user VALUES(%s,%s)',(name,pas))        #execute mysql query
    mysql.connection.commit()
    cur.close()      #connection close
    return '<h1>suucess</h1>'

if __name__=='__main__':
    app.run(debug=True)