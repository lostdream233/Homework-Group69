# Project1: implement the naïve birthday attack of reduced SM3

## 生日攻击

生日攻击基于生日悖论，对于长度为 $2^n$ 的hash值，只需要枚举 $2^{\frac{n}{2}}$ 次即可找到一对碰撞。

## 代码实现

函数attack()中对字符串进行枚举，当出现前n比特相同的hash值时返回结果。已经计算的hash值存储在preSubHash列表中。

![Alt text](2.png)

## 运行结果

寻找32比特的hash碰撞使用了47000+ms的时间，枚举次数也与2^16=65536接近。

![Alt text](1.png)
