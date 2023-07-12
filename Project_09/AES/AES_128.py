import numpy as np
import sys

#!S盒
s_box = [[
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B,
    0xFE, 0xD7, 0xAB, 0x76
],
         [
             0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2,
             0xAF, 0x9C, 0xA4, 0x72, 0xC0
         ],
         [
             0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5,
             0xF1, 0x71, 0xD8, 0x31, 0x15
         ],
         [
             0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80,
             0xE2, 0xEB, 0x27, 0xB2, 0x75
         ],
         [
             0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6,
             0xB3, 0x29, 0xE3, 0x2F, 0x84
         ],
         [
             0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE,
             0x39, 0x4A, 0x4C, 0x58, 0xCF
         ],
         [
             0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02,
             0x7F, 0x50, 0x3C, 0x9F, 0xA8
         ],
         [
             0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA,
             0x21, 0x10, 0xFF, 0xF3, 0xD2
         ],
         [
             0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E,
             0x3D, 0x64, 0x5D, 0x19, 0x73
         ],
         [
             0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8,
             0x14, 0xDE, 0x5E, 0x0B, 0xDB
         ],
         [
             0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC,
             0x62, 0x91, 0x95, 0xE4, 0x79
         ],
         [
             0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4,
             0xEA, 0x65, 0x7A, 0xAE, 0x08
         ],
         [
             0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74,
             0x1F, 0x4B, 0xBD, 0x8B, 0x8A
         ],
         [
             0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57,
             0xB9, 0x86, 0xC1, 0x1D, 0x9E
         ],
         [
             0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87,
             0xE9, 0xCE, 0x55, 0x28, 0xDF
         ],
         [
             0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D,
             0x0F, 0xB0, 0x54, 0xBB, 0x16
         ]]

#!轮常量
RCon = ((0x00, 0x00, 0x00, 0x00), (0x01, 0x00, 0x00, 0x00),
        (0x02, 0x00, 0x00, 0x00), (0x04, 0x00, 0x00, 0x00),
        (0x08, 0x00, 0x00, 0x00), (0x10, 0x00, 0x00, 0x00),
        (0x20, 0x00, 0x00, 0x00), (0x40, 0x00, 0x00, 0x00),
        (0x80, 0x00, 0x00, 0x00), (0x1b, 0x00, 0x00, 0x00), (0x36, 0x00, 0x00,
                                                             0x00))


#!密钥扩展
def key_expansion(key: str):
    key = list(key)
    w = []
    key_t = []

    #转为十六进制表示
    for num in key:
        num_hex = hex(ord(num))[2:]
        key_t.append(num_hex)
    #用0补位
    length = len(key)
    n = 16 - length
    while (n > 0):
        key_t.append('30')
        n -= 1
    key = key_t

    #print(key)

    #?循环移位
    def rot_word(w: list):
        return w[1:] + w[:1]

    #?S盒代换
    def sub_word(w):
        for index, num in enumerate(w):
            #十六进制表示的高位为行数，低位为列数
            y, x = int(w[index][0], 16), int(w[index][1], 16)
            #查表变换
            w[index] = (hex(s_box[y][x])[2:]).zfill(2)
        #print(w)

        return w

    #填充前4个字
    for i in range(4):
        w.append(list(key[4 * i:4 * i + 4]))

    #填充后面40个字
    for i in range(4, 44):
        temp = w[i - 1]
        #整除4时需要特殊处理
        if (i % 4 == 0):
            temp = sub_word(rot_word(temp))
            for j in range(4):
                temp[j] = int(temp[j], 16) ^ RCon[int(i / 4)][j]
            w_t = []
            for k in range(4):
                w_t.append(
                    hex(int(w[i - 4][k], 16) ^ int(temp[k]))[2:].zfill(2))
            w.append(w_t)
        #其他情况直接填充
        else:
            w_t = []
            for k in range(4):
                w_t.append(
                    hex(int(w[i - 4][k], 16) ^ int(temp[k], 16))[2:].zfill(2))
            w.append(w_t)
    #print(w)

    return w


#!1.sub_bytes
def sub_bytes(state: np.ndarray):

    #S盒变换
    #将矩阵展平后进行操作
    trans_list = state.flatten()
    for index, num in enumerate(trans_list):
        #十六进制表示的高位为行数，低位为列数
        loc_hex = trans_list[index].zfill(2)
        y, x = int(loc_hex[0], 16), int(loc_hex[1], 16)
        #查表变换
        trans_list[index] = (hex(s_box[y][x])[2:]).zfill(2)
    #print(trans_list)

    #转为4×4的状态矩阵
    state = np.array(trans_list).reshape(4, 4)
    #print(f'State:\n{state}\n')

    return state


#!2.shift_rows
def shift_rows(state: np.ndarray):
    #行移位
    for i in range(1, 4):
        state[i] = np.concatenate((state[i][i:], state[i][:i]), axis=0)
    #print(f'After shift_rows:\n{state}\n')

    return state


#!3.mix_column
def mix_column(state: np.ndarray):
    #得到state对应的行向量
    x0, x1, x2, x3 = state[0], state[1], state[2], state[3]

    #print(x0, x1, x2, x3)

    #?有限域上的乘2计算
    def mul2_GF(n: int):
        #如果n×2>=256，则要舍弃溢出位并异或0x1b
        m = n << 1
        if m >= 0xff:
            return (m & 0xff) ^ 0x1b
        else:
            return m

    #列混淆
    y0, y1, y2, y3 = [], [], [], []
    for j in range(4):
        s0 = int(x0[j], 16)
        s1 = int(x1[j], 16)
        s2 = int(x2[j], 16)
        s3 = int(x3[j], 16)

        y0.append(str(mul2_GF(s0 ^ s1) ^ s1 ^ s2 ^ s3))
        y1.append(str(mul2_GF(s1 ^ s2) ^ s0 ^ s2 ^ s3))
        y2.append(str(mul2_GF(s2 ^ s3) ^ s0 ^ s1 ^ s3))
        y3.append(str(mul2_GF(s3 ^ s0) ^ s0 ^ s1 ^ s2))
    state = np.vstack((y0, y1, y2, y3))
    #print(f'After mix_column:\n{state}\n')

    return state


#!4.add_round_key
def add_round_key(state: np.ndarray, round_key: list, i: int):
    #将轮密钥排列为4×4的矩阵
    round_key_matrix = np.vstack(round_key[i * 4:i * 4 + 4])
    #print(round_key_matrix)

    #将state和轮密钥的矩阵对应位置进行异或
    for i in range(4):
        for j in range(4):
            state[i][j] = int(state[i][j], 16) ^ int(round_key_matrix[i][j],
                                                     16)

    return state


#!AES加密
def AES_128(plaintext: str, key: str):
    #密钥扩展
    round_key = key_expansion(key)

    #将明文转为矩阵
    length = len(plaintext)
    text_list = list(plaintext)
    trans_list = []
    #转为十六进制表示
    for num in text_list:
        num_hex = hex(ord(num))[2:]
        trans_list.append(num_hex)
    #用0补位
    n = 16 - length
    while (n > 0):
        trans_list.append('30')
        n -= 1
    #print(trans_list)

    #明文转为4×4的状态矩阵
    state = np.array(trans_list).reshape(4, 4)
    state = state.T
    #print(f'State:\n{state}\n')

    #10轮加密
    for i in range(11):
        #第0轮：add_round_key
        if i == 0:
            state = add_round_key(state, round_key, i)
        #第1-9轮：
        elif i >= 1 and i <= 9:
            state = sub_bytes(state)
            state = shift_rows(state)
            state = mix_column(state)
            state = add_round_key(state, round_key, i)
        #第10轮
        else:
            state = sub_bytes(state)
            state = shift_rows(state)
            state = add_round_key(state, round_key, i)

    #转为十六进制表示
    temp = []
    for i in range(4):
        for j in range(4):
            temp.append(hex(int(state[i][j]))[2:])
    state = np.array(temp).reshape(4, 4)

    return state


if __name__ == '__main__':
    print('加密结果：')
    print(AES_128('202100460004', '202100460000'))