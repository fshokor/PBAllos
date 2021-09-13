# PBAllos

PBAllos is a program to analyze allosteric communication, by computing mutual information between encoded protein sequences, using Protein Blocks (PBs) as structural alphabet. Protein Blocks are structures defined by [De Brevern *et al.*](https://www.ncbi.nlm.nih.gov/pubmed/11025540) to analyze the dynamics and deformability of protein structures.   
GSATools, created by [Pandini *et al.*](https://academic.oup.com/bioinformatics/article/29/16/2053/200020), is a free software package to analyze conformational ensembles and to detect functional motions in proteins by means of a structural alphabet. It was implemented in C as a set of analysis programs for GROMACS 4.0.x.
This Python program is a re-implementation of GSATools, by using a different structural alphabet, and diffrent working environment.

## Requirements

- [Python](https://www.python.org/)= 3.6
- [Pandas](https://pandas.pydata.org/) = 1.3.2
- [NumPy](https://numpy.org/) >= 1.21
- [Matplotlib](http://matplotlib.org/) >= 3.4
- [MDAnalysis](https://code.google.com/p/mdanalysis/) >= 2.0
- [PBXplore](https://pbxplore.readthedocs.io/en/latest/)= 1.4

to create logo from PB sequences (optionel):

- [WebLogo 3](http://weblogo.threeplusone.com/)


## Installation


Install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

Clone the repository:

```shell
$ git clone https://github.com/lilianyc/pb
$ cd pbAllos
```

Create conda environment:

```shell
$ conda env create -f environment.yml
```

Activate conda environment:

```shell
$ conda activate PBAllos
```


## Usage

This program takes as input a [PDB](http://www.wwpdb.org/documentation/file-format) files.

It will return:
- Protein encoded sequences alignment: .PB.flat and PB.fasta files  
- Frequency table: .PB.count
- PB sequences list and table: .npy and .csv files
- Number sequences list and table: .npy and .csv files 
- Mutual information matrix: .csv and .npy files 
 

To compute the MI between positions in protein encoded sequences:

* Process the dataset using:
   * data.sh: install data from source and organize it 
   * encoding.sh: PB assignement 
* stat.sh: statistical analysis on PBs (frequency, Neq) (optionnel) 
* Run the `main.py` to compute the mutual information by choosing your parameters, e.g:
```shell
$ python main.py --input_path ~out/ --output_dir out/ 
```

# Data 


# References 

* GSATools: 

Pandini, A., Fornili, A., Fraternali, F., & Kleinjung, J. (2012). Detection of allosteric signal transmission by information-theoretic analysis of protein dynamics. FASEB journal : official publication of the Federation of American Societies for Experimental Biology, 26(2), 868–881. https://doi.org/10.1096/fj.11-190868


* PBxplore: 

Barnoud, J., Santuz, H., Craveur, P., Joseph, A. P., Jallu, V., de Brevern, A. G., & Poulain, P. (2017). PBxplore: a tool to analyze local protein structure and deformability with Protein Blocks. PeerJ, 5, e4013. https://doi.org/10.7717/peerj.4013


* Calf-1:

Goguet, M., Narwani, T. J., Petermann, R., Jallu, V., & de Brevern, A. G. (2017). In silico analysis of Glanzmann variants of Calf-1 domain of αIIbβ3 integrin revealed dynamic allosteric effect. Scientific reports, 7(1), 8001. https://doi.org/10.1038/s41598-017-08408-w


