### This script is adapted from https://github.com/KULL-Centre/papers/tree/main/2021/aSYN-ahmed-et-al

# import everything that is needed 
import subprocess
import os
import sys
import numpy as np

import os

# Path to Pepsi SAXS
Pepsi_path = '/home/alice/applications/Pepsi-SAXS'
SAXS_data = '../a03ws_run1/SAXS_data/saxs_orf6_ctr.dat'

# Go through all frames
nr_of_frames = 0
for _, _, files in os.walk('.'):
        for file in files:
                if file.startswith('frame') and file.endswith('.pdb'):
                        nr_of_frames += 1
                        
#first, fit all frames and all parameters
step=1
if step==1:
	for i in range(0,nr_of_frames+1):
		filename = "frame_%d.pdb" % i
		outfile = "frame_%d.fit" % i
		subprocess.run([Pepsi_path, filename, SAXS_data , '-o ', outfile, '-ms ' ,' 2' ,'-cst', '-j']) 

#find default r0
subprocess.run([Pepsi_path, 'frame_99.pdb', SAXS_data , '-o find_r0.fit', '-ms ' ,' 2', '--r0_min_factor 1.0', '--r0_max_factor 1.0', '--r0_N 1', '-cst','-j'])
with open('find_r0.log', 'r') as f:
        lines = f.readlines()
default_r0 = None  # Initialize default_r0 to None
for line in lines:
    if "Best r0 found" in line:
        parts = line.split(" ") # split the line into its parts separated by space
        #print(parts)
        default_r0 = float(parts[-2].strip()) # index into the value (-1 is unit, -2 is value) 
print(default_r0)

#then, parse all the log files to find best d_rho
print('parsing', nr_of_frames+1, 'log files')
d_rho_list = []
print(d_rho_list)
c = 0
for i in range(0, nr_of_frames+1):
    filename = "frame_%d.log" % i
    #print(filename)
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if "Best d_rho found" in line:
                #print(line)
                parts = line.split(" ")
                #print(parts)
                d_rho = float(parts[-2].strip())
                d_rho_list.append(d_rho)
                #print(d_rho_list)
    except IOError as e:
        print("An error occurred while processing the file:", e)
        
#then, parse all the log files to find best r0
print('parsing', nr_of_frames+1, 'log files')
r0_list = []
print(r0_list)
c = 0
for i in range(0, nr_of_frames+1):
    filename = "frame_%d.log" % i
    #print(filename)
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if "Best r0 found" in line:
                #print(line)
                parts = line.split(" ")
                #print(parts)
                r0 = float(parts[-2].strip())/default_r0
                r0_list.append(r0)
                #print(r0_list)
    except IOError as e:
        print("An error occurred while processing the file:", e)

print('d_rho list', d_rho_list)
print('r0 list', r0_list)

#Take the average to find ensemble min/max r0 factors and d_rho
avg_r0 = str(np.average(r0_list))
avg_d_rho = str(np.average(d_rho_list)*10) 

#refit all of the frames, using the ensemble parameters
for i in range(0,nr_of_frames+1):
        filename = "frame_%d.pdb" % i
        outfile = "Ave_AA_frame%d.fit" % i
        subprocess.run([Pepsi_path, filename, SAXS_data , '-o ', outfile, '-ms ' ,' 2' ,'-cst', '-j', '--r0_N 1', '--dro ', avg_d_rho, '--r0_min_factor ', avg_r0, '--r0_max_factor ', avg_r0]) 
                
print('ensemble d_rho', avg_d_rho) 
print('ensemble r0', avg_r0)
print('default r0', default_r0)
print('done')
