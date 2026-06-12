# DNA Sequence Analyzer 🧬

A Python-based bioinformatics project that performs DNA sequence analysis, mutation detection, transcription, and protein translation.

## Features

### DNA Validation
- Checks whether a DNA sequence contains only valid nucleotides (A, T, G, C)

### Nucleotide Count
- Counts the number of:
  - Adenine (A)
  - Thymine (T)
  - Guanine (G)
  - Cytosine (C)

### GC Content Analysis
- Calculates GC content percentage
- Classifies sequences as:
  - High GC Content
  - Low GC Content

### Complement Sequence
- Generates the complementary DNA strand

### Reverse Complement
- Generates the reverse complement sequence

### Mutation Detection
- Compares a reference sequence and a sample sequence
- Reports mutation positions and nucleotide changes

### DNA → mRNA Transcription
- Converts a DNA template strand into mRNA

### mRNA → Protein Translation
- Splits mRNA into codons
- Translates codons into amino acids
- Detects stop codons

---

## Example

### Input

```text
DNA: ATAGGGCCTTAAA
```

### Output

```text
Valid DNA sequence
GC Content: 38.46 %

Complement: TATCCCGGAATTT

Reverse Complement: TTTAAGGCCCTAT

mRNA: UAUCCCGGAAUUU

Protein: YPGI
```

---
## How to Run

1. Clone the repository

```bash
git clone https://github.com/famithav/dna-sequence-analyzer.git
```

2. Navigate to the project folder

```bash
cd dna-sequence-analyzer
```

3. Run the program

```bash
python dna_analyzer.py

```
## Technologies Used

- Python
- Dictionaries
- Loops
- Conditional Statements
- String Manipulation

---

## Future Improvements

- FASTA file support
- Restriction enzyme analysis
- Open Reading Frame (ORF) detection
- DNA sequence alignment
- Disease mutation database integration
- Graphical User Interface (GUI)

---

## Screenshots
<img width="1003" height="246" alt="terminal1" src="https://github.com/user-attachments/assets/495c7902-eb16-47ca-a779-171edf45de5c" />
<img width="745" height="246" alt="terminal 2" src="https://github.com/user-attachments/assets/8e6f504b-9586-478f-9c88-727f1e808a15" />
<img width="610" height="90" alt="terminal 3" src="https://github.com/user-attachments/assets/0e37de45-fc84-4c03-b791-f5d2ed4dece7" />


---

## Author

**Famitha Velusamy**

First bioinformatics project built while learning Python and Synthetic Biology.
