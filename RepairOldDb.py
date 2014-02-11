# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:57:07 2014

@author: Администратор
Converts to an appropriate file structure with vertical profiles of ozone.
Fixes:
* Add _FillFalue attribute 
* Add possimility for reeading data from matlab
* All profiles were interpolated on uniform grid
"""

import netCDF4 as ncdf
import numpy as np

INFILE = '2007.nc'
OUTFILE = 'b'+INFILE


ALT = np.arange(500)*240.0

F = ncdf.Dataset(INFILE, 'r+')
F1 = ncdf.Dataset(OUTFILE, 'w', format='NETCDF3_64BIT')
F1.set_fill_on()

for name in F.dimensions:
    dim = F.dimensions[name]
    print(name, len(dim), dim.isunlimited())
    if dim.isunlimited():
        F1.createDimension(name, None)
    else:
        F1.createDimension(name, len(dim))

for name in F.variables:
    var = F.variables[name]
    print(name)
    if name in ['ProfSize']:
        var1= F1.createVariable(name, var.dtype, var.dimensions, zlib=True, complevel=9, fill_value=-9999)
        var1.units='n/d'
        var1.description = 'Actual length of current profile'
        var1[...] = var[...]
    elif name in ['Alt']:
        var1= F1.createVariable(name, var.dtype, ('Length',), zlib=True, complevel=9, fill_value=np.nan)
        var1[...] = ALT
        var1.units = 'm.'
        var1.description='Altitude'
    elif name in ['Time']:
        var1= F1.createVariable(name, var.dtype, var.dimensions, zlib=True, complevel=9, fill_value=np.nan)
        var1.units = 'seconds since 2000-01-01 12:00:00'
        var1.calendar = 'gregorian'
        var1[...]=var[...]
    elif name in ['O3Du']:
        var1= F1.createVariable(name, var.dtype, var.dimensions, zlib=True, complevel=9, fill_value=np.nan)
        var1.units = 'Dobson Units'
        var1.description = 'Total Ozone Content in DU'
        var1[...]=var[...]
    elif name in ['BAer']:
        var1= F1.createVariable(name, var.dtype, var.dimensions, zlib=True, complevel=9, fill_value=np.nan)
        var1.units = 'sr^-1'
        var1.description = 'Columnar Backscatring coefficient'
        var1[...]=var[...]
    else:
        var1= F1.createVariable(name, var.dtype, var.dimensions, zlib=True, complevel=9, fill_value=np.nan)

        atts = var.ncattrs()
    
        for attrname in atts:
            var1.setncattr(attrname, var.getncattr(attrname))
            
    
        tmp = var[...]
        if var.dtype==np.float32:
            tmp[tmp>9.9e+36] = np.nan
            
        
        
        var1[...]=tmp[...]
        alt = F.variables['Alt'][...]
        alt[alt>9.9e+36] = np.nan
        
        for i in range(tmp.shape[0]):
            tmpa = var[i,:]
            var1[i,:] = np.interp(ALT, alt[i,:], tmpa, left=np.nan, right=np.nan)
    
    var1.set_auto_maskandscale(True)
#
#F.sync()
F1.sync()
F1.close()
F.close()

