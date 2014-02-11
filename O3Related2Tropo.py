# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:41:51 2014

@author: Администратор
"""

import netCDF4 as ncdf
import numpy as np
import glob
import os
import shutil

def main(item):
    # Copy existing file with added tropopause height to another file
    oldname, ext = os.path.splitext(item)
    newname = oldname+"-tropo"+ext
    shutil.copy(item, newname)
    print(newname)
    
    F = ncdf.Dataset(newname, 'r+')
    baseline = 'Earth'
    
    if 'Baseline' in F.ncattrs():
        baseline = F.Baseline

    if 'Earth' in baseline:
        Alt = np.linspace(-5000,20000,500)
        NTime = len(F.variables['Time'])
        O3 = F.variables['O3']
        ALT = F.variables['Alt'][...]
        meanOn = F.variables['meanOn']
        meanOff = F.variables['meanOff']        
        stdOn = F.variables['stdOn']
        stdOff = F.variables['stdOff']
        O3ppb = F.variables['O3ppb']
        O3Err = F.variables['O3Err']
        R = F.variables['R']
        for i in range(NTime):
            tmp = np.interp(Alt, \
                ALT-F.variables['HTropo'][i],\
                O3[i,:], left=np.nan, right=np.nan)
            O3[i,:] = tmp[:]
            
            tmp = np.interp(Alt, \
                ALT-F.variables['HTropo'][i],\
                meanOn[i,:], left=np.nan, right=np.nan)
            meanOn[i,:] = tmp[:]
            
            tmp = np.interp(Alt, \
                ALT-F.variables['HTropo'][i],\
                meanOff[i,:], left=np.nan, right=np.nan)
            meanOff[i,:] = tmp[:]
            
            tmp = np.interp(Alt, \
                ALT-F.variables['HTropo'][i],\
                stdOn[i,:], left=np.nan, right=np.nan)
            stdOn[i,:] = tmp[:]
            
            tmp = np.interp(Alt, \
                ALT-F.variables['HTropo'][i],\
                stdOff[i,:], left=np.nan, right=np.nan)
            stdOff[i,:] = tmp[:]
            
            tmp = np.interp(Alt, \
                ALT-F.variables['HTropo'][i],\
                O3ppb[i,:], left=np.nan, right=np.nan)
            O3ppb[i,:] = tmp[:]
            
            tmp = np.interp(Alt, \
                ALT-F.variables['HTropo'][i],\
                O3Err[i,:], left=np.nan, right=np.nan)
            O3Err[i,:] = tmp[:]
            
            tmp = np.interp(Alt, \
                ALT-F.variables['HTropo'][i],\
                R[i,:], left=np.nan, right=np.nan)
            R[i,:] = tmp[:]
            
            F.Baseline = 'Tropopause'
            
        F.variables['Alt'][...] = Alt[:]
    
    F.close()
    pass



if __name__ == "__main__":
    O3Mask = r'd:\disks\1TB\#data#\#LIDAR#\#ozone#\O3ProcessedData\b*.nc'
    files  = glob.glob(O3Mask)
    
    
    for item in files:
        main(item)
    
    