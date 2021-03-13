import json
import numpy as np

if __name__ == '__main__':
    '''
    pit = {'a': [[0, 1, 2], [3, 4, 5]],
           'b': [[0, 1, 2], [3, 4, 5]],
           }
    interest = {'route_ID': 1, 'content_name': 'c'}
    inface = interest['route_ID']
    content_name = interest['content_name']

    new_dict = {content_name: [[inface], []]}
    # pit.update(new_dict)
    a = [[0, {'b': 'yui'}], [1, {'c': 1}]]
    if a[0][1]['b'] == 'yui':
        print('1')
    
      ps = {}
    for i in range(12):
        pop = []
        a={}
        for j in range(10):
            # Generate content name
            content_name = 'r' + str(i) + '/' + str(j)
            pop.append(content_name)
        b = {'r' + str(i): pop}
        ps.update(b)
    print(ps)
    with open("./producer_contents.json", "w", encoding='utf-8') as f:
        # temp = json.dumps(ps)
        json.dump(ps, f)  # 写为一行

    with open('./producer_contents.json', 'r', encoding='utf8')as fp:
        producer_contents = json.load(fp)
        print(producer_contents)
    print(producer_contents)
    '''

    ps = {}
    for i in range(12):
        pop = []
        a={}
        for j in range(5):
            # Generate content name
            index1 = np.random.randint(0, 12)
            index = np.random.randint(0, 10)
            content_name = 'r' + str(index1) + '/' + str(index)
            # content_name = 'r' + str(i) + '/' + str(j)
            a = {'interest_ID': str(i)+'000'+str(j), 'content_name': content_name}
            pop.append(a)
        b = {'r' + str(i): pop}
        ps.update(b)
    print(ps)
    with open("./interests.json", "w", encoding='utf-8') as f:
        # temp = json.dumps(ps)
        json.dump(ps, f)  # 写为一行

    with open('./interests.json', 'r', encoding='utf8')as fp:
        interests = json.load(fp)
        print(interests)
    print(interests)



