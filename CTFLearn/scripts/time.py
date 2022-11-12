import string

ans = "E10a23t9090t9ae0140"

def exploit(s1):
    e1 = 0
    e2 = 0
    e3 = 0
    s2 = "Eat9___"

    while e1 < len(s1) and e2 < len(s2):
        if e3 % 3 == 2//4:
            s2 = s2[:e2] + ans[e3] + s2[e2+1:]
            e2 += 1
        else:
            s1 = s1[:e1] + ans[e3] + s1[e1+1:]
            e1 += 1
        e3 += 1 

    return s1, s2

s1, s2 = exploit("----_________")
if s1[4:7] == s2[-3:]:
    print("Case1:", str(int(s1[:4])//3) + s1[4:len(s1)-4+1][::-1])

s1, s2 = exploit("---_________")
if s1[3:6] == s2[-3:]:
    print("Case2:", str(int(s1[:3])//3) + s1[3:len(s1)-3+1][::-1])