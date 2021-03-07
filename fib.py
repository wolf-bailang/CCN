from __future__ import print_function

import time
import Table

fib = {'content_name': [[0, 0]]
      }
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
        self.fib = fib




    def Get_fib_entry(self, content_name):
        '''
        fib = {'content_name': [[cost, ], ...],
               ...
               }
        '''
        FIB_entry = self.fib[content_name]
        return FIB_entry

    def Init_fib(self):
        '''
            Network = [['r0', ['r1', 'r2']], ['r1' ,['r0', 'r2']], ['r2' ,['r0', 'r1']]]
            FIB = {'route_ID': [[content_name,[[cost, outface], ...]], ...], ... }
            fib = [[content_name, [[cost, outface], ...]], ...]
        '''
        for i in range(len(Table.Network)):
            route_ID = Table.Network[i][0]
            face = Table.Network[i][1]
            # fib_entry = [content_name, [[cost, outface], ...]
            fib_entry = dict([[route_ID, face]])
            Table.FIB.update(fib_entry)
        # print(Table.FIB)

    def Creat_fib_entry(self, inface, content_name):
        fib_entry = fib[inface]
        # print(fib_entry)
        fib_entry.append([content_name, [[cost, inface]]])
        # print(fib_entry)
        return fib_entry

    # 获取列表的第一个元素
    def takeSecond(self, elem):
        return elem[0]

    # The outface is updated to fib
    def Update_fib_outface(self, inface, route_ID, data):
        '''
            Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time, hop], ...],...}
            data = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time, hop]
            FIB = {'route_ID': [[content_name,[[cost, outface], ...]], ...], ... }
            fib = [[content_name, [[cost, outface], ...]], ...]
        '''
        fib = Table.FIB[route_ID]
        content_name = data[3]
        now_time = time.time()  # s
        cost = now_time - life_time
        # Check whether there is a record of an entry with the same name as the data packet in the FIB
        for i in range(len(fib)):
            # print(fib[i])
            fib_entry = fib[i]
            # print(fib_entry)
            if content_name == fib_entry[0]:
                fib_entry[2].append([cost, inface])
                # sort fib_entry based on cost
                fib_entry.sort(key=takeSecond)
                fib[i] = fib_entry
                # print(fib_entry)
                Table.FIB[route_ID] = fib
                # print(Table.FIB)
            else:
                fib_entry = self.Creat_fib_entry(inface, content_name)
                fib[i] = fib_entry
                # print(fib_entry)
                Table.FIB[route_ID] = fib
                # print(Table.FIB)

    def Search_fib_interest(self, inface, route_ID, interest):
        '''
            inface = route_ID
            Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
            interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
            FIB = {'route_ID': [[content_name,[[cost, outface], ...]], ...], ... }
            fib = [[content_name, [[cost, outface], ...]], ...]
        '''
        # Get the FIB record table of this router
        fib = Table.FIB[route_ID]
        # print(fib_entry)
        # Get the requested content name of the interest packet
        content_name = interest[3]
        # Check whether there is a record of an entry with the same name as the interest packet in the FIB
        for i in range(len(fib)):
            fib_entry = fib[i]
            # print(fib_entry)
            if content_name == fib_entry[0]:
                outface = Best_route(fib_entry[1])
                return outface
        outface = Brocast(fib)
        return outface




    def Search_fib_data(self, inface, data):
        '''
            inface = route_ID
            data = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time, hop]}
            pit = {'route_ID': [content_name,[inface],[outface]], [content_name,[inface],[outface]]}
        '''
        pit_entry = pit[inface]
        # print(pit_entry)
        content_name = data[inface][-3]
        for i in range(len(pit_entry)):
            print(pit_entry[i][0])
            if content_name == pit_entry[i][0]:

                # Delete_pit_entry
                fib_entry.append([content_name, [inface], []])  # Delete_pit_entry(inface, content_name)
                return True

        # Merge_pit_entry
        # fib_entry[i][1].append(inface)  # Merge_pit_entry(i, inface)
        # Drop_data(inface, data)
        return False

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