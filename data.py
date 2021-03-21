# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.03.05

from __future__ import print_function

import time
import matplotlib.pyplot as plt
import csv

import Table
from cs import CS
from pit import PIT
from fib import FIB
from forward import FORWARD

'''
data = {'type': 'data',
        # 'interest_ID': 0,
        'consumer_ID': 0,
        'route_ID': 0,
        'content_name': 'r0/0',
        'content_data': '',
        'data_hop': 0,
        'start_time': 0.0
       }
'''

data_f = open('./Output/Output_data.csv', 'w', encoding='utf-8', newline="")
data_csv_writer = csv.writer(data_f)
data_csv_writer.writerow(["Time", "Type", "Consumer_ID", "Route_ID", "Content_name", "Data_hop",
                          "Path", "Result", "Hit_consumer", "Hit_PIT", "Hit_Miss"])

class DATA():
    def __init__(self):
        self.data = {}

    def Create_data(self, route_ID, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                     'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0, 'path': ''}
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'run_start_time': 0, 'path': ''}
        self.data = data
        self.data['type'] = 'data'
        self.data['consumer_ID'] = interest['consumer_ID']
        self.data['route_ID'] = route_ID
        self.data['content_name'] = interest['content_name']
        content = '' # plt.imread('lena.png')
        # plt.imshow(content, cmap=plt.cm.binary)
        # plt.show()
        self.data['content_data'] = content
        self.data['data_hop'] = 0
        self.data['run_start_time'] = interest['run_start_time']
        self.data['path'] = 'p'
        return self.data

    def Send_data(self, Infaces, route_ID, data):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        '''
        Datas = []
        data['data_hop'] += 1
        data['route_ID'] = route_ID
        data['path'] += str(route_ID)+'/'
        # print(Infaces)
        for i in range(len(Infaces)):
            # print(' i= ' + str(i))
            Datas.append([Infaces[i], data])
        return Datas

    # data packet processing
    def On_data(self, sizes, route_ID, data, tables):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        '''
        Cs = CS()
        Pit = PIT()
        Fib = FIB()
        Forward = FORWARD()
        network, ps, cs, pit, fib = tables
        _, cache_size, fib_size = sizes
        #print(data)
        #print('')
        consumer_ID = data['consumer_ID']
        # Check whether there is an entry matching the content name of the data packet in the pit
        PIT_search_ACK = Pit.Search_pit_data(pit, data)
        # data match in PIT
        if PIT_search_ACK:
            ############################################################
            # Cs.Cache_cs_data(cs, cache_size, data)
            # Fib.Update_fib_outface(fib, route_ID, fib_size, data)
            ############################################################
            Infaces = Forward.Forward_data(pit, data)
            Pit.Remove_pit_entry(pit, data)
            if consumer_ID != route_ID:
                Datas = self.Send_data(Infaces, route_ID, data)
                # print('data hit in PIT')
                times = int(time.time())
                self.Output_data_txt(data, times=times, result='Data hit in PIT', hit_consumer=0, hit_PIT=1, miss_PIT=0)
                #print(Datas)
                return Datas
            else:
                # print('YES consumer')
                times = int(time.time())
                self.Output_data_txt(data, times=times, result='Data hit in consumer', hit_consumer=1, hit_PIT=0, miss_PIT=0)
                packet = []
                return packet
        # data miss in PIT
        else:
            # fib_data(inface, data)
            # Pit.Remove_pit_entry(pit, data)
            # print('data miss in PIT')
            times=int(time.time())
            self.Output_data_txt(data, times=times, result='Data miss in PIT', hit_consumer=0, hit_PIT=0, miss_PIT=1)
            #self.Drop_data(inface, data)
            packet = []
            return packet


    def Drop_data(self, inface, data):
        print('Drop_data')


    def Output_data_txt(self, data, times, result, hit_consumer, hit_PIT, miss_PIT):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'run_start_time': 0, 'data_start_time': 0, 'data_hop_time': 0, 'path': ''}

        data_f = open('Output_data.csv', 'a+', encoding='utf-8', newline="")
        data_csv_writer = csv.writer(data_f)
        data_csv_writer.writerow(["Time", "Type", "consumer_ID", "Route_ID", "Content_name", "Data_hop",
                                  "Path", "Result", "Hit_consumer", "Hit_PIT", "Miss"])
        '''
        # data是前面运行出的数据，先将其转为字符串才能写入
        data2str = [str(times-data['run_start_time']), data['type'], data['consumer_ID'],  data['route_ID'],
                    data['content_name'], data['data_hop'], data['path'], result, hit_consumer, hit_PIT, miss_PIT]
        data_csv_writer.writerow(data2str)
        # f.close()

if __name__ == '__main__':
    # Create_data(inface, route_ID= 'r0', interest = ['i0', 'c0', 'r0', 'r1/1', 10., 100.])
    # On_data(inface= 'r0',route_ID= 'r0', data=  ['d','i0', 'c0', 'r0', 'r1/1', 10., 100., 1.])
    print('data')


