#! /usr/bin/env python3


###################################################################  BIOL 5153 Assignment 5 ###################################################################################



#Print in FASTA format all features in the watermelon.gff file -- ">" header should combine the organism name and gene



###################################################################  Plan of Action ##########################################################################################

#Use SeqIO to parse the GFF file

#Read in the genome (FASTA format), store it in a variable - use SeqIO for this --> having trouble converting gff to fasta with SeqIO
	#attempted to download BioPython GFF converter with BCBio-gff package -- still no luck
	#will attempt manually writing in watermelon.fsa file 

#Open the GFF file
#Read in line by line using a for loop

#Note: line 0 = organism name, 3 = beginning coordinate, 4 = end coordinate, 5 = length, 8 = gene name

#Split the GFF string into a list -- split function [on a tab] -- split line on the tab so that each line is a list instead of a string
#Go into each list and pull out sequence using [ : ] - print to screen



################################################################## Begin Code ###############################################################################################

"""
#load the required modules
from Bio import SeqIO


#Declare variable that holds the watermelon genome [watermelon.fsa] ; read in file
genome = SeqIO.read("/Users/heb001/Desktop/watermelon_files/watermelon.fsa", "fasta") 

#Declare variable that holds and opens watermelon.gff
GFF = open("/Users/heb001/Desktop/watermelon_files/watermelon.gff")


for line in GFF:
	#(species, type, beginning, end, length, gene) = line.split('/t')
	features = line.split('\t')
	species = (features[0])
	beginning = int(features[3])
	end = int(features[4])
	length = int(features[5])
	gene = (features[8])
	print(">" + species + " | " + gene + "Length: " +str(length) + "\n" +  genome.seq[beginning-1:end])
	calculated_length = len(genome.seq[beginning-1:end])
	print("Verifying length of gene: " + str(calculated_length))

#Close watermelon.gff file
GFF.close()
"""

################################### incorporating argparse to script to accept inputs from command line into parseGFF.py ###################################################

#load the required argparse module
import argparse

#Create an ArgumentParser object ('parser') that will hold all the info necessary to parse the command line
	 #description = summary of what script does -- similar to blast --help print output

parser = argparse.ArgumentParser(description="This script extracts sequences from FASTA file based on features of a given GFF file")

#use the add_argument() method to add a positional argument
	#positional arguments are *required* inputs, so their order/position matters
	### argparse treats all options as strings unless told to do otherwise ###

parser.add_argument("fasta", help="name of FASTA file")
parser.add_argument("gff", help="name of GFF file")

#parse the arguments

args = parser.parse_args()

print("Open the FASTA file: ", args.fasta)
print("Open the GFF file: ", args.gff)


#####################################################################################################


#load the SeqIO module
from Bio import SeqIO

fasta = SeqIO.read(args.fasta, "fasta")

#open GFF file

GFF = open(args.gff)

#Create a for loop to read each line, split the string into a list based on presence of tab characters ("\t"), and name each desired variable of header
#NOTE: FASTA format is zero-based, but the GFF file is one-based -- denotes the beginning coordinate as base "1" instead of "0"
        #to account for this, subtract one bp from the "beginning coordinate" of for loop print statement

for line in GFF:
	features = line.split('\t')
	species = (features[0])
	beginning = int(features[3])
	end = int(features[4])
	length = int(features[5])
	gene = (features[8])
	print(">" + species + " | " + gene + "Length: " +str(length) + "\n" +  fasta.seq[beginning-1:end])
	calculated_length = len(fasta.seq[beginning-1:end])
	print("Verifying length of gene: " + str(calculated_length))

#Note: int = integer -- used on numerical data within the gff file
        #print statement includes the charactersitc ">" fasta header, the organism name and gene [defined in for loop], length of gene according to GFF and beginning
                #and end coordinates relative to whatever FASTA file is read in
        #Second print statement prints the calculated string length to verify the gene length listed on GFF file
