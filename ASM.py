# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:46:27 2022

@author: crazy
"""

import timeit

str1 = input('Enter String 1: ')
str2 = input('Enter String 2: ')

'''
#Edit Distance recursive
def edDist(strA, strB):
    #base cases
    if len(strA)==0:
        return len(strB)
    elif len(strB)==0:
        return len(strA)
    #other cases
    else:
        if strA[-1] == strB[-1]:
            diff = 0
        else:
            diff = 1
        return min(edDist(strA[:-1], strB[:-1]) + diff,  #case 1 match/substitution
                   edDist(strA, strB[:-1]) + 1,          #case 2 addition/insertion
                   edDist(strA[:-1], strB) + 1)          #case 3 deletion
    
timestart = timeit.default_timer()

print(edDist(str1, str2))
print(timeit.default_timer() - timestart)
'''













'''
#Edit Distance with Dynamic Programming (Memoization)
def editDist(strA, strB):
    C = []

    for i in range(0, len(strA)):
        if i ==0:
            C.append([i for j in range(0, len(strB))])
        else:
             C.append([0 for j in range(0, len(strB))])
    for i in range (1, len(strA)):
        for j in range (1, len(strB)):
            if strA[i] == strB[j]:
                diff = 0
            else:
                diff = 1
                
            CMS = C[i-1][j-1] + diff
            CI = C[i][j-1] + 1
            CD = C[i-1][j] + 1
            
            C[i][j] = min(CMS, CI, CD)
    return C[i][j]

timestart = timeit.default_timer()

print(edDist(str1, str2))
print(timeit.default_timer() - timestart)
'''






#'''
#Edit Distance with Dynamic Programming, path added
def editDistwPath(strA, strB):
    #C = []
    
    for i in range(0, len(strA)):
        P.append(['' for j in range(0, len(strB))])
            
    for i in range(0, len(strA)):
        C.append([0 for j in range(0, len(strB))])
    
    for i in range (0, len(strA)):
        C[i][0] = i
    
    for i in range (0, len(strA)):
        for j in range (0, len(strB)):
            if strA[i] == strB[j]:
                diff = 0
            else:
                diff = 1
            if i > 0 and j > 0:
                CMS = C[i-1][j-1] + diff
                CI = C[i][j-1] + 1
                CD = C[i-1][j] + 1
                
                C[i][j] = min(CMS, CI, CD)
                if CMS < min(CI,CD):
                    P[i][j] = 'CMS'
                elif CI < min(CMS,CD):
                    P[i][j] = 'CI'
                else:
                    P[i][j] = 'CD'       
            else:
                C[i][j] = diff
    return C[i][j]

P = []
C = []
timestart = timeit.default_timer()

print(editDistwPath(str1, str2))
print(timeit.default_timer() - timestart)
#'''