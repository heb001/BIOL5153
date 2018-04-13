#! /usr/bin/env python3

#Load required modules
from Bio import SeqIO
import argparse

#Create an ArgumentParser object ('parser') that will hold all the info necessary to parse the command line
parser = argparse.ArgumentParser(description="This script filters out specified sequences from a FASTA file")

#Add a positional argument with add_argument() -- to be treated as a string

parser.add_argument("fasta", help="name of FASTA file")
parser.add_argument("remove", help="name of file containing sequence(s) user wishes to remove")

#Parse arguments

args = parser.parse_args()

print("We're gonna open this FASTA file: ", args.fasta)
print("filter out sequence contained in this file ", args.remove)

fasta = SeqIO.parse(args.fasta, "fasta")

#NOTE: Account for multiple headers in the FASTA file with parse

remove = SeqIO.read(args.remove, "fasta")
for sequence in fasta:
	if sequence.description != remove.description:
		print(sequence.format("fasta"))
