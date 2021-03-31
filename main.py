
import time

from server import Server
# from generate_data import *
# from ps import PS
# from network import NETWORK
import json

# Read parameters
def load_peremiters():
    with open('./Input/peremiters.json', 'r', encoding='utf8')as fp:
        peremiters = json.load(fp)
    return peremiters

# Read the contents produced by each producer
def input_producer_contents():
    with open('./Input/producer_contents.json', 'r', encoding='utf8')as fp:
        producer_contents = json.load(fp)
    return producer_contents

# Read the interest packets to be sent by each router
def input_interests():
    with open('./Input/interests.json', 'r', encoding='utf8')as fp:
        interests = json.load(fp)
    return interests

def main():
    '''
    peremiters = {"route_num": 12,      # Number of routers
                  "frequency": 3,       # How many interest packets sent by each router to the network per second
                  "content_num": 100,   # The amount of content produced by each producer
                  "run_time": 10,       # Simulator running time
                  "queue_size": 10,     # The storage space size of the queue
                  "cache_size": 10,     # CS storage space size
                  "FIB_size": 10}       # FIB storage space size
    '''
    producer_contents = input_producer_contents()
    interests = input_interests()
    peremiters = load_peremiters()

    server_num = peremiters['route_num']
    frequency = 1 # peremiters['frequency']  # 10/s
    route_num = peremiters['route_num']
    content_num = peremiters['content_num']
    run_time = 100 #peremiters['run_time']
    queue_size = peremiters['queue_size']
    cache_size = peremiters['cache_size']
    fib_size = peremiters['fib_size']
    #
    sizes = [queue_size, cache_size, fib_size]
    # server_num = route_num
    # Get the start time of the simulator
    run_start_time = int(time.time())
    # network = Network(server_num)
    # networks = network.Network_init()
    # uptime = run_start_time
    # step = 0
    server_list = []
    for i in range(server_num):
        server = Server(i, sizes, producer_contents, run_start_time)
        server.start()
        server_list.append(server)

    '''
    for i in server_list:
        # The router sends new interest packets to the network
        i.start_network(run_start_time, frequency, content_num, route_num, interests)  #, step=step, uptime=uptime
    
    uptime= int(time.time())
    step = 0
    while True:
        print(int(time.time()) - int(run_start_time))
        if int(time.time()) - uptime > 1:
            uptime = int(time.time())
            for i in server_list:
                # The router sends new interest packets to the network
                i.start_network(run_start_time, frequency, content_num, route_num, interests, step)
            step +=1
        # time.sleep(1)continue
        # Whether it's the end time of the simulator / 2
        if int(time.time()) - int(run_start_time) > int(run_time):
            # print(str(int(time.time())))
            # print(str(run_start_time))
            print(str(int(time.time()) - int(run_start_time)))
            print('end')
            for i in server_list:
                i.join()
            break
    '''

    while True:
        for i in server_list:
            # The router sends new interest packets to the network
            i.start_network(run_start_time, frequency, content_num, route_num, interests)  # , step=step, uptime=uptime
        # Whether it's the end time of the simulator
        if int(time.time()) - int(run_start_time) > int(run_time):
            print(str(time.time()))
            print(str(run_start_time))
            print(str(int(time.time()) - int(run_start_time)))
            print('end')
            for i in server_list:
                i.join()
            break


if __name__ == '__main__':
    main()
