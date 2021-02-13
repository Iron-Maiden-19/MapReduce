#!/usr/bin/env python

import sys	

linect = 0
line = sys.stdin.readline()
linect += 1
#set linect = 1 and when linect = 1 read next line.this skips header
if linect == 1:
    line = sys.stdin.readline()

while line:
#Do something with line here to create/output
        
        line = line.strip()
        x = len(line)
        if x > 0:
       
            line = line.split(",")
            invoiceNo = line[0]
             
#if 1st char of invoiceNo = 'C' then read  next line
            if invoiceNo[0] == 'C':
             
                line = sys.stdin.readline()
                continue
            
            custId = line[6]
#if custId is blank do not process and read next line 
            if custId == '':
                line = sys.stdin.readline()
                continue
   	 
            quantity  = line[3]     
            quantity = int(quantity) 
            InvDate = line[4]
            month1 = InvDate.split('/')
            month = month1[0]    
            price = line[5]
            price = float(price)          
            amount = quantity *  price
            Country = line[7]	
#output line with Country, custId and month as key separated by ':' and amount is value separated from key by tab
            
#    	    output = str(Country) +":"+str(custId)+":"+str(month)+"\t"+str(amount)
            output = str(month.zfill(2)) + "," +str(Country)+":"+str(custId)+"\t"+str(amount)
            print(output)
            
            line = sys.stdin.readline()

