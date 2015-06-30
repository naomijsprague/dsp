# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:36:44 2015

@author: naomi
"""

list_pounds = [25,150,300,2000,5000]

def to_kg(pounds, logp):
    #print list_pounds
    list_kg = []
    for i in pounds:
        
        if logp ==1 :
            print
            print i
        list_kg.append(i/2.2046)
        
        if logp == 1:
            print pounds
            print "list_kg:", list_kg
    return list_kg
    
#print list_pounds
print to_kg(list_pounds, 0)

S = [x**2 for x in range(10)]

print S

also_kg = [x/2.2046 for x in list_pounds]
print also_kg
#-----------------------------------------------------------------------------
##map

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temperature = (36.5, 37, 37.5,39)

F = map(fahrenheit, temperature)
C = map(celsius, F)

def pounds(dollars):
    return dollars/1.57
def dollars(pounds):
    return pounds/0.64
    
prices_pounds = (1.25, 20.0, 30.0, 50.0)

prices_dollars = map(dollars,prices_pounds)
print prices_dollars

#-----------------------------------------------------------------------------
##filter

fib = [0,1,1,2,3,5,8,13,21,34,55]
print fib
result = filter(lambda x: x % 2, fib)
print result

result = filter(lambda x: x % 2 == 0, fib)
print result

# my example of Filter
roster = ('Fred', 'Anne', 'George', 'Arthur', 'Catherine', 'Amy', 'Elizabeth')
print roster

print len(roster)

short_names = filter(lambda x: len(x)<=4, roster)

print short_names
print len(short_names)