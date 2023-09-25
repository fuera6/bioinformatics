from Bio import SeqIO
from Bio import Entrez
import pandas as pd

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
    return gene[2 : -2]

def return_product(product):
    return product[2 : -2]

def return_direction(direction):
    if direction == "-1":
        return "-"
    else:
        return "+"

def return_translation(translation):
    return translation[2 : len(translation)-2]

name = input("accession number 입력: ")
Entrez.email = "ksjross@gmail.com"
with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=name) as handle:
    seq = SeqIO.read(handle, "genbank")
    type_list = []
    start_loc_list = []
    end_loc_list = []
    gene_list = []
    product_list = []
    direction_list = []
    translated_list = []
    for i in range(2, len(seq.features), 2):
        if seq.features[i].type == "tRNA" or seq.features[i].type == "rRNA":
            type_list.append(seq.features[i].type)
            start_loc_list.append(return_start(str(seq.features[i].location)))
            end_loc_list.append(return_end(str(seq.features[i].location)))
            gene_list.append("")
            product_list.append(return_product(str(seq.features[i].qualifiers["product"])))
            direction_list.append(return_direction(str(seq.features[i].strand)))
            translated_list.append("")
        elif seq.features[i].type == "CDS":
            type_list.append(seq.features[i].type)
            start_loc_list.append(return_start(str(seq.features[i].location)))
            end_loc_list.append(return_end(str(seq.features[i].location)))
            gene_list.append(return_gene(str(seq.features[i].qualifiers["gene"])))
            product_list.append(return_product(str(seq.features[i].qualifiers["product"])))
            direction_list.append(return_direction(str(seq.features[i].strand)))
            translated_list.append(return_translation(str(seq.features[i].qualifiers["translation"])))

raw_data = {"type" : type_list, "start" : start_loc_list, "end" : end_loc_list, "gene" : gene_list, "product" : product_list, "direction" : direction_list, "translation" : translated_list}
raw_data = pd.DataFrame(raw_data)
excel_name = name + " map data.xlsx"
raw_data.to_excel(excel_writer = excel_name)