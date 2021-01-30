from __future__ import print_function

from PIT import PIT_search_data

'''
data = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]}
'''
data = {}

def Drop_data(inface, data):
    print('2')

def On_data(inface, data):
    if PIT_search_data(inface, data):
        # CS_search_interest(inface, interest)
        # PS_search_data(inface, data)

    else:
        Drop_data(inface, data)
        print('2')

if __name__ == '__main__':
    data = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    On_data(inface, data)
    print('data')


