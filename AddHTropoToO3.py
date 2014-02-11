# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:23:02 2014

@author: Администратор


"""


import netCDF4 as ncdf
import numpy as np
import glob


def main(O3File, MeteoMask):
#    
#    

    #If a file with data on ozone profiles already contains information on the 
    #height of the tropopause - just updated it, otherwise - create a new variable.
    FO3 = ncdf.Dataset(O3File,'r+')
    FMeteo = ncdf.MFDataset(MeteoMask)
    
    if not 'HTropo' in FO3.variables:
        var=FO3.createVariable('HTropo','float32',('Time',), zlib=True, complevel=9, fill_value=np.nan)
        var.units = 'm.'
        var.description = 'Height of the tropopause.'
    else:
        var=FO3.variables['HTropo']
    
    TimeO3 = FO3.variables['Time']
    TimeMet = ncdf.MFTime(FMeteo.variables['Time'])
    
    dtTimeO3 = ncdf.num2date(TimeO3, TimeO3.units, TimeO3.calendar)
    idxMet = ncdf.date2index(dtTimeO3, TimeMet, calendar=TimeMet.calendar, select='nearest')
    HTropo = FMeteo.variables['HTropo'][idxMet,0]
    
    var[...] = HTropo
    
    
    
    FO3.close()
    FMeteo.close()
    return 0
    
    
if __name__ == '__main__':
    O3Mask = r'd:\disks\1TB\#data#\#LIDAR#\#ozone#\O3ProcessedData\b*.nc'
    MeteoMask = r'd:\disks\1TB\#data#\#METEO#\nc\#31977\*.nc3'
    filesO3 = glob.glob(O3Mask)
    
    for item in filesO3:
        print(item)
        main(item, MeteoMask)
    