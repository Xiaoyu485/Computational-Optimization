# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:52:41 2016

@author: Shaw
"""
import scipy
import numpy
import matplotlib
import matplotlib.pylab
import parabola

    

afunc = parabola.Parabola([1,2,3,4],[0,0,0,0])

class SGD:
    def __init__(self,x0,proj=None,histsize = -1,smallhist=False,ndata=100,keepobj=True):
        afunc = parabola.Parabola([1,2,3,4],[0,0,0,0])        
        self.sgrad = afunc.sgrad(x0)
        self.feval = []
        self.feval.append(afunc.feval(x0))
        self.seval = afunc.seval(x0)
        self.n = 1
        self.sfunc = self.step_size(0.8,self.n,0.7)
        self.setStart(x0)
    
    def step_size(self,gamma,n,start=1):
        size = start / (self.n**gamma)
        return size
        
    def setStart(self,x0):
        self.x = x0
        self.hist = x0
#       
#    def reset(self):
#        self.x = self.x0
#    
    def dostep(self):
        stepsize = self.sfunc
        self.x = self.x - stepsize*(self.sgrad)
        self.n=self.n+1
        self.hist.extend(self.x.tolist())
    
    def nsteps(self,an = 1):
        for i in range(an):
            self.dostep()
            self.n=self.n+1
            self.sfunc = self.step_size(0.8,self.n,0.7)
            
            