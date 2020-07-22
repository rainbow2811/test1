import sys


n = int(sys.argv[1])

l1 = ['A','C','G','T']
l2 = ['A','C','G','T']

def mer(l1,l2,n):
	if n ==1 :
		return l2

	l_tmp = []
	for s1 in l1:
		for s2 in l2: 
			l_tmp.append(s1+s2)
		return mer(l1,l_tmp,n-1)

print(mer(l1,l2,n))



