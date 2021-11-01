from flask import*
from adaServer import *

app = Flask(__name__)

@app.route("/")
def main():
    if sub('test-feed') != '0':
        data = 'ON'
    else:
        data ='OFF'
    dosang = sub2('test')
    return render_template('index.html',mode=dosang)

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

@app.route('/on')
def turnOn():
    pub('test-feed','{"id":"1","name":"LED","data":"1","unit":""}')
    dosang = sub2('test')
    return render_template('index.html',mode=dosang)

@app.route('/off')
def turnOff():
    pub('test-feed','{"id":"1","name":"LED","data":"0","unit":""}')
    dosang = sub2('test')
    return render_template('index.html',mode=dosang)

if __name__ == "__main__":
    app.run()