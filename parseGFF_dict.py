#! /usr/bin/env python3

# This script will parse a GFF file, extracting sequences for the annotated features

# watermelon.gff watermelon.fsa > out.fasta

# Load required modules
import sys
import os
import re
import argparse
from Bio import SeqIO
from collections import defaultdict

def get_args():
	# Create an ArgumentParser object ('parser')
	parser = argparse.ArgumentParser()

	# Add required/positional arguments
	parser.add_argument("gff",   help="name of GFF file")
	parser.add_argument("fasta", help="name of FASTA file")

	# Parse the arguments
	return parser.parse_args()


def parse_fasta():
	# Open and read the FASTA file
	genome = SeqIO.read(args.fasta, 'fasta')
	return genome.seq


def get_feature_sequence(dna, start, end, strand):
	# Extract the corresponding sequence
	fragment = dna[int(start)-1:int(end)]

        # Print the sequence, either forward or reverse complemented
	if(strand == "+"):
        	return fragment
	else:
        	return fragment.reverse_complement()


def parse_gff(dna):
	# Open and parse the GFF file
	gff_file = open(args.gff, 'r')
	
	# Dictionary to store exons: key = gene name, value = list of exon sequences
	exons_dictionary = {}

	for line in gff_file:
		# Split each line on a tab
		(seqid, source, feature, start, end, length, strand, phase, attributes) = line.split('\t')

		if(feature == 'CDS' or feature == 'tRNA' or feature == 'rRNA'):
			# Split the attributes field
			atts = attributes.split(" ; ")
			# Grab the gene name and, if present, the exon number
			gene = re.search("^Gene\s+(\S+)", atts[0])
			exon = re.search("exon\s+(\d+)",  atts[0])
			
			# If both the gene and exon are defined, meaning that this gene has introns and multiple exons, store the feature sequence

			if(gene and exon):
				
				# Is this gene already in the dictionary? If yes, index exon by number 
				if gene.group(1) in exons_dictionary:
					exons_dicitonary[gene.group(1)] [exon.group(1)] = get_feature_sequence(dna, start, end, strand)
 				
				# If the gene is not in the dictionary, initialize the exons list, then store the feature sequence by []
				else:
					exons_dictionary[gene.group(1)] = defaultdict(list) # Initialize the list
						# or = [] but you have to define position 0 in your index
					exons_dicitonary[gene.group(1)] [exon.group(1)] = get_feature_sequence(dna, start, end, strand) # Store the sequence
					
			else:
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1))
				print(get_feature_sequence(dna, start, end, strand))

			# Else statement = only gene is defined -- so there are no introns and it can be printed here
			
			
	gff_file.close()

	# Splice and print CDS for genes with introns, stored in exons_dictionary{}
	for gene, exons in exons_dictionary.items():
		# Items method assigns gene name as the key and exons as list/value
		# Print the FASTA header
		print(">" + gene) 
		
		# Initialize a new variable, cds, that will hold the CDS sequence
		cds = ''
		
		# Assemble the CDS sequence by looping over each exon in the list and appending it to the cds string
		for i in exons:
			print(">" + gene + "exon_" + i)
			print(i)
			cds += exons[i]
		# += will concatenate the new exon at the end of the cds, then print outside of the for loop
		print(cds)

# Blast output saved to out.fasta [./parseGFF_02_may_2018.py watermelon.gff watermelon.fsa > out.fasta] against watermelon genes in watermelon_nt (watermelon_genes.fa)
	# cp out.fasta ~/Desktop/watermelon_files/watermelon_nt
	# makeblastdb -in watermelon_genes.fa -dbtype nucl 
	# blastn -query out.fasta -db watermelon_genes.fa -outfmt '6 std qcovs' | column -t | 1
		# Limit number of hits to 1 "max target seqs 1"	

def main():
	genome = parse_fasta()
	parse_gff(genome)

# Get the command-line arguments
args = get_args()

main()
