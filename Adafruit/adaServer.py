from Adafruit_IO import*
import json
aio = Client('vhhung', 'aio_kKKP15QsEGorIzlZemZCBwzyi9x7') # Tự test với server 
aio2= Client('hungpham9469', 'aio_ytyr44KXjO5xLSMDC6dZqd9qBt6u')

def Light_Turn_On_Strong():
    test_feed = aio.feeds('bk-iot-led') #truyền vô key của thiết bị
    aio.send_data(test_feed.key,'{ "id":"1", "name":"LED", "data":"2", "unit":"" }') 
   
def Light_Turn_On():
    test_feed = aio.feeds('bk-iot-led') #truyền vô key của thiết bị
    aio.send_data(test_feed.key,'{ "id":"1", "name":"LED", "data":"1", "unit":"" }') #truyền vô data
    
def Light_Turn_Off():
    test_feed = aio.feeds('bk-iot-led')
    aio.send_data(test_feed.key,'{ "id":"1", "name":"LED", "data":"0", "unit":"" }')
    
def Fan_Turn_On():
    test_feed = aio.feeds('bk-iot-drv')
    aio.send_data(test_feed.key,'{ "id":"10", "name":"DRV_PWM", "data":"100", "unit":"" }')

def Fan_Turn_Off():
    test_feed = aio.feeds('bk-iot-drv')
    aio.send_data(test_feed.key,'{ "id":"10", "name":"DRV_PWM", "data":"0", "unit":"" }')
    
def Get_Temp():
    test_feed = aio.feeds('bk-iot-temp-humid') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'] # json, ->STring

def Get_Light():
    test_feed = aio.feeds('bk-iot-light') #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'] # json, lấy vùng dữ liệu
