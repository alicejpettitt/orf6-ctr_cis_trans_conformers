# An integrative characterisation of proline cis and trans conformers in a disordered peptide

This repository contains scripts to reproduce analysis of the trajectories from metadynamics simulations as reported for the manuscript 'An integrative characterisation of proline cis and trans conformers in a disordered peptide' by Pettitt et al. DOI: [`10.1016/j.bpj.2024.09.028`](10.1016/j.bpj.2024.09.028)

## Reproducibility information 
For input files to generate trajectories, see ../PLUMED_input_files or PLUMED NEST (plumID:24.027, https://www.plumed-nest.org/eggs/24/027/). [![plumID:24.027](https://www.plumed-nest.org/eggs/24/027/badge.svg)](https://www.plumed-nest.org/eggs/24/027/)

## This repository contains: 

#### Jupyter notebook 
A Jupyter Notebook detailing the analysis performed to reproduce the figures as reported in the manuscript is included as `ORF6-CTR-METADYNAMICS-ANALYSIS.ipynb`. The easiest way to try out the notebooks is by using [`conda`](https://www.anaconda.com/products/individual). We include the environment, which specifies the packages needed for the analysis and plotting of the results. To create the environment, run `conda env create -f environment.yml` for Mac and `conda env create -f environment_linux.yml` for Linux operating systems. This can take a hot minute to complete depending on the operating system. Activate the new environment with `conda activate analysis`. 

If the above environments do not work, the following packages are required for running the jupyter notebook:
- Numpy
- SciPy
- Pandas 
- Matplotlib
- Lmfit
- MDTraj
- Seaborn
- SciKit-Learn 

Open the Jupyter notebook with `jupyter lab` and select the notebook from the sidebar. Large data files referenced in the Notebook (including trajectories, metadynamics weights, and SAXS BME weights) are hosted on Zenodo [`https://doi.org/10.5281/zenodo.13748215`](https://doi.org/10.5281/zenodo.13748215). The data should be downloaded and placed in a directory called `Metadynamic_simulations_Zenodo`. This should be in the same diectory as `ORF6-CTR-METADYNAMICS-ANALYSIS.ipynb`, with the `README_metadynamic_simulations.md` file. 

#### System subdirectories   
Each system used in the manuscript has a subdirectory containing experimental data and PLUMED files required for `ORF6-CTR-METADYNAMICS-ANALYSIS.ipynb`. 
1. The PBMetaD bias from the `COLVAR_nohead` file is required for blocking analysis for each system.
2. The chemical shifts and `camshift_plumed.dat` are available to run CamShift (1) for each trajectory locally. Experimental chemical shift data was measured at 310.15 K (37 degrees celsius). 

For `a03ws_run1`, `a03ws_run2`, and `c36m`
3. `camshift_cis` and `camshift_trans` directories are available to run CamShift locally. Experimental chemical shift data was measured at 310.15 K (37 degrees celsius). 
4. `SAXS_bme_reweight` the scripts to perform the SAXS BME reweighting (see below) and the output from the BME reweighting `<system>_saxs_bme_reweight_output.dat`, which contains the experimental and ensemble-averaged system predicted SAXS data, as well as details on the fitting at the end of the file. 

#### Blocking analysis 
Blocking analysis scripts were taken from [`blocking analysis scripts`](https://github.com/fpesceKU/BLOCKING) (2). Both of these python scripts are used in the Jupyter notebook 

## SAXS BME reweight 
We used the following two GitHub repositories to perform the SAXS BME reweighting [`here`](https://github.com/KULL-Centre/papers/tree/main/2021/aSYN-ahmed-et-al) and [`here`](https://github.com/KULL-Centre/BME) (3-4). 

Pepsi-SAXS was used to predict the SAXS scattering curve for each frame in the trajectory. See `pepsi_saxs.py` for an adapted script for how to do this (3). For each system the calculated SAXS scattering curves were combined into one file for BME reweighting. The files are hosted on Zenodo and can be downloaded at [`https://doi.org/10.5281/zenodo.13748215`](https://doi.org/10.5281/zenodo.13748215), along with the experimental data.

The first line in the calculated SAXS data is a header that defines the type of data and the error model it should use. BME has only gaussain error model implemented
	
	DATA=SAXS PRIOR=GAUSS    

In column 1, 2 and 3 we have the experimental value of the: scatter vector, intensity and error, respectively. The number of the rows is equal to the number of data points. In this manuscript we have  2570.

The `BME.py` script was used to perform the SAXS reweighting. Here, we used a theta value of 100. To repeat this analysis yourself, use the following notebook: [`here`](https://github.com/KULL-Centre/papers/blob/main/2021/aSYN-ahmed-et-al/BME_analysis/BME_analysis_example.ipynb) 

## References
1. Kohlhoff KJ, Robustelli P, Cavalli A, Salvatella X, Vendruscolo M. Fast and accurate predictions of protein NMR chemical shifts from interatomic distances. J Am Chem Soc. 2009 Oct 7;131(39):13894-5. doi: 10.1021/ja903772t. PMID: 19739624.
2. Pesce F, Newcombe EA, Seiffert P, Tranchant EE, Olsen JG, Grace CR, Kragelund BB, Lindorff-Larsen K. 2023. Assessment of models for calculating the hydrodynamic radius of intrinsically disordered proteins. Biophys J. 122:310–21. 
3. Ahmed MC, Skaanning LK, Jussupow A, Newcombe EA, Kragelund BB, Camilloni C, Langkilde AE, Lindorff-Larsen K. 2021. Refinement of α-Synuclein Ensembles Against SAXS Data: Comparison of Force Fields and Methods. Front Mol Biosci. 8:654333.
4. Bottaro S, Bengtsen T, Lindorff-Larsen K. 2020. Integrating Molecular Simulation and Experimental Data: A Bayesian/Maximum Entropy Reweighting Approach. Methods Mol Biol. 2112:219–40.

