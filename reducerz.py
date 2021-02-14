#!/usr/bin/env python3


import sys
from collections import Counter
 
#Variables that keep track of the keys.


#Do not add anything above this line. The one
#exception is that you can add import statements.

dict_in = {}
dup_free = []
for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        value = value.split(',')
        value = [int(i) for i in value]
        dict_in[key] =value
            

        dict_out = {}
        for key in dict_in: 
          for k,v in dict_in.items():     
              for y in v:  
                  if int(key) in v and y != int(key):
                       dict_out.setdefault(key, []).append(y)

conxn_out = list(dict_out.items())
connect_cnt = [(i, dict(Counter(l))) for i, l in conxn_out]


print('connect_cnt = ',connect_cnt)





                          




        



   
        
      


         
        
