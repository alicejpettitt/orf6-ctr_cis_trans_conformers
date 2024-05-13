# An integrative characterisation of proline cis and trans conformers in a disordered peptide

This repository contains scripts to reproduce analysis of the nuclear magnetic resonance spectroscopy (NMR) chemical shifts, 15N relaxation data, and 15N diffusion data as reported in the manuscript 'An integrative characterisation of proline cis and trans conformers in a disordered peptide' by Pettitt et al. 

## Subdirectories (ORF6-CTR)
1. `1H-15N-temp-titration` 1H-15N heteronuclear single quantum coherence (HSQC) chemical shift assignments at 275.65, 278, 283, 288, 293, 298, 303, 308, 310, and 313 K. This data was used to calculate cis-P57 populations at 288 and 310 K, and to produce the Van't Hoff plots. 
2. `ssp_orf6_ctr_cis_15deg` contains the output from the secondary structure propensity algorithm (1) for the cis-P57 Calpha, Cbeta, and Halpha chemical shifts at 288 K. The subdirectory contains the data and scripts for you to repeat the analysis. The `ssp-orf6-ctr-288K-cis.txt` was used in the Jupyter notebook to produce the manuscript figure. 
3. `ssp_orf6_trans_cis_15deg` contains the output from the secondary structure propensity algorithm (1) for the trans-P57 Calpha, Cbeta, and Halpha chemical shifts at 288 K. The subdirectory contains the data and scripts for you to repeat the analysis. The `ssp-orf6-ctr-288K-trans.txt` was used in the Jupyter notebook to produce the manuscript figure. 
4. `relaxation_data` contains two subdirectories for the cis and trans 15N-labelled relaxation data. Within these subdirectories is the analysis for all the relaxation experiments. 
5. `dosy` contains the 1H-15N DOSY HSQC analysis for the E55, Q56, M58, and E59 cis-P57 and trans-P57 peaks for 15N-labelled ORF6-CTR. The intensities of these peaks were quantified by lineshape-fitting with the software package FuDA and labelled as *.out, with `c` indicating cis-P57 peaks (2). The subdirectory also contains the FuDA input file (param.fuda) and the peak.list. For more details on FuDA see: https://www.ucl.ac.uk/hansen-lab/fuda/
param.fuda is executed using nmrPipeFit.py param.fuda fuda, where output data is stored in the directory `fuda`. 

## References
1. Marsh JA, Singh VK, Jia Z, Forman-Kay JD. 2006. Sensitivity of secondary structure propensities to sequence differences between α- and γ-synuclein: Implications for fibrillation. Protein Sci. 15:2795.
2. Hansen DF, Yang D, Feng H, Zhou Z, Wiesner S, Bai Y, Kay LE. 2007. An exchange-free measure of 15N transverse relaxation: an NMR spectroscopy application to the study of a folding intermediate with pervasive chemical exchange. J Am Chem Soc. 129:11468–79. 


