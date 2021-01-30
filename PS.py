from __future__ import print_function

''''''
# ps = {'route_ID': [content_name 0-100]}
ps = {}

def PS_search_interest(inface, interest):
    '''
    ps = {'route_ID': [content_name 0-100]}
    '''
    # Get the requested content name of the interest packet
    content_name = interest[inface][-3]
    # Get the PIT record table of this router
    ps_entry = ps[inface]
    # Check whether there is a record of an entry with the same name as the interest packet in the PIT
    for i in range(len(ps_entry)):
        # print(pit_entry[i][0])
        if content_name == ps_entry[i]:
            # print(ps_entry[i])
            return True
    return False

def PS_init(route_num, content_num):
    content_name = []
    ps = {}
    for i in range(route_num):
        for j in range(content_num):
            route_ID = 'r' + str(i)
            content_name.append(route_ID + '/' + str(j))
        ps_entry = dict([[inface, content_name]])
        ps.update(ps_entry)
    return  ps


if __name__ == '__main__':
    # ps = {'r0': ['r0/0', 'r0/1', 'r1/1'], 'r1': ['r2/0', 'r2/1', 'r2/1']}
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    route_num = 12
    content_num = 100
    # PS_search_interest(inface, interest)
    ps = PS_init(route_num, content_num)
    print(ps)
