# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.03.05

from __future__ import print_function

import time
import numpy as np
import Table
from interest import INTEREST

pit = {'content_name': [[0], [0]]
      }

class PIT():
    def __init__(self):
        self.pit = pit

    def Get_pit_entry(self, content_name):
        PIT_entry = self.pit[content_name]
        return PIT_entry

    # The outface is updated to pit
    def Update_pit_outface(self, Outfaces, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        Outfaces = [outface, ...]
        '''
        content_name = interest['content_name']
        # Check whether there is a record of an entry with the same name as the interest packet in the PIT
        pit_entry = self.pit[content_name]
        for j in range(len(Outfaces)):
            pit_entry[1].append(Outfaces[j])
        self.pit[content_name] = pit_entry

    # The inface of the received interest packet is merged into the same content name
    def Merge_pit_entry(self, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        '''
        inface = interest['route_ID']
        content_name = interest['content_name']
        PIT_entry = self.Get_pit_entry(content_name)
        PIT_entry[0].append(inface)
        # 去除重复的元素
        PIT_entry[0] = list(set(PIT_entry[0]))

    # Create a pit entry
    def Creat_pit_entry(self, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        '''
        inface = interest['route_ID']
        content_name = interest['content_name']
        new_dict = {content_name: [[inface], []]}
        self.pit.update(new_dict)

    # Check whether there is an entry matching the content name of the interest packet in the pit
    def Search_pit_interest(self, interest):
        """
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        """
        # Get the requested content name of the interest packet
        content_name = interest['content_name']
        # Check whether there is a record of an entry with the same name as the interest packet in the PIT
        if content_name in self.pit:
            # The inface of the received interest packet is merged into the same content name
            self.Merge_pit_entry(interest)
            return False
        else:
            # Create a pit entry
            self.Creat_pit_entry(interest)
            return True

    def Search_pit_data(self, data):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        '''
        # Get the requested content name of the interest packet
        content_name = data['content_name']
        # Check whether there is a record of an entry with the same name as the interest packet in the PIT
        if content_name in self.pit:
            return True
        else:
            return False

    # The content_name entry is removed to pit
    def Remove_pit_entry(self, data):
        '''
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        '''
        content_name = data['content_name']
        # Delete content_name entry in pit
        del self.pit[content_name]





if __name__ == '__main__':
    """
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
        PIT = {'route_ID': [[content_name, [inface, ...], [outface, ...]], ...], ...}
        pit = [[content_name, [inface, ...], [outface, ...]], ...]
        Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time, hop], ...], ... }
        data = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time, hop]
    
    Table.Data_table = {'r0': ['i0', 'c0', 'r0', 'r1/0', 10., 100., 1.0]}
    Table.PIT = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]]}
    # Time_out(inface, interest)
    # Merge_pit_entry(1, inface='r1', route_ID='r0')
    # Creat_pit_entry(inface='r11', route_ID='r11', content_name='r6/100')
    # PIT_search_interest(inface= 'r11', route_ID= 'r0', interest= ['i0', 'c0', 'r0', 'r1/0', 10., 100.])
    # PIT_search_data(inface= 'r11', route_ID= 'r0', data= ['i0', 'c0', 'r0', 'r1/0', 10., 100., 1.0])
    # PIT_update_outface(Outface= ['r11', 'r12'], route_ID= 'r0', interest= ['i0', 'c0', 'r0', 'r1/0', 1.0, 10., 100.])
    """


