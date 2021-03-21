# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.02.27

from __future__ import print_function

import Table


class PS():
    def __init__(self):
        # self.route_num = route_num
        # self.content_num = content_num
        self.ps = []

    # Producer generates unique content name
    def Creat_ps(self, route_ID, route_num, content_num, producer_content):
        '''
        PS = [content_name,...]

        # for i in range(route_num):
            # route_ID_name = 'r' + str(route_ID)
        for j in range(content_num):
            # Generate content name
            content_name = 'r' + str(route_ID) + '/' + str(j)
            self.ps.append(content_name)

        print('r' + str(route_ID) + ' ps')
        print(self.ps)
        print(' ')

        return self.ps
        '''
        self.ps = producer_content
        return self.ps

    def Get_ps(self):
        return self.ps

    def Search_ps_interest(self, ps, content_name):
        '''
        ps = [content_name,...]
        interest = {'type': 'interest', 'interest_ID': 0, 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0',
                    'interest_hop': 0, 'life_hop': 5, 'start_time': 0.0}
        '''
        # Check if there is data matching the content name in ps
        self.ps = ps
        for i in range(len(self.ps)):
            if content_name == self.ps[i]:
                return True
        # No data for content name found in ps
        return False


if __name__ == '__main__':
    # PS_search_interest(inface='r0', interest=['i0', 'c0', 'r0', 'r1/1', 10., 100.])
    # ps = PS(route_num=12, content_num=100)
    # ps.PS_init()
    print('PS')
