aa_dict = {
    "ALA":"A",
    "ARG":"R",
    "ASN":"N",
    "ASP":"D",
    "ASX":"B",
    "CYS":"C",
    "GLU":"E",
    "GLN":"Q",
    "GLX":"Z",
    "GLY":"G",
    "HIS":"H",
    "ILE":"I",
    "LEU":"L",
    "LYS":"K",
    "MET":"M",
    "PHE":"F",
    "PRO":"P",
    "SER":"S",
    "THR":"T",
    "TRP":"W",
    "TYR":"Y",
    "VAL":"V"
}

def aa_residue(key):
    try:
        return aa_dict[key]
    except Exception as e:
        return None

def chain_letter(chain, chain_letter):
    if chain_letter:
        return chain_letter
    return chain.split('_')[1]

def process_aa(aa , pdb_id, site):
    aa = aa.split('_')
    if len(aa[0]) == 3:
        if (aa[0] in aa_dict):
            pos = aa[1].split('(')
            with open("dataset/result/"+site+"_site.txt", "a") as f:
                result = pdb_id +'\t' +aa_residue(aa[0])+'\t'+pos[0]+"\n"
                f.write(result)
            return aa_residue(aa[0])+" - "+pos[0]
    else:
        with open("process_error.txt", "a") as log:
            result = aa[0].upper() +" "+pdb_id.upper() +" "+site+"\n"
            log.write(result)
    return None


def insert_annotations(string, array,xter):
    sequence= [0];
    new_string = "";
    i = 1;
    for i in range(len(array)):
        sequence.append(array[i]) #seems the uniprot position counts from zero
        new_string += string[sequence[i]:sequence[i+1]]+xter
    new_string += string[sequence[-1]:]+"\n"
    return new_string