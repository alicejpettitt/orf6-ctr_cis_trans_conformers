#!/usr/bin/python

# Fit ratio from col[1] and use uncertainty from col[2]
# Assumes that first value is reference, and second is NOE
#
# by D. F. Hansen 
# October 2005,  
# flemming@pound.med.utoronto.ca
###################################################################

import sys
import math
import string

if (len(sys.argv)<2):
  sys.stderr.write("\nUSAGE:\n %s datafile0 [datafile1, [datafile2, .. ]] \n\n" % (sys.argv[0],))
  sys.exit(0)

sys.stdout.write("#%9s%15s%13s\n" % ('Name','NOE','Esd(NOE)'))
for file in range(len(sys.argv)-1):
    # Get name of the peak
    Name=string.split(string.strip(sys.argv[file+1]),'.')[0]
    # Load data file
    inputfile = open(sys.argv[file+1],'r')
    lines=inputfile.readlines()
    Data=[]
    for line in lines:
        if not ( line[0] == "#"):
            # Read the data.
            temp=string.split(line)
            Data.append(temp)
    #
    I1 =float(Data[1][1])
    dI1=float(Data[1][2])
    I2 =float(Data[0][1]) 
    dI2=float(Data[0][2])
    #
    NOE =I1/I2
    dNOE=math.pow(                \
      math.pow(dI1/I2,2.)+        \
      math.pow(dI2*I1/(I2*I2),2.) \
      ,0.5)
    #
    # Print out results
    sys.stdout.write("%10s" % (Name,))    
    sys.stdout.write("%15.6f%13.6f" % (NOE,dNOE))
    sys.stdout.write("\n")
    inputfile.close()
