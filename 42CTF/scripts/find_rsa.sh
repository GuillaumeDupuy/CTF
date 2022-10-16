#!/bin/bash

openssl rsa -noout -text -inform PEM -in key_pub1.pem -pubin > pubkey.txt
cat pubkey.txt | sed -e 's/^Pub.*//' -e 's/^Mod.*//' -e 's/Exp.*//' -e 's/://g' -e 's/ //g' > temp
tr -d '\n' < temp > N.txt
cat pubkey.txt > pubkey.txt
rm temp

# public key value ==> N
cat N.txt | xargs python -c "import sys; print(int(str(sys.argv[1]), 16))" > N.txt

# ciphertext value ==> c
cat message1.txt | xargs python -c "import sys; print(int(str(sys.argv[1]), 16))" > C.txt