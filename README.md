# Starcode: Multiscattering DM simulation
This code simulates the miulti-scattering process using Python3 and integration from subroutine of tu4 from Swifter.
It is highly recommended to put swifter as one of the inner directories with main.py.

## Getting the code
Before installation, make sure you have git running on your machine
```
git clone https://github.com/kittenK531/starcode.git && git switch fort90
```

## Installation of swifter (Linux)
For Linux users, it is required to have a fortran compiler. In order to successfully compile the program, a few modifications must be made.

First pulling the package is required.

```
cd starcode
mkdir recom && cd recom
wget https://www.boulder.swri.edu/swifter/swifter.tar.gz && tar xvf swifter.tar.gz
```

So your swifter should exist in this hierachy `starcode/recom/swifter`.

After decompressing the package, modify the following.
1. swifter/Makefile.Defines
```
    SWIFTER_HOME    = [Your working directory of swifter]
    ...
    FORTRAN         = gfortran
    FFLAGS          = -O
    CFLAGS          = -O -Wformat -Wimplicit-function-declaration
```
2. swifter/tool/tool_follow.f90 line: 194
Change from 
```
 1001                              FORMAT(1x,e15.7,1x,i3,6(1x,es15.7))
```
to 
```
 1001                              FORMAT(1x,e15.7,1x,i3,6(1x,e15.7))
```
This removes abnormalities to display the data to produce our target file in order to obtain heliocentric coordinates and velocity after one simulation cycle using sympletic integration.

After so, compiling is easy by 
```
cd swifter && make
```

## How to use starcode?

### Pre-requisites and virt env
After compilation, it is recommended to use a virtual isolated environment for the simulation, I choose Anaconda.
```
conda create -ny starcode python==3.9.0
conda activate starcode
pip install matplotlib numpy pathlib
pip install -e swifter .
```
One more step and you are ready to go!

Since we are only interested to know the trajectory of heavy DM particle moving around the Sun, it is natural to have the input files modified.

1. swifter/pl.in

Paste the following to modify the Sun settings only.
```
 1
 1 2.959139768995959E-04
 .0 .0 .0
 .0 .0 .0
```
2. swifter/tp.in

Likewise,
```
 1
 6
 1.0 .0 .0
 .0 1.721420632E-2 .0
```

3. swifter/param.in

Change the following lines
```
T0             0.0E0
TSTOP          3.6525E2            ! simulation length is 1 yr
DT             3.6525E0            ! stepsize is 0.0005 * 1 year ==> 1.8263E-1
...
ISTEP_OUT      5                   !
...
OUT_TYPE       XDR4                ! 4-byte XDR formatted output
OUT_FORM       XV                  ! osculating element output
```

Quoting from swifter 

> The code requires units in which the gravitational constant G is unity.  Any
combination of lengths, masses, and times that keeps that true is OK.  For
example, one could use lengths specified in AU and time in days, thus forcing
the Solar mass to be approximately 2.96E-4.

Which is the exact unit sets we use to compute our velocities and positions in heliocentric coordinates.

## Expected outputs
```
$ python3 main.py

************* SWIFTER: Version 0.1 *************

Authors:

    Martin Duncan: Queen's University
    Hal Levison  : Southwest Research Institute

Please address comments and questions to:

    Hal Levison or David Kaufmann
    Department of Space Studies
    Southwest Research Institute
    1050 Walnut Street, Suite 400
    Boulder, Colorado  80302
    303-546-0290 (HFL), 720-240-0119 (DEK)
    303-546-9687 (fax)
    hal@gort.boulder.swri.edu (HFL)
    kaufmann@boulder.swri.edu (DEK)

************************************************

Enter name of parameter data file: Parameter data file is param1477027.in                                                                                                                 
  
NPLMAX         =           -1
NTPMAX         =           -1
T0             =    0.0000000000000000     
TSTOP          =    365.25000000000000     
DT             =    3.6524999999999999     
PL_IN          =  pl.in
TP_IN          =  tp1477027.in
IN_TYPE        =  ASCII
ISTEP_OUT      =            5
BIN_OUT        =  bin.dat
OUT_TYPE       =  XDR4
OUT_FORM       =  XV
OUT_STAT       =  NEW
ISTEP_DUMP     =         1000
J2             =    0.0000000000000000     
J4             =    0.0000000000000000     
CHK_CLOSE      =  F
CHK_RMIN       =   -1.0000000000000000     
CHK_RMAX       =    1000.0000000000000     
CHK_EJECT      =   -1.0000000000000000     
CHK_QMIN       =   -1.0000000000000000     
CHK_QMIN_COORD =  HELIO
CHK_QMIN_RANGE =   -1.0000000000000000       -1.0000000000000000     
ENC_OUT        =  enc.dat
EXTRA_FORCE    =  F
BIG_DISCARD    =  T
RHILL_PRESENT  =  F
  
  *************** MAIN LOOP *************** 

Normal termination of SWIFTER (Version 0.1)
------------------------------------------------

************* SWIFTER: Version 0.1 *************

Authors:

    Martin Duncan: Queen's University
    Hal Levison  : Southwest Research Institute

Please address comments and questions to:

    Hal Levison or David Kaufmann
    Department of Space Studies
    Southwest Research Institute
    1050 Walnut Street, Suite 400
    Boulder, Colorado  80302
    303-546-0290 (HFL), 720-240-0119 (DEK)
    303-546-9687 (fax)
    hal@gort.boulder.swri.edu (HFL)
    kaufmann@boulder.swri.edu (DEK)

************************************************

Enter name of parameter data file: Parameter data file is dump_param1.dat                                                                                                                 
  
NPLMAX         =            1
NTPMAX         =            1
T0             =    365.25000000000000     
TSTOP          =    365.25000000000000     
DT             =    3.6524999999999999     
PL_IN          =  dump_pl1.bin
TP_IN          =  dump_tp1.bin
IN_TYPE        =  XDR8
ISTEP_OUT      =            5
BIN_OUT        =  bin.dat
OUT_TYPE       =  XDR4
OUT_FORM       =  XV
OUT_STAT       =  APPEND
ISTEP_DUMP     =         1000
J2             =    0.0000000000000000     
J4             =    0.0000000000000000     
CHK_CLOSE      =  F
CHK_RMIN       =   -1.0000000000000000     
CHK_RMAX       =    1000.0000000000000     
CHK_EJECT      =   -1.0000000000000000     
CHK_QMIN       =   -1.0000000000000000     
CHK_QMIN_COORD =  HELIO
CHK_QMIN_RANGE =   -1.0000000000000000       -1.0000000000000000     
ENC_OUT        =  enc.dat
EXTRA_FORCE    =  F
BIG_DISCARD    =  T
RHILL_PRESENT  =  F
  
Enter the id of the particle to follow:  Following particle            6
Enter the frequency:  Tmax =    365.25000000000000
```

