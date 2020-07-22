import sys

if len(sys.argv) !=2:
	print(f"#usage: python {sys.argv[0]} [fasta]")
	sys.exit()

f = sys.argv[1]
d = {}

open with (f,'r') as handle:
	for line in handle






