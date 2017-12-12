
# -*- coding : utf-8 -*-
# usr/bin/python
# file Fisher

import numpy as np
import sys
import getopt
import re

def get_file(file1,file2):
    
    pos = [] 

    with open(file1,'rt') as f:
        for line in f:
            l = line.replace('\n','').split('\t')
            pos.append(l)
    neg = []
    with open(file2,'rt') as f:
        for line in f:
            l = line.replace('\n','').split('\t')
            neg.append(l)
    pos = np.array(pos,dtype = float)
    neg = np.array(neg,dtype = float)
    return pos,neg

def Fisher(array1,array2):
    pos = array1
    neg = array2
    
    sum_p = []
    sum_q = []
    
    n = len(pos[0])
    p = len(pos)
    q = len(neg)
    
    for i in range(n):
        sum_p.append(sum(pos[:,i:(i+1)]))
        sum_q.append(sum(neg[:,i:(i+1)]))
        
    s = np.zeros((n,n))
    d = np.zeros((n,1))
    for i in range(n):
        for j in range(n):
            s[i][j] = sum(pos[k,i] * pos[k,j] for k in range(p)) + sum(neg[k,i] * neg[k,j] for k in range(q)) - sum_p[i] * sum_p[j]/p - sum_q[i]*sum_q[j]/q
            d[i,0] = sum_p[i] / p - sum_q[i]/q
    
    # F(x1,x2,.....,xn) = c1x1 + c2x2 + ... + cnxn        
    c = np.zeros(n)
    if (np.linalg.det(s) != 0):
        for i in range(n):
            D = s.copy()
            D[:,i:(i+1)] = d 
            c[i] = np.linalg.det(D)
    # C =(p * average(y1) + q * average(y2)) / (p + q)
    y1 = 0
    y2 = 0
    for i in range(n):
        y1 += c[i] * sum_p[i] / p
        y2 += c[i] * sum_q[i] / q 
    C = (p * y1 + q * y2) / (q + p)
    
    # classification basis C and average(y1),average(v2)
    sample = sample_data
    y = 0
    for i in range(n):
        y += c[i]*sample[i]
    
    print ('Sample:  ' + str(sample))    
    if (y1>y2):
        if (y > C):
            print ('Sample belongs to positive')
        else:
            print ('Sample belongs to negative')
    else:
        if (y > C):
            print ('Sample belongs to negative')
        else :
            print ('Sample belongs to positive')
    

if __name__ == '__main__':
    
  
    
    opts , args = getopt.getopt(sys.argv[1:],['pos=','neg=','sample='])
    
    pos_file = 'data/positive.txt'
    neg_file = 'data/negative.txt'
    
    pos_array , neg_array = get_file(pos_file,neg_file)
    
    sample_data = neg_array[1]
    
    
    
    
    for op , value in opts:
        if op == '--pos':
            pos_file = value
        if op == '--neg':
            neg_file = value
        if op == '--sample':
            if value == 'n,d':
                i = int(value.split(',')[1])
                if i > len (neg_array):
                    print ( ' Index out of range')
                    exit()
                sample_data = neg_array[i]
            if value == 'n,d':
                i = int(value.split(',')[1])
                if i > len(pos_array):
                    print (' Index out of range')
                    exit()
                sample_data = pos_array[i]
                
    Fisher(pos_array,neg_array)
    
    
    
    
    
    
        