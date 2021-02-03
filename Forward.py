from __future__ import print_function

import Table

def Forward_interest(route_ID, interest):
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]

        # Not optimized
        FIB =｛'route_ID'： ['route_ID', ...], ... ｝
        fib = ['route_ID', ...]

        # Can be optimized
        FIB = {'route_ID': [[content_name,[[cost, outface], ...]], ...], ... }
        fib = [[content_name,[[cost, outface], ...]], ...]

    # Can be optimized
    # Get the requested content name of the interest packet
    content_name = interest[3]
    # Get the fib record table of this router
    fib = Table.FIB[route_ID]
    # Check whether there is a record of an entry with the same name as the interest packet in the fib
    for i in range(len(fib)):
        fib_entry = fib[i]
        # print(pit_entry[0])
        if content_name == fib_entry[0]:
            Outface = fib_entry[2]
            # print(Outface)
            return Outface
    '''
    # Not optimized
    # Get the fib record table of this router
    fib = Table.FIB[route_ID]
    Outface = fib
    # print(Outface)
    return Outface

def Forward_data(route_ID, data):
    '''
        Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time], ...],...}
        data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
    '''
    # Get the requested content name of the interest packet
    content_name = data[3]
    # Get the pit record table of this router
    pit = Table.PIT[route_ID]
    # Check whether there is a record of an entry with the same name as the interest packet in the pit
    for i in range(len(pit)):
        # print(pit[i])
        pit_entry = pit[i]
        # print(pit_entry[0])
        if content_name == pit_entry[0]:
            Inface = pit_entry[1]
            # print(Inface)
            return Inface

if __name__ == '__main__':
    Table.PIT = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r2/1', ['r2', 'r9'], ['r8', 'r7']]],
                 'r1': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/11', ['r2', 'r9'], ['r8', 'r7']]]}
    Table.Interest_table = {'r0': [['i0', 'c0', 'r1', 'r2/1', 10., 100.], ['i1', 'c0', 'r0', 'r1/1', 10., 100.]],
                            'r1': [['i2', 'c0', 'r0', 'r3/1', 10., 100.], ['i3', 'c0', 'r0', 'r4/1', 10., 100.]]}
    Table.PS = {'r0': ['r1/1', 'r3/0', 'r4/0', 'r5/0'],
                'r1': ['r1/1', 'r2/1', 'r9/1', 'r8/1', 'r7/1']}
    Table.FIB = {'r0': ['r5'],
                 'r1': ['r2', 'r9', 'r8', 'r7']}
    # Forward_data(route_ID = 'r0', data = ['i0', 'c0', 'r0', 'r1/0', 2, 10., 100.])
    # Forward_interest(route_ID = 'r1', interest = ['i0', 'c0', 'r0', 'r1/0', 10., 100.])