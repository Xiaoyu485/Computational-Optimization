# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 17:31:46 2016

@author: Shaw
"""

##Homework 1


import numpy as nm
import matplotlib as mat 
import matplotlib.pylab as pyl
a = nm.array([nm.arange(20)]*20)
b = nm.transpose(a)

Val = nm.zeros((20,20))

Val = nm.sqrt(a**2+b**2)

fig = pyl.figure(figsize=(10,10))
ax = fig.add_subplot(321)
ax.set_xlabel('(a) Distance from (0,0), with imshow defaults',fontsize=8)
ax.imshow(Val)
ax2 = fig.add_subplot(322)
ax2.set_xlabel('(b) Distance from (0,0), play with interpolation',fontsize=8)
ax2.imshow(Val,interpolation='nearest')
Val2=nm.sqrt((a-5)**2+(b-5)**2)

ax3 = fig.add_subplot(323)
ax3.set_xlabel('(c) Distance from (5,5)',fontsize=8)
ax3.imshow(Val2,interpolation='nearest')

ax4 = fig.add_subplot(324)
ax4.set_xlabel('(d) Distance from (5,5), play with interpolation and cmap',fontsize=8)
cmap=mat.cm.hot_r
ax4.imshow(Val2,interpolation='bicubic',cmap=cmap)

def val3():
    points = input('Input points: \n')
    Val3 = nm.sqrt((a-points[0][0])**2+((b-points[0][1])**2))    
    for m in range(len(points)):
         Val3 = nm.minimum(Val3,nm.sqrt((a-points[m][0])**2+((b-points[m][1])**2)))
    return Val3
    
Val3 = val3();           
ax5 = fig.add_subplot(325)
ax5.set_xlabel('(e) Distance from ((0,0), (5,5), (19,19), (19,0), (0,19))',fontsize=8)
ax5.imshow(Val3,cmap=cmap)
ax6 = fig.add_subplot(326)
ax6.set_xlabel('(e) Distance from ((0,0), (5,5), (19,19), (19,0), (0,19))',fontsize=8)
ax6.imshow(Val3,interpolation='nearest',cmap=cmap)



fig2 = pyl.figure()
ax7 = fig2.add_subplot(111)
ax7.set_xlabel('X coord', fontsize=10)
ax7.set_ylabel('Y coord',fontsize=10)
ax7.set_title('Distance to Closest Point')
img=ax7.imshow(Val3,interpolation='nearest',cmap=cmap)
pyl.colorbar(img)
pyl.show()
