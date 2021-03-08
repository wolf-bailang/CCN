

if __name__ == '__main__':
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
