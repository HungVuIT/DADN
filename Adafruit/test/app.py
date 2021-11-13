from flask import *
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('signup.html')


    
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    _name = request.form['inputName']
    print(_name)

if __name__ == "__main__":
    app.run()