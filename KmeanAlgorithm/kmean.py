###############################################################################################
##################################### VISHAL KULKARNI | VVK27 #################################
###############################################################################################

import sys
import random
import math

datafile = sys.argv[1]

f = open(datafile, 'r')
data = []
# i = 0
l = f.readline()

#################
### Read Data ###
#################

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))

    #    l2.append(float(1))
    data.append(l2)

    l = f.readline()

rows = len(data)
cols = len(data[0])
#print(data)

#print("rows=", rows, " cols=", cols)

f.close()
# print(data)



##################################
########## initialize m ##########
##################################