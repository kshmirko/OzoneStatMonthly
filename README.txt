

OzoneStatsMonthly - a set of scripts for data processing of lidar sensing of 
the vertical distribution Ozna in the upper troposphere and stratosphere.

RepairOldDb.py  -   designed to organize the processed data in a uniform format.


Baseline: 
~~~~~~~~~
    -   Result of the program meteodownloader. 
    -   The results of calculations of the vertical ozone profiles. 

Order of execution of scripts.: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1.  CalcHTropo.py           -   this script performs calculations tropopause 
                                    height and adds the result to files with 
                                    weather data. 

    2.  AddHTropoToO3.py        -   this script adds the height of the tropopause
                                    to ozone profiles data.

    3.  AddJetParamsToO3.py     -   this script adds subtropical jet parameters 
                                    (windspeed ad kernel altitude) to ozone 
                                    profiles data.        

    4.  O3Related2Tropo.py      -   Make a dataset with ozone profiles related
                                    to tropopause.

    5.  O3Related2Jet.py        -   Make a dataset with ozone profiles related 
                                    to tropopause.

    6.  O3MonthlyStatTropo.py   -   calculates ozone profiles statistics related 
                                    to tropopause height.

    7.  O3MonthlyStatJet.py     -   calculates ozone profiles statistics related 
                                    to jet stream height.


