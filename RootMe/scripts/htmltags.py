import string
import binascii

UC= string.ascii_uppercase
LC = string.ascii_lowercase
text = "HtmLheaDMEtaMEtaMetalINKLiNkLiNKTiTlETitLeheAdBODYheADerDivdIVAADiVDiVDiVdivNAvuLlIaAlILIaaLiLIAALilIAalIuLNavHEADerDiVSEctiONh1sPansPaNH1PPSECTIONSECTIONDIVH2H2ppdivsectionsectiondivh2h2ppdivdivh2h2ppdivsectionsectiondivppdivsectiondivscriptscriptscriptscriptscriptscriptscriptscriptscriptscriptbodyhtml"

b = []
x = ""
for c in text:
    if c in UC:
        x += "0"
    elif c in LC:
        x += "1"
    if len(x) == 8:
        b.append(x)
        x = ""

y = ""
for i in range(len(b)):
    X = int(b[i],2)
    H = hex(X)[2:]
    if len(H)%2 != 0:
        H = "0"+H
    try:
        z = binascii.unhexlify(H.encode()).decode()
        if z in string.printable:
            y += z
    except:
        continue