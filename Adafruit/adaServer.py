from Adafruit_IO import*
from database import *
import json
aio2 = Client('vhhung', 'aio_kKKP15QsEGorIzlZemZCBwzyi9x7') # Tự test với server 
aio= Client('hungpham9469', 'aio_ytyr44KXjO5xLSMDC6dZqd9qBt6u')

def Led_Turn_On_Strong():
    test_feed = aio.feeds('bk-iot-led') #truyền vô key của thiết bị 
    aio.send_data(test_feed.key,'{ "id":"1", "name":"LED", "data":"2", "unit":"" }') #truyền vô data
    sql = 'insert into LightHistory(FeedData) values(2)'
    executeQuery(sql)
   
def Led_Turn_On():
    test_feed = aio.feeds('bk-iot-led') 
    aio.send_data(test_feed.key,'{ "id":"1", "name":"LED", "data":"1", "unit":"" }') 
    sql = 'insert into LightHistory(FeedData) values(1)'
    executeQuery(sql)
    
def Led_Turn_Off():
    test_feed = aio.feeds('bk-iot-led')
    aio.send_data(test_feed.key,'{ "id":"1", "name":"LED", "data":"0", "unit":"" }')
    sql = 'insert into LightHistory(FeedData) values(0)'
    executeQuery(sql)
    
def Fan_Turn_On():
    test_feed = aio.feeds('bk-iot-drv')
    aio.send_data(test_feed.key,'{ "id":"10", "name":"DRV_PWM", "data":"100", "unit":"" }')

def Fan_Turn_Off():
    test_feed = aio.feeds('bk-iot-drv')
    aio.send_data(test_feed.key,'{ "id":"10", "name":"DRV_PWM", "data":"0", "unit":"" }')
  
def Get_Led(): # Lấy trạng thái hiện tại của đèn led
    test_feed = aio.feeds('bk-iot-led') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data']

def Get_Fan(): # Lấy trạng thái hiện tại của quạt
    test_feed = aio.feeds('bk-iot-led') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data']

def Get_Temp():
    test_feed = aio.feeds('bk-iot-temp-humid') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'][0]+json.loads(data.value)['data'][1] # json, ->STring

def Get_Light(): # Lấy độ sáng môi trường hiện tại thông qua cảm biết ánh sáng
    test_feed = aio.feeds('bk-iot-light') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'] # json, lấy vùng dữ liệu

#test function  
def Get_All_Data_From_Feed(id):
    data = aio.data(id)
    json_data = []
    for d in data:
        json_data.append(json.loads(d.value))
        #print("Data value: {0}".format(d.value))
    return json_data






