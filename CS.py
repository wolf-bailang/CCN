from __future__ import print_function

'''
# cs = {'route_ID': [content_name 0-100]}
cs = {}
'''

def CS_search_interest(inface, interest):
    '''
    CS = {'route_ID': [[content_name, cost, record_time], ...], ... }
    cs = [[content_name, cost, record_time], ...]
    interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
    '''
    # Get the requested content name of the interest packet
    content_name = interest[-3]
    # Get the cs record table of this router
    cs = CS[inface]
    # Check if there is data matching the content name in cs
    for i in range(len(cs)):
        # print(cs[i])
        ps_entry = cs[i]
        if content_name == ps_entry:
            # print(cs_entry)
            return True
    return False

if __name__ == '__main__':
    CS = {'r0': ['r0/0', 'r0/1', 'r1/1'], 'r1': ['r2/0', 'r2/1', 'r2/1']}
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    CS_search_interest(inface, interest)
    # print('CS')