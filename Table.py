from __future__ import print_function

"""
######  Format definition  ######
Route_ID = 'r0' 'r1'...
Consumer_ID =  'c0' 'c1'...
Interest_ID =  'i0' 'i1'...
Content_name = 'route_ID/0-100'.  example: 'r0/0'

######  Global table  ###### 
# Network router link
Network = [['route_ID', ['route_ID', ...]],
           ...
          ]
# 1200 content names
Content_table = [content_name, ...]
# Interest packets sent by consumer
Requerst_table = {'consumer_ID': [interest_ID, interest_ID, ...],
                  ...
                 }
# Interest packets received by router
Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...],
                  ...
                 }
# Data packets received by router
Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time], ...],
              ...
             }
# Quene_interest = {'route_ID':[]}
# Quene_data = {'route_ID':[]}
# Unique content name generated by producer
PS = {'route_ID': [content_name, ...],
      ...
     }
# Cache content information in the router's' CS
CS = {'route_ID': [[content_name, cost, record_time], ...],
      ...
     }
# Information recorded in the router's PIT 
PIT = {'route_ID': [[content_name,[inface, ...],[outface, ...]], ...],
       ...
      }
# Information recorded in the router's FIB
FIB = {'route_ID': [[content_name,[inface, ...],[outface, ...]], ...],
       ...
      }

######  Table for each router  ######
interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
ps = [content_name, ...]
pit = [[content_name,[inface, ...],[outface, ...]], ...]      
cs = [[content_name, cost, record_time], ...]      
fib = [[content_name,[inface, ...],[outface, ...]], ...]

"""
######  Global table  ######
# Network router link
Network = []
# 1200 content names
Content_table = []
# Interest packets sent by consumer
Requerst_table = {}
# Interest packets received by router
Interest_table = {}
# Data packets received by router
Data_table = {}
# Quene_interest = {'route_ID':[]}
# Quene_data = {'route_ID':[]}
# Unique content name generated by producer
PS = {}
# Cache content information in the router's' CS
CS = {}
# Information recorded in the router's PIT
PIT = {}
# Information recorded in the router's FIB
FIB = {}

