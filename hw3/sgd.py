# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:52:41 2016

@author: Shaw
"""
import scipy
import numpy
import matplotlib
import matplotlib.pylab as pylab
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
import parabola


class SGD:
    def __init__(self,x0,alpha,center,proj=None,histsize = -1,smallhist=False,ndata=100,keepobj=True):
#        self.afunc = parabola.Parabola(alpha, center)
        self.afunc = parabola.ParabolaDir(alpha, center)
        self.x0 = x0
        self.center = center
        self.dim = numpy.size(x0);        
        self.sgrad = self.afunc.sgrad(x0)
        self.feval = []
        self.feval.append(self.afunc.feval(x0))
        self.seval = self.afunc.seval(x0)
        self.n = 1
        self.sfunc = self.step_size(0.8,self.n,0.7)
        self.setStart(x0)
    
    def step_size(self,gamma,n,start=1):
        size = start / (self.n**gamma)
        return size
        
    def setStart(self,x0):
        self.x = x0
        self.hist=[]
        self.hist.append(x0)
#       
#    def reset(self):
#        self.x = self.x0
#    
    def dostep(self):
        stepsize = self.sfunc
        self.x = self.x - stepsize*(self.sgrad)
        self.n=self.n+1
        self.hist.append(self.x.tolist())
        self.feval.append(self.afunc.feval(self.x))
        self.sgrad = self.afunc.sgrad(self.x)
        self.sfunc = self.step_size(0.8,self.n,0.7)
    
    def nsteps(self,an = 1):
        for i in range(an):
            self.dostep()

    def getAvgSoln(self,wsize=10):
        points = self.feval[-wsize:-1]
        avg_sol = numpy.average(points)
        return avg_sol
    
    def getSoln(self,wsize=10,winterval=1,abstol=1e-6,reltol=1e-6):
        self.nsteps(wsize*(winterval+1))
        cri=1
        while cri == 1:
            self.dostep()
            if numpy.absolute(self.getAvgSoln(wsize) - self.getAvgSoln((wsize*(winterval+1))))<=abstol:
                cri=0
        return self.feval[-1]
         
    def plot(self,fname=None,n=100,alphaMult=1,axis=None):
        plot_point = numpy.asarray(self.hist[-n+1:-1])
        if self.dim == 1:
            val = 0
            points = plot_point.take([0],axis=1)
            pyplot.plot(points, numpy.zeros_like(points)+val,'.')
            pyplot.show()
        elif self.dim == 2:
            x = plot_point.take([0],axis=1)
            y = plot_point.take([1],axis=1)
            cmap,norm=matplotlib.colors.from_levels_and_colors(numpy.linspace(0, max(self.feval),4),['red','blue','green'])
            pyplot.plot(x,y,'.')
            pyplot.show()
        else:
            x = plot_point.take([0], axis=1)
            y = plot_point.take([1],axis=1)
            z = plot_point.take([2],axis=1)
            fig = pyplot.figure()
            col = x-y
            ax = fig.add_subplot(111)
            ax = pyplot.axes(projection='3d')
            ax.scatter(x,y,z,'.',s=8,c=col,cmap=matplotlib.cm.Blues,label='SGD')
            ax.scatter(self.center[0],self.center[1],self.center[2],'.',c='red',s=22,label='Center Point')
            pyplot.show()
        
        