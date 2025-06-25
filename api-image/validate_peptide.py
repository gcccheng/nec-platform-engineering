import sys
import re

VALID_AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")

def is_valid_peptide(sequence):
    sequence = sequence.strip().upper()
    return all(residue in VALID_AMINO_ACIDS for residue in sequence)

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_peptide.py <peptide_sequence>")
        sys.exit(1)
    sequence = sys.argv[1]
    if is_valid_peptide(sequence):
        print("Valid peptide sequence.")
    else:
        print("Invalid peptide sequence.")

if __name__ == "__main__":
    main()
