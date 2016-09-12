# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:48:50 2016

@author: Xiaoyu
"""

import geoplotter
import pandas
import scipy
import pylab
import matplotlib




class geological:
    
    def worldplot(self):
          g = geoplotter.GeoPlotter()
          g.clear()
          g.drawWorld();
          
    def readdata(self,filename):
        df = pandas.read_csv(filename)
        return df

    def pullout(self, yearnum, COW):
        df = self.readdata('NMC_v4_0.csv')
        cinc = df[df.year == yearnum][df.ccode==COW].cinc
        return cinc
    
    def COWs(self):
        df = self.readdata('NMC_v4_0.csv')
        COW = df.ccode
        COW = COW.drop_duplicates(keep = 'first')
        return COW
        
    def shapefile(self,filename,code):
        g = geoplotter.GeoPlotter()
        g.readShapefile(filename,'geodata')
        g.clear()
        g.drawWorld()
        usa = []        
        for i in scipy.arange(len(g.m.geodata_info)):
            if g.m.geodata_info[i]['COWCODE'] == code:
               usa.append(i)
        g.drawShapes('geodata', usa, edgecolor = 'red', facecolor = 'red', lw=1)         
        pylab.show();
        
class MilexPlotter:
    
    def __init__(self):
        csv_read = geological()
        self.CINC_df = csv_read.readdata('NMC_v4_0.csv')
        self.g = geoplotter.GeoPlotter()
        self.g.readShapefile('cshapes', 'geodata')
        self.ShapePolygon = self.g.m.geodata
        self.ShapeInfo = self.g.m.geodata_info
    
    def drawWorld(self):
        self.g.clear()
        self.g.drawMapBoundary()
        self.g.fillContinents(color = 'blue')
        self.g.drawCoastLines(linewidth=0.7)
        self.g.drawCountries(linewidth=1.5)
        self.g.drawStates(linewidth=0.7)
        
    def plotCountry(self, code, **kwargs):
        defaults = dict(edgecolor = 'red', facecolor = 'orange', lw=0) 
        defaults.update(kwargs)
        country = []        
        for i in scipy.arange(len(self.ShapeInfo)):
            if self.ShapeInfo[i]['COWCODE'] == code:
               country.append(i)
        self.g.drawShapes('geodata', country, **defaults) 
    
    def plotYear(self,year):
        self.drawWorld()
        self.g.clear()
        self.drawWorld()
        geo = geological()
        cows = geo.COWs()
        cows = pandas.Series.tolist(cows)
        notnull = []
        CINC = []
        for i in scipy.arange(len(cows)):
            if not(self.CINC_df[self.CINC_df.ccode == cows[i]][self.CINC_df.year == year].cinc is None) and (len(pandas.Series.tolist(self.CINC_df[self.CINC_df.ccode == cows[i]][self.CINC_df.year == year].cinc))>=1):                
                CINC.append(pandas.Series.tolist(self.CINC_df[self.CINC_df.ccode == cows[i]][self.CINC_df.year == year].cinc)[0])
                notnull.append(cows[i])
        maxCINC = max(CINC)
        norm = matplotlib.colors.Normalize(vmin=0,vmax=maxCINC)
        cmap = matplotlib.cm.hot
        color = matplotlib.cm.ScalarMappable(norm = norm, cmap = cmap)
        for c in notnull:
            cinc = self.CINC_df[self.CINC_df.ccode == c][self.CINC_df.year == year].cinc
            cinc = pandas.Series.tolist(cinc)[0]
            colorcode = color.to_rgba(cinc)          
            self.plotCountry(c, facecolor = colorcode, edgecolor = colorcode,lw=3)    

    
    def plotall(self):
        year = (self.CINC_df.year)
        year = year.drop_duplicates(keep = 'first')
        year = pandas.Series.tolist(year)
        for i in year:
            self.plotYear(i)
            self.g.savefig('F:\Study\Computational Optimization\World CINC png\HW2figure'+str(i), dpi=None, facecolor = 'w',edgecolor = 'black', orientation = 'portrait',
                            papertype = None, format = None, transparent = False, bbox_inches = None, pad_inches = 0.1, frameon = None)
                            
        
        
        
    

