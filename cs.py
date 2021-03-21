# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.03.21

from __future__ import print_function

import time

'''
# cs = {'route_ID': [content_name 0-100]}
cs = {}
'''

class CS():
    def __init__(self):
        # self.route_num = route_num
        # self.content_num = content_num
        self.cs = []

    # Producer generates unique content name
    def Creat_cs(self, route_ID):
        '''
        cs=[[content_name, data, time, cost],
            ...
           ]
        '''
        return self.cs

    def Get_cs(self):
        return self.cs

    def Search_cs_interest(self, cs, content_name):
        '''
        cs=[[content_name, data, time, cost],...]
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        '''
        # Check if there is data matching the content name in cs
        self.cs = cs
        for i in range(len(self.cs)):
            cs_entry = self.cs[i]
            if content_name == cs_entry[0]:
                return True
        # No data for content name found in cs
        return False

    def Creat_cs_entry(self, data):
        content_name = data['content_name']
        content_data = data['content_data']
        times = int(time.time())
        cost = data['data_hop']
        cs_entry = [content_name, content_data, times, cost]
        return cs_entry

    def Remove_cs_entry(self, cs):
        self.cs = cs
        self.cs.sort(key=lambda x:(x[-1]), reverse=False)
        index = -1
        del self.cs[index]

    def Cache_cs_data(self, cs, cache_size, data):
        self.cs = cs
        if self.cs < cache_size:
            cs_entry = self.Creat_cs_entry(data)
            self.cs.append(cs_entry)
        else:
            self.Remove_cs_entry(self.cs)
            cs_entry = self.Creat_cs_entry(data)
            self.cs.append(cs_entry)


if __name__ == '__main__':
    CS = {'r0': ['r0/0', 'r0/1', 'r1/1'], 'r1': ['r2/0', 'r2/1', 'r2/1']}
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    # CS_search_interest(inface, interest)
    # print('CS')