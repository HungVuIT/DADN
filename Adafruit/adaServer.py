from Adafruit_IO import*
import json
aio = Client('vhhung', 'aio_kyCW62jx8jJvl9WbnftC4YQwgvrH')
aio2= Client('hungpham9469', 'aio_ytyr44KXjO5xLSMDC6dZqd9qBt6u')

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
