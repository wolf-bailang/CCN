# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.02.27

from __future__ import print_function

import Table
from pit import *
from ps import PS
from fib import FIB

#network = {'':[0,0]
#          }

class NETWORK():
    def __init__(self):
        self.network = {}

    def Creat_network(self):
        self.network = {'r0':[1, 3], 'r1': [0, 2, 3], 'r2': [1, 4], 'r3': [0, 1, 5],
                        'r4': [2, 5, 6], 'r5': [3, 4, 5], 'r6': [4, 7], 'r7': [6, 8, 11],
                        'r8': [5, 7, 9], 'r9': [8, 10], 'r10': [9, 11], 'r11': [7, 10]}
        return self.network

    def Get_network(self):
        return self.network

    def Init_network(self, server_num):
        '''
        network = {'route_ID':[route_ID, ...],
                    ...
                  }
        '''
        Fib = FIB()
        self.network = {'r0':['r1', 'r3'], 'r1': ['r0', 'r2', 'r3'], 'r2': ['r1', 'r4'], 'r3': ['r0', 'r1', 'r5'],
                        'r4': ['r2', 'r5', 'r6'], 'r5': ['r3', 'r4', 'r5'], 'r6': ['r4', 'r7'], 'r7': ['r6', 'r8', 'r11'],
                        'r8': ['r5', 'r7', 'r9'], 'r9': ['r8', 'r10'], 'r10': ['r9', 'r11'], 'r11': ['r7', 'r10']}

        # Fib.Init_fib()
        return self.network


if __name__ == '__main__':
    """
        incomingface = route_ID
        interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
    
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/0', 10., 100.]}
    pit = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]]}
    inface = 'r0'
    # Time_out(inface, interest)
    # PIT_search_interest(inface, interest)
    # Creat_fib_entry(inface, 'r1/1')
    fib = FIB_init()
    """
    print('fib')