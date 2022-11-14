# Solution

```
└─$ ./Riyadh                      
Welcome to CTFlearn Riyadh Reversing Challenge!
Compile Options: ${CMAKE_CXX_FLAGS} -O0 -fno-stack-protector -mno-sse
Usage: Riyadh flag
```

Start with running the program and we we see the message `Usage: Riyadh flag` so I run with an argument this time. and get 
`You entered the wrong flag :-(`.

Fine it's time for Ghidra, let's see what is going on there. Checking the functions to find main, I notice several functinos called `Msg` and a number,
7 of them, that's interesting and clicking on one of them I see a XOR operations in a loop so yeah basically encrypted messages pretty cool.

How it affects us? Well, the thing is in reversing you first want to find the prints you get when running the program, this way you can understand where
you got and what checks you faild, but with those encrypted messages it's going to be hard.

```
    Msg1(buffer);
    puts(buffer);
    puts("Compile Options: ${CMAKE_CXX_FLAGS} -O0 -fno-stack-protector -mno-sse");
    if (param_1 == 1) {
        Msg2(buffer);
        puts(buffer);
    }
```
The main function start with that, and those are easy to understand.`Msg` is the greeting message, `Msg2` must be the usage message we get when not
passing any arguments.
```
    else {
        CTFLearnHiddenFlag();
        __s2 = *(char **)(param_2 + 8);
        Msg3(buffer);
        iVar4 = strcmp(buffer,__s2);
        if (iVar4 == 0) {
            param_1 = 2;
            Msg4(buffer);
            puts(buffer);
```
`CTFLearnHiddenFlag()` is an empty function with only `return`, I guess this way the author "commented" in the binary. We save the argument passed
in ``__s2` and call `Msg3` which is compared to the argument. Could it be the flag? most likely now because it is specified "HiddenFlag", but let's 
check what is it.

Run GDB, check where `Msg3` is called and put a breakpoint, then print the value of `buffer`.
```
(gdb) break *main+90
Breakpoint 1 at 0x115a
(gdb) run asdf
Starting program: /home/kali/Downloads/Riyadh/Riyadh asdf
Welcome to CTFlearn Riyadh Reversing Challenge!
Compile Options: ${CMAKE_CXX_FLAGS} -O0 -fno-stack-protector -mno-sse

Breakpoint 1, 0x000055555555515a in main ()
(gdb) x/s $rbp
0x5555555581c0 <buffer>:        "CTFlearn{Reversing_Is_Easy}"
```

Trying to pass this as the flag fails, makes sense, and passing it prints `You found the false flag!  It's not that easy dude!`, now we know that
this false flag is result of `Msg3` and the message we get for passing it is the result of `Msg4`

Next there is a lot of more code going on with loops and if statements. But we don't go reversing it all, instead we should take attention to this
```
        else {
            sVar5 = strlen(__s2);
            if (sVar5 == 0x1e) {
                param_1 = 0;
                puVar6 = (undefined8 *)operator.new[](0x100);
                Msg5((char *)puVar6);
                lVar7 = 0;
```
There is another encrypted message, this time `Msg5` and we totally want to know what is it. Similary as before we will place a breakpoint after the call
to the function and check what it returns. Notice that we need to pass a string with length 30, `if (sVar5 == 0x1e)`.

```
(gdb) break *main+151
Breakpoint 1 at 0x1197
(gdb) run aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Starting program: /home/kali/Downloads/Riyadh/Riyadh aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Welcome to CTFlearn Riyadh Reversing Challenge!
Breakpoint 1, 0x0000555555555197 in main ()o-stack-protector -mno-sse
(gdb) x/s $rbp
0x55555556b2c0: "CTFlearn{Masmak_Fortress_1865}"
```