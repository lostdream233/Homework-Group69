# Project 20: ECMH PoC

## 核心思想

ECMH的核心思想是将hash映射为椭圆曲线上的点，利用椭圆曲线上的加法代替原始的hash求和算法，采用ECMH方式比传统的hash求和更加安全。

## 参数选取

采用secp256k1椭圆曲线实现ECMH，参数如下：
q = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0
b = 7
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
x_G = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
y_G = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
G = (x_G, y_G)

## 代码实现

函数ECMH()将明文的hash值映射到椭圆曲线上，以得到x。然后计算y = QR(x)，即y是x的二次剩余。

函数ECMH_list()则实现将多个hash值累加的功能。

![Alt text](1.png)

## 运行结果

![Alt text](2.png)

