from enum import Flag

import threading, queue
import time
import socket
import json

from interest import INTEREST
from data import DATA
from ps import PS
import Table
from pit import PIT
from fib import FIB
from network import NETWORK

#FIB
network = [['r0', ['r1', 'r2']], ['r1', ['r0', 'r3']], ['r2', ['r0', 'r3']], ['r3', ['r1', 'r2']]]

class Server(threading.Thread):

    def __init__(self, serverID, HOST='127.0.0.1'):
        threading.Thread.__init__(self)
        self.HOST = HOST
        self.PORT= 8000 + serverID
        self.id = serverID  # 'r' + str(serverID)
        self.interest_queue = queue.Queue()
        self.data_queue = queue.Queue()

        Network = NETWORK()
        pit = PIT()
        ps = PS()
        fib = FIB()
        self.network = Network.Creat_network()
        self.pit = pit.Creat_pit(route_ID=self.id)
        self.ps = ps.Creat_ps(route_ID=self.id, route_num=12, content_num=100)
        self.fib = fib.Creat_FIB(route_ID=self.id)
        self.Tables = [self.network, self.ps, self.pit, self.fib]

    def run(self):
        threading.Thread(target = self.accept, daemon=True).start()
        threading.Thread(target = self.interest_process, daemon=True).start()
        threading.Thread(target = self.data_process, daemon=True).start()
        
    def start_network(self, run_time, frequency, content_num):
        Interest = INTEREST()
        for i in range(int(run_time)):
            start_packets = Interest.Generate_interest(route_ID=self.id, frequency=frequency, content_num=content_num)
            for i in start_packets:
                self.interest_queue.put(i)
            time.sleep(5)
        '''
        start = time.time()
        while int(time.time() - start) == 2:
            # time.time()
        '''
    '''
    def Init(self, route_num, content_num):
        ps = PS()
        ps.Creat_ps(route_ID=self.id, route_num=route_num, content_num=content_num)
        pit = PIT()
        pit.Creat_pit(route_ID=self.id)
        fib = FIB()
        fib.Creat_FIB(route_ID=self.id)
    '''

    def accept(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen(10)

        while True:
            conn, addr = server.accept()
            packet = conn.recv(1024)
            packet = json.loads(packet)
            # packet = [interest] or [data]
            if packet['type'] == 'interest':         # Interest packet received
                # self.interest_queue.put(packet)
                Interest = INTEREST()
                if Interest.Time_out(packet) == True:
                    self.interest_queue.put(packet)
                else:
                    pass
            elif packet['type'] == 'data':           # Data packet received
                self.data_queue.put(packet)

    def interest_process(self):
        while self.interest_queue.empty is not True:
            interest = self.interest_queue.get()
            Interest = INTEREST()
            #if Interest.Time_out(interest_packet) == True:
            packet = Interest.On_interest(route_ID=self.id, interest=interest, tables=self.Tables)
            if len(packet) :
                if packet[0][1]['type'] == 'data':  # send Datas packet
                    for i in range(len(packet)):
                        time.sleep(1)
                        send_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        # packet[i][0] = outface
                        send_data.connect((self.HOST, 8000 + packet[i][0]))
                        # packet[i][1] = data
                        send_data.sendall(bytes(json.dumps(packet[i][1]), encoding='utf-8'))
                elif packet[0][1]['type'] == 'interest':  # send Interests packet
                    for i in range(len(packet)):
                        send_interest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        # packet[i][0] = outface
                        send_interest.connect((self.HOST, 8000 + packet[i][0]))
                        # packet[i][1] = interest
                        send_interest.sendall(bytes(json.dumps(packet[i][1]), encoding='utf-8'))
            else:  # Drop interest
                pass
            #else:
            #    pass

    def data_process(self):
        while self.data_queue.empty is not True:
            data = self.data_queue.get()
            Data = DATA()
            packet = Data.On_data(inface=data['route_ID'], route_ID=self.id, data=data, tables=self.Tables)
            if len(packet) :
                if packet[0][1]['type'] == 'data':     # send Datas packet
                    for i in range(len(packet)):
                        time.sleep(1)
                        send_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        # packet[i][0] = outface
                        send_data.connect((self.HOST, 8000 + packet[i][0]))
                        # packet[i][1] = data
                        send_data.sendall(bytes(json.dumps(packet[i][1]), encoding='utf-8'))
            else:   # Drop data
                pass
