from __future__ import print_function

import Table

def PS_search_interest(route_ID, interest):
    '''
    PS = {'route_ID': [content_name,...], ...}
    interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
    '''
    # Get the requested content name of the interest packet
    content_name = interest[-3]
    # Get the ps record table of this router
    ps = Table.PS[route_ID]
    # Check if there is data matching the content name in ps
    for i in range(len(ps)):
        # print(ps[0])
        if content_name == ps[i]:
            # print(ps[i])
            return True
    # No data for content name found in ps
    return False

# Producer generates unique content name
def PS_init(route_num, content_num):
    '''
    PS = {'route_ID': [content_name,...], ...}
    '''
    for i in range(route_num):
        route_ID = 'r' + str(i)
        content_name = []
        for j in range(content_num):
            # Generate content name
            content_name.append(route_ID + '/' + str(j))
        PS_entry = dict([[route_ID, content_name]])
        Table.PS.update(PS_entry)

if __name__ == '__main__':
    # PS_search_interest(inface='r0', interest=['i0', 'c0', 'r0', 'r1/1', 10., 100.])
    PS_init(route_num=12, content_num=100)
    print(Table.PS)
