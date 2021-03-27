# DeepCE - A novel and robust deep learning framework for high-throughput mechanism-driven phenotype compound screening and its application to COVID-19 drug repurposing
-----------------------------------------------------------------
Code by **Thai-Hoang Pham** at Ohio State University.

## 1. Introduction
This repository contains source code (**DeepCE**) and data for paper "[A deep learning framework for high-throughput mechanism-driven phenotype compound screening and its application to COVID-19 drug repurposing](https://www.nature.com/articles/s42256-020-00285-9)" (**Nature Machince Intelligence 3, 247–257 (2021)**)

**DeepCE** is a Python implementation of the mechanism-driven neural network-based model which captures 
high-dimensional associations among biological features as well as non-linear relationships between biological features 
and outputs to predict gene expression profiles given a chemical compound.

**DeepCE** achieves state-of-the-art results of predicting gene expression profiles compared to other models not only 
in *de novo* chemical setting but also in the traditional imputation setting. More importantly, **DeepCE** is shown to be 
effective in the challenge and urgent problem, finding treatment for **COVID-19**. In summary, **DeepCE** could be a powerful 
tool for phenotype-based compound screening. 

## 2. Pipeline

![alt text](docs/fig1-update.png "Pipeline")

Figure 1: General framework of training **DeepCE** for L1000 gene expression profile prediction and using it for 
downstream application (i.e. drug repurposing). The objective for the learning process is minimizing the loss 
between predicted profiles and grouth-truth profiles in L1000 dataset. After training, **DeepCE** is used for 
generating profiles for new chemicals in external molecular database (e.g. DrugBank, ChEMBL). These profiles 
are then used for **in silico** screening to find potential drugs for disease treatment

## 3. DeepCE

![alt text](docs/fig2.png "DeepCE")

Figure 2: Overall architecture of **DeepCE**

## 4. Installation

**DeepCE** depends on Numpy, SciPy, PyTorch (CUDA toolkit if use GPU), scikit-learn, and RDKit. 
You must have them installed before using **DeepCE**.

The simple way to install them is using conda:

```sh
	$ conda install numpy scipy scikit-learn rdkit pytorch
```
## 5. Usage

### 5.1. Data

The datasets used to train **DeepCE** are located at folder ``DeepCE/data/``

### 5.2. Training DeepCE

The training script for **DeepCE** is located at folder ``script/``

```sh
    $ cd script
    $ bash train_deepce.sh
```

Arguments in this scripts:

* ``--drug_file``:       path for SMILES representation file
* ``--gene_file``:         path for L1000 gene feature file
* ``--train_file``:        path for L1000 gene expression training data
* ``--dev_file``:        path for L1000 gene expression development data
* ``--test_file``:      path for L1000 gene expression testing data
* ``--dropout``: dropout value used in DeepCE
* ``--batch_size``:       batch size value for each training step
* ``--max_epoch``:     maximum number of training iterations

### 5.3. COVID-19 drug repurposing by scanning all drugs in Drugbank

Besides **DeepCE** source code, we also publicize the chemical-induced gene expression profiles generated from 
**DeepCE** at 8 cell lines including *A375*, *A549*, *HA1E*, *HELA*, *HT29*, *MCF7*, *PC3*, and *YAPC* for all drugs 
(i.e. 11179 drugs) in Drugbank and COVID-19 patients' gene expression profiles. Drug repurposing for COVID-19 can be 
conducted by comparing chemical-induced gene expression profiles with COVID-19 patients' gene expression profiles. 
We hope that this dataset could make significant a contribution to drug discovery and development in particular, 
and computational chemistry and biology research in general.

The script for getting these chemical-induced gene expression profiles and COVID-19 patients' gene expressions is 
located at folder ``script/``

```sh
    $ cd script
    $ bash get_gene_expression_data.sh
```

The downloaded dataset will be located at folder ``DeepCE/data/covid_data/``

After downloading this dataset, users can generate potential drugs for COVID-19 by running the scripts which are 
located at folder ``script/`` as follows:

```sh
    $ cd script
    $ bash covid_drug_repurposing.sh
```

Arguments in this scripts:

* ``--data_dir``:       path for COVID-19 data folder
* ``--patient_file``:         COVID-19 patient gene expression file name
* ``--num_cell``:        minimum number of cell lines that drugs appear on top ranked list
* ``--top``:        size of top drugs in ranked list for each cell line

## 6. References

[Pham, TH., Qiu, Y., Zeng, J. et al. A deep learning framework for high-throughput mechanism-driven phenotype compound screening and its application to COVID-19 drug repurposing. Nat Mach Intell 3, 247–257 (2021).](https://doi.org/10.1038/s42256-020-00285-9)

## 7. Contact

**Thai-Hoang Pham** < pham.375@osu.edu >

Department of Computer Science and Engineering, Ohio State University, USA
