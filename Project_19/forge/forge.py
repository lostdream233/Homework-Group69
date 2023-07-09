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


def ECDSA_sign(M):
    k = random.randint(1, int_hex(n) - 1)
    R = mul_ECC(G, k)
    r = int_hex(R[0]) % int_hex(n)
    e = sm3_hash(M)

    k_inv = inv(k, int_hex(n))
    tmp = int_hex(e) + int_hex(d) * r
    s = (k_inv * tmp) % int_hex(n)

    return hex(r)[2:], hex(s)[2:]


def ECDSA_verify(e, r, s):
    s_inv = inv(int_hex(s), int_hex(n))
    w = s_inv % int_hex(n)

    wG = mul_ECC(G, w)
    wP = mul_ECC(P, w)
    ewG = mul_ECC(wG, int_hex(e))
    rwP = mul_ECC(wP, int_hex(r))

    r_, s_ = add_ECC(ewG, rwP)
    if r == r_:
        return True
    return False


def forge():
    u, v = random.randint(1, int_hex(n) - 1), random.randint(1, int_hex(n) - 1)
    uG = mul_ECC(G, u)
    vP = mul_ECC(P, v)
    R = add_ECC(uG, vP)

    v_inv = inv(v, int_hex(n))
    r = int_hex(R[0]) % int_hex(n)
    s = (r * v_inv) % int_hex(n)
    e = (r * u * v_inv) % int_hex(n)

    return hex(r)[2:], hex(s)[2:], hex(e)[2:]


#参数设定
q = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f"
a = "0"
b = "7"
x_G = "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
y_G = "483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8"
G = (x_G, y_G)
n = "fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141"
d = hex(random.randint(pow(2, 127), pow(2, 128)))[2:]
P = mul_ECC(G, int_hex(d))

M = '6666'

r, s = ECDSA_sign(M)
print(f'r, s: {r, s}')

e = sm3_hash(M)
res = ECDSA_verify(e, r, s)
print(f'Res: {res}')

r_, s_, e_ = forge()
res_forge = ECDSA_verify(e_, r_, s_)
print(f'Res(forge): {res_forge}')