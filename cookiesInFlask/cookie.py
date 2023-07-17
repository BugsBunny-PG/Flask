from flask import Flask,render_template,redirect,url_for,make_response,request
app=Flask(__name__)


# how to set cookies

@app.route('/set')   #first set the cookies
def setcookie():
    res=make_response("<h2>Cookies is set</h2>")
    #Now set the cookies by set_cookie function
    res.set_cookie("Farmework","Flask")   #give name of cookie framework and value is flask
    return res
# how to get(fetch) Cookies
#now get the cookie
@app.route('/get')
def getcookie():
    ans=request.cookies['Farmework']
    return ans

@app.route('/')
def index():
    count=int(request.cookies.get('visit_count',0))
    count+=1
    mesg="visit this page "+ str(count)
    resp=make_response(mesg)
    resp.set_cookie('visit_count',str(count))
    return resp


if __name__=='__main__':
    app.run(debug=True)