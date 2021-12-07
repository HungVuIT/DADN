from flask import*
from adaServer import *
from database import *
from flask_socketio import SocketIO
data = {
    "room1": "123456",
    "room2": "123456",
    "room3": "123456"
}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def admin():
    return render_template('login.html')

#########################################################################
# LOAD ITEM
#########################################################################


@app.route('/room1')
def room1():
    sql = 'select * from Room where Id = 1;'
    data = getQuery(sql).fetchone()
    led = Get_Led()
    fan = Get_Fan()
    return render_template('user.html', room=data, led=led, fan=fan)


@app.route('/room2')
def room2():
    sql = 'select * from Room where Id = 2;'
    data = getQuery(sql).fetchone()
    led = Get_Led()
    fan = Get_Fan()
    return render_template('user.html', room=data, led=led, fan=fan)


@app.route('/room3')
def room3():
    sql = 'select * from Room where Id = 3;'
    data = getQuery(sql).fetchone()
    led = Get_Led()
    fan = Get_Fan()
    return render_template('user.html', room=data, led=led, fan=fan)


@app.route('/room4')
def room4():
    sql = 'select * from Room where Id = 4;'
    data = getQuery(sql).fetchone()
    led = Get_Led()
    fan = Get_Fan()
    return render_template('user.html', room=data, led=led, fan=fan)


@app.route('/room5')
def room5():
    sql = 'select * from Room where Id = 5;'
    data = getQuery(sql).fetchone()
    led = Get_Led()
    fan = Get_Fan()
    return render_template('user.html', room=data, led=led, fan=fan)


#########################################################################
# CHAT
#########################################################################

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

#########################################################################
# LOGIN
#########################################################################


@app.route('/login', methods=["POST", "GET"])
def Login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['pass']
        if user == "admin" and password == "123456":
            return render_template('admin.html')
        else:
            sql = "SELECT * FROM Persons WHERE tk = '"+user+"' and mk = '" + password + "'"
            user = getQuery(sql)
            user = user.fetchone()
            if user == None:
                return render_template('login.html')
            else:
                id = user.room
                sql = 'select * from Room where Id ='+id+' ;'
                data = getQuery(sql).fetchone()
                led = Get_Led()
                fan = Get_Fan()
                return render_template('user.html', room=data, led=led, fan=fan)

#########################################################################
# USER MANAGER
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
# AUTO MODE
#########################################################################


@app.route('/autoOn')
def auto():
    # read the posted values from the UI
    lihgtnow = int(Get_Light())
    if(lihgtnow < 100):
        Led_Turn_On()
    else:
        Led_Turn_Off()
    led = Get_Led()
    return render_template('demo.html', led=led)

#########################################################################
# FAN AND LED BTN
#########################################################################


@app.route('/stop', methods=['POST'])
def stop():
    Fan_Turn_Off()
    msg = "good"
    return jsonify(msg)


@app.route('/first', methods=['POST'])
def first():
    Fan_Turn_On_1()
    msg = "good"
    return jsonify(msg)


@app.route('/second', methods=['POST'])
def second():
    Fan_Turn_On_2()
    msg = "good"
    return jsonify(msg)


@app.route('/third', methods=['POST'])
def third():
    Fan_Turn_On_3()
    msg = "good"
    return jsonify(msg)


@app.route('/ledon', methods=['POST'])
def ledon():
    Led_Turn_On()
    msg = "good"
    return jsonify(msg)


@app.route('/ledoff', methods=['POST'])
def ledoff():
    Led_Turn_Off()
    msg = "good"
    return jsonify(msg)


#########################################################################
# HISTORY
#########################################################################

@app.route("/user", methods=["POST", "GET"])
def showHistory():
    # return render_template('showHistory.html', data=Get_All_Data_From_Feed("bk-iot-led"), data2=Get_All_Data_From_Feed("bk-iot-drv"))
    sql = 'select * from LightHistory;'
    data = getQuery(sql).fetchall()
    sql2 = 'select * from FanHistory;'
    data2 = getQuery(sql2).fetchall()
    sql3 = 'select temperature from Temperature where RoomID = 1;'
    data3 = getQuery(sql3).fetchall()
    if request.method == "POST":
        temp_input = request.form['input_temp']
        sql4 = 'update Temperature set temperature =' + temp_input + 'where RoomID = 1;'
        executeQuery(sql4)
    # print(request.form['input_temp'])
    return render_template('user.html', light_data=data, fan_data=data2, temp_data=data3)


"""
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
"""
if __name__ == "__main__":
    socketio.run(app, debug=True)
