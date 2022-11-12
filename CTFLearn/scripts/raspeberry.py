import string
from subprocess import PIPE, Popen

flag = "CTFlearn{???????????????????????"
candidates = string.ascii_uppercase+string.ascii_lowercase+string.digits+'_'+'+'+'}'

for i in range(9, len(flag)):
    for c in candidates:
        flag = flag[:i] + c + flag[i+1:]
        p = Popen(["./Raspberry", flag], stdout=PIPE)
        output = p.stdout.read()
        if b'Bad Character' not in output:
            print("found", flag)
            break

        begin = output.find(b'kcbowhunter')+len('kcbowhunter')
        end = output.find(b'Bad', begin)
        matchs = output[begin:end].strip().split(b'\n')

        if len(matchs) > i:
            break

print('flag', flag)