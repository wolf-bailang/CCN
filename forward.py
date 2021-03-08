from __future__ import print_function

from pit import PIT
from fib import FIB
from network import NETWORK
import Table

class FORWARD():
    def __init__(self):
        self.forward = 0

    def Forward_data(self, pit, data):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        '''
        # Get the requested content name of the data packet
        content_name = data['content_name']
        # Get the pit_entry of this content_name
        Pit = PIT()
        pit_entry = pit# Pit.Get_pit_entry(content_name)
        Infaces = pit_entry[0]
        return Infaces

    def Forward_interest(self, network, route_ID, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                            'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        # Not optimized
        fib = network = {'route_ID':[route_ID, ...], ...}

        # Can be optimized
        fib = [[content_name,[[cost, outface], ...]], ...]
        '''
        # Get the fibs record table of this router
        Network = NETWORK()
        network = network # Network.Get_network()
        FIB_entry = network['r'+str(route_ID)]
        # print('FIB_entry')
        # print(FIB_entry)
        '''
        # Get the requested content name of the interest packet
        # content_name = interest['content_name']
        # Get the fib record table of this router
        # Fib = FIB()
        # FIB_entry = Fib.Get_FIB_entry(content_name)
        # Check whether there is a record of an entry with the same name as the interest packet in the fib
        for i in range(len(fib)):
            fib_entry = fib[i]
            # print(pit_entry[0])
            if content_name == fib_entry[0]:
                Outface = fib_entry[2]
                # print(Outface)
                return Outface
        '''
        Outfaces = FIB_entry
        return Outfaces



if __name__ == '__main__':
    '''
    Table.PIT = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r2/1', ['r2', 'r9'], ['r8', 'r7']]],
                 'r1': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/11', ['r2', 'r9'], ['r8', 'r7']]]}
    Table.Interest_table = {'r0': [['i0', 'c0', 'r1', 'r2/1', 10., 100.], ['i1', 'c0', 'r0', 'r1/1', 10., 100.]],
                            'r1': [['i2', 'c0', 'r0', 'r3/1', 10., 100.], ['i3', 'c0', 'r0', 'r4/1', 10., 100.]]}
    Table.PS = {'r0': ['r1/1', 'r3/0', 'r4/0', 'r5/0'],
                'r1': ['r1/1', 'r2/1', 'r9/1', 'r8/1', 'r7/1']}
    Table.FIB = {'r0': ['r5'],
                 'r1': ['r2', 'r9', 'r8', 'r7']}
    '''
    # Forward_data(route_ID = 'r0', data = ['i0', 'c0', 'r0', 'r1/0', 10., 100., 2])
    # Forward_interest(route_ID = 'r1', interest = ['i0', 'c0', 'r0', 'r1/0', 10., 100.])