# Project11: impl sm2 with RFC6979

## SM2

### 加密流程

![Alt text](1.png)

### 解密流程

![Alt text](2.png)

## 代码实现

### 十六进制字符串转十进制数

![Alt text](3.png)

### SM3-hash

使用gmssl的SM3-hash函数。
![Alt text](4.png)

### 求逆元

![Alt text](6.png)

### 椭圆曲线加法

![Alt text](7.png)

### 二倍点

![Alt text](8.png)

### 多倍点

![Alt text](9.png)

### 检查是否在椭圆曲线上

![Alt text](10.png)

### KDF

![Alt text](17.png)
![Alt text](5.png)

### 加密

同流程图。
![Alt text](1.png)
![Alt text](11.png)

### 解密

同流程图。
![Alt text](2.png)
![Alt text](12.png)

### 参数设定

![Alt text](16.png)
![Alt text](13.png)

## 运行结果

对随机数进行加密和解密。
![Alt text](14.png)
![Alt text](15.png)