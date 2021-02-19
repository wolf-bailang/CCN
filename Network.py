from __future__ import print_function

import Table
from PIT import *
from PS import PS_init
from FIB import FIB_init

def Network_init(route_num): #route_num, content_num
    Table.Network = [['r0', ['r1', 'r3']], ['r1', ['r0', 'r2', 'r3']], ['r2', ['r1', 'r4']], ['r3', ['r0', 'r1', 'r5']],
               ['r4', ['r2', 'r5', 'r6']], ['r5', ['r3', 'r4', 'r5']], ['r6', ['r4', 'r7']], ['r7', ['r6', 'r8', 'r11']],
               ['r8', ['r5', 'r7', 'r9']], ['r9', ['r8', 'r10']], ['r10', ['r9', 'r11']], ['r11', ['r7', 'r10']]]
    # fib = \
    FIB_init()

    # return  fib

if __name__ == '__main__':
    """
        incomingface = route_ID
        interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
    """
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/0', 10., 100.]}
    pit = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]]}
    inface = 'r0'
    # Time_out(inface, interest)
    # PIT_search_interest(inface, interest)
    # Creat_fib_entry(inface, 'r1/1')
    fib = FIB_init()
    print(fib)