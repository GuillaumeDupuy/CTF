## Solution

We get a bin file , Lets execute and see what we get.  

![Screenshot from 2019-12-09 15-32-45](https://user-images.githubusercontent.com/57364083/70432722-940d5e80-1a88-11ea-8aee-306b3b1dc609.png)

So we need to guess the password and the password should be the flag.  
Take a look in IDA to see the flow of the program.

<img width="501" alt="Capture" src="https://user-images.githubusercontent.com/57364083/70432900-f2d2d800-1a88-11ea-9bb1-7fb5a1bdb8ea.PNG">
 
Its look like after we enter the password the program store two important values-
1. strlen - len of our password
2. shr strlen , 1  =  **shr - shift right = divide by 2** , **shl - shift left = mul by 2** so the second value is **strlen/2**  

keep forward...

<img width="872" alt="Capture" src="https://user-images.githubusercontent.com/57364083/70433183-b81d6f80-1a89-11ea-9663-10d802755a24.PNG">
Because of "mov [rbp+var_CC], 0" we will take the jump to the right side. In the end after some operations that we will see now 
we will visit in the left side where the important compare has been executed and decide if our password is the correct flag.  
This is the operations that been executed on our password and then the been compared.    

<img width="479" alt="Capture" src="https://user-images.githubusercontent.com/57364083/70433973-b48ae800-1a8b-11ea-8f48-e0680cc4f165.PNG">

As you can see we have in the for loop this instruction "v18[j] = *(&v8 + i) ^ s[j];"   
s - array of our password    
*(&v8 + i) - we need to check the value , we will see in gdb  
v18 - array where the xor result been saved   

After that we have this instruction "if ( v18[k] != v14[k] )" And if the value are not the same we message get a "Wrong Password"    
So, If all the values in **v18 will equal to v14** we will get the good message "Successful Login""  

We now that in xor operation:  
**if (a^b == c ) -------> a^c == b , b^c ==a**   
So we need to preform ""v14[k] ^ *(&v8 + i) == s[k]"" lets find the missing parts  
After debug the program in gdb i found that the first half of our password been xor with **0x10** , And for the rest of our password been xor with **0x18**    
xor 'a' with 0x10 -  
![Screenshot from 2019-12-09 16-07-15](https://user-images.githubusercontent.com/57364083/70434629-6b3b9800-1a8d-11ea-8028-9359c5b4cfcb.png)

xor 'a' (in the second half of our password) with 0x18 -   

![Screenshot from 2019-12-09 16-25-42](https://user-images.githubusercontent.com/57364083/70435591-e7cf7600-1a8f-11ea-8c65-ad7e1ee2ef0d.png)

RDX is equal to "*(&v8 + i)"  and RAX is equal to "s[j]" and the result stored in "v18[j]".
So now we only need to find v14[k] that is need to be equal to "v18[j]" and xor with "*(&v8 + i)".
We can find v14[k] in gdb -  
![Screenshot from 2019-12-09 16-12-51](https://user-images.githubusercontent.com/57364083/70434894-2a904e80-1a8e-11ea-95b7-51e0a89bfbe4.png)

Now all we have to do is : xor the first half of **"h_bO}EcDOR+G)uh(jl,vL"** with **0x10** and the second half with **0x18**

#### First half  
<img width="1247" alt="Capture" src="https://user-images.githubusercontent.com/57364083/70434998-67f4dc00-1a8e-11ea-891f-2d4d76e8d137.PNG">

#### Second half  
<img width="1238" alt="Capture" src="https://user-images.githubusercontent.com/57364083/70435658-12b9ca00-1a90-11ea-92a4-57b0a3d25ba2.PNG">