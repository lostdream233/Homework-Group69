# Project2: implement the Rho method of reduced SM3

## Rho method

对于每个已经计算过的hash值，将其放入已计算的hash表中。如果之后的hash值已经存在于hash表中，则说明成功找到了一对碰撞。

## 代码实现

函数attack()中，将每个计算过的hash值存入preSubHash中，并在每次计算新的hash值时查找是否已经含有该hash值。
![Alt text](1.png)

## 运行结果

对于24比特的碰撞，只使用了400+ms的时间，效果明显优于生日碰撞攻击。
![Alt text](2.png)