import math;
from sympy.ntheory.residue_ntheory import discrete_log

# I. Cryptanalysis of the Diffie-Hellman protocol.

print()
print("---------------------------------------------------------------")
print("    Cryptanalysis of the Diffie-Hellman public key protocol    ")
print("---------------------------------------------------------------")
print()

# 1. Collect public information, i.e., the prime, generator and sendings.

p = 2468642135797531
g = 2

A = 679217732839784 # A = g^{a} mod p where a is the secret integer of Alice
B = 1255037608816496 # B = g^{b} mod p where b is the secret integer of Bob

print("p:",p)
print("g:",g)
print("A:",A)
print("B:",B)
print()

''' # BruteForce
# A = 2^a mod p
# c = b^e mod m
for i in range(0,p): # not in the first 1 billion - took a few minutes to calculate
    x = pow(2,i,p)
    if(x==A):
        print("a:",i)
    elif(x==B):
        print("b:",i)
'''

# 2. Find an integer x in [1,p-1] s.t. g^{x} = A mod p and g^{x} = B mod p.
# Note that the complexity of this computation is exponential as it is the discrete logarithm problem.
x = discrete_log(p, A, 2)
y = discrete_log(p, B, 2)
print("x:",x)
print("y:",y)

if (pow(2,x,p) == A):
    print("a:",x)
    a = x

if (pow(2,y,p) == B):
    print("b:",y)
    b = y

print()

# 3. Compute the secret common key. (to verify correct keys)
k_a = pow(B,a,p)
k_b = pow(A,b,p)
print("k_a:",k_a,"\nk_b:",k_b)
k = k_a # Note that k = k_a = k_b
print("Their secret common key:",k)

print()

fa=bytes.fromhex(hex(a)[2:])
fb=bytes.fromhex(hex(b)[2:])

print("[+] a secret is: ",fa)
print("[+] b secret is: ",fb)
