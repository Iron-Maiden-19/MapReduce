#!/usr/bin/env python3.6
 
import sys
 
#Variables that keep track of the keys.
current_key_being_processed = None

#Do not add anything above this line. The one
#exception is that you can add import statements.

#You can create any global variables you want here that you will use per key.
#For example, we can create a dictionary variable called temp and/or set a variable to 0:
#temp = {}
#temp_num = 0
#However, we must reset these once a new key is found, see below.

next_key_found = None
cust_dictionary = {}
cust_total = 0

for line in sys.stdin:
  line = line.strip()
  next_key_found, value = line.split('\t')
  if current_key_being_processed == next_key_found:
    #The next key read in is the same one we've been processing. 
    #You'll likely want to add some code here.
     cust_total = float(cust_total) + float(value)
     cust_total = round(cust_total) 
     
    
  else:
    #One of two things happened here:
    #1. The first key was found.
    #2. A new key was found.

    if current_key_being_processed:
      #2. happened, a new key was found.
      #Output something based on the (key,value) pairs that 
      #we have just seen where all of them had the same key.
     
     
               
      cust_dictionary[current_key_being_processed] = float(cust_total)
                      
    #end of the if statement for number 2. happening.
    #Since the next key found was a new key, we need to clear any global variables 
    #we have created right now. If we do not clear them out, our code is not stateless.
    #Therefore, we clear the dictionary and reset the variable to 0.
    cust_total = 0

    #Lastly, we set the current_key_being_processed to be the new key we just read in.
    current_key_being_processed = next_key_found
    cust_total = float(cust_total) + float(value)
    cust_total = round(cust_total,2)
    
    
        
#for loop ends here

if current_key_being_processed == next_key_found:
       cust_total = round(cust_total,2)      
       cust_dictionary[next_key_found] = float(cust_total) 

#create new_dict with new key
new_data = {}
for key, val in cust_dictionary.items():
    newkey, idnum = key.split(':')
    new_data.setdefault(newkey, []).append((val, idnum))

# Sort the values for each 'month,country' key,
# and get the IDnums corresponding to the highest values
for key, val in new_data.items():
    val = sorted(val, reverse=True)
    highest = val[0][0]
    # Collect all IDnums that have the highest value
    ids = []
    for v, idnum in val:
        if v != highest:
            break
        ids.append(idnum)
    print(key + ':' + ', '.join(ids))
        
       
       
  



   
  
