from enum import Flag

import threading, queue
import time
import socket
import json

from network import NETWORK
from interest import INTEREST
from data import DATA
from ps import PS
from cs import CS
from pit import PIT
from fib import FIB


class Server(threading.Thread):
    def __init__(self, serverID, sizes, producer_contents, run_start_time, network, HOST='127.0.0.1'):
        threading.Thread.__init__(self)
        self.HOST = HOST
        self.PORT= 8000 + serverID
        self.id = serverID      # number
        self.sizes = sizes      # sizes = [queue_size, cache_size, fib_size]
        self.queue_size, _, _ = sizes
        self.interest_queue = queue.Queue(self.queue_size)      # queue.Queue()
        self.data_queue = queue.Queue(self.queue_size)          # queue.Queue()
        self.Last_time = run_start_time
        self.step = 0

        # Create class instance
        Network = NETWORK()
        Pit = PIT()
        Ps = PS()
        Cs = CS()
        Fib = FIB()
        # Create a network link table
        self.network = Network.Creat_network(network)
        # Create pit table
        self.pit = Pit.Creat_pit(route_ID=self.id)
        #######################################################
        # Get the producer contents of the current router
        # producer_content = producer_contents['r'+str(self.id)]
        # Create a producer content store table
        # self.ps = Ps.Creat_ps(route_ID=self.id, route_num=12, content_num=100, producer_content=producer_content)
        #######################################################
        # Create a producer content store table
        self.ps = producer_contents['r'+str(self.id)]
        # Create router CS table
        self.cs = Cs.Creat_cs(route_ID=self.id)
        # Create router FIB table
        self.fib = Fib.Creat_FIB(route_ID=self.id)
        self.Tables = [self.network, self.ps, self.cs, self.pit, self.fib]

    # Create thread
    def run(self):
        threading.Thread(target = self.accept, daemon=True).start()
        threading.Thread(target = self.interest_process, daemon=True).start()
        threading.Thread(target = self.data_process, daemon=True).start()

    # Each router sends a fixed number of new interest packets to the network every second
    def start_network(self, run_start_time, frequency, content_num, route_num, interests):
        start_packets = []
        Interest = INTEREST()
        interest = interests['r' + str(self.id)]
        print(int(time.time()) - int(run_start_time))
        while True:
            if int(time.time()) - self.Last_time > frequency:
                self.Last_time = int(time.time())
                print('self.step= ' + str(self.step))
                start_packets = Interest.Generate_interest(route_ID=self.id, run_start_time=run_start_time, frequency=frequency,
                                                           content_num=content_num, route_num=route_num,
                                                           interest=interest[frequency*self.step : frequency*self.step+frequency])
                self.step += 1
                # print('start_packets')
                # print(start_packets)
                for i in range(0, len(start_packets)):
                    if self.interest_queue.full():
                        break
                    else:
                        self.interest_queue.put(start_packets[i])
                break
        # time.sleep(1)

    # Receive packet
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
                Interest = INTEREST()
                if Interest.Time_out(packet) == True or self.interest_queue.full() == False:
                    self.interest_queue.put(packet)
                else:
                    pass
            elif packet['type'] == 'data':           # Data packet received'
                if self.data_queue.full() == False:
                    self.data_queue.put(packet)
                else:
                    pass

    # process interest
    def interest_process(self):
        while self.interest_queue.empty is not True:
            interest = self.interest_queue.get()
            Interest = INTEREST()
            # if Interest.Time_out(interest) == True:
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
            else:
                pass    # Drop interest

    # process data
    def data_process(self):
        while self.data_queue.empty is not True:
            data = self.data_queue.get()
            Data = DATA()
            packet = Data.On_data(sizes=self.sizes, route_ID=self.id, data=data, tables=self.Tables)
            if len(packet):
                if packet[0][1]['type'] == 'data':     # send Datas packet
                    for i in range(len(packet)):
                        time.sleep(1)
                        send_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        # packet[i][0] = outface
                        send_data.connect((self.HOST, 8000 + packet[i][0]))
                        # packet[i][1] = data
                        send_data.sendall(bytes(json.dumps(packet[i][1]), encoding='utf-8'))
            else:
                pass    # Drop data
