#!/usr/bin/env python3


import sys
from collections import Counter


 
#Variables that keep track of the keys.


#Do not add anything above this line. The one
#exception is that you can add import statements.

dict_in = {}
dup_free = []
final_dict = {}
for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        value = value.split(',')
        value = [int(i) for i in value]
        dict_in[key] =value
#print('dict_in = ',dict_in)            

dict_out = {}
for key in dict_in: 

#   print('key in =', key)
   for k,v in dict_in.items():
#       print('k =',k)
#       print('v =',v)     
       for y in v:  
           if (int(key) in v) and (y != int(key)) and (y not in dict_in[key]):
              dict_out.setdefault(int(key), []).append(y)

print('dict_out =',dict_out)

conxn_out = list(dict_out.items())


connect_cnt = [(i, dict(Counter(l))) for i, l in conxn_out]



network  = []
for i in connect_cnt:
    d = {}
    for j in i[1].keys():
        if i[1][j] > 1:
             d[j] = i[1][j]
    network.append((i[0],d))





output = {}
for name, connections in network:
    # If we've not added this name yet, create a blank entry:
    if name not in output:
        output[name] = {'probably': [], 'might': []}
    
    # Now loop through the connected people and add to the correct list:
    for other_name, mutuals in connections.items():
        if mutuals > 3:
            output[name]['probably'].append(other_name)
        else:
            output[name]['might'].append(other_name)
  





for name, contents in sorted(output.items()):
    might = ', '.join([str(i) for i in sorted(contents['might'])])
    probably = ', '.join([str(i) for i in sorted(contents['probably'])])
    if len(probably) > 0 and len(might) > 0:  
        print(f'{name}',f'Might:{might}', f'Probably:{probably}')
    elif len(probably) == 0 and len(might) > 0:  
        print(f'{name}',f'Might:{might}')
    elif len(probably) > 0 and len(might) == 0:
         print(f'{name}',f'Probably:{probably}')

# might = ', '.join([str(i) for i in sorted(contents['might'])])
# print(f'\tMight know: {might}')

#probably = ', '.join([str(i) for i in sorted(contents['probably'])])
   
# print(f'\tProbably knows: {probably}')


   



   







#   print(name)
      







 





















                          




        



   
        
      


         
        
