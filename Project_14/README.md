# Project14: Implement a PGP scheme with SM2

## SM2-PGP

分别采用对称加密和公钥加密进行加密。
加密时，使用会话密钥对明文M使用SM4加密，并对会话密钥使用SM2进行加密；解密时，先将会话密钥解密，再用解密得到的会话密钥解密密文得到明文M。
![Alt text](1.png)

## 代码实现

![Alt text](2.png)

## 运行结果

成功进行加解密操作。
![Alt text](3.png)
![Alt text](4.png)