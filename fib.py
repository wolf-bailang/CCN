from __future__ import print_function

import time

class FIB():
    def __init__(self):
        self.fib = {}
        self.fib_entry = []

    def Creat_FIB(self, route_ID):
        '''
        fib = {'content_name': [[outface, cost, time], ...],
               ...
               }
        '''
        return self.fib

    def Get_fib_entry(self, content_name):
        '''
        fib = {'content_name': [[outface, cost, time], ...], ... }
        fib_entry = [[outface, cost, time], ...]
        '''
        self.fib_entry = self.fib.get(key=content_name, default=None)
        return self.fib_entry

    def Add_fib_outface(self, data):
        outface = data['route_ID']
        cost = data['data_hop']
        # Record the time when the outface was added
        times = int(time.time())
        if len(self.fib_entry) < 10000000:
            self.fib_entry.append([outface, cost, times])
            # Sort by cost from smallest to largest
            self.fib_entry.sort(key=lambda x:(x[1]), reverse=False)
        else:
            # Delete the most costly outface
            x = self.fib_entry.pop(-1)
            self.fib_entry.append([outface, cost, times])
            # Sort by cost from smallest to largest
            self.fib_entry.sort(key=lambda x: (x[1]), reverse=False)

    # Remove the content name with the most cost
    def Remove_fib_entry(self):
        '''
        fib = {'content_name': [[outface, cost, time], ...], ... }
        '''
        max = 0
        content_name = ''
        # Find the content name with the most cost
        for key,value in self.fib.items():
            cost = value[0][1]
            # time = value[0][2]
            if cost > max:
                max = cost
                content_name = key
        del self.fib[content_name]

    def Add_fib_entry(self, data):
        content_name = data['content_name']
        outface = data['route_ID']
        cost = data['data_hop']
        # Record the time when the entry was added
        times = int(time.time())
        temp = {content_name: [outface, cost, times]}
        self.fib.update(temp)

    # The outface is updated to fib
    def Update_fib_outface(self, fib, route_ID, fib_size, data):
        '''
        fib = {'content_name': [[outface, cost, time], ...], ... }
        fib_entry = [[outface, cost, time], ...]
        '''
        self.fib = fib
        content_name = data['content_name']
        self.fib_entry = self.Get_fib_entry(content_name)
        if self.fib_entry == None:
            if len(self.fib) > fib_size:
                self.Remove_fib_entry()
                self.Add_fib_entry(data)
            else:
                self.Add_fib_entry(data)
        else:
            self.Add_fib_outface(data)

    # Forward interest packets to all neighbors
    def Brocast(self):
        outfaces = []
        for i in self.fib_entry:
            outfaces.append(i[0])
            return outfaces

    # Choose the outface with the min cost to forward the interest packet
    def Best_route(self):
        return [self.fib_entry[0][0]]

    # Find in FIB whether there is a matching interest packet entry
    def Search_fib_interest(self, fib, route_ID, interest):
        self.fib = fib
        content_name = interest['content_name']
        self.fib_entry = self.Get_fib_entry(content_name)
        if self.fib_entry == None:
            outface = self.Brocast()
        else:
            outface = self.Best_route()
        return outface
