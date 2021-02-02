from __future__ import print_function

import Table
from Interest import Send_interest

def Forward_interest(route_ID, interest):
    '''
    Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
    interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]

    # Not optimized
    FIB =｛'route_ID'： ['route_ID', ...], ... ｝
    fib = ['route_ID', ...]

    # Can be optimized
    FIB = {'route_ID': [[content_name,[inface, ...],[outface, ...]], ...], ... }
    fib = [[content_name,[inface, ...],[outface, ...]], ...]
    '''
    # Get the requested content name of the interest packet
    # content_name = interest[-3]
    # Get the fib record table of this router
    fib = Table.FIB[route_ID]
    # Check whether there is a record of an entry with the same name as the interest packet in the fib
    for i in range(len(fib)):
        outface = fib[i]
        # print(outface)
        Send_interest(outface, route_ID, interest)

if __name__ == '__main__':
    ps = {'r0': ['r0/0', 'r0/1', 'r1/1'], 'r1': ['r2/0', 'r2/1', 'r2/1']}
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    # print('ps')
