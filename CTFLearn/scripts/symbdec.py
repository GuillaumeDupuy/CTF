s="^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"

s1=""
l=len(s)
c=0
l=l-1

while c<=l:
    ch=s[c]
    if ch=='!':
        s1=s1 +'1'
    elif ch =='@':
        s1=s1+'2'
    elif ch =='#':
        s1=s1+'3'
    elif ch =='$':
        s1=s1+'4'
    elif ch =='%':
        s1=s1+'5'
    elif ch =='^':
        s1=s1+'6'
    elif ch =='&':
        s1=s1+'7'
    elif ch =='*':
        s1=s1+'8'
    elif ch =='(':
        s1=s1+'9'
    elif ch ==')':
        s1=s1+'0'
    else:
        s1=s1+' '
    c=c+1

print(s1)