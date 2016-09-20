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
        self.n = 1;
    
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
#        a = scipy.randn(1000,n)
        sgrad  = a*numpy.transpose(self.grad(x))
#        sgrad = numpy.sum(sgrad,axis=0)
        return sgrad
        
    def step_size(self,gamma,start=1):
        self.n=self.n+1
        size = start / (self.n**gamma)
        return size

class ParabolaDir(Parabola):
    def sgrad(self,x,ndata=None):
        size = numpy.size(x)
        direction = numpy.random.randint(2,size=size)
        sgrad  = direction*numpy.transpose(self.grad(x))
        return sgrad
    
    

#def step_size(gamma,start=1,n):
#        size = start / (n**gamma)
#        return size
#
#afunc = Parabola([1,2,3,4],[0,0,0,0])
#class SGD:
#    def __init__(self,afunc,x0,sfunc,proj=None,histsize = -1,smallhist=False,ndata=100,keepobj=True):
#        self.sgrad = afunc.sgrad(x0)
#        self.hist=x0
#        self.x = x0
#        self.feval = afunc.feval(x0)
#        self.seval = afunc.seval(x0)
#        self.par = p
#        self.n = 1;
#        
#        
#    def setStart(self,x0):
#        self.x = x0
#        self.hist = x0
##       
##    def reset(self):
##        self.x = self.x0
##    
#    def dostep(self):
#        stepsize = self.step_size(0.6,0.8)
#        self.x = self.x - stepsize*(self.sgrad)
#        self.hist.append(self.x)
#        
        
#        
#
#    
#    def nsteps(self, an = 1):
#    
#    def getAvgSoln(self, wsize=10):
#    
#    def getSoln(self,wsize=10,winterval=10,abstol = 1e-6, reltol=1e-6):
#    
#    def plot(self, fname=None, n=100, alphaMult=1, axis=None):
    
    
        
        