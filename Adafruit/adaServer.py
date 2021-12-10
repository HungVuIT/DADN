from Adafruit_IO import*
import json

aio = Client('vhhung', 'aio_FSvF92TbDObqI6n26usROGAZudp7') # Tự test với server 
aio1= Client('hungpham9469', 'aio_ytyr44KXjO5xLSMDC6dZqd9qBt6u')

   
def Led_Turn_On():
    test_feed = aio.feeds('bk-iot-led') 
    aio.send_data(test_feed.key,'{ "id":"1", "name":"LED", "data":"1", "unit":"" }') 
    sql = 'insert into LightHistory(feed_data) values(1)'
    executeQuery(sql)
    
def Led_Turn_Off():
    test_feed = aio.feeds('bk-iot-led')
    aio.send_data(test_feed.key,'{ "id":"1", "name":"LED", "data":"0", "unit":"" }')
    sql = 'insert into LightHistory(feed_data) values(0)'
    executeQuery(sql)

def Fan_Turn_On_3():
    test_feed = aio.feeds('bk-iot-drv')
    aio.send_data(test_feed.key,'{ "id":"10", "name":"DRV_PWM", "data":"200", "unit":"" }')
    sql = 'insert into FanHistory(feed_data) values(200)'
    executeQuery(sql)
def Fan_Turn_On_2():
    test_feed = aio.feeds('bk-iot-drv')
    aio.send_data(test_feed.key,'{ "id":"10", "name":"DRV_PWM", "data":"150", "unit":"" }')
    sql = 'insert into FanHistory(feed_data) values(150)'
    executeQuery(sql)
    
def Fan_Turn_On_1():
    test_feed = aio.feeds('bk-iot-drv')
    aio.send_data(test_feed.key,'{ "id":"10", "name":"DRV_PWM", "data":"100", "unit":"" }')
    sql = 'insert into FanHistory(feed_data) values(100)'
    executeQuery(sql)

def Fan_Turn_Off():
    test_feed = aio.feeds('bk-iot-drv')
    aio.send_data(test_feed.key,'{ "id":"10", "name":"DRV_PWM", "data":"0", "unit":"" }')
    sql = 'insert into FanHistory(feed_data) values(0)'
    executeQuery(sql)
  
def Get_Led(): # Lấy trạng thái hiện tại của đèn led
    test_feed = aio.feeds('bk-iot-led') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data']

def Get_Fan(): # Lấy trạng thái hiện tại của quạt
    test_feed = aio.feeds('bk-iot-drv') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data']

def Get_Temp():
    test_feed = aio.feeds('bk-iot-temp-humid') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'][0]+json.loads(data.value)['data'][1] # json, ->STring

def Get_Humid():
    test_feed = aio.feeds('bk-iot-temp-humid') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'][3]+json.loads(data.value)['data'][4] # json, ->STring

def Get_Light(): # Lấy độ sáng môi trường hiện tại thông qua cảm biết ánh sáng
    test_feed = aio.feeds('bk-iot-light') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'] # json, lấy vùng dữ liệu

