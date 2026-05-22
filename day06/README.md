# PeptideAtlas Peptide Mapper

## Overview

This project searches a peptide sequence in the PeptideAtlas ProMaST API and maps it to matching protein sequences.

The program takes a peptide sequence from the user, searches for it in the human proteome, and returns information about the matching protein. It also uses the protein accession to retrieve additional information from UniProt and searches PubMed for related papers.

## What the program does

The program:

1. Asks the user to enter a peptide sequence.
2. Searches the peptide in PeptideAtlas.
3. Finds matching protein records.
4. Extracts the protein accession.
5. Retrieves protein information from UniProt, including:
   - Gene symbol
   - Protein description
   - Primary protein sequence
   - Protein length
6. Searches PubMed for papers related to the protein accession.
7. Prints PubMed links.

## Database used

This project uses PeptideAtlas, a web-based proteomics database.

PeptideAtlas contains experimentally observed peptides and proteins identified by mass spectrometry. It allows users to map peptide sequences to proteins and proteomes.

In this project, I used the PeptideAtlas ProMaST API, which maps a peptide sequence to protein entries in a selected reference proteome.

## Additional databases used

### UniProt

UniProt is used to retrieve protein annotation information such as gene symbol, protein description, primary sequence, and sequence length.

### PubMed

PubMed is used to search for scientific papers related to the protein accession found from the peptide search.

## Requirements

Install the required package:

```bash
pip install -r requirements.txt

## AI Used

I used ChatGPT to write this code.
