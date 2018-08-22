import os
import sys
import numpy
from numpy import *
import string
import math
import random
ifile = open("temp","r")
n = input("enter no of atoms:")
lam = input("enter percent Al:")
atomid = zeros(n,int)
atomtype = zeros(n,int)
x = zeros(n,float)
y = zeros(n,float)
z = zeros(n,float)
k = 0
for line in ifile:
#    print k
    items = str.split(line)
    atomid[k] = int(items[0])
    atomtype[k] = int(items[1])
    x[k] = float(items[2])
    y[k] = float(items[3])
    z[k] = float(items[4])
    k = k + 1
l = 0.
for i in range(1000*n):
    m = int(n*random.random())
#    print m,y[m]
    if (y[m] >= 10.378) and (atomtype[m] == 1):
        atomtype[m] = 3
#        print m, y[m]
        l = l + 1.
#    print round((l/48)*100.)
    if l == round(lam*48.):
        break
ofile = open("temp1","w")
for i in range(n):
    file.write(ofile, str(atomid[i]) + '  ' + str(atomtype[i]) + '  ' + str(x[i]) + '  ' + str(y[i]) + '  ' + str(z[i]) + '\n')
file.close(ifile)
file.close(ofile)
