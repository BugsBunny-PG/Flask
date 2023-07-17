from flask import *
from flask_mail import *

app=Flask(__name__)
with open('mailInFlask\config.json','r') as f:                #open json file in readable mode
     params=json.load(f)['parameters']
#configuration
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gamil.com'      #gmail use karenge
app.config['MAIL_PORT']=465   #465 use for gmail
app.config['MAIL_USERNAME']=params['gmail-user'] # give thos email id which help to send email ,  we can also store these parameters in JSON file
app.config['MAIL_PASSWORD']=params['gamil-password']
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=True         

@app.route('/')
def home():
    mesg= Message('Important Mail',sender='gupta.pragya433@gmail.com',recipients=['pragyagupta002@gmail.com'])
    #first parameter is Subject,second sender gmail,third reciver gamil
    #message Body (message me kya dena hai)
    mesg.body="gives mail by Flask"
    #send mail this body message
    mail.send(mesg)
    
    return "hello"
    
    
if __name__=='__main__':
    app.run(debug=True)