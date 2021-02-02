from __future__ import print_function

import Table
import time

# Check whether the interest packet has timed out
def Time_out(interest):
    '''
        interest = [interest_ID, consumer_ID, route_ID=inface, content_name, start_time, life_time]
    '''
    start_time = interest[-2]
    # print(start_time)
    life_time = interest[-1]
    # print(life_time)
    now_time = time.time()  # s
    # print(now_time)
    if now_time - start_time < life_time:
        return True
    return False

# The inface of the received interest packet is merged into the same content name
def Merge_pit_entry(index, inface, route_ID):
    '''
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
    '''
    # Get the PIT record table of this router
    pit = Table.PIT[route_ID]
    pit_entry = pit[index]
    # print(pit_entry)
    pit_entry[1].append(inface)
    # print(pit_entry)
    pit[index] = pit_entry
    # print(pit)
    Table.PIT[route_ID] = pit
    # print(Table.PIT)

# Create a pit entry
def Creat_pit_entry(inface, route_ID, content_name):
    '''
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
    '''
    pit = Table.PIT[route_ID]
    pit_entry = [content_name, [inface],[]]
    # print(pit_entry)
    pit.append(pit_entry)
    # print(pit)
    Table.PIT[route_ID] = pit
    # print(Table.PIT)

# The outface is updated to pit
def PIT_update_outface(outface, route_ID, interest):
    pit = Table.PIT[route_ID]
    content_name = interest[-3]
    # Check whether there is a record of an entry with the same name as the interest packet in the PIT
    for i in range(len(pit)):
        # print(pit[i])
        pit_entry = pit[i]
        # print(pit_entry)
        if content_name == pit_entry[0]:
            pit_entry[2].append(outface)
            pit[i] = pit_entry
            # print(pit_entry)
            Table.PIT[route_ID] = pit
            # print(Table.PIT)

# Check whether there is an entry matching the content name of the interest packet in the pit
def PIT_search_interest(inface, route_ID, interest):
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
    '''
    # Check whether the interest packet has timed out
    if Time_out(interest):
        # Ack_interest(interest)
        return False
    # Get the PIT record table of this router
    pit = Table.PIT[route_ID]
    # print(pit)
    # Get the requested content name of the interest packet
    content_name = interest[-3]
    # Check whether there is a record of an entry with the same name as the interest packet in the PIT
    for i in range(len(pit)):
        # print(pit[i])
        pit_entry = pit[i]
        if content_name == pit_entry[0]:
            # The inface of the received interest packet is merged into the same content name
            Merge_pit_entry(i, inface, route_ID)
            return False
    # Create a pit entry
    Creat_pit_entry(inface, route_ID, content_name)
    return True




def PIT_search_data(inface, route_ID, data):
    '''
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
        Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time], ...], ... }
        data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
    '''
    # Get the PIT record table of this router
    pit = Table.PIT[route_ID]
    # print(pit)
    # pit_entry = pit[inface]
    # print(pit_entry)
    content_name = data[-3]
    for i in range(len(pit)):
        print(pit[i])
        pit_entry = pit[i]
        print(pit_entry[0])
        if content_name == pit_entry[0]:
            # Delete_pit_entry
            # pit_entry.append([content_name, [inface], []])  # Delete_pit_entry(inface, content_name)
            return True
    # Merge_pit_entry
    # pit_entry[i][1].append(inface)  # Merge_pit_entry(i, inface)
    # Drop_data(inface, data)
    return False

if __name__ == '__main__':
    """
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
        Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time], ...], ... }
        data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
    """
    Table.Data_table = {'r0': ['i0', 'c0', 'r0', 'r1/0', 1.0, 10., 100.]}
    Table.PIT = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]]}
    # Time_out(inface, interest)
    # Merge_pit_entry(1, inface='r1', route_ID='r0')
    # Creat_pit_entry(inface='r11', route_ID='r11', content_name='r6/100')
    # PIT_search_interest(inface= 'r11', route_ID= 'r0', interest= ['i0', 'c0', 'r0', 'r1/0', 10., 100.])
    PIT_search_data(inface= 'r11', route_ID= 'r0', data= ['i0', 'c0', 'r0', 'r1/0', 1.0, 10., 100.])


