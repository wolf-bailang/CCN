from server import Server
from generate_data import *
from PS import *
import time

def main():
    server_num = 4
    PS_init(route_num=4, content_num=100)
    # data = unique_strings(k=4, ntokens=400)
    # data = list(data)
    # data = [data[:100], data[101:200], data[201:300], data[301:400]]
    # data = dict([[route_ID, [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, cost_time]]])
    server_list = []

    for i in range(server_num):
        # interest_data = {"data": data[2][2], "id": 8000 + i, "time": time.time()}
        server = Server(i, data[i])
        server.start()
        server_list.append(server)

    for id , i in enumerate(server_list):
        interest_data = {"data": data[2][2], "id": 8000 + id, "time": time.time()}
        i.send_interest(interest_data)
        interest_data = {"data": data[1][1], "id": 8000 + id, "time": time.time()}
        i.send_interest(interest_data)
        interest_data = {"data": data[3][0], "id": 8000 + id, "time": time.time()}
        i.send_interest(interest_data)


if __name__ == '__main__':
    main()