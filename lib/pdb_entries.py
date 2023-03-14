from Bio.PDB import PDBList
from collections import defaultdict

DATA_DIR = "Data/"

class Pdb_Entries:

    # def __init__(self) -> None:
        
    #download file that contains all chains and sequences
    def download_pdb_entries(self):
        pdblist = PDBList()
        pdblist.get_seqres_file(savefile=DATA_DIR+'pdb_seqres.txt') 
        print('done downloading!')

    def return_chains(self):
        with open(DATA_DIR+'pdb_seqres.txt') as f:
            content = f.read().split('>')
            chains = [id[:6].replace('_','.') for id in content if len(id)>0]
        return chains

    #total number of protein chains
    def total_chains(self):
        return len(self.return_chains())

    #write all protein chains to file
    def write_chains_to_file(self):
        chains = self.return_chains()
        with open(DATA_DIR+'protein_chains.txt', 'a') as w:
            content = '\n'.join(chains)
            w.write(content)
    
    #return all protein chains and their corresponding sequences
    def chains_with_sequences(self):
        seq_dict = defaultdict(list)
        with open(DATA_DIR+"pdb_seqres.txt","r") as f:
            content = f.read().split('\n')
            for line in content:
                if '>' in line:
                    seq = ""
                    id = line[1:5]+'.'+line[6]
                    id = id.upper()
                else:
                    seq += line
                seq_dict[id] = seq
        return seq_dict