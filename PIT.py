from __future__ import print_function

import time
from Interest import Drop_interest

def Time_out(inface, interest):
    '''
        inface = route_ID
        interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
    '''
    start_time = interest[inface][-2]
    # print(start_time)
    life_time = interest[inface][-1]
    # print(life_time)
    now_time = time.time()  # s
    print(now_time)
    if now_time - start_time < life_time:
        Drop_interest(inface, interest)
    else:
        PIT_search_interest(inface, interest)

def Merge_pit_entry(index, inface):
    pit_entry = pit[inface]
    # print(pit_entry)
    pit_entry[index][1].append(inface)
    # print(pit_entry)
    # pit[inface] = pit_entry
    # print(pit)
def Creat_pit_entry(inface, content_name):
    pit_entry = pit[inface]
    # print(pit_entry)
    pit_entry.append([content_name, [inface],[]])
    # print(pit_entry)

def PIT_search_interest(inface, interest):
    '''
        inface = route_ID
        interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
        pit = {'route_ID': [content_name,[inface],[outface]], [content_name,[inface],[outface]]}
    '''
    pit_entry = pit[inface]
    # print(pit_entry)
    content_name = interest[inface][-3]
    for i in range(len(pit_entry)):
        print(pit_entry[i][0])
        if content_name == pit_entry[i][0]:
            # Merge_pit_entry
            pit_entry[i][1].append(inface)    # Merge_pit_entry(i, inface)
            Drop_interest(inface, interest)
            return False
    # Creat_pit_entry
    pit_entry.append([content_name, [inface],[]])   # Creat_pit_entry(inface, content_name)
    return True

def PIT_search_data(inface, data):
    '''
        inface = route_ID
        data = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]}
        pit = {'route_ID': [content_name,[inface],[outface]], [content_name,[inface],[outface]]}
    '''
    pit_entry = pit[inface]
    # print(pit_entry)
    content_name = data[inface][-3]
    for i in range(len(pit_entry)):
        print(pit_entry[i][0])
        if content_name == pit_entry[i][0]:

            # Delete_pit_entry
            pit_entry.append([content_name, [inface], []])  # Delete_pit_entry(inface, content_name)
            return True

    # Merge_pit_entry
    pit_entry[i][1].append(inface)  # Merge_pit_entry(i, inface)
    # Drop_data(inface, data)
    return False

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
    Creat_pit_entry(inface, 'r1/1')
