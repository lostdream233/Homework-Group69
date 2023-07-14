//
// Created by dell on 2023/6/11.
//

#include "SM4.h"

void R(int_32 *input, int_32 *output) {
    for (int i = 0; i < 4; i++) output[i] = input[3 - i];
}

void keyExpansion(const int_32 *MK, int_32 *RK) {
    int_32 K[36];
    int_32 i, j;

    for (i = 0; i < 4; i++) K[i] = MK[i] ^ FK[i];

    int_32 tmp1, tmp2, tmp3;
    int_8 a[4];
    int_8 b[4];
    for (i = 0; i < 32; i++) {
        tmp1 = K[i + 1] ^ K[i + 2] ^ K[i + 3] ^ CK[i];

        // 32b -> 8b
        for (j = 0; j < 4; j++) {
            tmp1 = j == 0 ? tmp1 : tmp1 >> 8;
            a[3 - j] = tmp1 & 0xff;
        }
        // Sbox
        int x, y;
        for (j = 0; j < 4; j++) {
            x = (a[j] >> 4) & 0xf;
            y = a[j] & 0xf;
            b[j] = Sbox[x][y];
        }
        // 8b -> 32b
        tmp2 = 0;
        for (j = 0; j < 4; j++)
            tmp2 |= (int_32) b[3 - j] << (j * 8);
        // L'
        tmp3 = tmp2 ^ (tmp2 << 13 | tmp2 >> 19) ^ (tmp2 << 23 | tmp2 >> 9);

        K[i + 4] = K[i] ^ (tmp3);
        RK[i] = K[i + 4];
    }
}

void SM4_Encrypt(const int_32 *MK, const int_32 *PT, int_32 *CT) {
    int_32 RK[32];
    keyExpansion(MK, RK);

    int_32 X[36];
    int_32 i, j, tmp1, tmp2, tmp3;

    for (i = 0; i < 4; i++) X[i] = PT[i];

    int_8 a[4];
    int_8 b[4];
    for (i = 0; i < 32; i++) {
        tmp1 = X[i + 1] ^ X[i + 2] ^ X[i + 3] ^ RK[i];

        // 32b -> 8b
        for (j = 0; j < 4; j++) {
            tmp1 = j == 0 ? tmp1 : tmp1 >> 8;
            a[3 - j] = tmp1 & 0xff;
        }
        // Sbox
        int x, y;
        for (j = 0; j < 4; j++) {
            x = (a[j] >> 4) & 0xf;
            y = a[j] & 0xf;
            b[j] = Sbox[x][y];
        }
        // 8b -> 32b
        tmp2 = 0;
        for (j = 0; j < 4; j++)
            tmp2 |= (int_32) b[3 - j] << (j * 8);
        // L
        tmp3 = tmp2 ^ (tmp2 << 2 | tmp2 >> 30) ^ (tmp2 << 10 | tmp2 >> 22) ^ (tmp2 << 18 | tmp2 >> 14) ^ (tmp2 << 24 | tmp2 >> 8);

        X[i + 4] = X[i] ^ tmp3;
    }

    int_32 Y[4];
    for (i = 0; i < 4; i++) Y[i] = X[i + 32];

    R(Y, CT);
}