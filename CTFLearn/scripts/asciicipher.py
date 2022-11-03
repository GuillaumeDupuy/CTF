def ascii_caesar_shift(message, distance):

    encrypted = ""

    for char in message:

        value = ord(char) + distance
        
        if value <= 33: # non-printable characters in ascii
            value -= 33
        encrypted += chr(value % 128) #128 for ASCII

    return encrypted
    
mess = '2m{y!”%w2\’z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0'

print(ascii_caesar_shift(mess, -18))