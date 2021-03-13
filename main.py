
import time

from server import Server
# from generate_data import *
# from ps import PS
# from network import NETWORK
import json

def load_peremiters():
    with open('./peremiters.json', 'r', encoding='utf8')as fp:
        peremiters = json.load(fp)
    return peremiters

def input_producer_contents():
    with open('./producer_contents.json', 'r', encoding='utf8')as fp:
        producer_contents = json.load(fp)
    return producer_contents

def input_interests():
    with open('./interests.json', 'r', encoding='utf8')as fp:
        interests = json.load(fp)
    return interests

def main():
    '''
    peremiters = {"route_num": 12, "frequency": 3, "content_num": 100, "run_time": 10, "queue_size": 10,
                  "cache_size": 10, "FIB_size": 10}
    '''
    producer_contents = input_producer_contents()
    interests = input_interests()
    peremiters = load_peremiters()

    server_num = peremiters['route_num']
    frequency = peremiters['frequency']  # 10/s
    route_num = peremiters['route_num']
    content_num = peremiters['content_num']
    run_time = peremiters['run_time']
    queue_size = peremiters['queue_size']
    cache_size = peremiters['cache_size']
    fib_size = peremiters['fib_size']
    server_num = route_num
    start_time = int(time.time())
    # network = Network(server_num)
    # networks = network.Network_init()

    # data = unique_strings(k=4, ntokens=400)
    # data = list(data)
    # data = [data[:100], data[101:200], data[201:300], data[301:400]]
    # data = dict([[route_ID, [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, cost_time]]])
    server_list = []

    for i in range(server_num):
        # interest_data = {"data": data[2][2], "id": 8000 + i, "time": time.time()}
        server = Server(i, producer_contents)
        server.start()
        server_list.append(server)
        
    for i in server_list:
        print('i'+str(i))
        i.start_network(start_time, frequency, content_num, route_num, interests)
        # time.sleep(1)
        
    while True:
        print(str(time.time()))
        print(str(start_time))
        print(str(int(time.time()) - int(start_time)))
        # if int(time.time()) - int(start_time) > int(run_time):
        if int(time.time()) - int(start_time) > 10:
            #print('111111111111111')
            for i in server_list:
                #print('222222222222222')
                i.join()
            break

if __name__ == '__main__':
    main()
