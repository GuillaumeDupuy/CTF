import base64
import re

def base64_decode(cipher):
	return base64.b64decode(cipher.encode('ascii')).decode('ascii')

# operands = [a, d, s, a, w]
# operators = [~, &, |, ^]
def push_to_stack(dec_cipher):
	operators = []
	operands = []

	ser = re.compile('[a-zA-Z]')
	
	itr = len(dec_cipher) - 1

	while itr >= 0:
		if(dec_cipher[itr] == '>'):
			operators.append(">>")
			itr -= 1
		elif(ser.fullmatch(dec_cipher[itr])):
			operands.append(pow(ord(dec_cipher[itr]), 3))
		else:
			operators.append(dec_cipher[itr])
		itr -= 1

	return operands, operators

def evaluate(operands, operators):

	while len(operators) > 0:
		cur_oper = operators.pop()
		
		op1 = operands.pop()
		op2 = operands.pop()
		if(cur_oper == '~'):
			# print("~", op1)
			operands.append(~op1)
		elif(cur_oper == '^'):
			operands.append(pow(op1, op2, 100000000))
			# print(op1, " ^ ", op2)
		else:
			statement = f"{op1} {cur_oper} {op2}"
			operands.append(eval(statement))
			# print(statement)

	return operands.pop()

def runner(operands, operators):

	itrs = len(operators)
	
	for i in range(itrs):
		# print(i)
		val = evaluate(operands.copy(), operators.copy())
		operands = operands[:-2]
		operands.append(val)
		operators = operators[:-1]

	print("CTFLearn{"+str(val)+"}")

if __name__ == "__main__":
	
	cipher = "YmluYXJ5cmVmaW5lcnl8JiY+PnxeXl4mJnx8fg=="
	
	dec_cipher = base64_decode(cipher)
	print("decoded cipher: ", dec_cipher)
	oprnd, oper = push_to_stack(dec_cipher)
	runner(oprnd, oper)
