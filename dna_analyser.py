valid = ("A", "T", "G", "C")
sequence = input("DNA:").upper()
is_valid = True
for char in sequence:
    if char not in valid:
        is_valid = False
        break
if is_valid:
    print("valid dna sequence")
else:
    print("invalid dna sequence")
print("sequence length:", len(sequence))
A_count = sequence.count("A")
T_count = sequence.count("T")
G_count = sequence.count("G")
C_count = sequence.count("C")
print("A:", A_count)
print("T:", T_count)
print("G:", G_count)
print("C:", C_count)
gc_content = (G_count+C_count)/len(sequence)*100
print("GC Content:", round(gc_content, 2), "%")
if gc_content > 50:
    print("High GC Content")
else:
    print("Low GC Content")
complement_seq = {"A": "T", "T": "A", "G": "C", "C": "G"}
complement = ""
for char in sequence:
    complement += complement_seq[char]
print("complement:", complement)
complement = ""
for char in sequence:
    complement += complement_seq[char]
print("reverse complement:", complement[::-1])
sequence_ref = input("DNA sequence_ref:").upper()
sequence_sample = input("DNA sequence_sample:").upper()
len_ref = len(sequence_ref)
len_sample = len(sequence_sample)
if len_ref != len_sample:
    print("sequences must have the same length")
for index in range(len_ref):
    if sequence_ref[index] != sequence_sample[index]:
        print("mutation at position", index + 1,
              sequence_ref[index], "->", sequence_sample[index])
mrna_complement_seq_template_strand = {"A": "U", "T": "A", "G": "C", "C": "G"}
template_strand = input("DNA template strand:").upper()
mrna = ""
for char in template_strand:
    mrna += mrna_complement_seq_template_strand[char]
print(mrna)
codon_table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "GCU": "A",
               "GCC": "A", "GCA": "A", "GCG": "A", "UAU": "Y", "UAC": "Y", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "UGU": "C", "UGC": "C", "UGG": "W", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", "UAA": "*", "UAG": "*", "UGA": "*"}
protein = ""
codons = []
for i in range(0, len(mrna), 3):
    codon = mrna[i:i+3]
    print(codon)
    if len(codon) < 3:
        print("not enough nucleotide for translation")
        break
    codons.append(codon)
    amino_acid = codon_table[codon]
    print(codon, "->", amino_acid)
    if amino_acid == "*":
        print("stop codon found, translation terminated")
        break

    protein += amino_acid
print("Codons:", "|".join(codons))
print("Protein:", protein)
