# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.03.21

from __future__ import print_function

import time


class CS():
    def __init__(self):
        # self.route_num = route_num
        # self.content_num = content_num
        self.cs = []

    # Each router creates an independent cache space
    def Creat_cs(self, route_ID):
        '''
        cs = [[content_name, data, time, cost],
              ...
             ]
        '''
        return self.cs

    # Get cs
    def Get_cs(self):
        return self.cs

    # Check if there is data matching the content name in cs
    def Search_cs_interest(self, cs, content_name):
        '''
        cs = [[content_name, data, time, cost],...]
        cs_entry = [content_name, data, time, cost]
        '''
        self.cs = cs
        for i in range(len(self.cs)):
            cs_entry = self.cs[i]
            if content_name == cs_entry[0]:
                return True
        # No data for content name found in cs
        return False

    # Add an entry to CS
    def Creat_cs_entry(self, data):
        '''
        cs = [[content_name, data, time, cost],...]
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'run_start_time': 0.0, 'path': ''}
        '''
        content_name = data['content_name']
        content_data = data['content_data']
        # Record the time this entry was created
        times = int(time.time())
        cost = data['data_hop']
        cs_entry = [content_name, content_data, times, cost]
        return cs_entry

    # Delete an entry from CS
    def Remove_cs_entry(self, cs):
        '''
        cs = [[content_name, data, time, cost],...]
        '''
        self.cs = cs
        # sort cost-based
        self.cs.sort(key=lambda x:(x[-1]), reverse=False)
        index = -1
        # Delete the most costly entry
        del self.cs[index]

    # Cache data
    def Cache_cs_data(self, cs, cache_size, data):
        self.cs = cs
        # Check if CS is full
        if self.cs < cache_size:
            cs_entry = self.Creat_cs_entry(data)
            self.cs.append(cs_entry)
        else:
            # Remove the most costly entry
            self.Remove_cs_entry(self.cs)
            cs_entry = self.Creat_cs_entry(data)
            self.cs.append(cs_entry)
