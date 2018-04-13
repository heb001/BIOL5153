#! /usr/bin/env python3

#load the required modules

import argparse
from Bio import SeqIO

#create an ArgumentParser object ('parser') that will hold all the information necessary to parse the command line.
	#description = summary of what script does -- similar to blast --help print output

parser = argparse.ArgumentParser(description="This script filters out sequences from a FASTA file that are shorter than a user-specified length cutoff")


## required arguments are POSITIONAL ARGUMENTS -- position in the command oine when entered is meaningful -- must be listed in order

#use the add_argument() method to add a positional argument
#positional arguments are *required* inputs, so their order/position matters
### argparse treats all options as strings unless told to do otherwise ###

#How to add an argument: use something that is descriptive

parser.add_argument("fasta", help="name of FASTA file")

## Add an optional argument = length cutoff for filter -- set with dashes "--"; signifies that it is optional and not required

parser.add_argument("-m", "--min_seq_length", help="filter sequences that are <= min_seq_length in length (default = 300 nt)", type=int, default=300)

#parse the arguments

args = parser.parse_args()

print("We're going to open this FASTA file: ", args.fasta)
print("filter sequences less than ", args.min_seq_length, "nt in length")

fasta = SeqIO.parse(args.fasta, "fasta")

for sequence in fasta:
        if len(sequence.seq) > args.min_seq_length:
                print(sequence.format("fasta"))
