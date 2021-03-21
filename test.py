import json
import numpy as np
import csv

# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]

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
    
    with open('Output_data.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(data2txt)  # 写入
        file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据

    f = open('Output_data.csv', 'w', encoding='utf-8', newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Time", "Type", "性别"])
    data2str= ['1', '2', '3']
    csv_writer.writerow(data2str)
    f.close()
    
    
    cs = [['4',2,3,4,1], ['2',3,4,1,2], ['3',4,1,2,3], ['1',1,2,3,4]]
    print(cs)
    # cs.sort(key=takeSecond, reverse=False)
    cs.sort(key=lambda x:(x[3]), reverse=False)
    print(cs)
    
    '''
    cs = {'4':[[1],[2],[3]], '2':[[3],[4],[1]], '3':[[4],[1],[2]], '1':[[2],[3],[4]]}
    print(cs)
    # cs.sort(key=takeSecond, reverse=False)
    # sorted(cs, key=lambda x: (x['3']), reverse=False)
    sorted(cs.items(), key=lambda x: x[1][1], reverse=False)
    print(cs)







