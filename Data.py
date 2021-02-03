from __future__ import print_function

import time
import Table
from PIT import PIT_search_data
from Forward import Forward_data

def Create_data(inface, route_ID, interest):
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
        Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time], ...], ... }
        data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
        PS = {'route_ID': [content_name, ...], ... }
        FIB =｛'route_ID'： ['route_ID', ...], ... ｝
        fib = ['route_ID', ...]
    '''
    interest_ID = interest[route_ID][0]
    consumer_ID = interest[route_ID][1]
    content_name = interest[route_ID][-3]
    hop = 0
    start_time = interest[route_ID][-2]
    cost_time = time.time()  # s
    data = dict([[route_ID, [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, cost_time]]])
    # print(data_temp)
    return data

def Send_data(Inface, route_ID, data):
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
        Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time], ...], ... }
        data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
        PS = {'route_ID': [content_name, ...], ... }
        FIB =｛'route_ID'： ['route_ID', ...], ... ｝
        fib = ['route_ID', ...]
    '''
    Data = []
    # The router ID of the data packet is updated to the output interface
    # data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
    data[4] = data[4] + 1
    for i in range(len(Inface)):
        Data.append([Inface[i], data])
    return Data

def Drop_data(inface, data):
    print('2')

# Interest packet processing
def On_data(inface, route_ID, data):
    '''
        Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time], ...],...}
        data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
    '''
    # Check whether there is an entry matching the content name of the data packet in the pit
    PIT_search_ACK = PIT_search_data(inface, route_ID, data)
    if PIT_search_ACK:
        # CS_cache_data(inface, data)
        Inface = Forward_data(route_ID, data)
        Data = Send_data(Inface, route_ID, data)
        print(Data)
    else:
        # fib_data(inface, data)
        Drop_data(inface, data)
        print('2')

if __name__ == '__main__':
    # Create_data(inface, route_ID= 'r0', interest = ['i0', 'c0', 'r0', 'r1/1', 10., 100.])
    On_data(inface= 'r0',route_ID= 'r0', data= ['i0', 'c0', 'r0', 'r1/1', 10., 100.])
    print('data')


