#!/usr/bin/env python3
 
import sys
 
#Variables that keep track of the keys.


#Do not add anything above this line. The one
#exception is that you can add import statements.

counts = {}

for line in sys.stdin:
        key, value = line.split('\t')
        key = ''.join(sorted(key))
        counts[key] = counts.get(key, 0) + int(value)
        
for key, value in counts.items():
     print("{}: {}".format(key, counts[key]))
      
