from __future__ import annotations
import requests
import json
import textwrap
import pandas as pd
from lib import make_http_requests as mhr
from lib import aadic as aa
from lib import pdb_entries
from collections import defaultdict
from tqdm import tqdm

wrapper = textwrap.TextWrapper(width=60)

pbe = pdb_entries.Pdb_Entries()
BINDING_SITES = "Data/binding_sites/"
ligands = defaultdict(list)
seq_dict = pbe.chains_with_sequences()

output_list = []
url = 'https://1d-coordinates.rcsb.org/graphql'

for k,v in seq_dict.items():
    myobj = {
    "operationName": "QueryAnnotations",
    "variables": {
        "queryId": k,
        "reference": "PDB_INSTANCE",
        "sources": [
        "PDB_ENTITY",
        "PDB_INSTANCE",
        "UNIPROT"
        ]
    },
    "query": "query QueryAnnotations($queryId: String!, $reference: SequenceReference, $sources: [Source], $range: [Int], $filters: [FilterInput]) {\n  annotations(queryId: $queryId, reference: $reference, sources: $sources, range: $range, filters: $filters) {\n    source\n    target_id\n    features {\n      type\n      provenance_source\n      description\n      feature_id\n      name\n      feature_positions {\n        beg_seq_id\n        end_seq_id\n        beg_ori_id\n        end_ori_id\n        range_id\n        open_begin\n        open_end\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    #myobj["variables"]["queryId"] = "1E8K.A"

    print(myobj["variables"]["queryId"])
    chain = myobj["variables"]["queryId"]
    x = requests.post(url, json= myobj)
    response = json.loads(x.text)


    data = response['data']['annotations']
    if len(data)>0:
        out_dict = {}
        output = {}
        dupl = []
        for i in range(len(data)):
            features = data[i]['features']
            for j in range(len(features)): 
                if features[j]["type"] == "BINDING_SITE":
                        name = features[j]['name']
                        if name and ('ligand' in name):
                            positions = []
                            out_dict['ligand'] = name.split()[1]
                            site = out_dict['ligand']
                            for pos in (features[j]['feature_positions']):
                                positions.append(pos['beg_seq_id'])
                                positions = list(set(positions))
                            
                            site = name.split('ligand')[1].strip()
                            if site in output.keys():
                                output[site].extend(positions) 
                            else:
                                output[site] = positions
                            output[site].sort()
    output['chain'] = chain
                            
    output_list.append(output)
for record in output_list:
    pdbid = record["chain"]
    for site in record.keys():
        annotations = list(record[site])
        if site != 'chain':
            with open(BINDING_SITES+site+'.fasta', "a",) as f:
                id = ('>'+pdbid).strip()
                id += '\n'
                seq = aa.insert_annotations(seq_dict[pdbid], annotations,'#')
                seq = wrapper.fill(text=seq)
                seq = id+seq+'\n'
                f.write(seq)