import sys

class FASTQ:
	def __init__(self,file_name:str):
		self.file_name = file_name
		self.read_num = 0

	def count_read_num(self):
		cnt = 0
		with open(self.file_name,'r') as handle:
			for line in handle:
				if cnt % 4 == 0:
					header = line.strip()
					self.read_num += 1
				elif cnt % 4 == 1:
					seq = line.strip()
				elif cnt % 4 == 3:
					qual = line.strip()
				cnt += 1

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"usage: python {sys.argv[0]} [fasta]")
		sys.exit()

	file_name = sys.argv[1]
	t = FASTQ(file_name)
	t.count_read_num()
	print(t.read_num)	

