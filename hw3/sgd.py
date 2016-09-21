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
        x0 = numpy.array(x0)
        self.afunc = parabola.Parabola(alpha, center)
        self.x0 = x0
        self.center = center
        self.dim = numpy.size(x0[0]);    
        self.sgrad = self.afunc.sgrad(x0)
        self.feval = []
        self.feval.append(self.afunc.feval(x0))
        self.seval = self.afunc.seval(x0)
        self.n = 1
        self.sfunc = self.step_size(0.8,self.n,4)
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
        self.sfunc = self.step_size(0.8,self.n,4)
    
    def nsteps(self,an = 1):
        for i in range(an):
            self.dostep()

    def getAvgSoln(self,wsize=10):
        points = self.feval[-wsize:-1]
        avg_sol = numpy.average(points)
        return avg_sol
    
    def getSoln(self,wsize=10,winterval=1,abstol=1e-6,reltol=1e-6):
        cri=1
        while cri == 1:
            self.nsteps(wsize*(winterval+1))
            if numpy.absolute(self.getAvgSoln(wsize) - self.getAvgSoln((wsize*(winterval+1))))<=abstol:
                cri=0
        return self.feval[-1]
         
    def plot(self,fname=None,n=100,alphaMult=1,axis=None):
        
        ndata = numpy.size(self.x0)/numpy.size(self.x0[0])
        starta = 0
        end = 0
        while end==0:
            if self.dim == 1:

                for i in range(ndata):                
                    val = 0
                    plot_point = numpy.asarray(self.hist[starta:min(numpy.size(self.hist),starta+n)])
                    points = plot_point.take([i],axis=1)
                    points = points.tolist()
                    x=[]
                    c=['red','yellow','green','k']
                    for m in points:
                        x.append(m[0][0])
                    pyplot.scatter(self.center[0], 0,c='red',s=130)
                    pyplot.scatter(x, numpy.zeros_like(x)+val)
                    starta = starta+n
                    if starta >= numpy.size(self.hist)/ndata:
                        end = 1
                pyplot.savefig('dim1_point'+str(i)+str(starta)+'.png',format='png')
                pyplot.clf()
            elif self.dim == 2:
                for i in range(ndata):
                    plot_point = numpy.asarray(self.hist[starta:min(numpy.size(self.hist),starta+n)])
                    points = plot_point.take([i],axis=1)
                    points = points.tolist()
                    x = []
                    y = []
                    c=['red','yellow','green','k']
                    for m in points:
                        x.append(m[0][0])
                        y.append(m[0][1])
                    s=numpy.sqrt((numpy.asarray(x)-self.center[0])**2+(numpy.asarray(y)-self.center[1])**2)
                    pyplot.scatter(x,y,s=s,c=s)
                    pyplot.scatter(self.center[0],self.center[1],s=40,c='red',label='Center')                    
                    pyplot.annotate('Center',xy=(self.center[0],self.center[1]),xytext=(0,+0.2))
                    starta = starta+n
                    if starta >= numpy.size(self.hist)/ndata:
                        end = 1
                pyplot.savefig('dim2_point'+str(i)+str(starta)+'.png',format='png')
                pyplot.clf()
            else:
                fig = pyplot.figure()
                for i in range(ndata):
                    plot_point = numpy.asarray(self.hist[starta:min(numpy.size(self.hist)/(numpy.size(x0)),starta+n)])
                    points = plot_point.take([i],axis=1)
                    points = points.tolist()
                    x = []
                    y = []
                    z = []
                    c=['red','yellow','green','k']
                    for m in points:
                        x.append(m[0][0])
                        y.append(m[0][1])
                        z.append(m[0][2])
#                    plot = ndata*10+100+i+1
                    ax = fig.add_subplot(111, projection='3d')                
                    ax.scatter(x,y,z)
                    ax.scatter(self.center[0],self.center[1],self.center[2],s=40,marker='o')
#                    ax.scatter(x[-1],y[-1],z[-1],'*',s=20)
                    ax.text(self.center[0],self.center[1],self.center[2],'Center',color='red')
                    starta = starta+n
                    if starta >= numpy.size(self.hist)/(numpy.size(self.x0)):
                        end = 1
                pyplot.savefig('dim3_point'+str(i)+str(starta)+'.png',format='png')
                pyplot.clf()
#            
#
        
        
        
        
#       
#        elif self.dim == 2:
#            for i in range(ndata):
#                points = plot_point.take(i,axis=1)
#                x = points.take([0],axis=1)
#                y = points.take([1],axis=1)
#                s=numpy.sqrt((x-self.center[0])**2+(y-self.center[1])**2)
#                pyplot.scatter(x,y,s=s,c=s)
#                pyplot.scatter(x[0],y[0],s=40,marker='*')
#                pyplot.scatter(self.center[0],self.center[1],s=40,c='red',label='Center')
#                pyplot.annotate('Center',xy=(self.center[0],self.center[1]),xytext=(0,+0.2))
#            pyplot.show()
#        else:
#            fig = pyplot.figure()
#            
#            
#            for i in range(ndata):
#                points = plot_point.take([i][0],axis=1)
#                x = points.take([0],axis=1)
#                y = points.take([1],axis=1)
#                z = points.take([2],axis=1)
#                plot = ndata*10+100+i+1
#                ax = fig.add_subplot(plot,projection='3d')                
#                ax.scatter(x,y,z)
#                ax.scatter(self.center[0],self.center[1],self.center[2],s=40,marker='o')
#                ax.scatter(x[-1],y[-1],z[-1],'*',s=20)
#                ax.text(self.center[0],self.center[1],self.center[2],'Center',color='red')
#            pyplot.show()
#            
#
#            
#        
#        