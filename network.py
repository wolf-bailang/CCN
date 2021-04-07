# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.02.27

from __future__ import print_function

from pit import *
from ps import PS
from fib import FIB


class NETWORK():
    def __init__(self):
        self.network = {}

    def Creat_network(self, network):
        '''
        self.network = {"r0": [1, 3], "r1": [0, 2, 3], "r2": [1, 4], "r3": [0, 1, 5],
                        "r4": [2, 5, 6], "r5": [3, 4, 5], "r6": [4, 7], "r7": [6, 8, 11],
                        "r8": [5, 7, 9], "r9": [8, 10], "r10": [9, 11], "r11": [7, 10]}
        '''
        self.network = network
        return self.network

    def Get_network(self):
        return self.network
