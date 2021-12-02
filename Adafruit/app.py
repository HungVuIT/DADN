from flask import*
from adaServer import *
from database import *
from datetime import *
data = {
    "room1":"123456",
    "room2":"123456",
    "room3":"123456"
}

app = Flask(__name__)

@app.route("/")
def main():
    sql='select * from Persons'
    data = executeQuery(sql)
    return render_template('userManager.html',data=data)

@app.route('/check',methods=['GET', 'POST'])
def login():
    # read the posted values from the UI
    _user = request.form['user']
    _password = request.form['pass']
    # validate the received values
    if data[_user]==_password:
        return render_template('main.html')
    else:
        return render_template('login.html')


@app.route('/on')
def turnOn():
    pub('led','{"id":"1","name":"LED","data":"1","unit":""}')
    dosang = sub('light')
    return render_template('index.html',mode=dosang)

@app.route('/off')
def turnOff():
    pub('led','{"id":"1","name":"LED","data":"0","unit":""}')
    dosang = sub('light')
    return render_template('index.html',mode=dosang)

@app.route("/showHistory")
def showHistory():
    #return render_template('showHistory.html', data=Get_All_Data_From_Feed("bk-iot-led"), data2=Get_All_Data_From_Feed("bk-iot-drv"))
    sql='select * from LightHistory;'
    data = getQuery(sql)
    sql2='select * from FanHistory;'
    #datafan = getQuery(sql2)
    return render_template('showHistory.html',data=data)
if __name__ == "__main__":
    app.run()