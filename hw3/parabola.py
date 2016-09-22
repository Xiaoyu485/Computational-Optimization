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
        fval = numpy.dot(mini,self.alpha)
        return fval
    
    def seval(self,x,ndata=None):
        fval = numpy.dot(numpy.subtract(x, self.center)**2,self.alpha)
        return fval
          
    def grad(self,x):
        raw = 2*numpy.multiply(numpy.subtract(x, self.center),self.alpha)
        gvalue = raw/numpy.linalg.norm(raw)
#        gvalue = gvalue/g
        return gvalue
    
    def sgrad(self,x,ndata=None):
        size = numpy.size(x[0])
        num_p = numpy.size(x)/size
        a = numpy.zeros(size)
        direct = numpy.random.randint(0,size,1)
        a[direct] = 1
        a=numpy.array([a]*num_p)
        sgrad  = a*(self.grad(x))
        return sgrad
        
    def step_size(self,gamma,start=1):
        self.n=self.n+1
        size = start / (self.n**gamma)
        return size

class ParabolaDir(Parabola):
    def sgrad(self,x,ndata=None):
        size = numpy.size(x[0])
        num_p = numpy.size(x)/size
        direction = scipy.randn(num_p,size)
#        norms = scipy.sqrt((direction*direction).sum(axis=1))
#        direction = direction/norms.reshape(num_p,1)
        direction = numpy.random.randint(2,size=size)
        direction = numpy.array([direction]*num_p)
        sgrad  = direction*(self.grad(x))
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
    
    
        
        