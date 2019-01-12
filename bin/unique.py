import sys
cset = set() 
for line in sys.stdin: 
    smiles = line.strip() 
    if smiles == '':
        continue 

    cset.add(smiles) 

for x in cset: 
    print(x) 
