from __future__ import print_function

''''''
# cs = {'route_ID': [content_name 0-100]}
cs = {}

def CS_search_interest(inface, interest):
    '''
    cs = {'route_ID': [content_name 0-100]}
    '''
    # Get the requested content name of the interest packet
    content_name = interest[inface][-3]
    # Get the PIT record table of this router
    cs_entry = cs[inface]
    # Check whether there is a record of an entry with the same name as the interest packet in the PIT
    for i in range(len(cs_entry)):
        # print(pit_entry[i][0])
        if content_name == cs_entry[i]:
            # print(ps_entry[i])
            return True
    return False

if __name__ == '__main__':
    cs = {'r0': ['r0/0', 'r0/1', 'r1/1'], 'r1': ['r2/0', 'r2/1', 'r2/1']}
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    CS_search_interest(inface, interest)
    # print('pcs')