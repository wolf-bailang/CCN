from __future__ import print_function

from pit import PIT
from fib import FIB
from network import NETWORK

class FORWARD():
    def __init__(self):
        self.forward = 0

    # Get data packet forwarding interface
    def Forward_data(self, pit, data):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'run_start_time': 0.0, 'path': ''}
        pit = {'content_name': [[inface, ...], [outface, ...]], ...}
        '''
        Infaces = []
        inface = data['route_ID']
        # Get the requested content name of the data packet
        content_name = data['content_name']
        # Get the pit_entry of this content_name
        Pit = PIT()
        pit_entry = pit[content_name]   # Pit.Get_pit_entry(content_name)
        for x in pit_entry[0]:
            if x != inface:
                Infaces.append(x)
        return Infaces

    # Get interest packet forwarding interface
    def Forward_interest(self, fib, network, route_ID, interest):
        '''
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                            'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        # Not optimized
        fib = network = {'route_ID':[route_ID, ...], ...}

        # Can be optimized
        fib = [[content_name,[[cost, outface], ...]], ...]
        '''
        Outfaces = []
        inface = interest['route_ID']
        # Get the fibs record table of this router
        # Network = NETWORK()
        network = network       # Network.Get_network()
        fib_entry = network['r'+str(route_ID)]

        ################################################
        # Fib = FIB()
        # fib_entry = Fib.Search_fib_interest(fib, route_ID, interest)
        ################################################
        for x in fib_entry:
            if x != inface or x != route_ID:
                Outfaces.append(x)
        return Outfaces
