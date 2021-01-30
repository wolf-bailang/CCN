from __future__ import print_function

from PIT import PIT_search_data
import time

'''
data = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, cost_time]}
'''
data = {}

def Drop_data(inface, data):
    print('2')

def Create_data(inface, route_ID, interest):
    '''
    interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
    '''
    interest_ID = interest[inface][0]
    consumer_ID = interest[inface][1]
    content_name = interest[inface][-3]
    hop = 1
    start_time = interest[inface][-2]
    cost_time = time.time()  # s
    data_temp = dict([[inface, [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, cost_time]]])
    # print(data_temp)
    return data_temp

def Send_data(inface, route_ID, interest):
    data_temp = Create_data(inface, route_ID, interest)
    data.update(data_temp)
    # print(data)

def On_data(inface, data):
    if PIT_search_data(inface, data):
        # CS_cache_data(inface, data)
        print('2')
    else:
        # fib_data(inface, data)
        Drop_data(inface, data)
        print('2')

if __name__ == '__main__':
    data = {'r1': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    route_ID = 'r0'
    # On_data(inface, data)
    Create_data(inface, route_ID, interest)
    print('data')


