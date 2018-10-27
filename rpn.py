#!/usr/bin/env python3
import operator

op={'+':operator.add, '-':operator.sub,'*':operator.mul, '/':operator.floordiv,'^':operator.pow}
def calculate(arg):
	#stack for calculater
	stack=[]
	# tokenize input
	tokens = arg.split()
	# process tokens
	for token in tokens:
		try:
			value=int(token)
			stack.append(value)
		except ValueError:
			val1=int(stack.pop())
			val2=int(stack.pop())
			func=op[token]
			result=func(val2,val1)
			stack.append(result)			
			return stack[0]

def main():
	while True:
		print(calculate(input("rpn calc> ")))
			
if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
 main()

