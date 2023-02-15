data_sent = open("../sputnik/transmission1.txt").read()
bases_measured = open("../sputnik/transmission2.txt").read()
bases_correct = open("../sputnik/transmission3.txt").read()

def get_agreed_bytes(data_sent, bases_measured, bases_correct, v1, v2):
    agreed_bits = []
    for i in range(len(bases_correct)):
        if bases_correct[i] == 'v':
            if bases_measured[i] == '+':
                if data_sent[i] == '-':
                    agreed_bits.append(v1)
                else:
                    agreed_bits.append(abs(v1 - 1))
            else:
                if data_sent[i] == '/':
                    agreed_bits.append(v2)
                else:
                    agreed_bits.append((abs(v2 - 1)))
    return hex(int("".join([str(c) for c in agreed_bits]), 2))[2:-1]

print(get_agreed_bytes(data_sent,bases_measured,bases_correct,0,0))
print(get_agreed_bytes(data_sent,bases_measured,bases_correct,0,1))
print(get_agreed_bytes(data_sent,bases_measured,bases_correct,1,0))
print(get_agreed_bytes(data_sent,bases_measured,bases_correct,1,1))