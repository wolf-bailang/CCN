from __future__ import print_function

from PIT import PIT_search_interest
from PS import PS_search_interest
from Data import Send_data
from Forward import Forward_interest

'''
interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
'''
interest = {}

def Drop_interest(inface, interest):
    print('2')

def On_interest(inface, route_ID, interest):
    global PS_search_ACK
    PIT_search_ACK = PIT_search_interest(inface, route_ID, interest)
    if PIT_search_ACK == True:
        # CS_search_interest(inface, interest)
        PS_search_ACK = PS_search_interest(inface, interest)
    else:
        Drop_interest(inface, interest)
        print('2')
        return

    if PS_search_ACK == True:
        Send_data(inface, route_ID, interest)
    else:
        Forward_interest()



if __name__ == '__main__':
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    route_ID = 'r0'
    On_interest(inface, route_ID, interest)
    print('interest')

