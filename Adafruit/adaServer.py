from Adafruit_IO import*
import json
aio = Client('vhhung', 'aio_kyCW62jx8jJvl9WbnftC4YQwgvrH') # Tự test với server 
aio2= Client('hungpham9469', 'aio_ytyr44KXjO5xLSMDC6dZqd9qBt6u')
"""
def sub(id):
    test_feed = aio.feeds(id)
    data = aio.receive(test_feed.key)
    #print('Latest value from Test: {0}'.format(data.value))
    return json.loads(data.value)['data'] #json
def pub(id,data):
    test_feed = aio.feeds(id)
    aio.send_data(test_feed.key, data)

def sub2(id):
    test_feed = aio2.feeds(id)
    data = aio2.receive(test_feed.key)
    #print('Latest value from Test: {0}'.format(data.value))
    return json.loads(data.value)['data'] #json
def pub2(id,data):
    test_feed = aio2.feeds(id)
    aio2.send_data(test_feed.key, data)
"""    
def Light_Turn_On():
    test_feed = aio.feeds('led') #truyền vô key của thiết bị
    aio.send_data(test_feed.key,'{"id":"1","name":"LED","data":"1","unit":""}') #truyền vô data
    
def Light_Turn_Off():
    test_feed = aio.feeds('led')
    aio.send_data(test_feed.key,'{"id":"1","name":"LED","data":"0","unit":""}')
    
def Fan_Turn_On():
    test_feed = aio.feeds('led')
    aio.send_data(test_feed.key,'{"id":"1","name":"LED","data":"0","unit":""}')

def Fan_Turn_Off():
    test_feed = aio.feeds('led')
    aio.send_data(test_feed.key,'{"id":"1","name":"LED","data":"0","unit":""}')
    
def Get_Temp():
    test_feed = aio.feeds(id) #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'] # json, lấy vùng dữ liệu

def Get_Light():
    test_feed = aio.feeds(id) #key thiết bị
    data = aio.receive(test_feed.key)
    return json.loads(data.value)['data'] # json, lấy vùng dữ liệu
