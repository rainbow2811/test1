import sys
import json

def read_txt(file_name: str)->str:
	ret =""
	with open(file_name,'r') as handle:
		for line in handle:
			if line.startswith(">"):
				continue
			ret += line.strip()
	return ret

def read_csv(file_nmae:str)->list:
	ret = []
	with open(file_name,'r') as handle:
		for line in handle:
			if line.startswith("#"):
				header = line.strip().split(',')
				continue
			splitted = line.strip().split(',')
			d = dict(zip(header, splitted))
	return ret

def read_tsv(file_name:str)->list:
	ret = []
	with open(file_name,'r') as handle:
		for line in handle:
			if line.startswith('#'):
				header = line.strip().split('\t')
				continue
			splitted = line.strip().split('\t')
			d = dict(zip(header,splitted))
			ret.append(d)
	return ret

def to_json(l: list) -> None:
	with open("read_sample.json",'w')










