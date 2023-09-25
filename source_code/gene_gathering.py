from Bio import SeqIO
from Bio import Entrez

def return_start(location):
    start = ""
    for s in location:
        if s.isdigit():
            start += s
        elif s == ":":
            return int(start)+1

def return_end(location):
    end=""
    for s in location:
        if s.isdigit():
            end += s
        elif s == ":":
            end=""
        elif s == "]":
            return int(end)

def return_gene(gene):
    return gene[2 : len(gene)-2]

def return_organism(organism):
    return organism[2: len(organism) - 2]

def return_direction(direction):
    if direction == "-1":
        return "-"
    else:
        return "+"

#LC276224.1 FJ997214.1 NC_013187.1 NC_013833.1 MG979470.1 GQ996415.1 NC_028002.1 NC_030595.1 NC_024586.1 NC_027503.1 NC_041142.1 NC_025334.1 KX688549.1 NC_029717.1 NC_030263.1 NC_023364.1 NC_014585.1 NC_014588.1 NC_014580.1 NC_014583.1 NC_021747.1
species_accession = input("띄어쓰기 구분으로 accession number 입력: ").split()

files = []
Entrez.email = "ksjross@gmail.com"
for name in species_accession:
    with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=name) as handle:
        seq = SeqIO.read(handle, "genbank")
        full_sequence = seq.seq
        for i in range(len(seq.features)):
            if seq.features[i].type == "CDS":
                gene_name = return_gene(str(seq.features[i].qualifiers["gene"]))
                species = return_organism(str(seq.features[0].qualifiers["organism"]))
                start_loc = return_start(str(seq.features[i].location))
                end_loc = return_end(str(seq.features[i].location))
                direction = return_direction(str(seq.features[i].strand))
                full_genome = str(full_sequence[start_loc - 1:end_loc])
                exist = False
                for file in files:
                    if file[0] == gene_name:
                        file[1].append([species, direction, full_genome])
                        exist = True
                        break
                if not exist:
                    files.append([gene_name, [[species, direction, full_genome]]])

for file in files:
    f=open(file[0]+'.txt','w')
    for element in file[1]:
        f.write('>'+element[0]+'('+element[1]+')'+'\n')
        f.write(element[2]+'\n'+'\n')
    f.close()