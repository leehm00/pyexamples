最近在看深度学习的东西，一开始看的吴恩达的UFLDL教程，有中文版就直接看了，后来发现有些地方总是不是很明确，又去看英文版，然后又找了些资料看，才发现，中文版的译者在翻译的时候会对省略的公式推导过程进行补充，但是补充的又是错的，难怪觉得有问题。反向传播法其实是神经网络的基础了，但是很多人在学的时候总是会遇到一些问题，或者看到大篇的公式觉得好像很难就退缩了，其实不难，就是一个链式求导法则反复用。如果不想看公式，可以直接把数值带进去，实际的计算一下，体会一下这个过程之后再来推导公式，这样就会觉得很容易了。

　　说到神经网络，大家看到这个图应该不陌生：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNDA2NDQ0MDYtNDA5ODU5NzM3LnBuZw)

 

　　这是典型的三层神经网络的基本构成，Layer L1是输入层，Layer L2是隐含层，Layer L3是隐含层，我们现在手里有一堆数据{x1,x2,x3,...,xn},输出也是一堆数据{y1,y2,y3,...,yn},现在要他们在隐含层做某种变换，让你把数据灌进去后得到你期望的输出。如果你希望你的输出和原始输入一样，那么就是最常见的自编码模型（Auto-Encoder）。可能有人会问，为什么要输入输出都一样呢？有什么用啊？其实应用挺广的，在图像识别，文本分类等等都会用到，我会专门再写一篇Auto-Encoder的文章来说明，包括一些变种之类的。如果你的输出和原始输入不一样，那么就是很常见的人工神经网络了，相当于让原始数据通过一个映射来得到我们想要的输出数据，也就是我们今天要讲的话题。

　　本文直接举一个例子，带入数值演示反向传播法的过程，公式的推导等到下次写Auto-Encoder的时候再写，其实也很简单，感兴趣的同学可以自己推导下试试：）

　　假设，你有这样一个网络层：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNDE0NDk2NzEtMTA1ODY3Mjc3OC5wbmc)

　　第一层是输入层，包含两个神经元i1，i2，和截距项b1；第二层是隐含层，包含两个神经元h1,h2和截距项b2，第三层是输出o1,o2，每条线上标的wi是层与层之间连接的权重，激活函数我们默认为sigmoid函数。

　　现在对他们赋上初值，如下图：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNDIwMTkxNDAtNDAyMzYzMzE3LnBuZw)

　　其中，输入数据  i1=0.05，i2=0.10;

　　　　　输出数据 o1=0.01,o2=0.99;

　　　　　初始权重  w1=0.15,w2=0.20,w3=0.25,w4=0.30;

　　　　　　　　　  w5=0.40,w6=0.45,w7=0.50,w8=0.55

 

　　目标：给出输入数据i1,i2(0.05和0.10)，使输出尽可能与原始输出o1,o2(0.01和0.99)接近。

 

　　**Step 1 前向传播**

　　1.输入层---->隐含层：

　　计算神经元h1的输入加权和：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNDI5MTUzNTktMjk0NDYwMzEwLnBuZw)

神经元h1的输出o1:(此处用到激活函数为sigmoid函数)：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTAxMTUzOTAtMTAzNTM3ODAyOC5wbmc)

 

 

　　同理，可计算出神经元h2的输出o2：

　　![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTAyNDQyNjUtMTEyODMwMzI0NC5wbmc)

 

　　2.隐含层---->输出层：

　　计算输出层神经元o1和o2的值：

　　![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTA1MTcxMDktMzg5NDU3MTM1LnBuZw)

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTA2MzgzOTAtMTIxMDM2NDI5Ni5wbmc)

 

这样前向传播的过程就结束了，我们得到输出值为[0.75136079 , 0.772928465]，与实际值[0.01 , 0.99]相差还很远，现在我们对误差进行反向传播，更新权值，重新计算输出。

 

**Step 2 反向传播**

1.计算总误差

总误差：(square error)

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTEyMDE4MTItMTAxNDI4MDg2NC5wbmc)

但是有两个输出，所以分别计算o1和o2的误差，总误差为两者之和：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTE0NTc1OTMtMTI1MDUxMDUwMy5wbmc)

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTE1MDg5OTktMTk2Nzc0NjYwMC5wbmc)

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTE1MTYwOTMtMTI1NzE2NjczNS5wbmc)

 

2.隐含层---->输出层的权值更新：

以权重参数w5为例，如果我们想知道w5对整体误差产生了多少影响，可以用整体误差对w5求偏导求出：（链式法则）

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTE5MTY3OTYtMTAwMTYzODA5MS5wbmc)

下面的图可以更直观的看清楚误差是怎样反向传播的：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTIwMTg5MDYtMTUyNDMyNTgxMi5wbmc)

现在我们来分别计算每个式子的值：

计算![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTIyMDY3ODEtNzk3NjE2OC5wbmc)：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTIyNTg0MzctMTk2MDgzOTQ1Mi5wbmc)

计算![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTI0MTcxMDktNzExMDc3MDc4LnBuZw)：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTI1MTE5MzctMTY2NzQ4MTA1MS5wbmc)

（这一步实际上就是对sigmoid函数求导，比较简单，可以自己推导一下）

 

计算![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTI2MjU1OTMtMjA4MzMyMTYzNS5wbmc)：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTI2NTgxMDktMjE0MjM5MzYyLnBuZw)

最后三者相乘：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTI4MTE2NDAtODg4MTQwMjg3LnBuZw)

这样我们就计算出整体误差E(total)对w5的偏导值。

回过头来再看看上面的公式，我们发现：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTMxMDMxODctNTE1MDUyNTg5LnBuZw)

为了表达方便，用![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTMyMDI4MTItNTg1MTg2NTY2LnBuZw)来表示输出层的误差：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTMyNTEyMzQtMTE0NDUzMTI5My5wbmc)

因此，整体误差E(total)对w5的偏导公式可以写成：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTM0MDUyOTYtNDM2NjU2MTc5LnBuZw)

如果输出层误差计为负的话，也可以写成：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTM1MTQ3MzQtMTU0NDYyODAyNC5wbmc)

最后我们来更新w5的值：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTM2MTQzNzQtMTYyNDAzNTI3Ni5wbmc)

（其中，![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTM3MDAwOTMtNzQzODU5NjY3LnBuZw)是学习速率，这里我们取0.5）

同理，可更新w6,w7,w8:

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTM4MDc2MjQtMTIzMTk3NTA1OS5wbmc)

 

3.隐含层---->隐含层的权值更新：

　方法其实与上面说的差不多，但是有个地方需要变一下，在上文计算总误差对w5的偏导时，是从out(o1)---->net(o1)---->w5,但是在隐含层之间的权值更新时，是out(h1)---->net(h1)---->w1,而out(h1)会接受E(o1)和E(o2)两个地方传来的误差，所以这个地方两个都要计算。

 

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTQzMTc1NjItMzExMzY5NTcxLnBuZw)

 

计算![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTQ3MTIyMDItMTkwNjAwNzY0NS5wbmc)：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTQ3NTg1MzEtOTM0ODYxMjk5LnBuZw)

先计算![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTQ5NTgyOTYtMTkyMjA5NzA4Ni5wbmc)：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTUwMTU1NDYtMTEwNjIxNjI3OS5wbmc)

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTUwMzY0MDYtOTY0NjQ3OTYyLnBuZw)

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTUxMTc2NTYtMTkwNTkyODM3OS5wbmc)

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTUxNTg0NjgtMTU3MDMyMDA1LnBuZw)

同理，计算出：

　　　　　　　　　　![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTUzMTA5MzctMjEwMzkzODQ0Ni5wbmc)

两者相加得到总值：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTU0MzUyMTgtMzk2NzY5OTQyLnBuZw)

再计算![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTU1NTU1NjItMTQyMjI1NDgzMC5wbmc)：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTU2MjgwNDYtMjI5NTA1NDk1LnBuZw)

再计算![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTU3MzE0MjEtMjM5ODUyNzEzLnBuZw)：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTU3MDY0MzctOTY0ODYxNzQ3LnBuZw)

最后，三者相乘：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNTU4Mjc3MTgtMTg5NDU3NDA4LnBuZw)

 为了简化公式，用sigma(h1)表示隐含层单元h1的误差：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNjAzNDUyODEtNjc5MzA3NTUwLnBuZw)

最后，更新w1的权值：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNjA1MjM0MzctMTkwNjAwNDU5My5wbmc)

同理，额可更新w2,w3,w4的权值：

![img](jiangjie.assets/aHR0cHM6Ly9pbWFnZXMyMDE1LmNuYmxvZ3MuY29tL2Jsb2cvODUzNDY3LzIwMTYwNi84NTM0NjctMjAxNjA2MzAxNjA2MDM0ODQtMTQ3MTQzNDQ3NS5wbmc)

 

　　这样误差反向传播法就完成了，最后我们再把更新的权值重新计算，不停地迭代，在这个例子中第一次迭代之后，总误差E(total)由0.298371109下降至0.291027924。迭代10000次后，总误差为0.000035085，输出为[0.015912196,0.984065734](原输入为[0.01,0.99]),证明效果还是不错的。