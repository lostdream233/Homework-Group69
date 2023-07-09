from gmssl import sm2, sm4


def sm2_enc(M, PK, SK):
    sm2_ = sm2.CryptSM2(public_key=PK, private_key=SK)
    return sm2_.encrypt(M)


def sm2_dec(CT, PK, SK):
    sm2_ = sm2.CryptSM2(public_key=PK, private_key=SK)
    return sm2_.decrypt(CT)


def sm4_enc(M, K):
    sm4_ = sm4.CryptSM4()
    sm4_.set_key(K, sm4.SM4_ENCRYPT)
    return sm4_.crypt_ecb(M)


def sm4_dec(CT, K):
    sm4_ = sm4.CryptSM4()
    sm4_.set_key(K, sm4.SM4_DECRYPT)
    return sm4_.crypt_ecb(CT)


def PGP_enc(M, K, PK, SK):
    M_enc = sm4_enc(M, K)
    K_enc = sm2_enc(K, PK, SK)

    return M_enc, K_enc


def PGP_dec(M_enc, K_enc, PK, SK):
    K = sm2_dec(K_enc, PK, SK)
    M = sm4_dec(M_enc, K)

    return M, K


SK = '0888B85B1FBFFE7573EA44BF6BE8B5CD578A2E8EE44A86F10536C2C48DC52A43'
PK = '77A8C798B2DC25D6E9819713976D38A52D45AA623C87BA294955A2AE498CEFDCC6E32B66C067BAE6B04D8CD638B3FC1C37F6563C6B38D0077EE17C666F308933'

K = b'66666666666666666666666666666666'
M = b'7777'

M_enc, K_enc = PGP_enc(M, K, PK, SK)
print((M_enc, K_enc))

M_dec, K_dec = PGP_dec(M_enc, K_enc, PK, SK)
print((M_dec, K_dec))