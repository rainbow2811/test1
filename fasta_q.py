from Bio import SeqIO

record = SeqIO.read("059.fasta","fasta")

A = record.seq.count("A")
C = record.seq.count("C")
G = record.seq.count("G")
T = record.seq.count("T")


print(record)
print("----------")
print(record.seq)
print("--------------")
print(f"A: {A}")
print(f"C: {C}")
print(f"G: {G}")
print(f"T: {T}")

