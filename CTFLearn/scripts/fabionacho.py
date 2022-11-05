import base64
from Cryptodome.Util import number


def find_fibonacci_index(values):
    ma = max(values)

    w = [0] * 100
    w[0] = 1
    w[1] = 1
    i = 2
    n = 0
    seq = [-1] * len(values)
    while n < ma:
        n = w[(i-1)%100] + w[(i-2)%100]
        w[i % 100] = n
        try:
            loc = -1
            while True:
                loc = values.index(n, loc+1, len(values)) 
                seq[loc] = i+1
        except ValueError:
            pass
        finally:
            i += 1

    return seq

buf = "OTI3MzcyNjkyMTkzMDc4OTk5MTc2IDE2NjQxMDI3NzUwNjIwNTYzNjYyMDk2IDgzNjIxMTQzNDg5ODQ4NDIyOTc3IDE1MDA1MjA1MzYyMDY4OTYwODMyNzcgMjI2OTgzNzQwNTIwMDY4NjM5NTY5NzU2ODIgOTI3MzcyNjkyMTkzMDc4OTk5MTc2IDc3Nzg3NDIwNDkgMTM1MzAxODUyMzQ0NzA2NzQ2MDQ5IDQ4MDc1MjY5NzYgNDM1NjY3NzYyNTg4NTQ4NDQ3MzgxMDUgMzI5NTEyODAwOTkgMjE4OTIyOTk1ODM0NTU1MTY5MDI2IDI0Mjc4OTMyMjgzOTk5NzUwODI0NTMgNDgwNzUyNjk3NiA1OTQyNTExNDc1NzUxMjY0MzIxMjg3NTEyNQ=="
values = base64.b64decode(buf).split()
values = list(map(int, values))
seq = find_fibonacci_index(values)
print(''.join(map(chr, seq)))