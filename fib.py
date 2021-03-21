from __future__ import print_function

import time
import Table

#fib = {'content_name': [[0, 0]]
#      }
##################################################################################################
'''
list = [{ "name" : "Taobao", "cost0" : 100, 'outface0': 1, "cost1" : 100, 'outface1': 2},
       { "name" : "Runoob", "cost0" : 7 ,  'outface0': 1, "cost1" : 200, 'outface1': 2},
       { "name" : "Google", "cost0" : 100, 'outface0': 1, "cost1" : 300, 'outface1': 2},
       { "name" : "Wiki" ,  "cost0" : 200, 'outface0': 1, "cost1" : 400, 'outface1': 2}]
'''
##################################################################################################

class FIB():
    def __init__(self):
        self.fib = {}
        self.fib_entry = []

    def Creat_FIB(self, route_ID):
        '''
        fib = {'content_name': [[outface, cost, time], ...],
               ...
               }

        print('r'+str(route_ID)+' fib')
        print(self.fib)
        print(' ')
        '''
        return self.fib

    def Get_fib_entry(self, content_name):
        '''
        fib = {'content_name': [[outface, cost, time], ...],
               ...
               }
        '''
        self.fib_entry = self.fib.get(key=content_name, default=None)
        return self.fib_entry

    def Add_fib_outface(self, data):
        outface = data['route_ID']
        cost = data['data_hop']
        times = int(time.time())
        if len(self.fib_entry) < 3:
            self.fib_entry.append([outface, cost, times])
            self.fib_entry.sort(key=lambda x:(x[1]), reverse=False)
        else:
            x = self.fib_entry.pop(-1)
            self.fib_entry.append([outface, cost, times])
            self.fib_entry.sort(key=lambda x: (x[1]), reverse=False)

    def Remove_fib_entry(self):
        '''
        fib = {'content_name': [[outface, cost, time], ...],
               ...
               }
        '''
        max = 0
        content_name = ''
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
        times = int(time.time())
        temp = {content_name: [outface, cost, times]}
        self.fib.update(temp)

    # The outface is updated to fib
    def Update_fib_outface(self, fib, route_ID, fib_size, data):
        '''
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'start_time': 0.0}
        FIB = {'route_ID': [[content_name, [[cost, outface], ...]], ...], ...}
        fib = [[content_name, [[cost, outface], ...]], ...]
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

    def Brocast(self):
        outfaces = []
        for i in self.fib_entry:
            outfaces.append(i[0])
            return outfaces

    def Best_route(self):
        return [self.fib_entry[0][0]]

    def Search_fib_interest(self, fib, route_ID, interest):
        self.fib = fib
        content_name = interest['content_name']
        self.fib_entry = self.Get_fib_entry(content_name)
        if self.fib_entry == None:
            outface = self.Brocast()
        else:
            outface = self.Best_route()
        return outface

    '''
    def Init_fib(self):
        Network = [['r0', ['r1', 'r2']], ['r1' ,['r0', 'r2']], ['r2' ,['r0', 'r1']]]
        FIB = {'route_ID': [[content_name,[[cost, outface], ...]], ...], ... }
        fib = [[content_name, [[cost, outface], ...]], ...]
        
        for i in range(len(Table.Network)):
            route_ID = Table.Network[i][0]
            face = Table.Network[i][1]
            # fib_entry = [content_name, [[cost, outface], ...]
            fib_entry = dict([[route_ID, face]])
            Table.FIB.update(fib_entry)
        # print(Table.FIB)
    '''

if __name__ == '__main__':
    """
        incomingface = route_ID
        interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
    
    # pit = {'route_ID': [content_name,[inface],[outface]], [content_name,[inface],[outface]]}
    Table.Network = [['r0', ['r1', 'r3']], ['r1', ['r0', 'r2', 'r3']], ['r2', ['r1', 'r4']], ['r3', ['r0', 'r1', 'r5']],
                     ['r4', ['r2', 'r5', 'r6']], ['r5', ['r3', 'r4', 'r5']], ['r6', ['r4', 'r7']],
                     ['r7', ['r6', 'r8', 'r11']],
                     ['r8', ['r5', 'r7', 'r9']], ['r9', ['r8', 'r10']], ['r10', ['r9', 'r11']], ['r11', ['r7', 'r10']]]
    Table.FIB = {}
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/0', 10., 100.]}
    pit = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]]}
    inface = 'r0'

    # Time_out(inface, interest)
    # PIT_search_interest(inface, interest)
    # Creat_fib_entry(inface, 'r1/1')
    FIB_init()
    """
    print('fib')