def prng_lcg(multiplier, increment, modulus, x_n):
    x_next = (multiplier * x_n + increment) % modulus
    return x_next

def crack_c(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return increment

def crack_a(states, modulus):
    left = (states[2] - states[1]) % modulus
    delta = states[1] - states[0]
    k = 0
    while True:
        tries = left + modulus * k
        if (tries % delta == 0):                         # if (left + k * m) is divided by delta with no remainder, then we find it.
            multiplier = tries // delta
            return multiplier
        k += 1

xn = [65001687610455615650, 880901038222735, 16032398895653777]
m = 121409833232633162281
a = crack_a(xn, m)
c = crack_c(xn, m, a)
# print("a = " + str(a) + ", c = " + str(c))

x3 = prng_lcg(a, c, m, 16032398895653777)
x3 = str(x3)

i = 0
flag = "CTFlearn{"
while i < len(x3):
    flag += chr(int(x3[i:i+2]))
    i += 2
flag += "}"
print(flag)