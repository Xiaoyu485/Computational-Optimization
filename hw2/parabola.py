# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:56:41 2016

@author: Xiaoyu
"""

import scipy;
import matplotlib
import matplotlib.pylab
import numpy


class Parabola:
    def __init__(self,alpha,center=0):
        self.alpha = alpha;
        self.center = center;
    
    def feval(self,x):
        mini = numpy.subtract(x,self.center);
        mini = mini**2
        fval = numpy.dot(self.alpha,mini)
        return fval
    
    def seval(self,x,ndata=None):
        fval = numpy.dot(self.alpha,numpy.subtract(x, self.center)**2)
        return fval
          
    def grad(self,x):
        gvalue = 2*numpy.multiply(self.alpha,numpy.subtract(x, self.center))
        print numpy.size(gvalue)
        return gvalue
    
    def sgrad(self,x,ndata=None):
        n = numpy.size(x)
        a = numpy.zeros(n)
        direct = numpy.random.randint(0,n,1)
        a[direct] = 1
        sgrad  = a*numpy.transpose(self.grad(x))
        return sgrad

class ParabolaDir(Parabola):
    def sgrad(self,x,ndata=None):
        size = numpy.size(x)
        direction = numpy.random.randint(2,size=size)
        sgrad  = direction*numpy.transpose(self.grad(x))
        return sgrad