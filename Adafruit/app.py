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

#########################################################################
###############           LOGIN              
#########################################################################

@app.route('/login', methods=["POST", "GET"])
def Login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['pass']
        if user == "admin" and password == "123456":
            return render_template('admin.html')
        else:
            sql = "SELECT * FROM Persons WHERE tk = '"+user+"' and mk = '"+ password +"'"
            user = getQuery(sql)
            user = user.fetchone()
            if user == None:
                return render_template('login.html')
            else:
                return render_template('demo.html',user=user)

#########################################################################
###############           USER MANAGER              
#########################################################################

@app.route('/userManager')
def userManager():
    sql = "SELECT * FROM Persons ORDER BY id"
    user = getQuery(sql)
    return render_template('userManager.html', user=user)


@app.route("/ajax_add", methods=["POST", "GET"])
def ajax_add():
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtusername = request.form['txtusername']
        txtpassword = request.form['txtpassword']
        print(txtname)
        if txtname == '':
            msg = 'Please Input Name'
        elif txtdepartment == '':
            msg = 'Please Input Department'
        elif txtusername == '':
            msg = 'Please Input User Name'
        elif txtpassword == '':
            msg = 'Please Input Password'
        else:
            executeQuery("INSERT INTO Persons (name,tk,mk,room) VALUES ('" + txtname +
                         "','" + txtusername + "','" + txtpassword + "','" + txtdepartment+"')")
            msg = 'New record created successfully'
    return jsonify(msg)


@app.route("/ajax_update", methods=["POST", "GET"])
def ajax_update():
    if request.method == 'POST':
        string = request.form['string']
        print(string)
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtusername = request.form['txtusername']
        print('6')
        txtpassword = request.form['txtpassword']
        print(string)
        executeQuery("UPDATE Persons SET name = '" + txtname + "' , tk = '" + txtusername +
                     "', mk =  '" + txtpassword + "', room =  '" + txtdepartment + "' WHERE id =  " + string + " ")
        msg = 'Record successfully Updated'
    return jsonify(msg)


@app.route("/ajax_delete", methods=["POST", "GET"])
def ajax_delete():
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        executeQuery('DELETE FROM Persons WHERE id = {0}'.format(getid))
        msg = 'Record deleted successfully'
    return jsonify(msg)


#########################################################################
###############           HISTORY              
#########################################################################

@app.route("/user")
def showHistory():
    #return render_template('showHistory.html', data=Get_All_Data_From_Feed("bk-iot-led"), data2=Get_All_Data_From_Feed("bk-iot-drv"))
    sql='select * from LightHistory;'
    data = getQuery(sql)
    sql2='select * from FanHistory;'
    data2 = getQuery(sql2)
    sql3='select temperature from Temperature where RoomID = 1;'
    data3 = getQuery(sql3)
    #print(request.form['input_temp'])
    return render_template('user.html',light_data=data, fan_data=data2, temp_data=data3)

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


if __name__ == "__main__":
    app.run()
