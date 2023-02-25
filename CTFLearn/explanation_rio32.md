# Solution

This lesson seems quite easy, our task is to enter 2 numbers whose sum is 20 and their calculation is 100.

<img src="../files/rio.png" alt="Photo explain"/>

=> only a pair of numbers 10, 10 is satisfied

<img src="../files/rio2.png" alt="Photo explain"/>
<img src="../files/rio3.png" alt="Photo explain"/>

(edx holds the sum and eax holds the product)

But if we enter 10 10, we stumble upon a function check

<img src="../files/rio4.png" alt="Photo explain"/>

Notice in the program there is a function GetArgs

I created a patch, changed the check command in this function to help me enter 2 or more characters

Before transferring:

<img src="../files/rio5.png" alt="Photo explain"/>

After transferring

<img src="../files/rio6.png" alt="Photo explain"/>