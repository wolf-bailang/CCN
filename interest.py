# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.03.05

from __future__ import print_function

import time
import numpy as np
import csv

import Table
from pit import PIT
from ps import PS
from cs import CS
from data import DATA
from forward import FORWARD

'''
interest = {'type': 'interest',
            'interest_ID': 0,
            'consumer_ID': 0,
            'route_ID': 0,
            'content_name': 'r0/0',
            'interest_hop': 0,
            'life_hop': 0,
            'start_time': 0.0
           }
'''

interest_f = open('Output_interest.csv', 'w', encoding='utf-8', newline="")
interest_csv_writer = csv.writer(interest_f)
interest_csv_writer.writerow(["Time", "Type", "Interest_ID", "Consumer_ID", "Route_ID", "Content_name",
                              "Interest_hop", "Path", "Result", "Hit", "Miss"])

class INTEREST():
    def __init__(self):
        self.interest_ID_count = 0
        self.interest = {}

    # Consumer generated interest packet
    def Generate_interest(self, route_ID, run_start_time, frequency, content_num, route_num, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                     'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}

        Interests = []
        for i in range(0, frequency):
            interest_temp = {'type': "interest", 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': '',
                             'interest_hop': 0, 'life_hop': 0, 'start_time': 0, 'path': ''}
            interest_temp['type'] = 'interest'
            interest_temp['consumer_ID'] = route_ID
            interest_temp['interest_hop'] = 0
            interest_temp['life_hop'] = 5
            interest_temp['interest_ID'] = self.interest_ID_count
            self.interest_ID_count += 1
            interest_temp['route_ID'] = route_ID
            #index = np.random.randint(0, content_num)
            #interest_temp['content_name'] = Table.Content_table[index]
            index1 = np.random.randint(0, route_num)
            index = np.random.randint(0, content_num)
            interest_temp['content_name'] = 'r'+str(index1)+'/'+str(index)
            interest_temp['start_time'] = int(time.time())
            interest_temp['path'] = str(route_ID)
            Interests.append(interest_temp)
        return Interests
        '''
        Interests = []
        for i in range(0, len(interest)):
            interest_temp = {'type': "interest", 'interest_ID': '', 'consumer_ID': 0, 'route_ID': 0, 'content_name': '',
                             'interest_hop': 0, 'life_hop': 0, 'run_start_time': 0, 'path': ''}
            interest_temp['type'] = 'interest'
            interest_temp['interest_ID'] = interest[i]['interest_ID']
            interest_temp['consumer_ID'] = route_ID
            interest_temp['route_ID'] = route_ID
            interest_temp['content_name'] = interest[i]['content_name']
            interest_temp['interest_hop'] = 0
            interest_temp['life_hop'] = 5
            interest_temp['run_start_time'] = run_start_time
            interest_temp['path'] = 'p'+str(route_ID)
            Interests.append(interest_temp)
        return Interests

    # Check whether the interest packet has timed out
    def Time_out(self, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        '''
        interest_hop = interest['interest_hop']
        life_hop = interest['life_hop']
        if interest_hop <= life_hop:
            return True
        else:
            # Drop interest
            self.Output_interest_txt(interest, times=int(time.time()), result='Time out', hit=0, miss=1)
            return False

    def Send_interest(self, pit, Outfaces, route_ID, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                     'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        Outfaces = [outface, ...]
        '''
        # Send interest
        Interests = []
        interest['route_ID'] = route_ID
        interest['interest_hop'] += 1
        interest['path'] += '/'+str(route_ID)
        for i in range(len(Outfaces)):
            Interests.append([Outfaces[i], interest])
        # The outface is updated to pit
        Pit = PIT()
        Pit.Update_pit_outface(pit, Outfaces, interest)
        return Interests

    # Interest packet processing
    def On_interest(self, route_ID, interest, tables):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        '''
        Ps = PS()
        Cs = CS()
        Pit = PIT()
        Data = DATA()
        Forward = FORWARD()
        Interest = INTEREST()
        network, ps, cs, pit, fib = tables
        # ps = Ps.Get_ps()
        #print('r' + str(route_ID) + ' ps')
        #print(ps)
        # pit = Pit.Get_pit()
        #print('r' + str(route_ID) + ' pit')
        #print(pit)
        #print(interest)
        #print('')

        content_name = interest['content_name']
        # Find the data of the content name in ps
        Search_ps_ACK = Ps.Search_ps_interest(ps, content_name)
        # interest hit in PS
        if Search_ps_ACK == True:
            # Return data packet
            data = Data.Create_data(route_ID, interest)
            inface = [interest['route_ID']]
            # Infaces = Forward.Forward_data(data)
            Datas = Data.Send_data(inface, route_ID, data)
            self.Output_interest_txt(interest, times=int(time.time()), result='Hit in PS', hit=1, miss=0)
            # print('interest hit in PS')
            # print(Datas)
            return Datas
        # interest miss in PS
        else:
            self.Output_interest_txt(interest, times=int(time.time()), result='Miss in PS', hit=0, miss=1)
            # print('interest miss in PS')
            ########################################################
            '''
            Search_cs_ACK = Cs.Search_cs_interest(cs, content_name)
            # interest hit in CS
            if Search_cs_ACK == True:
                # Return data packet
                data = Data.Create_data(route_ID, interest)
                inface = [interest['route_ID']]
                # Infaces = Forward.Forward_data(data)
                Datas = Data.Send_data(inface, route_ID, data)
                self.Output_interest_txt(interest, times=int(time.time()), result='Hit in CS', hit=1, miss=0)
                # print('interest hit in CS')
                # print(Datas)
                return Datas
            else:
                self.Output_interest_txt(interest, times=int(time.time()), result='Miss in CS', hit=0, miss=1)
                # print('interest miss in CS')
            '''
            ########################################################
        # Check whether there is an entry matching the content name of the interest packet in the pit
        Search_pit_ACK = Pit.Search_pit_interest(pit, interest)
        # interest miss in PIT
        if Search_pit_ACK == True:
            # Forward the interest packet to the next router
            Outfaces = Forward.Forward_interest(fib, network, route_ID, interest)
            Interests = Interest.Send_interest(pit, Outfaces, route_ID, interest)
            # print('interest miss in PIT')
            # print(Interests)
            return Interests
        # interest match in PIT
        else:
            # Drop_interest(in PSroute_ID, interest)
            # print('interest match in PIT')
            # self.Drop_interest(route_ID, interest)
            packet = []
            return packet

    def Output_interest_txt(self, interest, times, result, hit, miss):
        '''
        interest = {'type': "interest", 'interest_ID': '', 'consumer_ID': 0, 'route_ID': 0, 'content_name': '',
                    'interest_hop': 0, 'life_hop': 0, 'run_start_time': 0, 'path': ''}

        interest_f = open('Output_interest.csv', 'a+', encoding='utf-8', newline="")
        interest_csv_writer = csv.writer(interest_f)
        interest_csv_writer.writerow(["Time", "Type", "Interest_ID", "Consumer_ID", "Route_ID", "Content_name",
                                      "Interest_hop", "Path", "Result", "Hit", "Miss"])
        '''
        # interest是前面运行出的数据，先将其转为字符串才能写入
        interest2str = [str(times-interest['run_start_time']), interest['type'], interest['interest_ID'],
                        interest['consumer_ID'], interest['route_ID'], interest['content_name'],
                        interest['interest_hop'], interest['path'], result, hit, miss]
        interest_csv_writer.writerow(interest2str)
        # interest_f.close()

    def Drop_interest(self, route_ID, interest):
        print('Drop_interest')



    # Remove the interest packet from the interest packet table of the current router
    def Remove_interest_entry(self, route_ID, interest):
        interest_entry = Table.Interest_table[route_ID]
        interest_ID = interest[0]
        for i in range(len(interest_entry)):
            if interest_ID == interest_entry[i][0]:
                del interest_entry[i]
                Table.Interest_table[route_ID] = interest_entry
                # print(Table.Interest_table)
                break

if __name__ == '__main__':
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
        PS = {'route_ID': [content_name, ...], ... }
        FIB =｛'route_ID'： ['route_ID', ...], ... ｝
        fib = ['route_ID', ...]
    
    Table.PIT = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r2/1', ['r2', 'r9'], ['r8', 'r7']]],
                 'r1': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/11', ['r2', 'r9'], ['r8', 'r7']]]}
    Table.Interest_table = {'r0': [['i0', 'c0', 'r1', 'r2/1', 10., 100.], ['i1', 'c0', 'r0', 'r1/1', 10., 100.]],
                            'r1': [['i2', 'c0', 'r0', 'r3/1', 10., 100.], ['i3', 'c0', 'r0', 'r4/1', 10., 100.]]}
    Table.PS = {'r0': ['r1/1', 'r3/0', 'r4/0', 'r5/0'],
                'r1': ['r1/1', 'r2/1', 'r9/1', 'r8/1', 'r7/1']}
    Table.FIB = {'r0': ['r5'],
                 'r1': ['r2', 'r9', 'r8', 'r7']}
    # Send_interest(outface= 'r120', route_ID= 'r0', interest= ['i0', 'c0', 'r1', 'r2/1', 10., 100.])
    On_interest(inface= 'r2', route_ID= 'r0', interest= ['i0', 'c0', 'r2', 'r1/7', 10., 100.])
    #print(Table.Interest_table)
    #print(Table.PIT)
    #print('interest')

    #Table.Route_ID = ['r0', 'r1', 'r2']
    #index = Table.Route_ID.index('r2')
    #print(index)
    index = []
    interest_ID = index[0][1][0]
    '''
    print('interest')

