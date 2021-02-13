#!/usr/bin/env python3.6

import sys
 
line = sys.stdin.readline()

while line:
    current_person, connections = line.split(":"):
                                      
        output=  current_person  +"\t" + connections
        print(output)       
    line = sys.stdin.readline()    
