# An integrative characterisation of proline cis and trans conformers of a disordered peptide

This repository contains scripts to reproduce analysis of the nuclear magnetic resonance spectroscopy (NMR) chemical shifts, 15N relaxation data, and 15N diffusion data as reported in the manuscript 'An integrative characterisation of proline cis and trans conformers in a disordered peptide' by Pettitt et al. 

## Reproducibility information 
Experimental NMR data files (.ft2 and .ft3 format) are hosted on Zenodo [`https://doi.org/10.5281/zenodo.13748215`](https://doi.org/10.5281/zenodo.13748215) for you to repeat the analysis yourself. Spectra in this manuscript were produced using NMRFAM-Sparky (1) and Adobe Illustrator. 

Chemical shift assignments have been deposited on BMRB https://bmrb.io/

## This repository contains:

#### Jupyter notebook 
A Jupyter Notebook detailing the analysis performed to reproduce the figures as reported in the manuscript is included as `ORF6-CTR-NMR-ANALYSIS.ipynb`. The easiest way to try out the notebooks is by using [`conda`](https://www.anaconda.com/products/individual). We include the environment, which specifies the packages needed for the analysis and plotting of the results. To create the environment, run `conda env create -f environment.yml` for Mac and `conda env create -f environment_linux.yml` for Linux operating systems. This can take a hot minute to complete depending on the operating system. Activate the new environment with `conda activate analysis`. 

## Subdirectories 
1. `NAc-orf6-ctr` contains the 2D 1H-1H total correlation spectroscopy (TOCSY) chemical shift assignments for the 800 micromolar unlabelled N-acetylated ORF6-CTR at 288, 283, 288, 293, 298, 303, 308, and 310 K to calculate the temperature coefficients. 
2. `orf6-ctr` contains 5 subdirectories for NMR data on the uniformly 15N-labelled and 13C,15N-labelled ORF6-CTR.

## References
1. Lee W, Tonelli M, Markley JL. 2015. NMRFAM-SPARKY: enhanced software for biomolecular NMR spectroscopy. Bioinformatics. 31:1325. 


