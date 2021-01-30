from __future__ import print_function

from PIT import PIT_search_interest
from PS import PS_search_interest

'''
interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
'''
interest = {}

def Drop_interest(inface, interest):

    print('2')

def On_interest(inface, interest):
    if PIT_search_interest(inface, interest):
        # CS_search_interest(inface, interest)
        PS_search_interest(inface, interest)

    else:
        Drop_interest(inface, interest)
        print('2')

if __name__ == '__main__':
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    On_interest(inface, interest)
    print('interest')

