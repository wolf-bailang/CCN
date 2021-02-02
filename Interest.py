from __future__ import print_function

import Table
from PIT import PIT_search_interest, PIT_update_outface
from PS import PS_search_interest
from Data import Send_data
# from Forward import Forward_interest

def Drop_interest(inface, interest):
    print('2')

def On_interest(inface, route_ID, interest):
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
    '''
    global PS_search_ACK
    # Check whether there is an entry matching the content name of the interest packet in the pit
    PIT_search_ACK = PIT_search_interest(inface, route_ID, interest)
    # match
    if PIT_search_ACK == True:
        # CS_search_interest(inface, interest)
        # Find the data of the content name in ps
        PS_search_ACK = PS_search_interest(route_ID, interest)
    # miss
    else:
        Drop_interest(route_ID, interest)
        return
    # Find
    if PS_search_ACK == True:
        # Return data packet
        # Send_data(inface, route_ID, interest)
        return
    # miss
    # else:
        # Forward the interest packet to the next router
        # Forward_interest(route_ID, interest)

# Remove the interest packet from the interest packet table of the current router
def Remove_interest_entry(route_ID, interest):
    interest_entry = Table.Interest_table[route_ID]
    interest_ID = interest[-3]
    for i in range(len(interest_entry)):
        if interest_ID == interest_entry[i][0]:
            del interest_entry[i]
            Table.Interest_table[route_ID] = interest_entry
            # print(Table.Interest_table)
            break

def Send_interest(outface, route_ID, interest):
    '''
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID = inface, content_name, start_time, life_time]
    '''
    # The router ID of the interest packet is updated to the output interface
    # interest = [interest_ID, consumer_ID, route_ID = outface, content_name, start_time, life_time]
    interest[2] = outface
    # Send interest

    # Remove the interest packet from the interest packet table of the current router
    Remove_interest_entry(route_ID, interest)
    # The outface is updated to fib
    PIT_update_outface(outface, route_ID, interest)
    # print(interest)

if __name__ == '__main__':
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
    '''
    Table.PIT = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]],
                 'r1': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]]}
    Table.Interest_table = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]],
                            'r1': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]]}
    # On_interest(inface= 'r0', route_ID= 'r0', interest= ['i0', 'c0', 'r0', 'r1/1', 10., 100.])
    Send_interest(outface= 'r120', route_ID= 'r0', interest= ['i0', 'c0', 'r0', 'r1/1', 10., 100.])
    print('interest')

