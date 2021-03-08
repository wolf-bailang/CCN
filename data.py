# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.03.05

from __future__ import print_function

import time
import matplotlib.pyplot as plt

import Table
from pit import PIT
from forward import FORWARD

data = {'type': 'data',
        # 'interest_ID': 0,
        'consumer_ID': 0,
        'route_ID': 0,
        'content_name': 'r0/0',
        'content_data': '',
        'data_hop': 0,
        'start_time': 0.0
       }

class DATA():
    def __init__(self):
        self.data = data

    def Create_data(self, route_ID, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                     'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        '''
        self.data['type'] = 'data'
        self.data['consumer_ID'] = interest['consumer_ID']
        self.data['route_ID'] = route_ID
        self.data['content_name'] = interest['content_name']
        content = '' # plt.imread('lena.png')
        # plt.imshow(content, cmap=plt.cm.binary)
        # plt.show()
        self.data['content_data'] = content
        self.data['data_hop'] = 0
        self.data['start_time'] = interest['start_time']
        return self.data

    def Send_data(self, Infaces, route_ID, data):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        '''
        Datas = []
        data['data_hop'] += 1
        data['route_ID'] = route_ID
        for i in range(len(Infaces)):
            Datas.append([Infaces[i], data])
        return Datas

    # data packet processing
    def On_data(self, inface, route_ID, data, tables):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        '''
        Pit = PIT()
        Forward = FORWARD()
        network, ps, pit, fib = tables
        print(data)
        print('')

        # Check whether there is an entry matching the content name of the data packet in the pit
        PIT_search_ACK = Pit.Search_pit_data(pit, data)
        # data match in PIT
        if PIT_search_ACK:
            ############################################################
            # CS_cache_data(inface, data)
            # FIB_update_outface(inface, route_ID, data)
            ############################################################
            Infaces = Forward.Forward_data(pit, data)
            Datas = self.Send_data(Infaces, route_ID, data)
            Pit.Remove_pit_entry(pit, data)
            return Datas
        # data miss in PIT
        else:
            # fib_data(inface, data)
            self.Drop_data(inface, data)
            packet = []
            return packet



    def Drop_data(self, inface, data):
        print('Drop_data')

if __name__ == '__main__':
    # Create_data(inface, route_ID= 'r0', interest = ['i0', 'c0', 'r0', 'r1/1', 10., 100.])
    # On_data(inface= 'r0',route_ID= 'r0', data=  ['d','i0', 'c0', 'r0', 'r1/1', 10., 100., 1.])
    print('data')


