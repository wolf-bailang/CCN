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

    def accept(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen(10)

        while True:
            conn, addr = server.accept()
            packet = conn.recv(1024)
            packet = json.loads(packet)
            if packet[0] == "I":
                self.interest_queue.put(packet)
            else:
                self.data_queue.put(packet)

    def interest_process(self):
        while self.interest_queue.empty is not True:
            interest = self.interest_queue.get()
            return_interest, flag = On_interest(interest[2], self.id, interest)
            if flag:
                for i in range(len(return_interest)):
                    send_interest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    send_interest.connect((self.HOST, return_interest[i][0]))
                    send_interest.sendall(bytes(json.dumps(return_interest[i][1]), encoding='utf-8'))
            else:
                pass

    def data_process(self):
        while self.data_queue.empty is not True:
            data = self.data_queue.get()
            return_data, flag = On_data(data[2], self.id, data)
            if flag:
                for i in range(len(return_data)):
                    send_interest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    send_interest.connect((self.HOST, return_data[i][0]))
                    send_interest.sendall(bytes(json.dumps(return_data[i][1]), encoding='utf-8'))
            else:
                pass