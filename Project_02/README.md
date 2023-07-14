# Project2: implement the Rho method of reduced SM3

## Rho method

随机生成一个初始字符串，对其不断进行hash，直到找到碰撞。

## 代码实现

与生日攻击类似，只是改变了迭代方式。

![Alt text](1.png)

## 运行结果

对于32比特的碰撞，只使用了8700+ms的时间，时间消耗和枚举次数明显优于生日碰撞攻击。

![Alt text](2.png)
