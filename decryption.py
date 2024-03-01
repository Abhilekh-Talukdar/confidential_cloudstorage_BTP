def DecimalToBinary(num):                               # Decimal to Binary
    binary_str = format(int(num), 'b')
    return binary_str


def repeatingString(string):
    length = len(string)
    midpoint = length // 2

    first_half = string[:midpoint]
    second_half = string[midpoint:]

    if first_half == second_half:
        return True
    else:
        return False


def euclidean_GCD(p, q):
    a=1
    b=1

    while(a<10000):
        b=1
        while(b < a*10):

            if (a*p - b*q == 1):
                return a, -b
            
            if(b*q - a*p == 1):
                return -a, b
            b = b+1
        a = a+1
    return a, b


keys = open('keys.txt', 'r')
p = int(keys.read(4))
q = int(keys.read(4))
n = p * q
keys.close()


a,b = euclidean_GCD(p, q)

decrypt = open('decrypt.txt', 'w')
with open("cypher.txt", "r") as cypher:
    while True:
        char1 = cypher.read(32)
    
        if not char1:
            break

        c = int(char1, 2)

        r = 1
        for i in range(0, int((p+1)/4)):                     # r = (c **((p+1)/4)) % p
            r = (r * c) % p
        
        s = 1
        for i in range(0, int((q+1)/4)):                     # s = (c **((q+1)/4)) % q
            s = (s * c) % q

        
        x = (a*p*s + b*q*r) % n
        y = (a*p*s - b*q*r) % n

        m1 = x
        m2 = y
        m3 = n - x
        m4 = n - y

        bin_m1 = DecimalToBinary(m1)
        bin_m2 = DecimalToBinary(m2)
        bin_m3 = DecimalToBinary(m3)
        bin_m4 = DecimalToBinary(m4)


        if repeatingString(bin_m1):
            length = len(bin_m1)
            midpoint = length // 2
            plain = bin_m1[:midpoint]
            
        elif repeatingString(bin_m2):
            length = len(bin_m2)
            midpoint = length // 2
            plain = bin_m2[:midpoint]

        elif repeatingString(bin_m3):
            length = len(bin_m3)
            midpoint = length // 2
            plain = bin_m3[:midpoint]

        elif repeatingString(bin_m4):
            length = len(bin_m4)
            midpoint = length // 2
            plain = bin_m4[:midpoint]
        
        else:
            plain = "1111110"
        
        m = int(plain, 2)
        decrypt.write(chr(m))

decrypt.close()      