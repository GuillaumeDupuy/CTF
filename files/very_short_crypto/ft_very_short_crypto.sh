#!/bin/bash

openssl rsa -noout -text -inform PEM -in pub.pem -pubin > pubkey
cat pubkey | sed -e 's/^Pub.*//' -e 's/^Mod.*//' -e 's/Exp.*//' -e 's/://g' -e 's/ //g' > temp
tr -d '\n' < temp > N
cat pubkey && echo ""
rm temp

cat N && echo "\n- modulus edited\n"

cat N | xargs python -c "import sys; print(int(str(sys.argv[1]), 16))"
echo "- public key value (integer) n\n"

cat ciphertext | xargs python -c "import sys; print(int(str(sys.argv[1]), 16))"
echo "- ciphertext value (integer) c"