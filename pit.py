# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.03.05

from __future__ import print_function

class PIT():
    def __init__(self):
        self.pit = {}

    # Each router creates an independent PIT table
    def Creat_pit(self, route_ID):
        '''
        pit = {'content_name': [[inface, ...], [outface, ...]],
               ...
               }
        '''
        return self.pit

    def Get_pit(self):
        return self.pit

    # Get the entry of the content name from the pit
    def Get_pit_entry(self, content_name):
        PIT_entry = self.pit[content_name]
        return PIT_entry

    # The outface is updated to pit
    def Update_pit_outface(self, pit, Outfaces, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        Outfaces = [outface, ...]
        pit_entry = [[inface, ...], [outface, ...]]
        '''
        self.pit = pit
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
        # Remove duplicate inface
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
    def Search_pit_interest(self, pit, interest):
        """
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        """
        self.pit = pit
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

    # Check whether there is an entry matching the content name of the data packet in the pit
    def Search_pit_data(self, pit, data):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        '''
        self.pit = pit
        # Get the requested content name of the interest packet
        content_name = data['content_name']
        # Check whether there is a record of an entry with the same name as the interest packet in the PIT
        if content_name in self.pit:
            return True
        else:
            return False

    # The content_name entry is removed from pit
    def Remove_pit_entry(self, pit, data):
        '''
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        '''
        self.pit = pit
        content_name = data['content_name']
        # Delete content_name entry in pit
        del self.pit[content_name]
