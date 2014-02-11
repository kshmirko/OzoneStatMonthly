# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:29:12 2014

@author: Администратор

Generates file with monthly statistics of ozone vertical distribution 
for the period from 2007 to 2013.
"""

import pandas as pds
import netCDF4 as ncdf
import numpy as np
import pylab as plt

#Lambda-functions to filter data
Year = lambda x: x.year
Month= lambda x: x.month
Day  = lambda x: x.day
YearMonth = lambda x: (x.year, x.month)


O3Mask = r'd:\disks\1TB\#data#\#LIDAR#\#ozone#\O3ProcessedData\b*tropo.nc'

FO3 = ncdf.MFDataset(O3Mask)
ncTime = ncdf.MFTime(FO3.variables['Time'])
HTropo = FO3.variables['HTropo'][...]
O3 = FO3.variables['O3'][...]
#lO3 = [O3[i] for i in range(O3.shape[0])]
Alt = FO3.variables['Alt'][...]



time = ncdf.num2date(ncTime, ncTime.units, ncTime.calendar)

dfO3 = pds.DataFrame(index=time, columns=Alt, data=O3)

statO3Mean = dfO3.groupby([Month]).mean().T
statO3Std  = dfO3.groupby([Month]).std().T


statO3Mean.plot()
statO3Std.plot()

HTropo = FO3.variables['HTropo'][...]
FO3.close()

#plt.plot(time, HTropo,'ro--', alpha=0.7, ms=9)
#plt.grid(True)
plt.show()

