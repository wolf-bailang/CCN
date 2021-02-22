from enum import Flag
from Interest import On_interest
from Data import On_data
import Table
import threading, queue
import time
import socket
import json

#FIB
network = [['r0', ['r1', 'r2']], ['r1', ['r0', 'r3']], ['r2', ['r0', 'r3']], ['r3', ['r1', 'r2']]]

class Server(threading.Thread):

    def __init__(self, serverID, HOST='127.0.0.1'):
        threading.Thread.__init__(self)
        self.HOST = HOST
        self.PORT= 8000 + serverID
        self.id = 'r' + str(serverID)
        self.interest_queue = queue.Queue()
        self.data_queue = queue.Queue()

    def run(self):
        threading.Thread(target = self.accept, daemon=True).start()
        threading.Thread(target = self.interest_process, daemon=True).start()
        threading.Thread(target = self.data_process, daemon=True).start()
        
    def start_network(self, stime):
        while time.time() - stime == 1:
            # start_packet = func(self.id)
            for i in start_packet:
                self.interest_queue.put(i)

    def accept(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen(10)

        while True:
            conn, addr = server.accept()
            packet = conn.recv(1024)
            packet = json.loads(packet)
            # packet = ["interest", interest] or ["data", data]
            if packet[0] == "interest":         # Interest packet received
                self.interest_queue.put(packet[1])
            else:                               # Data packet received
                self.data_queue.put(packet[1])

    def interest_process(self):
        while self.interest_queue.empty is not True:
            interest = self.interest_queue.get()
            # interest[2] = inface, self.id = route_ID
            packet, flag = On_interest(interest[2], self.id, interest)
            if flag==1:     # send Datas packet
                data_packet = packet
                for i in range(len(data_packet)):
                    send_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # data_packet[i][0] = outface
                    send_data.connect((self.HOST, data_packet[i][0]))
                    # data_packet[i][1] = data
                    send_data.sendall(bytes(json.dumps(data_packet[i][1]), encoding='utf-8'))
            elif flag==2:     # send Interests packet
                interest_packet = packet
                for i in range(len(interest_packet)):
                    send_interest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # interest_packet[i][0] = outface
                    send_interest.connect((self.HOST, interest_packet[i][0]))
                    # interest_packet[i][1] = interest
                    send_interest.sendall(bytes(json.dumps(interest_packet[i][1]), encoding='utf-8'))
            else:       # Drop interest
                pass

    def data_process(self):
        while self.data_queue.empty is not True:
            data = self.data_queue.get()
            # data[2] = inface, self.id = route_ID
            packet, flag = On_data(data[2], self.id, data)
            if flag==1:     # send Datas packet
                data_packet = packet
                for i in range(len(data_packet)):
                    send_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # data_packet[i][0] = outface
                    send_data.connect((self.HOST, data_packet[i][0]))
                    # data_packet[i][1] = data
                    send_data.sendall(bytes(json.dumps(data_packet[i][1]), encoding='utf-8'))
            else:       # Drop data
                pass
