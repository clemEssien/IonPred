import os
import sys
import pandas as pd
import numpy as np
import argparse
import csv
from lib.extract_fragment import extractFragforPredict

def main():
    metals = ["ZN","CU","FE2","FE3","CA","MG","MN","NA","K"]
    radicals = ["CO3","NO2","PO4", "SO4"]
    halides = ["B","F","I","CL"]
    ion_list = ["ZN","CU","FE2","FE3","CA","MG","MN","NA","K","CO3","NO2","PO4", "SO4","B","F","I","CL"]
    parser=argparse.ArgumentParser(description='Prediction of ion-ligand binding sites using ELECTRA.')
    parser.add_argument('-input', dest='inputfile', type=str, help='Protein sequences to be predicted in fasta format.', required=True)
    parser.add_argument('-predict-type',  
                        dest='predicttype', 
                        type=str, 
                        help='predict types. \'metal\' for predicting metal ions \n \
                        \'radical\' for predicting radicals.\n \
                        \'halide\' for predicting halides. \n \
                        It indicates two files [-model-prefix]_HDF5model and [-model-prefix]_parameters.', required=False)
    parser.add_argument('-ion', dest='ion', type=str, help='indicates the specific ion you want to predict e.g. \'CA\' or \'MG\' or \'F\' or \'SO4\' etc.', required=True,default=None)
    parser.add_argument('-residue-types', dest='residues', type=str, help='Residue types that to be predicted, only used when -predict-type is \'general\'. For multiple residues, seperate each with \',\'',required=False,default="C,H,E,D")
    
    args = parser.parse_args()

    
    inputfile=args.inputfile
    predicttype=args.predicttype
    residues=args.residues.split(",")
    ion=args.ion
    test_path='data/finetuning_data/'
    window=12
    
    for i in ion_list:
        t_path = test_path + i+'/'
        os.makedirs(t_path, exist_ok=True)
    
    if ion is None or ion not in ion_list:
            print("wrong parameter for -predict_type \n Must be one of the following: "+','.join(ion_list)+ "\n")
            exit()
            
    '''if predicttype == 'metal':
        residues = "C,H,E,D"
    elif predicttype == 'radical':
        residues = "G,H,K,R,S"
    elif predicttype == 'halide':
        residues = "G,K,N,R"
    else:
        print("wrong parameter for -predict-type!\n")
        exit()'''
        
    
    testfrag,ids,poses,focuses=extractFragforPredict(inputfile,window,'-',focus=residues) 
    testlabel = testfrag[0]
    testfrag = testfrag[range(1,26)].apply(' '.join, axis = 1)
    testset=np.column_stack((testlabel, testfrag, ids, poses, focuses))
    testset=pd.DataFrame(testset)
    testset.to_csv(test_path + ion+"/dev.tsv", index=False, header=None, sep='\t')
    
    #dev_set = np.column_stack((testlabel, testfrag))
    #dev_set = pd.DataFrame(dev_set)
    #testset.to_csv(test_path + ion+"/dev.tsv", index=False, header=None, sep='\t')
    
    
    
    os.system('python3 run_finetuning.py \
    --data-dir data \
    --model-name ionpred  \
    --hparams \'{"model_size": "small", "do_train": true,"do_eval": true,"task_names": ["' + ion + '"]}\'' 
    )
        
    # os.system('rm -rf ' + test_path + ion+'/*')
    # os.system('rm -rf data/models/protein_small_quater_1m/finetuning_tfrecords/*')
    
print("Predictions completed successfully!\n")
    
            
if __name__ == "__main__":
    main()  
        
