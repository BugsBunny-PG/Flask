from flask import Flask,render_template,redirect,url_for    #import these classes from flask Framework/Module/laibrary
app=Flask(__name__)  #from flask class make instance(Which is call our website that name is app)

@app.route('/')  #with the help of this app website we made routes(route is a different different 
# end points/section(like home aboute help etc)             website)
def home():  #this is a function of that perticular route what logic will be perform at backend side  
    return render_template('index2.html')

@app.route('/about')
def about():
    name='Pragya'
    li=['motu','patlu','tom','jerry','shinchan','doremon','Nobita'] 
    return render_template('index.html',name=name,li=li)
if __name__=='__main__':          #main function of python
    app.run(debug=True)
'''By enabling debug mode, the server will automatically reload if code changes, and will show an
interactive debugger in the browser if an error/logs occurs during a request.
At the time of hosting our website we don't wants to enable debuge mode because you can't show any typers
of logs or error to the usere side'''