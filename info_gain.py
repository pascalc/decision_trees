#!/usr/bin/env python

import dtree as d
import monkdata as m

monkset = [m.monk1, m.monk2, m.monk3]
mtrain = [m.monk1test, m.monk2test, m.monk3test]

#Assignement 1
print 'Entropy for monk1-3'
j = 1
for monk in monkset:
   #s = '\ta' + str(j++) + ': ' + str(d.entropy(monk))
   print d.entropy(monk)

#Assignement 2
attributes = [0, 0, 0]
print '\nInformation gain for attributes a1 to a6'
for i in range(0, len(monkset)):
   print 'Monk', i+1
   s = ""
   greatest = 0
   for x in range(0, 6):
       averageGain = d.averageGain(monkset[i], m.attributes[x])
       if averageGain > greatest: greatest = averageGain
       s = s + str(averageGain)+ ' '
   print s
   attributes[i] = greatest