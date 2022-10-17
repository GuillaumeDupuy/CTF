import hashlib

comp = ['Free', 'Iliad', '42', 'Mediawan', 'Scaleway']
name = ['Delphine', 'Elisa', 'Michel', 'Camille', 'John', 'Jules']

for i in range(43):
    for r in range(1, 51):
        for c in comp:
            for n in name:
                s = str(i) + c + str(r) + n
                res = hashlib.md5(s.encode())
                print(s, res.hexdigest())