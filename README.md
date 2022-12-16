# IonPred: Prediction of ion-ligand binding sites with ELECTRA

## Introduction
Interactions between proteins and ions are essential for the proteins to carry out various biological functions like structural stability, metabolism, signal transport, etc. As more than half of all proteins bind to ions, it becomes necessary to identify ion-binding sites. This helps to understand their biological functions and is also very useful in drug discovery studies. While several computational approaches have been proposed, this remains a difficult problem due to the small size and high versatility of the metal and acid radical. In this study, we propose IonPred, a sequence-based approach using ELECTRA (Pretraining Text Encoders as Discriminators Rather Than Generators) which is based on replacement token detection of amino acid residues from protein sequences. This model is designed to predict 9 metal ions (Zn<sup>2+</sup>, Cu<sup>2+</sup>, Fe<sup>2+</sup>, Fe<sup>3+</sup>, Ca<sup>2+</sup>, Mg<sup>2+</sup>, Mn<sup>2+</sup>, Na<sup>+</sup>, and K<sup>+</sup>) and 8 acid radical ion ligands (CO<sub>3</sub><sup>2−</sup>, SO<sub>3</sub><sup>2−</sup>, PO<sub>4</sub><sup>3−</sup>, NO<sup>2−</sup>, F<sup>−</sup>, Cl<sup>−</sup>, and I<sup>−</sup>).   To the best of our knowledge, IonPred is the first deep-learning method for predicting halide ions that bind to proteins.

## Requirements
- Python 3.6
- [TensorFlow 1.15](https://www.tensorflow.org/)
- [NumPy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/stable/) and [SciPy](https://scipy.org/) 
- [Pandas](https://pandas.pydata.org/)

## Set up
The input for this tool consists of raw protein sequences in fasta format. While the output consists of probability scores for each candidate site. 
- The threshold used is 0.5. So candidate residues that have a probability >= 0.5 are considered to be ion-binding sites. 
- Data sets used to be used to run prediction must be placed in the directory called `test` 
- While the results for each residue binding site would be found in the directory`results`. It would be saved in a directory labeled with the corresponding ion name.
- A batch size of 128 was used while running predictions but this parameter can be modified.

## Run Prediction
For example to predict Calcium binding site i.e. Ca<sup>2+</sup>, run the command:

`python3 predict.py -input ca.fasta_without_annotation -ion-type CA`

For guidance on other parameters, run:

`python3 predict.py -help`
