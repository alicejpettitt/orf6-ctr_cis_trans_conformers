# An integrative characterisation of proline cis and trans conformers in a disordered peptide

This repository contains scripts to reproduce analysis of the nuclear magnetic resonance spectroscopy (NMR) chemical shifts, 15N relaxation data, and 15N diffusion data as reported in the manuscript 'An integrative characterisation of proline cis and trans conformers in a disordered peptide' by Pettitt et al. {DOI}

The software package FuDA (1) was used to quantify peak intensities and to calculate 15N relaxation rates by fitting the intensity profiles to mono-exponential decay functions. Each subdirectory contains a FuDA input file (param.fuda) and the peak.list. For more details on FuDA see: https://www.ucl.ac.uk/hansen-lab/fuda/
param.fuda is executed using nmrPipeFit.py param.fuda fuda, where output data is stored in the directory `fuda`. 

## Subdirectories (cis)
This subdirectory contains the chemical shift assignments at 600 and 800 MHz, and the following subdirectories which include files uploaded to the `ORF6-CTR-NMR-ANALYSIS.ipynb` Jupyter notebook for the cis-P57 conformation: 
1. `600_r1` contains a file for the 600 MHz 15N R1 rates (`r1_600_cis.txt`) uploaded to the Jupyter notebook, the relaxation delay times `vdlist_r1` and FuDA input files.  
2. `600_r1rho` contains a file for the 600 MHz 15N R1 rates (`r1_rho_600_cis.txt`) uploaded to the Jupyter notebook, the relaxation delay times `vdlist_r1rho` and FuDA input files.  
3. `800_r1` contains a file for the 800 MHz 15N R1 rates (`r1_800_cis.txt`) uploaded to the Jupyter notebook, the relaxation delay times `vdlist_r1` and FuDA input files.  
4. `800_r1rho` contains a file for the 800 MHz 15N R1 rates (`r1_rho_800_cis.txt`) uploaded to the Jupyter notebook, the relaxation delay times `vdlist_r1rho` and FuDA input files.  

## Subdirectories (trans)
This subdirectory contains the chemical shift assignments at 600 and 800 MHz, and the following subdirectories which include files uploaded to the `ORF6-CTR-NMR-ANALYSIS.ipynb` Jupyter notebook for the trans-P57 conformation: 
1. `600_r1` contains a file for the 600 MHz 15N R1 rates (`r1_600_cis.txt`) uploaded to the Jupyter notebook, the relaxation delay times `vdlist_r1` and FuDA input files.  
2. `600_r1rho` contains a file for the 600 MHz 15N R1 rates (`r1_rho_600_cis.txt`) uploaded to the Jupyter notebook, the relaxation delay times `vdlist_r1rho` and FuDA input files.  
3. `800_r1` contains a file for the 800 MHz 15N R1 rates (`r1_800_cis.txt`) uploaded to the Jupyter notebook, the relaxation delay times `vdlist_r1` and FuDA input files.  
4. `800_r1rho` contains a file for the 800 MHz 15N R1 rates (`r1_rho_800_cis.txt`) uploaded to the Jupyter notebook, the relaxation delay times `vdlist_r1rho` and FuDA input files.  
5. `600_noe` contains a file for the 600 MHz noe's (`noe_600.fit`) uploaded to the Jupyter notebook, the relaxation delay times `vclist_noe` and FuDA input files. There is also a python script `NOE.py` to repeat the NOE analysis yourself. The script calculates the ratio and uncertainty assuming the first input value is from the reference spectra and the second value is the NOE taken from the FuDA (.out) files, which you can execute yourself by downloading the noe.ft2 files from Zenodo and usign FuDA. 
6. `800_noe` contains a file for the 800 MHz noe's (`noe_800.fit`) uploaded to the Jupyter notebook, the relaxation delay times `vclist_noe` and FuDA input files. There is also a python script `NOE.py` (see `600_noe`).
7. `600_rdd` contains data for the exchange-free measure of 15N transverse relaxation (1). The subdirectory contains FuDA input files, the relaxation delay times (8), but repeated 4 times for the 4 rates measured in the pulse experiment, `rdlist_rdd`. There is also a file `Rdd_600.txt` that contains the saved 15N Rdd rates calculated in the `ORF6-CTR-NMR-ANALYSIS.ipynb` Jupyter notebook. The data was processed using FuDA and then sorted using the `run.sh` script to separate the output files into tau, intensity, and esd in blocks of 8 (12 columns total) for each residue (numbered 43-61, excluding P57). The files in the subdirectory Four_rates were uploaded to the Jupyter notebook to calculate Rdd. 


## References
1. Hansen DF, Yang D, Feng H, Zhou Z, Wiesner S, Bai Y, Kay LE. 2007. An exchange-free measure of 15N transverse relaxation: an NMR spectroscopy application to the study of a folding intermediate with pervasive chemical exchange. J Am Chem Soc. 129:11468–79. 


