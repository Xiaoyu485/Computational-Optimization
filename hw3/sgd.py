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
        self.n = 1
        self.sfunc = self.step_size(0.9,self.n,1)
        self.setStart(x0)
    
    def step_size(self,gamma,n,start=1):
        size = start / (self.n**gamma)
        return size
        
    def setStart(self,x0):
        self.x = x0
        self.hist=[]
        self.hist.append(x0)
#       
    def reset(self):
        self.sgrad = self.afunc.sgrad(self.x0)
        self.hist.append(self.x0)
        self.feval = []
        self.feval.append(self.afunc.feval(self.x0))
        self.n = 1
        self.sfunc = self.step_size(0.9,self.n,1)
        self.setStart(self.x0)
        
    def dostep(self):
        stepsize = self.sfunc
        self.x = self.x - stepsize*(self.sgrad)
        self.n=self.n+1
        self.hist.append(self.x.tolist())
        self.feval.append(self.afunc.feval(self.x))
        self.sgrad = self.afunc.sgrad(self.x)
        self.sfunc = self.step_size(0.9,self.n,1)
    
    def nsteps(self,an = 1):
        for i in range(an):
            self.dostep()

    def getAvgSoln(self,wsize=10):
        points = self.feval[-wsize:-1]
        avg_sol = numpy.average(points)
        return avg_sol
    
    def getSoln(self,wsize=10,winterval=1,abstol=1e-6,reltol=1e-6):
        cri=0
        while cri ==0:
            self.nsteps(wsize*(winterval+1))
            dif =numpy.absolute(self.getAvgSoln(wsize) - self.getAvgSoln((wsize*(winterval+1))))
            if dif<=abstol:
                cri=1
        return self.feval[-1]
         
    def plot(self,fname=None,n=100,alphaMult=1,axis=None):
        
        ndata = numpy.size(self.x0)/numpy.size(self.x0[0])
        starta = 0
        end = 0
        while end==0:
            end=1
            if self.dim == 1:
                starta = 0
                xlow = min([row[0] for row in self.x0])
                xlow = min(xlow,self.center[0])
                xmax = max([row[0] for row in self.x0])
                xmax = max(xmax,self.center[0])
                while starta<=numpy.size(self.hist)/(ndata*self.dim):
                    fig = pyplot.figure()
                    ax=fig.add_subplot(111)
                    ax.set_xlim(xlow-1,xmax+1)
                    ax.set_ylim(-0.1,0.1)
                    plot_point = numpy.asarray(self.hist[starta:min(numpy.size(self.hist)/(ndata*self.dim),starta+n)])
                    for i in range(ndata):
                        vol = [row[i] for row in plot_point]
                        x = [row[0] for row in vol]
                        ax.scatter(x,numpy.zeros_like(x),s=6)
                        ax.scatter(self.center[0],0,marker = 'o',c='red')
                        ax.text(self.center[0],0,'Center',color='red')
                    pyplot.savefig('dim_1_'+'start_'+str(starta)+'.png',format='png')
                    starta = starta+(n/2)

            elif self.dim == 2:
                starta = 0
                xlow = min([row[0] for row in self.x0])
                xlow = min(xlow,self.center[0])
                xmax = max([row[0] for row in self.x0])
                xmax = max(xmax,self.center[0])
                ylow = min([row[1] for row in self.x0])
                ylow = min(ylow,self.center[1])
                ymax = max([row[1] for row in self.x0])
                ymax = max(ymax,self.center[1])
                c = ['red','blue','k','purple']
                while starta<=numpy.size(self.hist)/(ndata*self.dim):
                    fig = pyplot.figure()
                    ax=fig.add_subplot(111)
                    ax.set_xlim(xlow-1,xmax+1)
                    ax.set_ylim(ylow-1,ymax+1)                    
                    plot_point = numpy.asarray(self.hist[starta:min(numpy.size(self.hist)/(ndata*self.dim),starta+n)])
                    for i in range(ndata):
                        vol = [row[i] for row in plot_point]
                        x = [row[0] for row in vol]
                        y = [row[1] for row in vol]
                        ax.plot(x,y,lw=1)
                        ax.scatter(self.center[0],self.center[1],s=60,c=c[i])
                        ax.text(self.center[0],self.center[1],'Center',color='red')
                    pyplot.savefig('test5_dim_2_'+'start_'+str(starta)+'.png',format='png')
                    pyplot.close(fig)
                    starta = starta+(n/2)
               
            else:
                starta = 0
                xlow = min([row[0] for row in self.x0])
                xlow = min(xlow,self.center[0])
                xmax = max([row[0] for row in self.x0])
                xmax = max(xmax,self.center[0])
                ylow = min([row[1] for row in self.x0])
                ylow = min(ylow,self.center[1])
                ymax = max([row[1] for row in self.x0])
                ymax = max(ymax,self.center[1])
                zlow = min([row[2] for row in self.x0])
                zlow = min(zlow,self.center[2])
                zmax = max([row[2] for row in self.x0])
                zmax = max(zmax,self.center[2])
                while starta<=numpy.size(self.hist)/(ndata*self.dim):
                    fig = pyplot.figure()
                    ax=fig.add_subplot(111,projection='3d')
                    ax.set_xlim(xlow-1,xmax+1)
                    ax.set_ylim(ylow-1,ymax+1)
                    ax.set_zlim(zlow-1,zmax+1)
                    plot_point = numpy.asarray(self.hist[starta:min(numpy.size(self.hist)/(ndata*self.dim),starta+n)])
                    for i in range(ndata):
                        vol = [row[i] for row in plot_point]
                        x = [row[0] for row in vol]
                        y = [row[1] for row in vol]
                        z = [row[2] for row in vol]
                        
                        ax.plot(x,y,z,'<-',lw=2,c='k',ms=3)
                        ax.scatter(self.center[0],self.center[1],self.center[2],'o',s=60,c='red')
#                        ax.text(self.center[0],self.center[1],self.center[2],'Center',color='red')
                    pyplot.savefig('t4dim_3_'+'start_'+str(starta)+'.png',format='png')
                    pyplot.close(fig)
                    starta = starta+(n/2)


#
#
#                for i in range(ndata):                
#                    val = 0
#                    plot_point = numpy.asarray(self.hist[starta:min(numpy.size(self.hist),starta+n)])
#                    points = plot_point.take([i],axis=1)
#                    points = points.tolist()
#                    x=[]
#                    c=['red','yellow','green','k']
#                    for m in points:
#                        x.append(m[0][0])
#                    pyplot.scatter(self.center[0], 0,c='red',s=130)
#                    pyplot.scatter(x, numpy.zeros_like(x)+val)
#                    starta = starta+n
#                    if starta >= numpy.size(self.hist)/ndata:
#                        end = 1
#                pyplot.savefig('dim1_point'+str(i)+str(starta)+'.png',format='png')
#                pyplot.clf()
# for i in range(ndata):
#                    plot_point = numpy.asarray(self.hist[starta:min(numpy.size(self.hist),starta+n)])
#                    points = plot_point.take([i],axis=1)
#                    points = points.tolist()
#                    x = []
#                    y = []
#                    c=['red','yellow','green','k']
#                    for m in points:
#                        x.append(m[0][0])
#                        y.append(m[0][1])
#                    s=numpy.sqrt((numpy.asarray(x)-self.center[0])**2+(numpy.asarray(y)-self.center[1])**2)
#                    pyplot.scatter(x,y,s=s,c=s)
#                    pyplot.scatter(self.center[0],self.center[1],s=40,c='red',label='Center')                    
#                    pyplot.annotate('Center',xy=(self.center[0],self.center[1]),xytext=(0,+0.2))
#                    starta = starta+n
#                    if starta >= numpy.size(self.hist)/ndata:
#                        end = 1
#                pyplot.savefig('dim2_point'+str(i)+str(starta)+'.png',format='png')
#                pyplot.clf()