import sys
import struct
import random
from math import gcd, ceil, floor
from gmssl import sm3


def int_hex(str):
    return int(str, 16)


def sm3_hash(message):
    message = message.encode('utf-8')
    msg_list = [i for i in message]
    hash_hex = sm3.sm3_hash(msg_list)

    return hash_hex


def inv(a, m):
    if gcd(a, m) != 1:
        return None

    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

    t1, x, t2 = extended_gcd(a, m)
    return x % m


def add_ECC(P, Q):
    if P == 0:
        return Q
    if Q == 0:
        return P
    x1, y1, x2, y2 = int_hex(P[0]), int_hex(P[1]), int_hex(Q[0]), int_hex(Q[1])
    q_int = int_hex(q)
    tmp1, tmp2 = y2 - y1, inv(x2 - x1 % q_int, q_int)
    l = tmp1 * tmp2 % q_int
    x = (l * l - x1 - x2) % q_int
    y = (l * (x1 - x) - y1) % q_int
    res = (hex(x)[2:], hex(y)[2:])
    return res


def double_ECC(P):
    if P == 0:
        return P
    x1, y1 = int_hex(P[0]), int_hex(P[1])
    a_int, q_int = int_hex(a), int_hex(q)
    tmp1 = 3 * x1 * x1 + a_int
    tmp2 = inv(2 * y1, q_int)
    l = (tmp1 * tmp2) % q_int
    x = (l * l - 2 * x1) % q_int
    y = (l * (x1 - x) - y1) % q_int
    Q = (hex(x)[2:], hex(y)[2:])
    return Q


def mul_ECC(P, k):
    k_bin = bin(k)[2:]
    i = len(k_bin) - 1
    Q = P
    if i > 0:
        k = k - 2**i
        while i > 0:
            Q = double_ECC(Q)
            i -= 1
        if (k > 0):
            Q = add_ECC(Q, mul_ECC(P, k))

    return Q


def check_ECC(P):
    x, y = int_hex(P[0]), int_hex(P[1])
    q_int, a_int, b_int = int_hex(q), int_hex(a), int_hex(b)
    if (y * y) % q_int == (x * x * x + a_int * x + b_int) % q_int:
        return True
    else:
        return False


#参数设定
q = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f"
a = "0"
b = "7"
x_G = "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
y_G = "483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8"
G = (x_G, y_G)
n = "fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141"
#私钥
d_A = hex(random.randint(pow(2, 127), pow(2, 128)))[2:]
P_A = mul_ECC(G, int_hex(d_A))


def legendre(n, p):
    return pow(n, (p - 1) // 2, p)


def QR(n, p):
    if legendre(n, p) == 1: return

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p): break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def ECMH(M):
    a_int, b_int, q_int = int_hex(a), int_hex(b), int_hex(q)
    y = -1
    while (y == -1):
        M_hash = sm3_hash(M)
        x = (pow(int_hex(M_hash), 3) + a_int * int_hex(M_hash) + b_int) % q_int
        y = QR(x, q_int)
    return hex(x)[2:], hex(y)[2:]


def ECMH_list(M_list):
    tmp = []
    for m in M_list:
        tmp.append(ECMH(m))
    
    res = tmp[0]
    for i in range(1,len(tmp)):
        res = add_ECC(res,tmp[i])
        
    return res


t1 = ECMH('66666')
print(t1)

t2 = ECMH_list(('66666', '77777', '88888'))
print(t2)