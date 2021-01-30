# This is a sample Python script.

from __future__ import print_function
from PIT import *
from PS import PS_init
from FIB import FIB_init

def CCN_init(route_num, content_num):
    #
    # ps = {'route_ID': [content_name 0-100]}
    ps = PS_init(route_num, content_num)
    # CCN_network(route_num)

    interest = {'r0': ['i0', 'c0', 'r0', 'r1/0', 10., 100.]}
    pit = {'r0': []}
    print(' ')
    return ps

if __name__ == '__main__':
    """
        inface = route_ID
        interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
    """
    interest = {}
    pit = {}
    # ps = {}
    route_num = 12
    content_num = 100
    ps = CCN_init(route_num, content_num)
    print('main')

