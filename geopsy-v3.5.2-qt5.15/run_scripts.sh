#!/bin/sh
export LD_LIBRARY_PATH=/home/user/geopsy/lib/:$LD_LIBRARY_PATH
gfortran fortran-disp-curve.f90 -L/home/user/geopsy/lib/ -lQGpCoreTools -lQGpCoreWave -o testfo
./testfo