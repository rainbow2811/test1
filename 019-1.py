import sys

if len(sys.argv) != 2:
	print("#usage: python {sys.argv[0]} [num]")
	sys.exit()


try:
	num = int(sys.argv[1])
	print(10/num)

except ZeroDivisionError:
	print("0으로는 못 나눠요")
	sys.exit()

except ValueError:
	print("input not valid")
	sys.exit()
