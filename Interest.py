from __future__ import print_function

import time
import Table
from PIT import PIT_search_interest, PIT_update_outface
from PS import PS_search_interest
from Data import Send_data, Create_data
from Forward import Forward_interest, Forward_data

def Send_interest(Outfaces, route_ID, interest):
    '''
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID = inface, content_name, start_time, life_time]
        Outfaces = [outface, ...]
    '''
    # Send interest
    Interests = []
    # The router ID of the interest packet is updated to the output interface
    # interest = [interest_ID, consumer_ID, route_ID = outface, content_name, start_time, life_time]
    # interest[-2] = time.time()
    for i in range(len(Outfaces)):
        Interests.append([Outfaces[i], interest])
    # Remove the interest packet from the interest packet table of the current router
    Remove_interest_entry(route_ID, interest)
    # The outface is updated to fib
    PIT_update_outface(Outfaces, route_ID, interest)
    return Interests

# Remove the interest packet from the interest packet table of the current router
def Remove_interest_entry(route_ID, interest):
    interest_entry = Table.Interest_table[route_ID]
    interest_ID = interest[0]
    for i in range(len(interest_entry)):
        if interest_ID == interest_entry[i][0]:
            del interest_entry[i]
            Table.Interest_table[route_ID] = interest_entry
            # print(Table.Interest_table)
            break

# Interest packet processing
def On_interest(inface, route_ID, interest):
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
    '''
    # Check whether there is an entry matching the content name of the interest packet in the pit
    PIT_search_ACK = PIT_search_interest(inface, route_ID, interest)
    # interest match in PIT
    if PIT_search_ACK == True:
        # CS_search_ACK = CS_search_interest(inface, interest)
        # Find the data of the content name in ps
        PS_search_ACK = PS_search_interest(route_ID, interest)
    # interest miss in PIT
    else:
        # Drop_interest(in PSroute_ID, interest)
        flag = 0    # Drop interest
        packet = []
        return packet, flag
    # interest hit in PS
    if PS_search_ACK == True:
        # Return data packet
        data = Create_data(inface, route_ID, interest)
        Inface = Forward_data(route_ID, data)
        Send_data(Inface, route_ID, data)
        flag = 1    # send Data packet
        return Data, flag
    # interest miss in PS
    else:
        # Forward the interest packet to the next router
        Outfaces = Forward_interest(route_ID, interest)
        # print(Outfaces)
        Interests = Send_interest(Outfaces, route_ID, interest)
        flag = 2    # send Interests packet
        # print(Interests)
        return Interests, flag

def Drop_interest(inface, route_ID, interest):

    print('Drop_interest')


if __name__ == '__main__':
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
        PS = {'route_ID': [content_name, ...], ... }
        FIB =｛'route_ID'： ['route_ID', ...], ... ｝
        fib = ['route_ID', ...]
    '''
    Table.PIT = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r2/1', ['r2', 'r9'], ['r8', 'r7']]],
                 'r1': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/11', ['r2', 'r9'], ['r8', 'r7']]]}
    Table.Interest_table = {'r0': [['i0', 'c0', 'r1', 'r2/1', 10., 100.], ['i1', 'c0', 'r0', 'r1/1', 10., 100.]],
                            'r1': [['i2', 'c0', 'r0', 'r3/1', 10., 100.], ['i3', 'c0', 'r0', 'r4/1', 10., 100.]]}
    Table.PS = {'r0': ['r1/1', 'r3/0', 'r4/0', 'r5/0'],
                'r1': ['r1/1', 'r2/1', 'r9/1', 'r8/1', 'r7/1']}
    Table.FIB = {'r0': ['r5'],
                 'r1': ['r2', 'r9', 'r8', 'r7']}
    # Send_interest(outface= 'r120', route_ID= 'r0', interest= ['i0', 'c0', 'r1', 'r2/1', 10., 100.])
    On_interest(inface= 'r2', route_ID= 'r0', interest= ['i0', 'c0', 'r2', 'r1/7', 10., 100.])
    print(Table.Interest_table)
    print(Table.PIT)
    print('interest')

