import random

primes = [1019, 1031, 1039, 1051, 1063, 1087, 1091, 1103, 1123, 1151, 1163, 1171, 1187, 1223, 1231, 1259, 1279, 1283, 1291, 1303, 1307, 1319, 1327, 1367, 1399, 1423, 1427, 1439, 1447, 1451, 1459, 1471, 1483, 1487, 1499, 1511, 1523, 1531, 1543, 1559, 1567, 1571, 1579, 1583, 1607, 1619, 1627, 1663, 1667, 1699, 1723, 1747, 1759, 1783, 1787, 1811, 1823, 1831, 1847, 1867, 1871, 1879, 1907, 1931, 1951, 1979, 1987, 1999, 2003, 2011, 2027, 2039, 2063, 2083, 2087, 2099, 2111, 2131, 2143, 2179, 2203, 2207, 2239, 2243, 2251, 2267, 2287, 2311, 2339, 2347, 2351, 2371, 2383, 2399, 2411, 2423, 2447, 2459, 2467, 2503, 2531, 2539, 2543, 2551, 2579, 2591, 2647, 2659, 2663, 2671, 2683, 2687, 2699, 2707, 2711, 2719, 2731, 2767, 2791, 2803, 2819, 2843, 2851, 2879, 2887, 2903, 2927, 2939, 2963, 2971, 2999, 3011, 3019, 3023, 3067, 3079, 3083, 3119, 3163, 3167, 3187, 3191, 3203, 3251, 3259, 3271, 3299, 3307, 3319, 3323, 3331, 3343, 3347, 3359, 3371, 3391, 3407, 3463, 3467, 3491, 3499, 3511, 3527, 3539, 3547, 3559, 3571, 3583, 3607, 3623, 3631, 3643, 3659, 3671, 3691, 3719, 3727, 3739, 3767, 3779, 3803, 3823, 3847, 3851, 3863, 3907, 3911, 3919, 3923, 3931, 3943, 3947, 3967, 4003, 4007, 4019, 4027, 4051, 4079, 4091, 4099, 4111, 4127, 4139, 4159, 4211, 4219, 4231, 4243, 4259, 4271, 4283, 4327, 4339, 4363, 4391, 4423, 4447, 4451, 4463, 4483, 4507, 4519, 4523, 4547, 4567, 4583, 4591, 4603, 4639, 4643, 4651, 4663, 4679, 4691, 4703, 4723, 4751, 4759, 4783, 4787, 4799, 4831, 4871, 4903, 4919, 4931, 4943, 4951, 4967, 4987, 4999, 5003, 5011, 5023, 5039, 5051, 5059, 5087, 5099, 5107, 5119, 5147, 5167, 5171, 5179, 5227, 5231, 5279, 5303, 5323, 5347, 5351, 5387, 5399, 5407, 5419, 5431, 5443, 5471, 5479, 5483, 5503, 5507, 5519, 5527, 5531, 5563, 5591, 5623, 5639, 5647, 5651, 5659, 5683, 5711, 5743, 5779, 5783, 5791, 5807, 5827, 5839, 5843, 5851, 5867, 5879, 5903, 5923, 5927, 5939, 5987, 6007, 6011, 6043, 6047, 6067, 6079, 6091, 6131, 6143, 6151, 6163, 6199, 6203, 6211, 6247, 6263, 6271, 6287, 6299, 6311, 6323, 6343, 6359, 6367, 6379, 6427, 6451, 6491, 6547, 6551, 6563, 6571, 6599, 6607, 6619, 6659, 6679, 6691, 6703, 6719, 6763, 6779, 6791, 6803, 6823, 6827, 6863, 6871, 6883, 6899, 6907, 6911, 6947, 6959, 6967, 6971, 6983, 6991, 7019, 7027, 7039, 7043, 7079, 7103, 7127, 7151, 7159, 7187, 7207, 7211, 7219, 7243, 7247, 7283, 7307, 7331, 7351, 7411, 7451, 7459, 7487, 7499, 7507, 7523, 7547, 7559, 7583, 7591, 7603, 7607, 7639, 7643, 7687, 7691, 7699, 7703, 7723, 7727, 7759, 7823, 7867, 7879, 7883, 7907, 7919, 7927, 7951, 7963, 8011, 8039, 8059, 8087, 8111, 8123, 8147, 8167, 8171, 8179, 8191, 8219, 8231, 8243, 8263, 8287, 8291, 8311, 8363, 8387, 8419, 8423, 8431, 8443, 8447, 8467, 8527, 8539, 8543, 8563, 8599, 8623, 8627, 8647, 8663, 8699, 8707, 8719, 8731, 8747, 8779, 8783, 8803, 8807, 8819, 8831, 8839, 8863, 8867, 8887, 8923, 8951, 8963, 8971, 8999, 9007, 9011, 9043, 9059, 9067, 9091, 9103, 9127, 9151, 9187, 9199, 9203, 9227, 9239, 9283, 9311, 9319, 9323, 9343, 9371, 9391, 9403, 9419, 9431, 9439, 9463, 9467, 9479, 9491, 9511, 9539, 9547, 9551, 9587, 9619, 9623, 9631, 9643, 9679, 9719, 9739, 9743, 9767, 9787, 9791, 9803, 9811, 9839, 9851, 9859, 9871, 9883, 9887, 9907, 9923, 9931, 9967]

p = random.choice(primes)
q = random.choice(primes)

while(p == q):
    q = random.choice(primes)

#p = 1019
#q = 1031

n = p * q                                               # print(str(p) + " " + str(q) + " " + str(n))

with open("keys.txt", "w") as keys:
    keys.write(str(p)+str(q))

def DecimalToBinary(num):                               # Decimal to Binary
    binary_str = format(int(num), 'b')
    return binary_str



cypher = open('cypher.txt', 'w')

with open("plaintext.txt", "r") as plain:

    while True:
        char1 = plain.read(1)

        if not char1:
            break
    
        p = ord(char1)                                  # to ASCII
        bin_str = DecimalToBinary(p)                    # to binary
        p_str = bin_str + bin_str                       # entend

        m = int(p_str, 2)                               # to int

        c = (m ** 2) % n

        cyp = DecimalToBinary(c)

        while (len(cyp) != 32):
            cyp = '0' + cyp
        
        cypher.write(cyp)

cypher.close()