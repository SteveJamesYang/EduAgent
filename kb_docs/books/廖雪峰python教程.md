1 Python 基础 4

1.1 数据类型和变量 4  
1.2字符串和编码 8  
1.3 使用 list 和 tuple ..... 12  
1.4条件判断 16  
1.5循环 18  
1.6 使用dict和set. 19

2 函数 23

2.1调用函数 23  
2.2 定义函数 24  
2.3 函数的参数 27  
2.4 递归函数 33

3高级特性 36

3.1 切片 36  
3.2迭代 38  
3.3 列表生成式 39  
3.4 生成器 41  
3.5迭代器 45

4 函数式编程 47

4.1 高阶函数 47

4.1.1 map/reduce 48  
4.1.2 filter. 51  
4.1.3 sorted. 52

4.2返回函数 54  
4.3匿名函数 56  
4.4装饰器 56  
4.5 偏函数 59

5模块 61

5.1 使用模块 62  
5.2 安装第三方模块 64

6 面向对象编程 66

6.1 类和实例 67  
6.2 访问限制 69  
6.3 继承和多态 71  
6.4 获取对象信息 74  
6.5 实例属性和类属性 ..... 78

7 面向对象高级编程 80

7.1 使用slots 80  
7.2 使用@property 81  
7.3多重继承 83  
7.4 定制类 85  
7.5 使用枚举类 91  
7.6 使用元类 93

8错误、调试和测试 98

8.1错误处理 98  
8.2 调试 104

8.3单元测试 107  
8.4 文档测试 110

# 9IO编程 113

9.1 文件读写 113  
9.2 StringIO和BytesIO 115  
9.3 操作文件和目录 ..... 116  
9.4序列化 118

# 10 进程和线程 122

10.1 多进程 123  
10.2 多线程 ..... 127  
10.3 ThreadLocal 131  
10.4 进程 vs 线程 ..... 133  
10.5 分布式进程 134

# 11 正则表达式 ..... 138

# 12 常用内建模块 141

12.1 datetime 141  
12.2 collections 144  
12.3 base64 146  
12.4 struct 148  
12.5 hashlib 149  
12.6 itertools 151  
12.7 XML 153  
12.8 HTMLParser 155  
12.9urllib 156

# 13 常用第三方模块 160

13.1 PIL 160  
13.2 virtualenv 161

# 14 图形界面 163

# 15 网络编程 ..... 165

15.1 TCP/IP简介 165  
15.2 TCP编程 166  
15.3 UDP编程 169

# 16 电子邮件 ..... 170

16.1 SMTP发送邮件 171  
16.2 POP3 收取邮件 ..... 175

# 17 访问数据库 179

17.1 使用SQLite 181  
17.2 使用MySQL 183  
17.3 使用 SQLAlchemy 184

# 18 Web 开发 ..... 187

18.1 HTTP协议简介 187  
18.2 HTML 简介 190  
18.3 WSGI 接口 ..... 193  
18.4 使用Web框架 195  
18.5 使用模板 197

# 19 异步 IO 201

19.1 协程 201  
19.2asyncio 203  
19.3 async/await 205  
19.4 aiohttp 206

20 实战 208

From Cameocus

# 1 Python 基础

Python 是一种计算机编程语言。计算机编程语言和我们日常使用的自然语言有所不同，最大的区别就是，自然语言在不同的语境下有不同的理解，而计算机要根据编程语言执行任务，就必须保证编程语言写出的程序决不能有歧义，所以，任何一种编程语言都有自己的一套语法，编译器或者解释器就是负责把符合语法的程序代码转换成 CPU 能够执行的机器码，然后执行。Python 也不例外。

Python 的语法比较简单，采用缩进方式，写出来的代码就像下面的样子。

```python
print absolute value of an integer:  
a = 100  
if a >= 0:  
    print(a)  
else:  
    print(-a)
```

以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。其他每一行都是一个语句，当语句以冒号：结尾时，缩进的语句视为代码块。

缩进有利有弊。好处是强迫你写出格式化的代码，但没有规定缩进是几个空格还是Tab。按照约定俗成的管理，应该始终坚持使用4个空格的缩进。缩进的另一个好处是强迫你写出缩进较少的代码，你会倾向于把一段很长的代码拆分成若干函数，从而得到缩进较少的代码。

缩进的坏处就是“复制一粘贴”功能失效了，这是最坑爹的地方。当你重构代码时，粘贴过去的代码必须重新检查缩进是否正确。此外，IDE很难像格式化Java代码那样格式化Python代码。

最后，请务必注意，Python程序是大小写敏感的，如果写错了大小写，程序会报错。

Python 使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用 4 个空格的缩进。

在文本编辑器中，需要设置把Tab自动转换为4个空格，确保不混用Tab和空格。

# 1.1 数据类型和变量

数据类型

计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地可以处理各种数值。但是，计算机能处理的远不止数值，还可以处理文本、图形、音频、视频、网页等各种各样的数据，不同的数据，需要定义不同的数据类型。在Python中，能够直接处理的数据类型有以下几种：

·整数

Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

·浮点数

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如， $1.23 \times 10^{9}$  和  $12.3 \times 10^{8}$  是完全相等的。浮点数可以用数学写法，如 1.23, 3.14, -9.01, 等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把 10 用 e 替代， $1.23 \times 10^{9}$  就是  $1.23 \mathrm{e} 9$  ，或者  $12.3 \mathrm{e} 8$  ，0.000012 可以写成  $1.2 \mathrm{e} - 5$  ，等等。

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

- 字符串

字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，0，K这6个字符。

如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：

```txt
'I\`m \\"OK\"!
```

表示的字符串内容是：

```csv
I'm "OK"!
```

转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看：

```perl
>>> print('I\'m ok.')  
I'm ok.  
>>> print('I\'m learning\nPython.')  
I'm learning  
Python.  
>>> print('\\n')  
\
```

如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python 还允许用 r'' 表示'' 内部的字符串默认不转义，可以自己试试：

```txt
>>> print('\\\\t\\\\')  
\  
>>> print(r'\\\\t\\\\')  
\\\\t
```

如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用''...''的格式表示多行内容，可以自己试试：

```txt
>>> print('''line1
...
...
...
...
...
...
...
line1
...
line2
...
line3
```

上面是在交互式命令行内输入，注意在输入多行内容时，提示符由>>>变为...，提示你可以接着上一行输入。如果写成程序，就是：

```txt
print('''line1 line2 line3'')
```

多行字符串'...'...''还可以在前面加上r使用，请自行测试。

# ·布尔值

布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：

```txt
>>> True and True  
True  
>>> True and False  
False  
>>> False and False  
False  
>>> 5 > 3 and 3 > 1  
True
```

or 运算是或运算，只要其中有一个为 True，or 运算结果就是 True:

```txt
>>> True or True  
True  
>>> True or False  
True
```

```txt
>>>False or False False   
>>>5>3or1>3 True
```

not 运算是非运算，它是一个单目运算符，把 True 变成 False，False 变成 True:

```txt
>>> not True  
False  
>>> not False  
True  
>>> not 1 > 2  
True
```

布尔值经常用在条件判断中，比如：

```javascript
if age  $\geq 18$  print('adult') else: print('teenager')
```

# ·空值

空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。

# ·变量

变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，比如：

```txt
a = 1
```

变量a是一个整数。

```python
t_007 = 'T007'
```

变量t_007是一个字符串。

```txt
Answer = True
```

变量 Answer 是一个布尔值 True。

在Python中，等号  $=$  是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：

```txt
a = 123 # a 是整数  
print(a)  
a = 'ABC' # a 变为字符串  
print(a)
```

这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如 Java 是静态语言，赋值语句如下（// 表示注释）：

```txt
int a = 123; // a 是整数类型变量  
a = "ABC"; // 错误：不能把字符串赋给整型变量
```

和静态语言相比，动态语言更灵活，就是这个原因。

请不要把赋值语句的等号等同于数学的等号。比如下面的代码：

```latex
$\begin{array}{l}\texttt{x} = \texttt{10}\\ \texttt{x} = \texttt{x} +\texttt{2} \end{array}$
```

如果从数学上理解  $x = x + 2$  那无论如何是不成立的，在程序中，赋值语句先计算右侧的表达式  $x + 2$ ，得到结果12，再赋给变量  $x$ 。由于  $x$  之前的值是10，重新赋值后， $x$  的值变成12。

最后，理解变量在计算机内存中的表示也非常重要。当我们写：

```txt
a = 'ABC'
```

时，Python解释器干了两件事情：

1. 在内存中创建了一个'ABC'的字符串；  
2. 在内存中创建了一个名为 a 的变量，并把它指向 'ABC'。

也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：

```txt
a = 'ABC'  
b = a  
a = 'XYZ'  
print(b)
```

最后一行打印出变量b的内容到底是'ABC'呢还是'XYZ'?如果从数学意义上理解，就会错误地得出b和a相同，也应该是'XYZ'，但实际上b的值是'ABC'，让我们一行一行地执行代码，就可以看到到底发生了什么事：

执行  $a = \text{ABC}$ ，解释器创建了字符串 'ABC' 和变量 a，并把 a 指向 'ABC'：

![](images/50f357413da765441f682620806f62f9890d1a458c62bf2b11417253aeb2fad1.jpg)

执行  $\mathsf{b} = \mathsf{a}$ ，解释器创建了变量  $\mathsf{b}$ ，并把  $\mathsf{b}$  指向  $\mathsf{a}$  指向的字符串 'ABC'：

![](images/ce34b6c4e5fb3ac3422742da7c1b4cb86403e571f0a03a1596c3d403b00b2b2d.jpg)

执行  $a = {}^{\prime}XYZ^{\prime}$  ，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：

![](images/5004687bdcd48a3575ff3f8545b4fdf744b1eebe1ecc6b9f2e7f033e22ef95eb.jpg)

所以，最后打印变量b的结果自然是'ABC'了。

# ·常量

所谓常量就是不能变的变量，比如常用的数学常数  $\pi$  就是一个常量。在Python中，通常用全部大写的变量名表示常量：

```txt
PI = 3.14159265359
```

但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。

最后解释一下整数的除法为什么也是精确的。在Python中，有两种除法，一种除法是:/:

```txt
>>> 10 / 3  
3.333333333333335
```

除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

```txt
>>9/3 3.0
```

还有一种除法是//，称为地板除，两个整数的除法仍然是整数：

```txt
>>>10//3 3
```

你没有看错，整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以。因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：

```txt
>>> 10 % 3  
1
```

# 1.2 字符串和编码

# - 字符编码

我们已经讲过了，字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。

因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制  $11111111 =$  十进制255)，如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。

由于计算机是美国人发明的，因此，最早只有127个字母被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。

但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。

你可以想得到的是，全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。

![](images/ca38881b1d144338f6a328dc9149d0aeb7600183c5752311803ea744476edd32.jpg)

因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。

Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。

现在，捋一捋 ASCII 编码和 Unicode 编码的区别：ASCII 编码是 1 个字节，而 Unicode 编码通常是 2 个字节。

字母A用ASCII编码是十进制的65，二进制的01000001；

字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；

汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的0100111000101101。

你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是000000001000001。

新的问题又出现了：如果统一成 Unicode 编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用 Unicode 编码比 ASCII 编码需要多一倍的存储空间，在存储和传输上就十分不划算。

所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

<table><tr><td>字符</td><td>ASCII</td><td>Unicode</td><td>UTF-8</td></tr><tr><td>A</td><td>01000001</td><td>00000000 01000001</td><td>01000001</td></tr><tr><td>中</td><td>x</td><td>01001110 00101101</td><td>11100100 10111000 10101101</td></tr></table>

从上面的表格还可以发现，UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

搞清楚了 ASCII、Unicode 和 UTF-8 的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的 UTF-8 字符被转换为 Unicode 字符到内存里，编辑完成后，保存的时候再把 Unicode 转换为 UTF-8 保存到文件：

![](images/d2d57b3035d72c536fc1e897382d1e3027cc79e8d032add0878c8082e9b427f0.jpg)

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：

![](images/fa87d73b9c7bccd9a13b6071cbd14cdfb843cf2cefae9d2f526e96e608e51443.jpg)

所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的 UTF-8 编码。

# - Python 的字符串

搞清楚了令人头疼的字符编码问题后，我们再来研究Python的字符串。

在最新的Python3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：

```txt
>>> print('包含中文的 str')
```

包含中文的 str

对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

```txt
>>>ord('A')   
65   
>>>ord('中')   
20013   
>>>chr(66)   
'B'   
>>>chr(25991)   
文
```

如果知道字符的整数编码，还可以用十六进制这么写 str:

```txt
>>> '\u4e2d'\u6587'  
中文'
```

两种写法完全是等价的。

由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

Python对bytes类型的数据用带b前缀的单引号或双引号表示：

```latex
$\mathbf{x} = \mathbf{b}'\mathbf{A}\mathbf{B}\mathbf{C}'$
```

要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：

```txt
>>> 'ABC'.encode('ascii')  
b'ABC'  
>>> '中文'.encode('utf-8')  
b'\xe4\xb8\xad\xe6\x96\x87'  
>>> '中文'.encode('ascii')  
Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>  
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

纯英文的 str 可以用 ASCII 编码为 bytes，内容是一样的，含有中文的 str 可以用 UTF-8 编码为 bytes。含有中文的 str 无法用 ASCII 编码，因为中文编码的范围超过了 ASCII 编码的范围，Python 会报错。

在 bytes 中，无法显示为 ASCII 字符的字节，用 \x##显示。

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是 bytes。要把 bytes 变为 str，就需要用 decode() 方法：

```txt
>>>b'ABC'.decode('ascii') 'ABC'   
>>>b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') '中文'
```

要计算 str 包含多少个字符，可以用 len()函数：

```txt
>>>len('ABC')   
3   
>>>len('中文')   
2
```

len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：

```python
>>>len(b'ABC')   
3   
>>>len(b'\xe4\xb8\dad\xe6\x96\x87')   
6   
>>>len('中文'.encode('utf-8'))   
6
```

可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

在操作字符串时，我们经常遇到 str 和 bytes 的互相转换。为了避免乱码问题，应当始终坚持使用 UTF-8 编码对 str 和 bytes 进行转换。

由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

```shell
!/usr/bin/env python3
# --coding: utf-8 --
```

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

申明了 UTF-8 编码并不意味着你的.py 文件就是 UTF-8 编码的，必须并且要确保文本编辑器正在使用 UTF-8 without BOM 编码：

![](images/ac28d2d2572bb8dd5bc7ad7141e68a3df0b756da38db334c54ee00e057b64dbe.jpg)

如果.py文件本身使用UTF-8编码，并且也申明了# -\*-coding：utf-8 -\*-，打开命令提示符测试就可以正常显示

![](images/86e2b24fc98a626b0bb82ce71c08b820c90b9400e8c0cd1c9e39966044cc507c.jpg)

中文：

# - 格式化

最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。

'Hi %s, your score is %d.' % ('Bart', 59)

![](images/0cce1947c8f1e9d678c6e3c1177d7e82634a86b1b8e32bd730694a16f214634c.jpg)

![](images/501042aa514e9846850cacdc7c5e822c86976444793d97eac4ca67df2a134145.jpg)

在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：

```perl
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
```

你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%，括号可以省略。

常见的占位符有：

<table><tr><td>%d</td><td>整数</td></tr><tr><td>%f</td><td>浮点数</td></tr><tr><td>%s</td><td>字符串</td></tr><tr><td>%x</td><td>十六进制整数</td></tr></table>

其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

```txt
>>> '2d-%02d' % (3, 1)  
' 3-01'  
>>> '%.2f' % 3.1415926  
'3.14'
```

如果你不太确定应该用什么，%s 永远起作用，它会把任何数据类型转换为字符串：

```txt
>>> 'Age: %s. Gender: %s' % (25, True)  
'Age: 25. Gender: True'
```

有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

```txt
>>> 'growth rate: %d %' % 7 'growth rate: 7'
```

·练习

小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位。

# 1.3 使用list和tuple

- list

Python 内置的一种数据类型是列表：list。list 是一种有序的集合，可以随时添加和删除其中的元素。

比如，列出班里所有同学的名字，就可以用一个list表示：

```python
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']
```

变量 classmates 就是一个 list。用 len()函数可以获得 list 元素的个数：

```txt
>>>len(classmates) 3
```

用索引来访问 list 中每一个位置的元素，记得索引是从  $\theta$  开始的：

```txt
>>> classmates[0]  
'Michael'  
>>> classmates[1]  
'Bob'
```

```txt
>>> classmates[2]  
'Tracy'  
>>> classmates[3]  
Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>  
IndexError: list index out of range
```

当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。

如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：

```txt
>>> classmates[-1] 'Tracy'
```

以此类推，可以获取倒数第2个、倒数第3个：

```txt
>>> classmates[-2] 'Bob'   
>>> classmates[-3] 'Michael'   
>>> classmates[-4]   
Traceback (most recent call last): File "<stdin>", line 1, in <module>   
IndexError: list index out of range
```

当然，倒数第4个就越界了。

list 是一个可变的有序表，所以，可以往 list 中追加元素到末尾：

```python
>>> classmates.append('Adam')  
>>> classmates  
['Michael', 'Bob', 'Tracy', 'Adam']
```

要删除 list 末尾的元素，用 pop()方法：

```coffeescript
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']
```

要删除指定位置的元素，用 pop(i) 方法，其中 i 是索引位置：

```coffeescript
>>> classmates.pop(1) 'Jack'   
>>> classmates ['Michael', 'Bob', 'Tracy']
```

要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

```python
>>> classmates[1] = 'Sarah'  
>>> classmates  
['Michael', 'Sarah', 'Tracy']  
list里面的元素的数据类型也可以不同，比如：  
>>> L = ['Apple', 123, True]  
list元素也可以是另一个list，比如：  
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
```

```txt
>>> len(s) 4
```

注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：

```txt
>>> p = ['asp', 'php']
>>> s = ['python', 'java', p, 'scheme']
```

要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。

如果一个 list 中一个元素也没有，就是一个空的 list，它的长度为 0:

```txt
>>> L = []  
>>> len(L)  
0
```

- tuple

另一种有序列表叫元组：tuple。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改，比如同样是列出同学的名字：

```python
>>> classmates = ('Michael', 'Bob', 'Tracy')
```

现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

不可变的 tuple 有什么意义？因为 tuple 不可变，所以代码更安全。如果可能，能用 tuple 代替 list 就尽量用 tuple。

tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：

```txt
>>> t = (1, 2)  
>>> t  
(1, 2)
```

如果要定义一个空的 tuple，可以写成():

```txt
>>> t = ()  
>>> t  
()
```

但是，要定义一个只有1个元素的tuple，如果你这么定义：

```erlang
>>> t = (1)  
>>> t  
1
```

定义的不是 tuple，是 1 这个数！这是因为括号()既可以表示 tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python 规定，这种情况下，按小括号进行计算，计算结果自然是 1。

所以，只有1个元素的tuple定义时必须加一个逗号，，来消除歧义：

```txt
>>> t = (1,)  
>>> t  
(1,)
```

Python 在显示只有 1 个元素的 tuple 时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

最后来看一个“可变的”tuple:

```txt
>>> t = ('a', 'b', ['A', 'B'])  
>>> t[2][0] = 'X'  
>>> t[2][1] = 'Y'
```

```txt
>>>t (a'，'b'，['X'，'Y']）
```

这个 tuple 定义的时候有 3 个元素，分别是 'a'，'b' 和一个 list。不是说 tuple 一旦定义后就不可变了吗？怎么后来又变了？

别急，我们先看看定义的时候 tuple 包含的 3 个元素：

![](images/ba94a1491058c0f4a80971fe43e899790e87e174a7bec2e0272ac2eca395a52f.jpg)

当我们把 list 的元素 'A' 和 'B' 修改为 'X' 和 'Y' 后，tuple 变为：

![](images/c7c60a8ad75ad1e882d95108013d3747e6b04e5f4d41d9d32e2fdcea4cdb091a.jpg)

表面上看，tuple 的元素确实变了，但其实变的不是 tuple 的元素，而是 list 的元素。tuple 一开始指向的 list 并没有改成别的 list，所以，tuple 所谓的“不变”是说，tuple 的每个元素，指向永远不变。即指向 'a'，就不能改成指向 'b'，指向一个 list，就不能改成指向其他对象，但指向的这个 list 本身是可变的！

理解了“指向不变”后，要创建一个内容也不变的 tuple 怎么做？那就必须保证 tuple 的每一个元素本身也不能变。

·练习

请用索引取出下面 list 的指定元素：

```txt
# -- coding: utf-8 --  
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]  
# 打印 Apple:
print(?)  
# 打印 Python:
```

```txt
print(?) #打印Lisa: print(?)
```

# 1.4条件判断

# ·条件判断

计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。

比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：

```python
age  $= 20$    
if age  $\geq 18$  .. print('your age is', age) print('adult')
```

根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：

```python
age  $= 3$    
if age  $\geq 18$  .. print('your age is', age) print('adult')   
else: print('your age is', age) print('teenager')
```

注意不要少写了冒号：。

当然上面的判断是很粗略的，完全可以用elif做更细致的判断：

```txt
age  $= 3$    
if age  $\geqslant 18$  print('adult')   
elif age  $\geqslant 6$  print('teenager')   
else: print('kid')
```

elif是elseif的缩写，完全可以有多个elif，所以if语句的完整形式就是：

```txt
if <条件判断1>： <执行1>   
elif <条件判断2>： <执行2>   
elif <条件判断3>： <执行3>   
else: <执行4>
```

if 语句执行有个特点，它是从上往下判断，如果在某个判断上是 True，把该判断对应的语句执行后，就忽略掉剩下的elif和 else，所以，请测试并解释为什么下面的程序打印的是 teenager:

```txt
age  $= 20$    
if age  $\Rightarrow 6$  print('teenager')   
elif age  $\Rightarrow 18$  . print('adult')   
else: print('kid')
```

if判断条件还可以简写，比如写：

```python
if x: print('True')
```

只要  $x$  是非零数值、非空字符串、非空 list 等，就判断为 True，否则为 False。

- 再议 input

最后看一个有问题的条件判断。很多同学会用 input()读取用户的输入，这样可以自己输入，程序运行得更有意思：

```txt
birth  $=$  input('birth:'）  
if birth  $<  2000$  ： print('00前')  
else: print('00后')
```

输入1982，结果报错：

```typescript
Traceback (most recent call last): File "<stdin>", line 1, in <module>TypeError: unorderable types: str() > int()
```

这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：

```python
s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
```

再次运行，就可以得到正确地结果。但是，如果输入 abc 呢？又会得到一个错误信息：

```txt
Traceback (most recent call last): File "<stdin>", line 1, in <module> ValueError: invalid literal for int() with base 10: 'abc'
```

原来int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了。

如何检查并捕获程序运行期的错误呢？后面的错误和调试会讲到。

·练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

- 低于18.5：过轻  
18.5-25：正常

25-28：过重  
28-32：肥胖  
- 高于32：严重肥胖

用if-elif判断并打印结果。

# 1.5 循环

# ·循环

要计算  $1 + 2 + 3$  ，我们可以直接写表达式

```txt
>>1+2+3 6
```

要计算  $1 + 2 + 3 + \dots + 10$ ，勉强也能写出来。

但是，要计算  $1 + 2 + 3 + \ldots + 10000$  ，直接写表达式就不可能了。

为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。

Python 的循环有两种，一种是 for...in 循环，依次把 list 或 tuple 中的每个元素迭代出来，看例子：

```txt
names  $=$  ['Michael', 'Bob', 'Tracy'] for name in names: print(name)
```

执行这段代码，会依次打印 names 的每一个元素：

```txt
Michael   
Bob   
Tracy
```

所以 for x in ... 循环就是把每个元素代入变量 x，然后执行缩进块的语句。

再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：

```txt
sum  $= 0$    
for  $\mathbf{x}$  in [1,2,3,4,5,6,7,8,9,10]: sum  $=$  sum  $^+\times$    
print(sum)
```

如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：

```txt
>>> list(range(5))  
[0, 1, 2, 3, 4]
```

range(101)就可以生成 0-100 的整数序列，计算如下：

```txt
sum  $= 0$    
for  $\mathbf{x}$  in range(101): sum  $=$  sum  $^+$  x   
print(sum)
```

请自行运行上述代码，看看结果是不是当年高斯同学心算出的5050。

第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：

```txt
sum  $= 0$    
n  $= 99$    
while  $\mathsf{n} > \mathsf{0}$  .. sum  $=$  sum  $+$  n n  $= \texttt{n - 2}$    
print(sum)
```

在循环内部变量  $n$  不断自减，直到变为-1时，不再满足while条件，循环退出。

·练习

请利用循环依次对list中的每个名字打印出Hello，xxx！：

```txt
$\# -^{*} -$  coding: utf-8  $-^{*} -$  L  $=$  ['Bart', 'Lisa', 'Adam']
```

# 1.6 使用dict和set

- dict

Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

举个例子，假设要根据同学的名字查找对应的成绩，如果用 list 实现，需要两个 list:

```toml
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
```

给定一个名字，要查找对应的成绩，就先要在 names 中找到对应的位置，再从 scores 取出对应的成绩，list 越长，耗时越长。

如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：

```txt
>>>d  $=$  {'Michael':95,'Bob':75,'Tracy':85}   
>>>d['Michael']   
95
```

为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

dict 就是第二种实现方式，给定一个名字，比如 'Michael'，dict 在内部就可以直接计算出 Michael 对应的存放成绩的 "页码"，也就是 95 这个数字存放的内存地址，直接取出来，所以速度非常快。

你可以猜到，这种 key-value 存储方式，在放进去的时候，必须根据 key 算出 value 的存放位置，这样，取的时候才能根据 key 直接拿到 value。

把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：

```txt
>>>d['Adam']=67   
>>>d['Adam']   
67
```

由于一个 key 只能对应一个 value，所以，多次对一个 key 放入 value，后面的值会把前面的值冲掉：

```txt
>>>d['Jack']  $= 90$
```

```txt
>>>d['Jack']   
90   
>>>d['Jack']  $= 88$    
>>>d['Jack']   
88
```

如果key不存在，dict就会报错：

```txt
>>> d['Thomas']  
Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>  
KeyError: 'Thomas'
```

要避免 key 不存在的错误，有两种办法，一是通过 in 判断 key 是否存在：

```txt
>>> 'Thomas' in d False
```

二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value:

```txt
>>> d.get('Thomas')  
>>> d.get('Thomas', -1)  
-1
```

注意：返回 None 的时候 Python 的交互式命令行不显示结果。

要删除一个 key，用 pop(key) 方法，对应的 value 也会从 dict 中删除：

```txt
>>>d.pop('Bob')   
75   
>>>d   
{'Michael':95,'Tracy':85}
```

请务必注意，dict 内部存放的顺序和 key 放入的顺序是没有关系的。

和 list 比较，dict 有以下几个特点：

1. 查找和插入的速度极快，不会随着 key 的增加而变慢；  
2. 需要占用大量的内存，内存浪费多。

而list相反：

1. 查找和插入的时间随着元素的增加而增加；  
2. 占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

dict 可以用在需要高速查找的很多地方，在 Python 代码中几乎无处不在，正确使用 dict 非常重要，需要牢记的第一条就是 dict 的 key 必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key:

```txt
>>>key  $= [1,2,3]$    
>>>d[key]  $\equiv$  'alist'   
Traceback (most recent call last): File "<stdin>", line 1,in <module>   
TypeError: unhashable type:'list'
```

# set

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合：

```txt
>>>s  $\equiv$  set([1,2,3])   
>>>s   
{1，2，3}
```

注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。

重复元素在 set 中自动被过滤：

```txt
>>>s  $\equiv$  set([1,1,2,2,3,3])   
>>>s   
{1，2，3}
```

通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：

```txt
>>>s.add(4)   
>>>s   
{1,2,3,4}   
>>>s.add(4)   
>>>s   
{1,2,3,4}
```

通过remove(key)方法可以删除元素：

```txt
>>>s.remove   
>>>s   
{1,2,3}
```

set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作：

```erlang
>>>s1  $=$  set([1,2,3])   
>>>s2  $=$  set([2,3,4])   
>>>s1&s2   
{2,3}   
>>>s1|s2   
{1,2,3,4}
```

set 和 dict 的唯一区别仅在于没有存储对应的 value，但是，set 的原理和 dict 一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证 set 内部“不会有重复元素”。试试把 list 放入 set，看看是否会报错。

# - 再议不可变对象

上面我们讲了，str是不变对象，而list是可变对象。

对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

```txt
>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
```

而对于不可变对象，比如str，对str进行操作呢：

```txt
>>> a = 'abc'  
>>> a.replace('a', 'A')  
'Abc'  
>>> a  
'abc'
```

虽然字符串有个 replace() 方法，也确实变出了 'Abc'，但变量 a 最后仍是 'abc'，应该怎么理解呢？

我们先把代码改成下面这样：

```python
>>> a = 'abc'  
>>> b = a.replace('a', 'A')  
>>> b  
'Abc'  
>>> a  
'abc'
```

要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：

![](images/0eb39525eabd7f8a440fd7c18ad5afa0a50d7f22603351f6015c6fa17c0bf344.jpg)

当我们调用 a.replace('a', 'A')时，实际上调用方法 replace 是作用在字符串对象 'abc' 上的，而这个方法虽然名字叫 replace，但却没有改变字符串 'abc' 的内容。相反，replace 方法创建了一个新字符串 'Abc' 并返回，如果我们用变量 b 指向该新字符串，就容易理解了，变量 a 仍指向原有的字符串 'abc'，但变量 b 却指向新字符串 'Abc' 了：

![](images/6760fb19574bdcdc0fa9cc579ec91e06bc19fd7767f18877dd16ef8e8020e460.jpg)

所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

# ·小结

使用 key-value 存储结构的 dict 在 Python 中非常有用，选择不可变对象作为 key 很重要，最常用的 key 是字符串。tuple 虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入 dict 或 set 中，并解释结果。

# 2 函数

我们知道圆的面积计算公式为：

$$
S = \pi r ^ {2}
$$

当我们知道半径  $r$  的值时，就可以根据公式计算出面积。假设我们需要计算3个不同大小的圆的面积：

```txt
r1 = 12.34  
r2 = 9.08  
r3 = 73.1  
s1 = 3.14 * r1 * r1  
s2 = 3.14 * r2 * r2  
s3 = 3.14 * r3 * r3
```

当代码出现有规律的重复的时候，你就需要当心了，每次写  $3.14 * x * x$  不仅很麻烦，而且，如果要把 3.14 改成 3.14159265359 的时候，得全部替换。

有了函数，我们就不再每次写  $s = 3.14 * x * x$ ，而是写成更有意义的函数调用  $s = \text{area_of_circ}(x)$ ，而函数 area_of_circle 本身只需要写一次，就可以多次调用。

基本上所有的高级语言都支持函数，Python也不例外。Python不但能非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用。

抽象

抽象是数学中非常常见的概念。举个例子：

计算数列的和，比如：  $1 + 2 + 3 + \ldots + 100$  ，写起来十分不方便，于是数学家发明了求和符号  $\sum$  ，可以把  $1 + 2 + 3 + \ldots + 100$  记作：  $\sum_{n=1}^{100} n$

这种抽象记法非常强大，因为我们看到  $\Sigma$  就可以理解成求和，而不是还原成低级的加法运算。

而且，这种抽象记法是可扩展的，比如： $\sum_{n=1}^{100}(n^2 + 1)$

还原成加法运算就变成了：

$$
(1 \times 1 + 1) + (2 \times 2 + 1) + (3 \times 3 + 1) + \dots + (1 0 0 \times 1 0 0 + 1)
$$

可见，借助抽象，我们才能不关心底层的具体计算过程，而直接在更高的层次上思考问题。

写计算机程序也是一样，函数就是最基本的一种代码抽象的方式。

# 2.1 调用函数

Python 内置了很多有用的函数，我们可以直接调用。

要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数 abs，只有一个参数。可以直接从 Python 的官方网站查看文档：

http://docs.python.org/3/library/functions.html#abs

也可以在交互式命令行通过 help(abs) 查看 abs 函数的帮助信息。

调用abs函数：

```txt
>>> abs(100)  
100  
>>> abs(-20)  
20  
>>> abs(12.34)  
12.34
```

调用函数的时候，如果传入的参数数量不对，会报TypeError 的错误，并且 Python 会明确地告诉你：abs()有且仅有 1 个参数，但给出了两个：

```txt
>>> abs(1, 2)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
```

如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError 的错误，并且给出错误信息：str 是错误的参数类型：

```typescript
>>> abs('a')   
Traceback (most recent call last): File "<stdin>", line 1, in <module>   
TypeError: bad operand type for abs(): 'str'
```

而max函数max()可以接收任意多个参数，并返回最大的那个：

```txt
>>> max(1, 2)  
2  
>>> max(2, 3, 1, -5)  
3
```

# 数据类型转换

Python 内置的常用函数还包括数据类型转换函数，比如 int() 函数可以把其他数据类型转换为整数：

```txt
>>> int('123')
123
>>> int(12.34)
12
>>> float('12.34')
12.34
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
>>> bool ')' 
False
```

函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

```txt
>>> a = abs # 变量 a 指向 abs 函数  
>>> a(-1) # 所以也可以通过 a 调用 abs 函数
```

练习

请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串。

# 2.2 定义函数

在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号：，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

我们以自定义一个求绝对值的my_abs函数为例：

```python
def my_abs(x):
    if x >= 0:
        return x
```

```txt
else: return -x
```

请自行测试并调用my_abs看看返回结果是否正确。

请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有 return 语句，函数执行完毕后也会返回结果，只是结果为 None。

return None 可以简写为 return。

在Python交互环境中定义函数时，注意Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下。如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：

# ·空函数

如果想定义一个什么事也不做的空函数，可以用pass语句：

```python
def nop(): pass
```

pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

pass 还可以用在其他语句里，比如：

```txt
if age  $\geq 18$  pass
```

缺少了pass，代码运行就会有语法错误。

# - 参数检查

调用函数时，如果参数个数不对，Python 解释器会自动检查出来，并抛出 TypeError:

```erlang
>>> my_abs(1, 2)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: my_abs() takes 1 positional argument but 2 were given
```

但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别：

```python
>>> my_abs('A')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in my_abs
TypeError: unordered types: str() >= int()
>>> abs('A')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
```

当传入了不恰当的参数时，内置函数 abs 会检查出参数错误，而我们定义的 my_abs 没有参数检查，会导致 if 语句出错，出错信息和 abs 不一样。所以，这个函数定义不够完善。

让我们修改一下 my_abs 的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数 isinstance()实现：

```python
def my_abs(x):
    if not isinstance(x, (int, float)):
```

```python
raise TypeError('bad operand type')  
if x >= 0:  
    return x  
else:  
    return -x
```

添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误：

```txt
>>> my_abs('A')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 3, in my_abs
TypeError: bad operand type
```

错误和异常处理将在后续讲到。

# - 返回多个值

函数可以返回多个值吗？答案是肯定的。

比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：

```python
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
```

import math 语句表示导入 math 包，并允许后续代码引用 math 包里的 sin、cos 等函数。

然后，我们就可以同时获得返回值：

```txt
>>> x, y = move(100, 100, 60, math.pi / 6)  
>>> print(x, y)  
151.96152422706632 70.0
```

但其实这只是一种假象，Python函数返回的仍然是单一值：

```txt
>>> r = move(100, 100, 60, math.pi / 6)  
>>> print(r)  
(151.96152422706632, 70.0)
```

原来返回值是一个 tuple！但是，在语法上，返回一个 tuple 可以省略括号，而多个变量可以同时接收一个 tuple，按位置赋给对应的值，所以，Python 的函数返回多值其实就是返回一个 tuple，但写起来更方便。

# 小结

定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用 return 随时返回函数结果；

函数执行完毕也没有 return 语句时，自动 return None。

函数可以同时返回多个值，但其实就是一个 tuple。

# ·练习

请定义一个函数quadratic(a,b,c)，接收3个参数，返回一元二次方程：

```txt
ax² + bx + c = 0
```

的两个解。

提示：计算平方根可以调用math.sqrt()函数

# 2.3 函数的参数

定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

Python 的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# - 位置参数

我们先写一个计算  $x^{2}$  的函数：

```python
def power(x):
    return x * x
```

对于 power(x) 函数，参数 x 就是一个位置参数。

当我们调用 power 函数时，必须传入有且仅有的一个参数 x:

```txt
>>> power(5)   
25   
>>> power(15)   
225
```

现在，如果我们要计算  $x^3$  怎么办？可以再定义一个 power3 函数，但是如果要计算  $x^4$ 、 $x^5$ ……怎么办？我们不可能定义无限多个函数。

你也许想到了，可以把 power(x)修改为 power(x, n)，用来计算  $x^n$ ，说干就干：

```python
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

对于这个修改后的 power(x, n) 函数，可以计算任意 n 次方：

```txt
>>> power(5, 2)  
25  
>>> power(5, 3)  
125
```

修改后的 power(x, n) 函数有两个参数: x 和 n, 这两个参数都是位置参数, 调用函数时, 传入的两个值按照位置顺序依次赋给参数 x 和 n。

# - 默认参数

新的 power(x, n) 函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：

```txt
>>> power(5)  
Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>
```

```txt
TypeError: power() missing 1 required positional argument: 'n'
```

Python 的错误信息很明确：调用函数 power() 缺少了一个位置参数 n。

这个时候，默认参数就排上用场了。由于我们经常计算  $x^{2}$ ，所以，完全可以把第二个参数  $n$  的默认值设定为 2：

```python
def power(x, n=2):  
    s = 1  
while n > 0:  
    n = n - 1  
s = s * x  
return s
```

这样，当我们调用 power(5)时，相当于调用 power(5, 2):

```txt
>>> power(5)   
25   
>>> power(5, 2)   
25
```

而对于  $n > 2$  的其他情况，就必须明确地传入  $n$ ，比如 power(5, 3)。

从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。使用默认参数有什么好处？最大的好处是能降低调用函数的难度。举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数：

```python
def enroll(name, gender):
    print('name: ', name)
    print('gender: ', gender)
```

这样，调用 enroll()函数只需要传入两个参数：

```txt
>>> enroll('Sarah', 'F')  
name: Sarah  
gender: F
```

如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。

我们可以把年龄和城市设为默认参数：

```python
def enroll(name, gender, age=6, city='Beijing'):  
    print('name: ', name)  
    print('gender: ', gender)  
    print('age: ', age)  
    print('city: ', city)
```

这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：

```yaml
>>> enroll('Sarah', 'F')
name: Sarah
gender: F
age: 6
```

```txt
city: Beijing
```

只有与默认参数不符的学生才需要提供额外的信息：

```txt
enrollment('Bob', 'M', 7)  
enrollment('Adam', 'M', city='Tianjin')
```

可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。

有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用 enroll('Bob', 'M', 7)，意思是，除了 name, gender 这两个参数外，最后 1 个参数应用在参数 age 上，city 参数由于没有提供，仍然使用默认值。

也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用 enroll('Adam', 'M', city='Tianjin')，意思是，city 参数用传进去的值，其他默认参数继续使用默认值。

默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：

先定义一个函数，传入一个 list，添加一个 END 再返回：

```txt
def add_end  $(L = [])$  .. L.append('END') return L
```

当你正常调用时，结果似乎不错：

```txt
>>>add_end([1,2,3])   
[1，2，3，'END']   
>>>add_end(['x'，'y'，'z'])   
['x'，'y'，'z'，'END']
```

当你使用默认参数调用时，一开始结果也是对的：

```txt
>>>add_en ['END']
```

但是，再次调用add_end()时，结果就不对了：

```python
>>>add_end()   
['END'，'END']   
>>>add_end()   
['END'，'END'，'END']
```

很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

原因解释如下：

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

要修改上面的例子，我们可以用 None 这个不变对象来实现：

```python
def add_end(L=None): if L is None: L = [] L.append('END') return L
```

现在，无论调用多少次，都不会有问题：

```txt
>>>add_end() ['END']   
>>>add_end() ['END']
```

为什么要设计 str、None 这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

# - 可变参数

在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

我们以数学题为例子，给定一组数字a，b，c....，请计算  $a^2 + b^2 + c^2 + \dots$

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：

```python
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

但是调用的时候，需要先组装出一个list或tuple：

```txt
>>> calc([1, 2, 3])  
14  
>>> calc((1, 3, 5, 7))  
84
```

如果利用可变参数，调用函数的方式可以简化成这样：

```txt
>>> calc(1, 2, 3)  
14  
>>> calc(1, 3, 5, 7)  
84
```

所以，我们把函数的参数改为可变参数：

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个\*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

```txt
>>> calc(1, 2)  
5  
>>> calc()  
0
```

如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

```txt
>>> nums = [1, 2, 3]  
>>> calc(numbers[0], nums[1], nums[2])  
14
```

这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个\*号，把list或tuple的元素变成可变参数传进去：

```txt
>>> nums = [1, 2, 3]  
>>> calc(*numbers)  
14
```

* nums 表示把 nums 这个 list 的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

# 关键字参数

可变参数允许你传入  $\theta$  个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple。而关键字参数允许你传入  $\theta$  个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict。请看示例：

```prolog
def person(name, age, **kw):  
    print('name: ', name, 'age: ', age, 'other: ', kw)
```

函数 person 除了必选参数 name 和 age 外，还接受关键字参数 kw。在调用该函数时，可以只传入必选参数：

```txt
>>> person('Michael', 30)  
name: Michael age: 30 other: {}
```

也可以传入任意个数的关键字参数：

```txt
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

关键字参数有什么用？它可以扩展函数的功能。比如，在 person 函数里，我们保证能接收到 name 和 age 这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

```txt
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}  
>>> person('Jack', 24, city=extra['city'], job=extra['job'])  
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

当然，上面复杂的调用可以用简化的写法：

```txt
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}  
>>> person('Jack', 24, **extra)  
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

**extra 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函数的 **kw 参数，kw 将获得一个 dict，注意 kw 获得的 dict 是 extra 的一份拷贝，对 kw 的改动不会影响到函数外的 extra。

# - 命名关键字参数

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

仍以 person()函数为例，我们希望检查是否有 city 和 job 参数：

```python
def person(name, age, **kw):  
    if 'city' in kw:  
        # 有city参数  
        pass  
    if 'job' in kw:  
        # 有job参数  
        pass  
    print('name: ', name, 'age: ', age, 'other: ', kw)
```

但是调用者仍可以传入不受限制的关键字参数：

```txt
>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
```

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收 city 和 job 作为关键字参数。这种方式定义的函数如下：

```txt
def person(name, age, *, city, job): print(name, age, city, job)
```

命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：

```python
>>> person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: person() takes 2 positional arguments but 4 were given
```

由于调用时缺少参数名 city 和 job，Python 解释器把这 4 个参数均视为位置参数，但 person()函数仅接受 2 个位置参数。

命名关键字参数可以有缺省值，从而简化调用：

```txt
def person(name, age, *, city='Beijing', job): print(name, age, city, job)
```

由于命名关键字参数 city 具有默认值，调用时，可不传入 city 参数：

```txt
>>> person('Jack', 24, job='Engineer')  
Jack 24 Beijing Engineer
```

使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python 解释器将无法识别位置参数和命名关键字参数：

```txt
def person(name, age, city, job): #缺少\*,city和job被视为位置参数 pass
```

# - 参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

比如定义一个函数，包含上述若干种参数：

```m4
def f1(a, b, c=0, *args, **kw):  
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
```

```python
def f2(a, b, c=0, *, d, **kw):  
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)
```

在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

```txt
>>>f1(1,2)   
a  $= 1$  b  $= 2$  c  $= 0$  args  $= ()$  kw  $= \{\}$    
>>>f1(1,2,c=3)   
a  $= 1$  b  $= 2$  c  $= 3$  args  $= ()$  kw  $= \{\}$    
>>>f1(1,2,3,'a'，'b')   
a  $= 1$  b  $= 2$  c  $= 3$  args  $= (^{\prime}a^{\prime},^{\prime}b^{\prime})$  kw  $= \{\}$    
>>>f1(1,2,3,'a'，'b'，x=99)   
a  $= 1$  b  $= 2$  c  $= 3$  args  $= (^{\prime}a^{\prime},^{\prime}b^{\prime})$  kw  $= \{'x':99\}$    
>>>f2(1,2,d=99,ext=None)   
a  $= 1$  b  $= 2$  c  $= 0$  d  $= 99$  kw  $= \{'ext':None\}$
```

最神奇的是通过一个 tuple 和 dict，你也可以调用上述函数：

```python
>>> args = (1, 2, 3, 4)  
>>> kw = {'d': 99, 'x': '#'}  
>>> f1(*args, **kw)  
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}  
>>> args = (1, 2, 3)  
>>> kw = {'d': 88, 'x': '#'}  
>>> f2(*args, **kw)  
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

所以，对于任意函数，都可以通过类似 func(*args, **kw) 的形式调用它，无论它的参数是如何定义的。

小结

Python 的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

\*args是可变参数，args接收的是一个tuple;

\*\*kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装 list 或 tuple，再通过 *args 传入：func(*(1, 2, 3));  
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装 dict，再通过 **kw 传入：func(**{'a': 1, 'b': 2})。  
使用 *args 和 **kw 是 Python 的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符\*，否则定义的将是位置参数。

# 2.4 递归函数

在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

举个例子，我们来计算阶乘  $n! = 1 \times 2 \times 3 \times \ldots \times n$ ，用函数 fact(n) 表示，可以看出：

fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

所以，fact(n)可以表示为  $n \times \text{fact}(n-1)$ ，只有  $n = 1$  时需要特殊处理。

于是，fact(n)用递归的方式写出来就是：

```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
```

上面就是一个递归函数。可以试试：

```html
>>> fact(1)   
1   
>>> fact(5)   
120   
>>> fact(100)   
9332621544394415268169923885626670049071596826438162146859296389521759999322991560894146397615   
651828625369792082722375825118521091686400000000000000000
```

如果我们计算 fact(5)，可以根据函数定义看到计算过程如下：

```txt
$= = = >$  fact(5)   
 $\equiv \equiv \equiv >5^{*}$  fact(4)   
 $\equiv \equiv \equiv >5^{*}(4^{*} + 3^{*} + 2^{*})$ $\equiv \equiv \equiv >5^{*}(4^{*}(3^{*}(2^{*} + 1)))$ $\equiv \equiv \equiv >5^{*}(4^{*}(3^{*}(2^{*} + 1)))$ $\equiv \equiv \equiv >5^{*}(4^{*}(3^{*}(2))$ $\equiv \equiv \equiv >5^{*}(4^{*}(6))$ $\equiv \equiv \equiv >5^{*}24$ $\equiv \equiv \equiv >120$
```

递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试 fact(1000):

```txt
>>> fact(1000)   
Traceback (most recent call last): File "<stdin>", line 1, in <module> File "<stdin>", line 4, in fact File "<stdin>", line 4, in fact   
RuntimeError: maximum recursion depth exceeded in comparison
```

解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的 fact(n) 函数由于 return n * fact(n - 1) 引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：

```txt
def fact(n):
```

```python
return fact_iter(n, 1)  
def fact_iter(num, product):  
    if num == 1:  
        return product  
    return fact_iter(num - 1, num * product)
```

可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。

fact(5)对应的 fact_iter(5, 1)的调用如下：

```erlang
$= = = >$  fact_iter(5,1)   
 $= = = >$  fact_iter(4,5)   
 $= = = >$  fact_iter(3,20)   
 $= = = >$  fact_iter(2,60)   
 $= = = >$  fact_iter(1,120)   
 $= = = >$  120
```

尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

# ·小结

使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

# ·练习

汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

# 3 高级特性

掌握了Python的数据类型、语句和函数，基本上就可以编写出很多有用的程序了。

比如构造一个 1, 3, 5, 7, ..., 99 的列表，可以通过循环实现：

```txt
L = []  
n = 1  
while n <= 99:  
    L.append(n)  
    n = n + 2
```

取list的前一半的元素，也可以通过循环实现。

但是在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。

基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。

# 3.1 切片

取一个 list 或 tuple 的部分元素是非常常见的操作。比如，一个 list 如下：

```txt
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
```

取前3个元素，应该怎么做？笨办法：

```txt
>>> [L[0], L[1], L[2]]  
['Michael', 'Sarah', 'Tracy']
```

之所以是笨办法是因为扩展一下，取前N个元素就没辙了。取前N个元素，也就是索引为  $\theta-(\mathrm{N}-1)$  的元素，可以用循环：

```python
>>> r = []  
>>> n = 3  
>>> for i in range(n):  
... r.append(L[i])  
...  
>>> r  
['Michael', 'Sarah', 'Tracy']
```

对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python 提供了切片（Slice）操作符，能大大简化这种操作。对应上面的问题，取前 3 个元素，用一行代码就可以完成切片：

```txt
>>> L[0:3] ['Michael', 'Sarah', 'Tracy']
```

L[0:3]表示，从索引 0 开始取，直到索引 3 为止，但不包括索引 3。即索引 0，1，2，正好是 3 个元素。

如果第一个索引是  $\theta$  ，还可以省略：

```txt
>>> L[:3] ['Michael', 'Sarah', 'Tracy']
```

也可以从索引1开始，取出2个元素出来：

```txt
>>> L[1:3] ['Sarah', 'Tracy']
```

类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：

```txt
>>> L[-2:]  
['Bob', 'Jack']  
>>> L[-2:-1]  
['Bob']
```

记住倒数第一个元素的索引是-1。切片操作十分有用。我们先创建一个0-99的数列：

```txt
>>> L = list(range(100))  
>>> L  
[0, 1, 2, 3, \ldots, 99]
```

可以通过切片轻松取出某一段数列。比如前10个数：

```txt
>>> L[:10]  
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

后10个数：

```txt
>>> L[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```

前11-20个数：

```txt
>>> L[10:20]  
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

前10个数，每两个取一个：

```txt
>>> L[:10:2]  
[0, 2, 4, 6, 8]
```

所有数，每5个取一个：

```txt
>>> L[:5]  
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
```

甚至什么都不写，只写[:]就可以原样复制一个 list:

```txt
>>> L[:]  
[0, 1, 2, 3, ..., 99]
```

tuple 也是一种 list，唯一区别是 tuple 不可变。因此，tuple 也可以用切片操作，只是操作的结果仍是 tuple:

```txt
>>> (0, 1, 2, 3, 4, 5)[:3]  
(0, 1, 2)
```

字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

```txt
>>> 'ABCDEFG'[ :3]  
'ABC'  
>>> 'ABCDEFG'[ ::2]  
'ACEG'
```

在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。

# 小结

有了切片操作，很多地方循环就不再需要了。Python的切片非常灵活，一行代码就可以实现很多行循环才能完成的操作。

# 3.2 迭代

如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代(Iteration)。

在Python中，迭代是通过for…in来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：

```txt
for  $(\mathrm{i} = 0$  .i<list.length;  $\mathrm{i + + })$  { n  $=$  list[i];   
1
```

可以看出，Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

list 这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如 dict 就可以迭代：

```txt
>>>d  $=$  {'a':1,'b':2,'c':3}   
>>>for key in d: print(key)   
a   
c   
b
```

因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

由于字符串也是可迭代对象，因此，也可以作用于for循环：

```txt
>>> for ch in 'ABC':
...
...
print(ch)
...
A
B
C
```

所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

```txt
>>> from collections import iterable
>>> isinstance('abc', iterable) # str 是否可迭代
True
>>> isinstance([1,2,3], iterable) # list 是否可迭代
True
>>> isinstance(123, iterable) # 整数是否可迭代
False
```

最后一个小问题，如果要对 list 实现类似 Java 那样的下标循环怎么办？Python 内置的 enumerate 函数可以把一个 list 变成索引-元素对，这样就可以在 for 循环中同时迭代索引和元素本身：

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
...
...
print(i, value)
...
0 A
1 B
2 C
```

上面的 for 循环里，同时引用了两个变量，在 Python 里是很常见的，比如下面的代码：

```txt
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:  
... print(x, y)  
...  
1 1  
2 4  
3 9
```

·小结

任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。

# 3.3 列表生成式

列表生成式即 List Comprehensions，是 Python 内置的非常简单却强大的可以用来创建 list 的生成式。

举个例子，要生成list[1,2,3,4,5,6,7,8,9,10]可以用list(range(1,11)):

```txt
>>> list(range(1, 11))  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

但如果要生成  $[1 \times 1, 2 \times 2, 3 \times 3, \ldots, 10 \times 10]$  怎么做？方法一是循环：

```python
>> L = []  
>>> for x in range(1, 11):  
... L.append(x * x)  
...  
>>> L  
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的 list:

```txt
>>> [x * x for x in range(1, 11)]  
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

写列表生成式时，把要生成的元素  $x * x$  放到前面，后面跟 for 循环，就可以把 list 创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

```txt
>>> [x * x for x in range(1, 11) if x % 2 == 0]  
[4, 16, 36, 64, 100]
```

还可以使用两层循环，可以生成全排列：

```txt
>>> [m + n for m in 'ABC' for n in 'XYZ'] ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

三层和三层以上的循环就很少用到了。

运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

```txt
>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('/.') ] # os.listdir可以列出文件和目录
['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads'],
'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
```

for 循环其实可以同时使用两个甚至多个变量，比如 dict 的 items()可以同时迭代 key 和 value:

```txt
>>>d  $=$  {'x': 'A', 'y': 'B', 'z': 'C'}   
>>>for k,v in d.items(): print(k,'  $\equiv$  '，v)   
 $\mathbf{y} = \mathbf{B}$ $\mathbf{x} = \mathbf{A}$ $\texttt{Z} = \texttt{C}$
```

因此，列表生成式也可以使用两个变量来生成list：

```python
>>>d={'x': 'A', 'y': 'B', 'z': 'C'}  
>>> [k + ' = ' + v for k, v in d.items()  
['y=B', 'x=A', 'z=C']
```

最后把一个list中所有的字符串变成小写：

```txt
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
```

# ·练习

如果 list 中既包含字符串，又包含整数，由于非字符串类型没有 lower() 方法，所以列表生成式会报错：

```txt
>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'
```

使用内建的isinstance函数可以判断一个变量是不是字符串：

```txt
>>> x = 'abc'  
>>> y = 123  
>>> isinstance(x, str)  
True  
>>> isinstance(y, str)  
False
```

请修改列表生成式，通过添加 if 语句保证列表生成式能正确地执行。

# 3.4生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的 list，从而节省大量的空间。在 Python 中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个 generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个 generator:

```txt
>>> L = [x * x for x in range(10)]  
>>> L  
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
>>> g = (x * x for x in range(10))  
>>> g  
<generator object <genexpr> at 0x1022ef630>
```

创建 L 和 g 的区别仅在于最外层的[]和(), L 是一个 list, 而 g 是一个 generator。

我们可以直接打印出 list 的每一个元素，但我们怎么打印出 generator 的每一个元素呢？

如果要一个一个打印出来，可以通过 next()函数获得 generator 的下一个返回值：

```txt
>>> next(g)   
0   
>>> next(g)   
1   
>>> next(g)   
4   
>>> next(g)   
9   
>>> next(g)   
16   
>>> next(g)   
25   
>>> next(g)   
36   
>>> next(g)   
49   
>>> next(g)   
64   
>>> next(g)   
81   
>>> next(g)   
Traceback (most recent call last): File "<stdin>", line 1, in <module> StopIteration
```

我们讲过，generator 保存的是算法，每次调用 next(g)，就计算出 g 的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的错误。

当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：

```txt
>>>g  $\equiv$  (x \* x for x in range(10))   
>>>for n in g:   
... print(n)   
0   
1   
4   
9   
16   
25   
36   
49   
64   
81
```

所以，我们创建了一个 generator 后，基本上永远不会调用 next()，而是通过 for 循环来迭代它，并且不需要关心 StopIteration 的错误。

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

```python
def fib(max): n, a, b = 0, 0, 1 while n < max: print(b) a, b = b, a + b n = n + 1 return 'done'
```

上面的函数可以输出斐波那契数列的前N个数：

```txt
>>> fib(6)  
1  
1  
2  
3  
5  
8  
done
```

仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和 generator 仅一步之遥。要把 fib 函数变成 generator，只需要把 print(b) 改为 yield b 就可以了：

```python
def fib(max): n, a, b = 0, 0, 1
```

```gradle
while  $n <   \max$  ： yieldb a，  $b = b$  ，a+b n=n+1   
return 'done'
```

这就是定义 generator 的另一种方法。如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator:

```txt
>>>f  $=$  fib(6)   
>>>f   
<generator object fib at 0x104feaaa0>
```

这里，最难理解的就是 generator 和函数的执行流程不一样。函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回。而变成 generator 的函数，在每次调用 next()的时候执行，遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行。

举个简单的例子，定义一个 generator，依次返回数字 1，3，5：

```python
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
```

调用该 generator 时，首先要生成一个 generator 对象，然后用 next()函数不断获得下一个返回值：

```txt
>>> o = odd()
>>> next(o)
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
>>> next(o)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
StopIteration
```

可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

回到 fib 的例子，我们在循环过程中不断调用 yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。

同样的，把函数改成 generator 后，我们基本上从来不会用 next() 来获取下一个返回值，而是直接使用 for 循环来迭代：

```txt
>>> for n in fib(6):  
... print(n)  
...  
1  
1  
2  
3  
5  
8
```

但是用 for 循环调用 generator 时，发现拿不到 generator 的 return 语句的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在 StopIteration 的 value 中：

```txt
>>> g = fib(6)  
>>> while True:  
... try:  
... x = next(g)  
... print('g:", x)  
... except StopIteration as e:  
... print('Generator return value:", e.value)  
... break  
...  
g: 1  
g: 1  
g: 2  
g: 3  
g: 5  
g: 8  
Generator return value: done
```

关于如何捕获错误，后面的错误处理还会详细讲解。

·练习

杨辉三角定义如下：

```txt
1 1 1 1 2 1 1 3 3 1 4 6 4 1 5 10 10 5 1
```

把每一行看做一个 list，试写一个 generator，不断输出下一行的 list。

```txt
期待输出：  
# [1]  
# [1, 1]  
# [1, 2, 1]  
# [1, 3, 3, 1]  
# [1, 4, 6, 4, 1]
```

```python
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
```

小结

generator 是非常强大的工具，在 Python 中，可以简单地把列表生成式改成 generator，也可以通过函数实现复杂逻辑的 generator。

要理解 generator 的工作原理，它是在 for 循环的过程中不断计算出下一个元素，并在适当的条件结束 for 循环。对于函数改成的 generator 来说，遇到 return 语句或者执行到函数体最后一行语句，就是结束 generator 的指令，for 循环随之结束。

请注意区分普通函数和 generator 函数，普通函数调用直接返回结果：

```txt
>>> r = abs(6)  
>>> r  
6
```

generator函数的“调用”实际返回一个generator对象：

```txt
>>> g = fib(6)  
>>> g  
<generator object fib at 0x1022ef948>
```

# 3.5 迭代器

我们已经知道，可以直接作用于for循环的数据类型有以下几种：一类是集合数据类型，如list、tuple、dict、set、str等；一类是generator，包括生成器和带yield的generator function。这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Comparable对象：

```txt
>>> from collections import iterable
>>> isinstance [], Iterator)
True
>>> isinstance {}, Iterator)
True
>>> isinstance('abc', Iterator)
True
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance(100, Iterator)
False
```

而生成器不但可以作用于 for 循环，还可以被 next()函数不断调用并返回下一个值，直到最后抛出 StopIteration 错误表示无法继续返回下一个值了。

可以被 next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：

```txt
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance,[], Iterator)
False
>>> isinstance{}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

生成器都是 Iterator 对象，但 list、dict、str 虽然是 Iterator，却不是 Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：

```erlang
>>>isinstance(iterator([]),Iterator) True   
>>>isinstance(iterator('abc'),Iterator) True
```

你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator 甚至可以表示一个无限大的数据流，例如全体自然数。而使用 list 是永远不可能存储全体自然数的。

# 小结

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于 next()函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列；

集合数据类型如 list、dict、str 等是 Iterator 但不是 Iterator，不过可以通过 iter()函数获得一个 Iterator 对象。Python 的 for 循环本质上就是通过不断调用 next()函数实现的，例如：

```txt
for x in [1, 2, 3, 4, 5]: pass
```

实际上完全等价于：

```txt
首先获得Iterator对象：  
it  $=$  iter([1,2,3,4,5])  
#循环：  
while True:try:#获得下一个值： $\mathbf{x} =$  next(it）except StopIteration:#遇到StopIteration就退出循环break
```

# 4 函数式编程

函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

# 4.1 高阶函数

高阶函数英文叫Higher-order function。什么是高阶函数？我们以实际代码为例子，一步一步深入概念。

# - 变量可以指向函数

以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：

```txt
>> abs(-10) 10
```

但是，如果只写 abs 呢？

```txt
>>> abs  
<built-in function abs>
```

可见，abs(-10)是函数调用，而abs是函数本身。

要获得函数调用结果，我们可以把结果赋值给变量：

```txt
>>x  $=$  abs(-10)   
>>x   
10
```

但是，如果把函数本身赋值给变量呢？

```txt
>>>f  $=$  abs   
>>>f   
<built-in function abs>
```

结论：函数本身也可以赋值给变量，即：变量可以指向函数。

如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？用代码验证一下：

```txt
>>>f  $\equiv$  abs   
>>>f(-10)
```

成功！说明变量  $f$  现在已经指向了 abs 函数本身。直接调用 abs()函数和调用变量  $f()$  完全相同。

# - 函数名也是变量

那么函数名是什么呢？函数名其实就是指向函数的变量！对于 abs()这个函数，完全可以把函数名 abs 看成变量，它指向一个可以计算绝对值的函数！

如果把 abs 指向其他对象，会有什么情况发生？

```txt
>>> abs = 10  
>>> abs(-10)  
Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>  
TypeError: 'int' object is not callable
```

把 abs 指向 10 后，就无法通过 abs(-10) 调用该函数了！因为 abs 这个变量已经不指向求绝对值函数而是指向一个整数 10!

当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复 abs 函数，请重启 Python 交互环境。

注：由于 abs 函数实际上是定义在 import builtns 模块中的，所以要让修改 abs 变量的指向在其它模块也生效，要用 import builtns; builtns.abs = 10。

# ·传入函数

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

一个最简单的高阶函数：

```txt
def add(x, y, f): return f(x) + f(y)
```

当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，根据函数定义，我们可以推导计算过程为：

```latex
$\begin{array}{l}\mathrm{x} = \mathrm{-5}\\ \mathrm{y} = 6\\ \mathrm{f} = \mathrm{abs}\\ \mathrm{f(x) + f(y)} = = >\mathrm{abs(-5) + abs(6)} = = >11\\ \mathrm{return 11} \end{array}$
```

用代码验证一下：

```txt
>>>add(-5,6,abs) 11
```

编写高阶函数，就是让函数的参数能够接收别的函数。

# 小结

把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

# 4.1.1 map/reduce

Python 内建了 map() 和 reduce() 函数。

如果你读过 Google 的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白 map/reduce 的概念。

我们先看 map。map()函数接收两个参数，一个是函数，一个是 Iterator，map 将传入的函数依次作用到序列的每个元

素，并把结果作为新的 Iterator 返回。

举例说明，比如我们有一个函数  $f(x) = x^2$ ，要把这个函数作用在一个 list [1, 2, 3, 4, 5, 6, 7, 8, 9] 上，就可以用 map() 实现如下：

![](images/4a517253f3a57f72fbd670624f8cb37bd6faacea4d3ffe73c5ac10abf0b5793c.jpg)

现在，我们用Python代码实现：

```latex
>>> def f(x): return  $\texttt{x}^{*}\texttt{x}$ $\dots$ $\gg r = \mathsf{map}(f,[1,2,3,4,5,6,7,8,9])$    
>>> list(r)   
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

你可能会想，不需要 map()函数，写一个循环，也可以计算出结果：

```python
L = []  
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]: L.append(f(n))  
print(L)
```

的确可以，但是，从上面的循环代码，能一眼看明白“把  $f(x)$  作用在 list 的每一个元素并把结果生成一个新的 list”吗？

所以，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的  $f(x) = x^2$ ，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

```txt
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])) ['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

只需要一行代码。

再看reduce的用法。reduce把一个函数作用在一个序列[x1，x2，x3，...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

```txt
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

比方说对一个序列求和，就可以用reduce实现：

```python
>>> from functools import reduce  
>>> def add(x, y):  
    return x + y
```

```txt
>>> reduce(add, [1, 3, 5, 7, 9])  
25
```

当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

```python
>>> from functools import reduce
>>> def fn(x, y):
    ...
        return x * 10 + y
>>> reduce(fn, [1, 3, 5, 7, 9])
13579
```

这个例子本身没多大用处，但是，如果考虑到字符串 str 也是一个序列，对上面的例子稍加改动，配合 map()，我们就可以写出把 str 转换为 int 的函数：

```python
>>> from functools import reduce
>>> def fn(x, y):
    ... return x * 10 + y
>>> def char2num(s):
    ... return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
9}[s]
>>> reduce(fn, map(char2num, '13579'))
```

整理成一个str2int的函数就是：

```txt
from functools import reduce   
def str2int(s): def fn(x,y): return  $\texttt{x}^{*}\texttt{10} +\texttt{y}$  def char2num(s): return  $\{^{\prime}0^{\prime}:0,1^{\prime}:1,2^{\prime}:2,3^{\prime}:3,4^{\prime}:4,5^{\prime}:5,6^{\prime}:6,7^{\prime}:7,8^{\prime}:8,9^{\prime}:$  9}[s] return reduce(fn，map(char2num,s))
```

还可以用 lambda 函数进一步简化成：

```python
from functools import reduce   
def char2num(s): return  $\{0^{\prime}:0,1^{\prime}:1,2^{\prime}:2,3^{\prime}:3,4^{\prime}:4,5^{\prime}:6,6^{\prime}:7,8^{\prime}:8,9^{\prime}:9\} [s]$  def str2int(s): return reduce( lambda x,y:x\*10+y，map(char2num,s))
```

也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代

码！

# ·练习

1. 利用 map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']:  
2. Python 提供的 sum()函数可以接受一个 list 并求和, 请编写一个 prod()函数, 可以接受一个 list 并利用 reduce() 求积。  
3. 利用 map 和 reduce 编写一个 str2float 函数，把字符串 '123.456' 转换成浮点数 123.456:

# 4.1.2 filter

Python 内建的 filter()函数用于过滤序列。

和 map()类似，filter()也接收一个函数和一个序列。和 map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素。

例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

```python
def isOdd(n):
    return n % 2 == 1
list.filter(isOdd, [1, 2, 4, 5, 6, 9, 10, 15])
# 结果：[1, 5, 9, 15]
```

把一个序列中的空字符串删掉，可以这么写：

```python
def not_empty(s):
    return s and s.strip()
list.filter(not_empty, ['A', '', 'B', None, 'C', '']) #结果：['A', 'B', 'C']
```

可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# ·用filter求素数

计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

```txt
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
```

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

```txt
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
```

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

```txt
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
```

取新序列的第一个数 5 , 然后用 5 把序列的 5 的倍数筛掉:

```txt
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
```

不断筛下去，就可以得到所有的素数。

用Python来实现这个算法，可以先构造一个从3开始的奇数序列：

```python
def _odd_iter(): n = 1 while True: n = n + 2
```

```txt
yield n
```

注意这是一个生成器，并且是一个无限序列。

然后定义一个筛选函数：

```python
def _not_divisible(n): return lambda x:  $x \%$  n > 0
```

最后，定义一个生成器，不断返回下一个素数：

```python
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
```

这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

由于 primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

```txt
打印1000以内的素数：  
for n in primes():  
    if n < 1000:  
        print(n)  
    else:  
        break
```

注意到 Iterator 是惰性计算的序列，所以我们可以用 Python 表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

# ·练习

回数是指从左向右读和从右向左读都是一样的数，例如 12321，909。请利用 filter() 滤掉非回数：

```julia
测试：  
output = filter(is_palindrome, range(1, 1000))  
print(list(output))
```

# 小结

filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

# 4.1.3 sorted

# - 排序算法

排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

Python内置的sorted()函数就可以对list进行排序：

```txt
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```

此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

```erlang
>>> sorted([36, 5, -12, 9, -21], key=abs)  
[5, 9, -12, -21, 36]
```

key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序。对比原始的 list 和经过 key=abs 处理过的 list：

```javascript
list  $=$  [36,5，-12,9，-21] keys  $=$  [36,5，12,9，21]
```

然后 sorted()函数按照 keys 进行排序，并按照对应关系返回 list 相应的元素：

```txt
keys排序结果  $\Rightarrow$  [5,9，12，21，36] | | | | 最终结果  $\Rightarrow$  [5,9，-12，-21，36]
```

我们再看一个字符串排序的例子：

```txt
>>> sorted(['bob', 'about', 'Zoo', 'Credit']) ['Credit', 'Zoo', 'about', 'bob']
```

默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个 key 函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

这样，我们给 sorted 传入 key 函数，即可实现忽略大小写的排序：

```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower) ['about', 'bob', 'Credit', 'Zoo']
```

要进行反向排序，不必改动 key 函数，可以传入第三个参数 reverse=True:

```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True) ['Zoo', 'Credit', 'bob', 'about']
```

从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

·小结

sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。

·练习

假设我们用一组tuple表示学生名字和成绩：

```javascript
$L = [(Bob',75),(Adam',92),(Bart',66),(Lisa',88)]$
```

请用 sorted()对上述列表分别按名字排序，再按成绩从高到低排序。

# 4.2 返回函数

函数作为返回值

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：

```python
def calc_sum(*args):  
    ax = 0  
    for n in args:  
        ax = ax + n  
    return ax
```

但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：

```txt
def lazy_sum(*args): def sum(): ax  $= 0$  for n in args: ax  $=$  ax+n return ax return sum
```

当我们调用 lazy_sum()时，返回的并不是求和结果，而是求和函数：

```txt
>>>f  $=$  lazy_sum(1,3,5,7,9)   
>>>f   
<function lazy_sum.<locals>.sum at 0x101c6ed90>
```

调用函数  $f$  时，才真正计算求和的结果：

```txt
>>>f() 25
```

在这个例子中，我们在函数 lazy_sum 中又定义了函数 sum，并且，内部函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量，当 lazy_sum 返回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

请再注意一点，当我们调用 lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

```txt
>>>f1  $=$  lazy_sum(1,3,5,7,9)   
>>>f2  $=$  lazy_sum(1,3,5,7,9)   
>>>f1  $\equiv =$  f2   
False
```

f1()和f2()的调用结果互不影响。

·闭包

注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：

```bazel
def count():  $f s = []$
```

```python
for i in range(1, 4): def f(): return i*i fs.append(f) return fs   
f1, f2, f3 = count()
```

在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。

你可能认为调用f1(), f2()和f3()结果应该是1, 4, 9, 但实际结果是:

```txt
>>>f1()   
9   
>>>f2()   
9   
>>>f3()   
9
```

全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

```python
def count():
    def f(j):
        def g():
            return j * j
            return g
        fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
```

再看看结果：

```txt
>>>f1，f2，f3  $=$  count()   
>>>f1()   
1   
>>>f2()   
4   
>>>f3()   
9
```

缺点是代码较长，可利用 lambda 函数缩短代码。

小结

一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

# 4.3 匿名函数

当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算  $f(x) = x^2$  时，除了定义一个  $f(x)$  的函数外，还可以直接传入匿名函数：

```txt
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

通过对比可以看出，匿名函数 lambda x: x * x 实际上就是：

```python
def f(x):
    return x * x
```

关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

```txt
>>>f  $=$  lambda x:x\*x   
>>>f   
<function <lambda>at 0x101c6ef28>   
>>>f(5)   
25
```

同样，也可以把匿名函数作为返回值返回，比如：

```txt
def build(x, y): return lambda: x * x + y * y
```

小结

Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。

# 4.4 装饰器

由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

```txt
>>> def now():
...
...
print('2015-3-25')
...
>>> f = now
>>> f()
2015-3-25
```

函数对象有一个_name属性，可以拿到函数的名字：

```txt
>>> now._name_
'now'
>>> f._name_
'now'
```

现在，假设我们要增强 now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改 now()函数的定义，

这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

```python
def log(func): def wrapper(\*args, \*\*kw): print('call %s'):'% func._name_ return func(\*args, \*\*kw) return wrapper
```

观察上面的 log，因为它是一个 decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助 Python 的@语法，把 decorator 置于函数的定义处：

```txt
@log
def now():
    print('2015-3-25')
```

调用 now()函数，不仅会运行 now()函数本身，还会在运行 now()函数前打印一行日志：

```txt
>>> now()
call now():
2015-3-25
```

把@log放到now()函数的定义处，相当于执行了语句：

```txt
now = log(now)
```

由于 log() 是一个 decorator，返回一个函数，所以，原来的 now() 函数仍然存在，只是现在同名的 now 变量指向了新的函数，于是调用 now() 将执行新函数，即在 log() 函数中返回的 wrapper() 函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

```python
def log(text): def decorator(func): def wrapper(\*args, \*\*kw): print('%s %s():'  $\%$  (text, func._name_)) return func(\*args, \*\*kw) return wrapper return decorator
```

这个3层嵌套的decorator用法如下：

```txt
@log('execute') def now(): print('2015-3-25')
```

执行结果如下：

```txt
>>> now()
execute now():
2015-3-25
```

和两层嵌套的decorator相比，3层嵌套的效果是这样的：

```html
>>> now = log('execute')(now)
```

我们来剖析上面的语句，首先执行 log('execute')，返回的是 decorator 函数，再调用返回的函数，参数是 now 函数，返回值最终是 wrapper 函数。

以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有_name_等属性，但你去看经过decorator装饰之后的函数，它们的_name_已经从原来的'now'变成了'repeater':

```txt
>>> now._name_
'wrapper'
```

因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper._name_ = func._name_这样的代码，Python内置的functools wraps就是干这个事的，所以，一个完整的decorator的写法如下：

```python
import functools
def log(func):
    @functools wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__) return func(*args, **kw)
    return wrapper
```

或者针对带参数的decorator:

```python
import functools   
def log(text): def decorator(func): @functools wraps(func) def wrapper(\*args, \*\*kw): print('%s %s():' % (text, func._name_)) return func(\*args, \*\*kw) return wrapper return decorator
```

import functools 是导入 functools 模块。模块的概念稍候讲解。现在，只需记住在定义 wrapper()的前面加上 @functools wraps(func)即可。

·小结

在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：

```txt
@log def f():
```

```txt
pass
```

又支持：

```txt
@log('execute') def f(): pass
```

# 4.5 偏函数

Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。

在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

```txt
>>> int('12345')
12345
```

但 int()函数还提供额外的 base 参数，默认值为 10。如果传入 base 参数，就可以做 N 进制的转换：

```txt
>>> int('12345', base=8)
5349
>>> int('12345', 16)
74565
```

假设要转换大量的二进制字符串，每次都传入 int(x, base=2) 非常麻烦，于是，我们想到，可以定义一个 int2() 的函数，默认把 base=2 传进去：

```txt
def int2(x, base=2): return int(x, base)
```

这样，我们转换二进制就非常方便了：

```txt
>>> int2('1000000')
64
>>> int2('1010101')
85
```

functools_partial 就是帮助我们创建一个偏函数的，不需要我们自己定义 int2()，可以直接使用下面的代码创建一个新的函数 int2:

```txt
>>> import functools
>>> int2 = functools部分内容(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
```

所以，简单总结functools_partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：

```txt
>>> int2('1000000', base=10)
1000000
```

最后，创建偏函数时，实际上可以接收函数对象、\*args和\*\*kw这3个参数，当传入：

```python
int2 = functools_partial(int, base=2)
```

实际上固定了int()函数的关键字参数base，也就是：

```txt
int2('10010')
```

相当于：

```latex
\[
\begin{aligned}
& \text { kw } = \{\text { 'base': 2 }\} \\
& \text { int('10010', **kw)}
\end{aligned}
\]
```

当传入：

```txt
max2 = functools_partial(max, 10)
```

实际上会把10作为\*args的一部分自动加到左边，也就是：

```csv
max2(5,6,7)
```

相当于：

```latex
$\begin{array}{rl} & \text{arg}s = (10,5,6,7)\\ & \max (\text{*args}) \end{array}$
```

结果为10。

小结

当函数的参数个数太多，需要简化时，使用functools_partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

# 5 模块

在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。

为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）。

使用模块有什么好处？

最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。

使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。但是也要注意，尽量不要与内置函数名字冲突。点这里查看 Python 的所有内置函数。

你也许还想到，如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。

举个例子，一个 abc.py 的文件就是一个名字叫 abc 的模块，一个 xyz.py 的文件就是一个名字叫 xyz 的模块。

现在，假设我们的 abc 和 xyz 这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如 mycompany，按照如下目录存放：

![](images/9d9ad5f95d22fa75ef1c26b9e29ad9f40929d32f94d14cfb0a2f3f83f5414497.jpg)

引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py 模块的名字就变成了 mycompany.abc，类似的，xyz.py 的模块名变成了 mycompany.xyz。

请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：

![](images/77651264d11c291d473ba95e2da6ef1cbb93d55f46cead9316aad6d0d69f0600.jpg)

文件 www.py 的模块名就是 mycompany.web.www，两个文件 utils.py 的模块名分别是 mycompany.utils 和 mycompany.web.utils。

自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

mycompany.web 也是一个模块，请指出该模块对应的.py 文件。

# 5.1 使用模块

Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。

我们以内建的sys模块为例，编写一个hello的模块：

```python
#!/usr/bin/env python3   
# --coding: utf-8 --   
' a test module '   
_author_  $=$  'Michael Liao'   
import sys   
def test(): args  $=$  sys.argv if len(args)  $\equiv = 1$  print('Hello,world!') elif len(args)  $\equiv = 2$  print('Hello,%s!' % args[1]) else: print('Too many arguments!')   
if _name  $\equiv =$  'main': test()
```

第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码：

第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

第6行使用_author变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

后面开始就是真正的代码部分。

你可能注意到了，使用sys模块的第一步，就是导入该模块：

```txt
import sys
```

导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。

sys 模块有一个 argv 变量，用 list 存储了命令行的所有参数。argv 至少有一个元素，因为第一个参数永远是该.py 文件的名称，例如：

运行python3 hello.py获得的sys.argv就是['hello.py'];

运行 python3 hello.py Michael 获得的 sys.argv 就是['hello.py', 'Michael']。

最后，注意到这两行代码：

```python
if __name__ == 'main':
test()
```

当我们在命令行运行 hello 模块文件时，Python 解释器把一个特殊变量 __name__ 置为 __main__，而如果在其他地方导入该 hello 模块时，if 判断将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

我们可以用命令行运行hello.py看看效果：

```txt
$ python3 hello.py
Hello, world!
$ python hello.py Michael
Hello, Michael!
```

如果启动Python交互环境，再导入hello模块：

```txt
$ python3
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello
>>>
```

导入时，没有打印Hello,word!,因为没有执行test()函数。

调用 hello.test()时，才能打印出 Hello, word!：

```txt
>>> hello.test()  
Hello, world!
```

作用域

在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和_xxx这样的函数或变量就是非公开的（private)，不应该被直接引用，比如_abc，_abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

private 函数或变量不应该被别人引用，那它们有什么用呢？请看例子：

```python
def _private_1(name):
    return 'Hello, %s' % name
def _private_2(name):
    return 'Hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```

我们在模块里公开 greeting()函数，而把内部逻辑用 private 函数隐藏起来了，这样，调用 greeting()函数不用关心内部的 private 函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成 private，只有外部需要引用的函数才定义为 public。

# 5.2 安装第三方模块

在Python中，安装第三方模块，是通过包管理工具pip完成的。

如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。

如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Addpython.exe to Path。

在命令提示符窗口下尝试运行 pip，如果 Windows 提示未找到命令，可以重新运行安装程序添加 pip。

注意：Mac或Linux上有可能并存Python3.x和Python2.x，因此对应的pip命令是pip3。

现在，让我们来安装一个第三方库—Python Imaging Library，这是Python下非常强大的处理图像的工具库。不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的 Pillow项目开发非常活跃，并且支持最新的Python 3。

一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：

```batch
pip install Pillow
```

耐心等待下载并安装后，就可以使用 Pillow了。

有了 Pillow，处理图片易如反掌。随便找个图片生成缩略图：

```python
>>> from PIL import Image
>>> im = Image.open('test.png')
>>> print(im.format, im.size, im_mode)
PNG (400, 300) RGB
>>> im<thumbail((200, 100))
>>> im.save('thumb.jpg', 'JPEG')
```

其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等。

# - 模块搜索路径

当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：

```txt
>>> import mymodule
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ImportError: No module named mymodule
```

默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

```python
>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python-framework/Versions/3.4/lib/python34.zip',
'/Library/Frameworks/Python-framework/Versions/3.4/lib/python3.4',
'/Library/Frameworks/Python-framework/Versions/3.4/lib/python3.4/plat-darwin',
'/Library/Frameworks/Python-framework/Versions/3.4/lib/python3.4/lib-dynload',
'/Library/Frameworks/Python-framework/Versions/3.4/lib/python3.4/site-packages']
```

如果我们要添加自己的搜索目录，有两种方法：

一是直接修改sys.path，添加要搜索的目录：

```python
>>> import sys
>>> sys.path.append('/Users/michael/my_PYScripts')
```

这种方法是在运行时修改，运行结束后失效。

第二种方法是设置环境变量PythonPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

# 6 面向对象编程

面向对象编程—Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。

假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：

```python
std1 = { 'name': 'Michael', 'score': 98 }  
std2 = { 'name': 'Bob', 'score': 81 }
```

而处理学生成绩可以通过函数实现，比如打印学生的成绩：

```python
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
```

如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。

```python
class Student(object): def __init__(self, name, score): self.name = name self.score = score def print_score(self): print('%s: %s'  $\%$  (self.name, self.score))
```

给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。面向对象的程序写出来就像这样：

```python
bart = Student('Bart Simpson', 59)  
lisa = Student('Lisa Simpson', 87)  
bart.print_score()  
lisa.print_score()
```

面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，比如我们定义的 Class—Student，是指学生这个概念，而实例（Instance）则是一个个具体的 Student，比如，Bart Simpson 和 Lisa Simpson 是两个具体的 Student。

所以，面向对象的设计思想是抽象出 Class，根据 Class 创建 Instance。

面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

·小结

数据封装、继承和多态是面向对象的三大特点，我们后面会详细讲解。

# 6.1 类和实例

面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

仍以 Student 类为例，在 Python 中，定义类是通过 class 关键字：

```txt
class Student(object): pass
```

class 后面紧接着是类名，即 Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用 object 类，这是所有类最终都会继承的类。

定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：

```txt
>>>bart  $\equiv$  Student()   
>>>bart   
<main STUDent object at 0x10a67a590>   
>>>Student   
<class 'main'.Student'>
```

可以看到，变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。

可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：

```python
>>>bart.name  $=$  'Bart Simpson'   
>>>bart.name   
'Bart Simpson'
```

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

```python
class Student(object): def __init__(self, name, score): self.name = name self.score = score
```

注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

```txt
>>>bart  $\equiv$  Student('Bart Simpson',59)   
>>>bart.name   
'Bart Simpson'   
>>>bart.score   
59
```

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量 self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

# 数据封装

面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据，比如打印一个学生的成绩：

```python
>>> def print_score(std):  
... print('%s: %s' % (std.name, std.score))  
...  
>>> print_score(bart)  
Bart Simpson: 59
```

但是，既然 Student 实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在 Student 类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和 Student 类本身是关联起来的，我们称之为类的方法：

```python
class Student(object): def __init__(self, name, score): self.name = name self.score = score def print_score(self): print('%s: %s'  $\%$  (self.name, self.score))
```

要定义一个方法，除了第一个参数是 self 外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了 self 不用传递，其他参数正常传入：

```txt
>>>bart.print_score()   
Bart Simpson:59
```

这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

封装的另一个好处是可以给Student类增加新的方法，比如get_grade:

```python
class Student(object): def get_grade(self): if self.score >= 90: return 'A' elif self.score >= 60: return 'B' else: return 'C'
```

同样的，get_grade 方法可以直接在实例变量上调用，不需要知道内部实现细节：

```txt
>>>bart.get_grade() C
```

# 小结

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

```txt
>>>bart  $=$  Student('Bart Simpson',59)   
>>>lisa  $=$  Student('Lisa Simpson',87)   
>>>bart.age  $= 8$    
>>>bart.age   
8   
>>>lisa.age   
Traceback (most recent call last): File "<stdin>",line 1,in <module>   
AttributeError:'Student'object has no attribute 'age'
```

# 6.2 访问限制

在 Class 内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：

```txt
>>>bart  $=$  Student('Bart Simpson'，98)   
>>>bart.score   
98   
>>>bart.score  $= 59$    
>>>bart.score   
59
```

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

```python
class Student(object): def __init__(self, name, score): self._name = name self._score = score def print_score(self): print('%s: %s'  $\%$  (self._name, self._score))
```

改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量．name和实例变量．score了：

```txt
>>>bart  $=$  Student('Bart Simpson'，98)   
>>>bart._name   
Traceback (most recent call last): File "<stdin>",line 1,in <module>   
AttributeError:'Student'object has no attribute'_name'
```

这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法

```python
class Student(object): def get_name(self): return self._name def get_score(self): return self._score
```

如果又要允许外部代码修改 score 怎么办？可以再给 Student 类增加 set_score 方法：

```python
class Student(object): def set_score(self, score): self._score = score
```

你也许会问，原先那种直接通过bart.score = 59也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：

```python
lass Student(object): def set_score(self, score): if 0 <= score <= 100: self._score = score else: raise ValueError('bad score')
```

需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用_name__、_score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问_name是因为Python解释器对外把_name变量改成了_Student_name，所以，仍然可以通过_Student_name来访问_name变量：

```txt
>>>bart._Student_name 'Bart Simpson'
```

但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把_name改成不同的变量名。

总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

最后注意下面的这种错误写法：

```python
>>>bart  $=$  Student('Bart Simpson'，98)  
>>>bart.get_name()  
'Bart Simpson'  
>>>bart._name  $=$  'New Name'#设置_name变量！  
>>>bart._name  
'New Name'
```

表面上看，外部代码“成功”地设置了_name变量，但实际上这个_name变量和class内部的_name变量不是一个变量!内部的_name变量已经被Python解释器自动改成了_Student_name,而外部代码给bart新增了一个_name变量。不信试试：

```python
>>>bart.get_name()#get_name()内部返回self._name 'Bart Simpson'
```

# 6.3 继承和多态

在 OOP 程序设计中, 当我们定义一个 class 的时候, 可以从某个现有的 class 继承, 新的 class 称为子类 (Subclass), 而被继承的 class 称为基类、父类或超类 (Base class、Super class)。

比如，我们已经编写了一个名为 Animal 的 class，有一个 run()方法可以直接打印：

```python
class Animal(object): def run(self): print('Animal is running...')
```

当我们需要编写 Dog 和 Cat 类时，就可以直接从 Animal 类继承：

```python
class Dog(Animal): pass   
class Cat(Animal): pass
```

对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。

继承有什么好处？最大的好处是子类获得了父类的全部功能。由于 Animal 实现了 run() 方法，因此，Dog 和 Cat 作为它的子类，什么事也没干，就自动拥有了 run() 方法：

```lua
dog = Dog()
dog.run()
cat = Cat()
cat.run()
```

运行结果如下：

```txt
Animal is running... Animal is running...
```

当然，也可以对子类增加一些方法，比如Dog类：

```python
class Dog(Animal): def run(self): print('Dog is running...') def eat(self): print('Eating meat...')
```

继承的第二个好处需要我们对代码做一点改进。你看到了，无论是Dog还是Cat，它们run()的时候，显示的都是Animal

is running...，符合逻辑的做法是分别显示 Dog is running...和 Cat is running...，因此，对 Dog 和 Cat 类改进如下：

```python
class Dog(Animal): def run(self): print('Dog is running...')   
class Cat(Animal): def run(self): print('Cat is running...')
```

再次运行，结果如下：

```txt
Dog is running...  
Cat is running...
```

当子类和父类都存在相同的 run() 方法时，我们说，子类的 run() 覆盖了父类的 run()，在代码运行的时候，总是会调用子类的 run()。这样，我们就获得了继承的另一个好处：多态。

要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个 class 的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和 Python 自带的数据类型，比如 str、list、dict 没什么两样：

```txt
a = list() # a是list类型  
b = Animal() # b是Animal类型  
c = Dog() # c是Dog类型
```

判断一个变量是否是某个类型可以用isinstance()判断：

```txt
>>>isinstance(a, list)   
True   
>>>isinstance(b, Animal)   
True   
>>>isinstance(c,Dog)   
True
```

看来a、b、c确实对应着list、Animal、Dog这3种类型。

但是等等，试试：

```txt
>>>isinstance(c,Animal) True
```

看来c不仅仅是Dog，c还是Animal！

不过仔细想想，这是有道理的，因为Dog是从Animal继承下来的，当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是Animal也没错，Dog本来就是Animal的一种！

所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：

```txt
>>> b = Animal()  
>>> isinstance(b, Dog)  
False
```

Dog 可以看成 Animal, 但 Animal 不可以看成 Dog。

要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个 Animal 类型的变量：

```python
def run_twice(animal):
    animal.run()
    animal.run()
```

当我们传入 Animal 的实例时，run_twice()就打印出：

```txt
>>> run_twice(Animal())
Animal is running...
Animal is running...
```

当我们传入Dog的实例时，run_twice()就打印出：

```txt
>>> run_twice(Dog())
Dog is running...
Dog is running...
```

当我们传入Cat的实例时，run Twice()就打印出：

```txt
>>> run_twice(Cat())
Cat is running...
Cat is running...
```

看上去没啥意思，但是仔细想想，现在，如果我们再定义一个Tortoise类型，也从Animal派生：

```python
class Tortoise(Animal): def run(self): print('Tortoise is running slowly...')
```

当我们调用 run_twice()时，传入 Tortoise 的实例：

```txt
>>> run_twice(Tortoise())
Tortoise is running slowly...
Tortoise is running slowly...
```

你会发现，新增一个 Animal 的子类，不必对 run_twice() 做任何修改，实际上，任何依赖 Animal 作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：

对于一个变量，我们只需要知道它是 Animal 类型，无需确切地知道它的子类型，就可以放心地调用 run() 方法，而具体调用的 run() 方法是作用在 Animal、Dog、Cat 还是 Tortoise 对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种 Animal 的子类时，只要确保 run() 方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

对扩展开放：允许新增 Animal 子类；

对修改封闭：不需要修改依赖 Animal 类型的 run_twice()等函数。

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类 object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树：

![](images/dc2cf509a81df3bc2be2d95b1d396732ffd3c8361fed14e0797a110b7f8c4771.jpg)

# - 静态语言 vs 动态语言

对于静态语言（例如 Java）来说，如果需要传入 Animal 类型，则传入的对象必须是 Animal 类型或者它的子类，否则，将无法调用 run() 方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

```python
class Timer(object): def run(self): print('Start...')
```

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object”就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object”。许多函数接收的参数就是“file-like object”，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

# 小结

继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

# 6.4 获取对象信息

当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

# - 使用 type()

首先，我们来判断对象类型，使用type()函数：基本类型都可以用type()判断：

```txt
>>> type(123)
<class 'int'>  
>>> type('str')  
<class 'str'>  
>>> type(None)  
<class None>
```

如果一个变量指向函数或者类，也可以用 type()判断：

```txt
>>> type(abs)
<class 'builtin_function_or_method'> 
>>> type(a) 
<class __main__.Animal'>
```

但是 type()函数返回的是什么类型呢？它返回对应的 Class 类型。如果我们要在 if 语句中判断，就需要比较两个变量的 type 类型是否相同：

```txt
>>>type(123)  $= =$  type(456)   
True   
>>>type(123)  $= =$  int   
True   
>>>type('abc')  $= =$  type('123')   
True   
>>>type('abc')  $= =$  str   
True   
>>>type('abc')  $= =$  type(123)   
False
```

判断基本数据类型可以直接写 int，str 等，但如果要判断一个对象是否是函数怎么办？可以使用 types 模块中定义的常量：

```python
>>> import types
>>> def fn():
...
...
...
>>> type(fn) == types.FunctionType
True
>>> type(abs) == types BuiltInFunctionType
True
>>> type(lambda x: x) == types LambdaType
True
>>> type((x for x in range(10))) == types.generatorType
True
```

# - 使用isinstance()

对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。我们回顾上次的例子，如果继承关系是：

```txt
object -> Animal -> Dog -> Husky
```

那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：

```erlang
>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
```

然后，判断：

```html
>>>isinstance(h,Husky) True
```

没有问题，因为  $\mathsf{h}$  变量指向的就是Husky对象。

再判断：

```html
>>>isinstance(h，Dog) True
```

h虽然自身是Husky类型，但由于Husky是从Dog继承下来的，所以，h也还是Dog类型。换句话说，isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

因此，我们可以确信，h还是Animal类型：

```txt
>>> isinstance(h, Animal) True
```

同理，实际类型是Dog的d也是Animal类型：

```txt
>>> isinstance(d, Dog) and isinstance(d, Animal) True
```

但是，d不是Husky类型：

```txt
>>>isinstance(d,Husky) False
```

能用 type()判断的基本类型也可以用 isinstance()判断：

```txt
>>>isinstance('a',str)   
True   
>>>isinstance(123,int)   
True   
>>>isinstance(b'a',bytes)   
True
```

并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple:

```erlang
>>>isinstance([1,2,3], (list,tuple))   
True   
>>>isinstance((1,2,3)，(list,tuple))   
True
```

# ·使用dir()

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

```javascript
>>>dir('ABC') ['__add__','__class__','__contains__','__delattr__','__dir__','__doc__','__eq__', '__format__','__ge__','__getattribute__','__getitem__','__getnewargs__','__gt__', '__hash__','__init__','__iter__','__le__','__len__','__lt__','__mod__','__mul__', 'ne'，'new'，'reduce'，'reduce_ex'，'repr'，'rmod'，'rmul'，'setattr'，'sizeof'，'str'，'subclasshook'，'capatalize'，'casefold'，'center'， 'count'，'encode'，'endswith'，'expandtabs'，'find'，'format'，'format_map'，'index'，'isalnum'， 'isalpha'，'isdecimal'，'isdigit'，'isidentifier'，'islower'，'isnumeric'，'isprintable'， 'isspace'，'istitle'，'isupper'，'join'，'ljust'，'lower'，'lstrip'，'maketrans'，'partition'， 'replace'，'rfind'，'rindex'，'rjust'，'rpartition'，'rsplit'，'rstrip'，'split'，'splitslines'， 'startswith'，'strip'，'swapcase'，'title'，'translate'，'upper'，'zfill']
```

类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__( )方法，所以，下面的代码是等价的：

```txt
>>>len('ABC')   
3   
>>>ABC'.len_()   
3
```

我们自己写的类，如果也想用len(myObj)的话，就自己写一个len_()方法：

```txt
>>>class MyDog(object): deflen_self) return 100   
>>>dog  $=$  MyDog()   
>>>len(dog)   
100
```

剩下的都是普通属性或方法，比如 lower()返回小写的字符串：

```txt
>>> 'ABC'.lower()
'abc'
```

仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

```python
>>>class MyObject(object): def __init__(self): self.x = 9 def power(self): return self.x \* self.x   
>>>obj  $=$  MyObject()
```

紧接着，可以测试该对象的属性：

```txt
>>> hasattr(obj, 'x') # 有属性'x'吗?  
True  
>>> obj.x  
9  
>>> hasattr(obj, 'y') # 有属性'y'吗?  
False  
>>> setattr(obj, 'y', 19) # 设置一个属性'y'  
>>> hasattr(obj, 'y') # 有属性'y'吗?  
True  
>>> getattr(obj, 'y') # 获取属性'y'  
19  
>>> obj.y # 获取属性'y'  
19
```

如果试图获取不存在的属性，会抛出 AttributeError 的错误：

```txt
>>> getattr(obj, 'z') # 获取属性'z' Traceback (most recent call last): File "<stdin>", line 1, in <module>
```

```txt
AttributeError: 'MyObject' object has no attribute 'z'
```

可以传入一个 default 参数，如果属性不存在，就返回默认值：

```txt
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404404
```

也可以获得对象的方法：

```html
>>> hasattr(obj, 'power') # 有属性'power'吗？  
True  
>>> getattr(obj, 'power') # 获取属性'power'  
<bound method MyObject.power of __main__.MyObject object at 0x10077a6a0>>  
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn  
>>> fn # fn指向obj.power  
<bound method MyObject.power of __main__.MyObject object at 0x10077a6a0>>  
>>> fn() # 调用fn()与调用obj.power()是一样的  
81
```

# ·小结

通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

```txt
sum = obj.x + obj.y
```

就不要写：

```txt
sum = getattr(obj, 'x') + getattr(obj, 'y')
```

一个正确的用法的例子如下：

```python
def readImage(fp): if hasattr(fp, 'read'): return Data(fp) return None
```

假设我们希望从文件流 fp 中读取图像，我们首先要判断该 fp 对象是否存在 read 方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

# 6.5 实例属性和类属性

由于Python是动态语言，根据类创建的实例可以任意绑定属性。给实例绑定属性的方法是通过实例变量，或者通过self变量：

```python
class Student(object): def __init__(self, name): self.name = name  
s = Student('Bob')  
s.score = 90
```

但是，如果 Student 类本身需要绑定一个属性呢？可以直接在 class 中定义属性，这种属性是类属性，归 Student 类

所有：

```python
class Student(object):
    name = 'Student'
```

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：

```python
>>> class Student(object):
    ...     name = 'Student'
    ...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
```

从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# 7 面向对象高级编程

数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。

我们会讨论多重继承、定制类、元类等概念。

# 7.1 使用__slots__

正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

```txt
class Student(object): pass
```

然后，尝试给实例绑定一个属性：

```txt
>>>s  $\equiv$  Student()   
>>>s.name  $=$  'Michael' #动态给实例绑定一个属性   
>>>print(s.name)   
Michael
```

还可以尝试给实例绑定一个方法：

```python
>>> def set_age(self, age): # 定义一个函数作为实例方法
...
...
>>> self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果
25
```

但是，给一个实例绑定的方法，对另一个实例是不起作用的：

```typescript
>>>s2  $\equiv$  Student() # 创建新的实例   
>>>s2.set_age(25)# 尝试调用方法   
Traceback (most recent call last): File "<stdin>",line 1,in <module>   
AttributeError:'Student'object has no attribute 'set_age'
```

为了给所有实例都绑定方法，可以给class绑定方法：

```txt
>>> def set_score(self, score):  
... self.score = score  
...  
>>> Student.set_score = set_score
```

给class绑定方法后，所有实例均可调用：

```txt
>>>s.set_score(100)   
>>>s.score
```

```txt
100  
>>>s2.set_score(99)  
>>>s2.score  
99
```

通常情况下，上面的 set_score 方法可以直接定义在 class 中，但动态绑定允许我们在程序运行的过程中动态给 class 加上功能，这在静态语言中很难实现。

- 使用slots

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

然后，我们试试：

```python
>>>s = Student() # 创建新的实例  
>>>s.name = 'Michael' # 绑定属性'name'  
>>>s.age = 25 # 绑定属性'age'  
>>>s.score = 99 # 绑定属性'score'  
Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>  
AttributeError: 'Student' object has no attribute 'score'
```

由于'score'没有被放到__slots_中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。使用__slots要注意，__slots定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

```txt
>>>class GraduateStudent(Student): pass   
>>>g  $=$  GraduateStudent()   
>>>g.score  $= 9999$
```

除非在子类中也定义__slots，这样，子类实例允许定义的属性就是自身的__slots加上父类的__slots。

# 7.2 使用@property

在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

```txt
s = Student()
s.score = 9999
```

这显然不合逻辑。为了限制 score 的范围，可以通过一个 set_score()方法来设置成绩，再通过一个 get_score()来获取成绩，这样，在 set_score()方法里，就可以检查参数：

```python
class Student(object): def get_score(self): return self._score def set_score(self, value):
```

```python
if not isinstance(value, int): raise ValueError('score must be an integer!') if value  $< 0$  or value  $>100$  .. raise ValueError('score must between O \~ 100!') self._score  $=$  value
```

现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：

```txt
>>> s = Student()
>>> s.set_score(60) # ok!
>>> s.get_score()
60
>>> s.set_score(9999)
Traceback (most recent call last):
...
ValueError: score must between 0 ~ 100!
```

但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

```python
class Student(object): @property def score(self): return self._score @score setter def score(self, value): if not isinstance(value, int): raise ValueError('score must be an integer!') if value  $< 0$  or value  $>100$  .. raise ValueError('score must between O \~ 100!') self._score = value
```

@property 的实现比较复杂，我们先考察如何使用。把一个getter 方法变成属性，只需要加上@property 就可以了，此时，@property 本身又创建了另一个装饰器@score setter，负责把一个setter 方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

```txt
>>>s = Student()   
>>>s.score  $= 60$  #OK，实际转化为s.set_score(60)   
>>>s.score # OK，实际转化为s.get_score()   
60   
>>>s.score  $= 9999$    
Traceback (most recent call last):   
...   
ValueError: score must between 0 ~ 100!
```

注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

```python
class Student(object): @property def birth(self): return self._birth @birth setter def birth(self, value): self._birth = value @property def age(self): return 2015 - self._birth
```

上面的 birth 是可读写属性，而 age 就是一个只读属性，因为 age 可以根据 birth 和当前时间计算出来。

# 小结

@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

练习

请利用@property 给一个 Screen 对象加上 width 和 height 属性，以及一个只读属性 resolution.

# 7.3 多重继承

继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。

回忆一下 Animal 类层次的设计，假设我们要实现以下 4 种动物：

Dog -狗狗；  
- Bat - 蝙蝠;  
- Parrot - 鹦鹉;  
Ostrich - 驴鸟。

如果按照哺乳动物和鸟类归类，我们可以设计出这样的类的层次：

![](images/a1536fafa6be3b6b57b16230118144e05832c80f7512d2ab811ca921930c79d8.jpg)

但是如果按照“能跑”和“能飞”来归类，我们就应该设计出这样的类的层次：

![](images/7625cef52eefcec16051e85a064e5b9d6075a7539558aa38e75fc8c954af10a5.jpg)

如果要把上面的两种分类都包含进来，我们就得设计更多的层次：

哺乳类：能跑的哺乳类，能飞的哺乳类；  
- 鸟类：能跑的鸟类，能飞的鸟类。

这么一来，类的层次就复杂了：

![](images/c8ceaabb6907a3ad283319416cde578b6266792e3852780fe86f571656168d8a.jpg)

如果要再增加“宠物类”和“非宠物类”，这么搞下去，类的数量会呈指数增长，很明显这样设计是不行的。正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：

```python
class Animal(object): pass   
#大类:   
class Mammal(Animal): pass   
class Bird(Animal): pass   
#各种动物：   
class Dog(Mammal): pass   
class Bat(Mammal): pass   
class Parrot(Bird): pass   
class Ostrich(Bird): pass
```

现在，我们要给动物再加上 Runnable 和 Flyable 的功能，只需要先定义好 Runnable 和 Flyable 的类：

```python
class Runnable(object): def run(self): print('Running...')   
class Flyable(object): def fly(self): print('Flying...)
```

对于需要 Runnable 功能的动物，就多继承一个 Runnable，例如 Dog:

```txt
class Dog(Mammal, Runnable): pass
```

对于需要 Flyable 功能的动物，就多继承一个 Flyable，例如 Bat:

```txt
class Bat(Mammal, Flyable): pass
```

通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# - MixIn

在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich 继承自 Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让 Ostrich 除了继承自 Bird 外，再同时继承 Runnable。这种设计通常称之为 MixIn。

为了更好地看出继承关系，我们把 Runnable 和 Flyable 改为 RunnableMixIn 和 FlyableMixIn。类似的，你还可以定义出肉食动物 CarnivorousMixIn 和植食动物 HerbivoresMixIn，让某个动物同时拥有好几个 MixIn:

```txt
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn): pass
```

MixIn 的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个 MixIn 的功能，而不是设计多层次的复杂的继承关系。

Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。

比如，编写一个多进程模式的TCP服务，定义如下：

```txt
class MyTCPServer(TCPServer, ForkingMixIn): pass
```

编写一个多线程模式的 UDP 服务，定义如下：

```txt
class MyUDPServer(UDPServer, ThreadingMixIn): pass
```

如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn:

```txt
class MyTCPServer(TCPServer, CoroutineMixIn): pass
```

这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

# 小结

由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

只允许单一继承的语言（如 Java）不能使用 MixIn 的设计。

# 7.4 定制类

看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

```txt
- str
```

我们先定义一个Student类，打印一个实例：

```python
>>> class Student(object):
...
... def __init__(self, name):
...
... self.name = name
...
>>> print(Student('Michael'))
<__main__.Student object at 0x109afb190>
```

打印出一堆<__main__.Student object at 0x109afb190>，不好看。

怎么才能打印得好看呢？只需要定义好_str_()方法，返回一个好看的字符串就可以了：

```python
>>> class Student(object):
...
def __init__(self, name):
...
self.name = name
def __str__(self):
...
return 'Student object (name: %s)' % self.name
>>> print(Student('Michael'))
Student object (name: Michael)
```

这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。

但是细心的朋友会发现直接敲变量不用 print，打印出来的实例还是不好看：

```txt
>>>s  $\equiv$  Student('Michael')   
>>>s   
<__main_.Student object at 0x109afb310>
```

这是因为直接显示变量调用的不是_str_(，而是_repr_(，两者的区别是_str_(返回用户看到的字符串，而_repr_(返回程序开发者看到的字符串，也就是说，_repr_(是为调试服务的。

解决办法是再定义一个 repr (). 但是通常_str(   )和_repr (   )代码都是一样的, 所以, 有个偷懒的写法:

```python
class Student(object): def __init__(self, name): self.name = name def __str__(self): return 'Student object (name=%s)' % self.name __repr__ = __str__
```

```txt
- __iter__
```

如果一个类想被用于 for ... in 循环，类似 list 或 tuple 那样，就必须实现一个__iter__(方法，该方法返回一个迭代对象，然后，Python 的 for 循环就会不断调用该迭代对象的__next__(方法拿到循环的下一个值，直到遇到 StopIteration 错误时退出循环。

我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

```python
class Fib(object): def__init__(self): self.a,self.b  $= 0$  ，1#初始化两个计数器a，b def__iter__(self): return self #实例本身就是迭代对象，故返回自己
```

```python
def __next__(self):
    self.a, self.b = self.b, self.a + self.b # 计算下一个值
    if self.a > 100000: # 退出循环的条件
        raise StopIteration();
    return self.a # 返回下一个值
```

现在，试试把 Fib 实例作用于 for 循环：

```txt
>>> for n in Fib():
... print(n)
...
1
1
2
3
5
...
46368
75025
```

- __*_getitem

Fib 实例虽然能作用于 for 循环，看起来和 list 有点像，但是，把它当成 list 来使用还是不行，比如，取第 5 个元素：

```txt
>>> Fib() [5]  
Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>  
TypeError: 'Fib' object does not support indexing
```

要表现得像 list 那样按照下标取出元素，需要实现 __getitem__()方法：

```python
class Fib(object): def __*_self, n): a, b = 1, 1 for x in range(n): a, b = b, a + b return a
```

现在，就可以按下标访问数列的任意一项了：

```txt
>>>f  $=$  F1   
>>>f[0]   
1   
>>>f[1]   
1   
>>>f[2]   
2   
>>>f[3]   
3
```

```txt
>>>f[10]   
89   
>>>f[100]   
573147844013817084101
```

但是 list 有个神奇的切片方法:

```txt
>>> list(range(100))[5:10] [5, 6, 7, 8, 9]
```

对于Fib却报错。原因是_getitem()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：

```python
class Fib(object): def __*_self, n): if isinstance(n, int): #  $n$  是索引 a, b = 1, 1 for x in range(n): a, b = b, a + b return a if isinstance(n, slice): #  $n$  是切片 start = n.start stop = n.stop if start is None: start = 0 a, b = 1, 1 L = [] for x in range(stop): if x >= start: L.append(a) a, b = b, a + b return L
```

现在试试Fib的切片：

```txt
>>>f  $=$  Fib()   
>>>f[0:5]   
[1,1,2,3,5]   
>>>f[:10]   
[1,1,2,3,5,8,13,21,34,55]
```

但是没有对step参数作处理：

```json
>>>f[:10:2] [1,1,2,3,5,8,13,21,34,55,89]
```

也没有对负数作处理，所以，要正确实现一个_getitem_()还是有很多工作要做的。

此外，如果把对象看成dict，_getitem_()的参数也可能是一个可以作key的object，例如str。

与之对应的是__setitem__(方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__(方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动

态语言的“鸭子类型”，不需要强制继承某个接口。

```txt
- __getattr__
```

正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：

```python
class Student(object): def __init__(self): self.name = 'Michael'
```

调用name属性，没问题，但是，调用不存在的score属性，就有问题了：

```txt
>>>s  $\equiv$  Student()   
>>>print(s.name)   
Michael   
>>>print(s.score)   
Traceback (most recent call last):   
...   
AttributeError:'Student'object has no attribute 'score'
```

错误信息很清楚地告诉我们，没有找到 score 这个 attribute。

要避免这个错误，除了可以加上一个 score 属性外，Python 还有另一个机制，那就是写一个 __getattr__() 方法，动态返回一个属性。修改如下：

```python
class Student(object): def __init__(self): self.name  $=$  'Michael' def __getattr__(self, attr): if attr  $= =$  'score': return 99
```

当调用不存在的属性时，比如 score，Python 解释器会试图调用 __getattr__(self, 'score') 来尝试获得属性，这样，我们就有机会返回 score 的值：

```txt
>>>s  $\equiv$  Studen   
>>>s.name   
'Michael'   
>>>s.score   
99
```

返回函数也是完全可以的：

```python
class Student(object): def __getattr__(self, attr): if attr  $= =$  'age': return lambda: 25
```

只是调用方式要变为：

```txt
>>>s.age()
```

25

注意，只有在没有找到属性的情况下，才调用_getattr_，已有的属性，比如name，不会在_getattr_中查找。此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的_getattr_默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

```python
class Student(object): def __getattr__(self, attr): if attr  $= =$  'age': return lambda: 25 raise AttributeError('\'Student\' object has no attribute \%'s'' % attr)
```

这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

举个例子：

现在很多网站都搞RESTAPI，比如新浪微博、豆瓣啥的，调用API的URL类似：

- http://api.server/user/friends  
- http://api.server/user/timeline/list

如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的_getattr，我们可以写出一个链式调用：

```python
class Chain(object): def __init__(self, path  $=$  ): self._path  $\equiv$  path def __getattr__(self, path): return Chain('%s/%s' % (self._path, path)) def __str__(self): return self._path __repr_  $\equiv$  str
```

试试：

```txt
>>>Chain().status.usertimeline.list '/status/user/timeline/list'
```

这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！

还有些REST API会把参数放到URL中，比如GitHub的API：

```batch
GET /users/:user/repository
```

调用时，需要把:user 替换为实际用户名。如果我们能写出这样的链式调用：

```txt
Chain().users('michael').repo
```

就可以非常方便地调用API了。有兴趣的童鞋可以试试写出来。

```txt
-call
```

一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

```python
class Student(object): def __init__(self, name): self.name = name def __call__(self): print('My name is %s.'% self.name)
```

调用方式如下：

```txt
>>>s  $\equiv$  Student('Michael') >s() #self参数不要传入 MynameisMichael.
```

__call__(还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__( )的类实例：

```txt
>>> callable(Student())   
True   
>>> callable(max)   
True   
>>> callable([1, 2, 3])   
False   
>>> callable(None)   
False   
>>> callable('str')   
False
```

通过 callable()函数，我们就可以判断一个对象是否是“可调用”对象。

小结

Python 的 class 允许定义许多定制方法，可以让我们非常方便地生成特定的类。

# 7.5 使用枚举类

当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：

```matlab
JAN = 1  
FEB = 2  
MAR = 3  
...  
NOV = 11  
DEC = 12
```

好处是简单，缺点是类型是int，并且仍然是变量。

更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：

```python
from enum import Enum  
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
```

这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：

```python
for name, member in Month._members_.items(): print(name, ' $\Rightarrow$ ', member, ' $\),\($ , member.value)
```

value属性则是自动赋给成员的int常量，默认从1开始计数。

如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

```python
from enum import Enum, unique   
@unique   
class Weekday(Enum): Sun  $= 0$  #Sun的value被设定为0 Mon  $= 1$  Tue  $= 2$  Wed  $= 3$  Thu  $= 4$  Fri  $= 5$  Sat  $= 6$
```

@unique 装饰器可以帮助我们检查保证没有重复值。

访问这些枚举类型可以有若干种方法：

```txt
>>> day1 = Weekday.Mon  
>>> print(day1)  
Weekday.Mon  
>>> print(Weekday.Tue)  
Weekday.Tue  
>>> print(Weekday['Tue'])  
Weekday.Tue  
>>> print(Weekday.Tue.value)  
2  
>>> print(day1 == Weekday.Mon)  
True  
>>> print(day1 == Weekday.Tue)  
False  
>>> print(Weekday(1))  
Weekday.Mon  
>>> print(day1 == Weekday(1))  
True  
>>> Weekday(7)
```

```python
Traceback (most recent call last):   
...   
ValueError: 7 is not a valid Weekday   
>>> for name, member in Weekday._members_.items():   
... print(name,  $\mathbf{\Phi}^{\prime} = \mathbf{\Phi}^{\prime}$  , member)   
Sun  $= >$  Weekday.Sun   
Mon  $= >$  Weekday.Mon   
Tue  $= >$  Weekday.Tue   
Wed  $= >$  Weekday.Wed   
Thu  $= >$  Weekday.Thu   
Fri  $= >$  Weekday.Fri   
Sat  $= >$  Weekday.Sat
```

可见，既可以用成员名称引用枚举常量，又可以直接根据 value 的值获得枚举常量。

小结

Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。

# 7.6 使用元类

-type()

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

比方说我们要定义一个Hello的class，就写一个hello.py模块：

```python
class Hello(object):
    def hello(self, name='world():
        print('Hello, %s. % name')
```

当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象，测试如下：

```python
>>> from hello import Hello
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'> 
>>> print(type(h))
<class 'hello.Hello'>
```

type()函数可以查看一个类型或变量的类型，Hello 是一个 class，它的类型就是 type，而 h 是一个实例，它的类型就是 class Hello。

我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过 type()函数创建出 Hello 类，而无需通过 class Hello(object)...的定义：

```txt
>>> def fn(self, name='world'): # 先定义函数
...
...
print('Hello, %s.' % name)
...
...
```

```txt
>>>Hello  $=$  type('Hello'，(object,)，dict（hello  $\equiv$  fn))#创建Helloclass   
>>>h  $=$  Hello()   
>>>h.hello()   
Hello,world.   
>>>print(type(Hello))   
<class 'type'>   
>>>print(type(h))   
<class'_main_.Hello'>
```

要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；  
2. 继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，别忘了 tuple 的单元素写法；  
3. class 的方法名称与函数绑定，这里我们把函数 fn 绑定到方法名 hello 上。

通过 type()函数创建的类和直接写 class 是完全一样的，因为 Python 解释器遇到 class 定义时，仅仅是扫描一下 class 定义的语法，然后调用 type()函数创建出 class。

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

# - metaclass（重要）

除了使用 type()动态创建类以外，要控制类的创建行为，还可以使用 metaclass。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据 metaclass 创建出类，所以：先定义 metaclass，然后创建类。

连接起来就是：先定义 metaclass，就可以创建类，最后创建实例。

所以，metaclass 允许你创建类或者修改类。换句话说，你可以把类看成是 metaclass 创建出来的“实例”。

metaclass 是 Python 面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用 metaclass 的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。

我们先看一个简单的例子，这个 metaclass 可以给我们自定义的 MyList 增加一个 add 方法：

定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

metaclass是类的模板，所以必须从`type`类型派生：

```python
class ListMetaclass(type): def __new__(cls, name, bases, attrs): attrs['add'] = lambda self, value: self.append(value) return type.__new__(cls, name, bases, attrs)
```

有了 ListMetaclass，我们在定义类的时候还要指示使用 ListMetaclass 来定制类，传入关键字参数 metaclass:

```python
class MyList(list, metaclass=ListMetaclass): pass
```

当我们传入关键字参数 metaclass 时，魔术就生效了，它指示 Python 解释器在创建 MyList 时，要通过 ListMetaclass._new_() 来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

new_()方法接收到的参数依次是：

1. 当前准备创建的类的对象；  
2. 类的名字；  
3. 类继承的父类集合；

# 4. 类的方法集合。

测试一下 MyList 是否可以调用 add() 方法：

```txt
>>> L = MyList()
>>> L.add(1)
>> L
[1]
```

而普通的 list 没有 add() 方法:

```python
>>> L2 = list()
>>> L2.add(1)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'add'
```

动态修改有什么意义？直接在 MyList 定义中写上 add() 方法不是更简单吗？正常情况下，确实应该直接写，通过 metaclass 修改纯属变态。

但是，总会遇到需要通过 metaclass 修改类定义的。ORM 就是一个典型的例子。

ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

要编写一个 ORM 框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

让我们来尝试编写一个 ORM 框架。

编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个 ORM 框架，想定义一个 User 类来操作对应的数据库表 User，我们期待他写出这样的代码：

```txt
class User(Model): #定义类的属性到列的映射： id  $=$  IntegerField('id') name  $=$  StringField('username') email  $=$  StringField('email') password  $=$  StringField('password')
```

```txt
创建一个实例：  
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')  
# 保存到数据库：  
u.save()
```

其中，父类 Model 和属性类型 StringField、IntegerField 是由 ORM 框架提供的，剩下的魔术方法比如 save() 全部由 metaclass 自动完成。虽然 metaclass 的编写会比较复杂，但 ORM 的使用者用起来却异常简单。

现在，我们就按上面的接口来实现该 ORM。

首先来定义Field类，它负责保存数据库表的字段名和字段类型：

```python
class Field(object): def __init__(self, name, column_type): self.name = name self.columns_type = column_type def __str__(self):
```

class StringField(Field):  
```erb
return'<%s:%s>'% (self._class_.__name_, self.name)
```

在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：

class ModelMetaclass(type):  
```python
def __init__(self, name):
    super(StringField, self).__init__(name, 'varchar(100)')
ss IntegerField(Field):
def __init__(self, name):
    super(IntegerField, self).__init__(name, 'bigint')
```

下一步，就是编写最复杂的ModelMetaclass了：

```python
def __new__(cls, name, bases, attrs):
    if name == 'Model':
        return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s => %s' % (k, v))
                mappings[k] = v
            for k in mappings.keys():
                attrs.pop(k)
                attrs['__mappings__'] = mappings # 保存属性和列的映射关系
                attrs['__table__'] = name # 假设表名和类名一致
            return type.__new__(cls, name, bases, attrs)
```

以及基类 Model:

```python
class Model(dist, metaclass=ModelMetaclass): def __init__(self, **kw): super(Model, self).__init__(**kw) def __getattr__(self, key): try: return self[key] except KeyError: raise ValueError(r'''Model' object has no attribute '%s'" % key) def __setattr__(self, key, value): self[key] = value
```

```python
def save(self):
    fields = []
    params = []
    args = []
    for k, v in self._mappings_.items():
        fields.append(v.name)
        params.append(?')
        args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self._table_, ':', '.join(selfs), ','.join.params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
```

当用户定义一个 class User(Model)时，Python 解释器首先在当前类 User 的定义中查找 metaclass，如果没有找到，就继续在父类 Model 中查找 metaclass，找到了，就使用 Model 中定义的 metaclass 的 ModelMetaclass 来创建 User 类，也就是说，metaclass 可以隐式地继承到子类，但子类自己却感觉不到。

在ModelMetaclass中，一共做了几件事情：

1. 排除掉对 Model 类的修改；  
2. 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；  
3. 把表名保存到 table 中，这里简化为表名默认为类名。

在 Model 类中，就可以定义各种操作数据库的方法，比如 save(), delete(), find(), update 等等。

我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。

编写代码试试：

```python
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
```

输出如下：

```txt
Found model: User  
Found mapping: email => <StringField@email>  
Found mapping: password => <StringField-password>  
Found mapping: id => <IntegerField:uid>  
Found mapping: name => <StringField:name>  
SQL: insert into User (password, email, username, id) values (?,?,?,?)  
ARGS: ['my-pwd', 'test@orm.org', 'Michael', 12345]
```

可以看到，save()方法已经打印出了可执行的SQL语句，以及参数列表，只需要真正连接到数据库，执行该SQL语句，就可以完成真正的功能。

不到100行代码，我们就通过metaclass实现了一个精简的ORM框架。

# 小结

metaclass 是 Python 中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。

# 8 错误、调试和测试

在程序运行过程中，总会遇到各种各样的错误。

有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常称之为bug，bug是必须修复的。

有的错误是用户输入造成的，比如让用户输入 email 地址，结果得到一个空字符串，这种错误可以通过检查用户输入来做相应的处理。

还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了。这类错误也称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出。

Python 内置了一套异常处理机制，来帮助我们进行错误处理。

此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python 的 pdb 可以让我们以单步方式执行代码。

最后，编写测试也很重要。有了良好的测试，就可以在程序修改后反复运行，确保程序输出符合我们编写的测试。

# 8.1 错误处理

在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数 open()，成功时返回文件描述符（就是一个整数），出错时返回-1。

用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错：

```python
def foo(): r = some_function() if  $r == (-1)$  return(-1) #do something return r   
def bar(): r  $=$  foo() if  $r == (-1)$  print('Error') else: pass
```

一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。

所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。

try

让我们用一个例子来看看try的机制：

```python
try: print('try...')  $r = 10 / 0$  print('result:,'，r) except ZeroDivisionError as e: print('except:,'，e)
```

```python
finally: print('finally...') print('END')
```

当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

上面的代码在计算  $10 / 0$  时会产生一个除法运算错误：

```txt
try... except: division by zero finally... END
```

从输出可以看到，当错误发生时，后续语句 print('result: ', r) 不会被执行，except 由于捕获到 ZeroDivisionError，因此被执行。最后，finally 语句被执行。然后，程序继续按照流程往下走。

如果把除数0改成2，则执行结果如下：

```txt
try... result:5 finally... END
```

由于没有错误发生，所以 except 语句块不会被执行，但是 finally 如果有，则一定会被执行（可以没有 finally 语句）。

你还可以猜测，错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：

```javascript
try: print('try...') r = 10 / int('a') print('result: ', r) except ValueError as e: print('ValueError: ', e) except ZeroDivisionError as e: print('ZeroDivisionError: ', e) finally: print('finally...') print('END')
```

int()函数可能会抛出 ValueError，所以我们用一个 except 捕获 ValueError，用另一个 except 捕获 ZeroDivisionError。

此外，如果没有错误发生，可以在 except 语句块后面加一个 else，当没有错误发生时，会自动执行 else 语句：

```javascript
try: print('try...') r = 10 / int('2') print('result: ', r) except ValueError as e: print('ValueError: ', e)
```

```python
except ZeroDivisionError as e: print('ZeroDivisionError: ', e)   
else: print('no error!')   
finally: print('finally...')   
print('END')
```

Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

```python
try: foo() except ValueError as e: print('ValueError') except ValueError as e: print('UnicodeError')
```

第二个 except 永远也捕获不到 ValueError，因为 ValueError 是 ValueError 的子类，如果有，也被第一个 except 给捕获了。

Python 所有的错误都是从 BaseException 类派生的，常见的错误类型和继承关系看这里：

https://docs.python.org/3/library/exceptions.html#exception-hierarchy

使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo(), foo()调用bar(),结果bar()出错了，这时，只要main()捕获到了，就可以处理：

```python
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error: ', e)
    finally:
        print('finally...')
```

也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。

# ·调用堆栈

如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py:

```txt
err.py: def foo(s): return 10 / int(s) def bar(s):
```

```python
return foo(s) * 2
def main():
    bar('0')
main()
```

执行，结果如下：

```txt
$ python3 err.py
Traceback (most recent call last):
    File "err.py", line 11, in <module>
        main()
    File "err.py", line 9, in main
        bar('0')
    File "err.py", line 6, in bar
        return foo(s) * 2
    File "err.py", line 3, in foo
        return 10 / int(s)
ZeroDivisionError: division by zero
```

出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链：

错误信息第1行：

Traceback (most recent call last):

告诉我们这是错误的跟踪信息。

第2~3行：

```txt
File "err.py", line 11, in <module> main()
```

调用 main() 出错了，在代码文件 err.py 的第 11 行代码，但原因是第 9 行：

```txt
File "err.py", line 9, in main bar('0')
```

调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：

```txt
File "err.py", line 6, in bar return foo(s) * 2
```

原因是 return foo(s) * 2 这个语句出错了，但这还不是最终原因，继续往下看：

```txt
File "err.py", line 3, in foo return 10 / int(s)
```

原因是 return 10 / int(s) 这个语句出错了，这是错误产生的源头，因为下面打印了：

```txt
ZeroDivisionError: integer division or modulo by zero
```

根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10/0时出错，至此，找到错误源头。

# - 记录错误

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

Python 内置的 logging 模块可以非常容易地记录错误信息：

```python
err Logging.py   
import logging   
def foo(s): return 10 / int(s)   
def bar(s): return foo(s) \*2   
def main(): try: bar('0') except Exception as e: logging_exception(e)   
main()   
print('END')
```

同样是出错，但程序打印完错误信息后会继续执行，并正常退出：

```txt
$ python3 err Logging.py
ERROR:root:division by zero
Traceback (most recent call last):
    File "err Logging.py", line 13, in main
        bar('0')
    File "err Logging.py", line 9, in bar
        return foo(s) * 2
    File "err Logging.py", line 6, in foo
        return 10 / int(s)
ZeroDivisionError: division by zero
END
```

通过配置，logging 还可以把错误记录到日志文件里，方便事后排查。

# - 抛出错误

因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的 class，选择好继承关系，然后，用 raise 语句抛出一个错误的实例：

```txt
err raisepy   
class FooError(ValueError): pass   
def foo(s): n  $=$  int(s) if  $\mathsf{n} = =\mathsf{0}$  .. raise FooError('invalid value:  $\% s^{\prime}\% s$
```

```lua
return 10 / n  
foo('0')
```

执行，可以最后跟踪到我们自己定义的错误：

```python
$ python3 err rais.py
Traceback (most recent call last):
    File "errthrow.py", line 11, in <module>
        foo('0')
    File "errthrow.py", line 8, in foo
        raise FooError('invalid value: %s' % s)
    __main__.FooError: invalid value: 0
```

只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError,TypeError），尽量使用Python内置的错误类型。

最后，我们来看另一种错误处理的方式：

```python
err_eraise.py   
def foo(s): n = int(s) if  $\mathsf{n} = =\mathsf{0}$  .. raise ValueError('invalid value:  $\% s^{\prime}\% s$  1 return 10 / n   
def bar(): try: foo('0') except ValueError as e: print('ValueError!') raise   
bar()
```

在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？

其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

```javascript
try: 10 / 0 except ZeroDivisionError: raise ValueError('input error!')
```

只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。

# 小结

Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。

# 8.2 调试

程序能一次写完并正常运行的概率很小，基本不超过  $1\%$  。总会有各种各样的 bug 需要修正。有的 bug 很简单，看看错误信息就知道，有的 bug 很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复 bug。

第一种方法简单直接粗暴有效，就是用 print()把可能有问题的变量打印出来看看：

```python
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n
def main():
    foo('0')
main()
```

执行后在输出中查找打印的变量值：

```txt
$ python3 err.py
>>> n = 0
Traceback (most recent call last):
...
ZeroDivisionError: integer division or modulo by zero
```

用 print() 最大的坏处是将来还得删掉它，想想程序里到处都是 print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。

# ·断言

凡是用 print()来辅助查看的地方，都可以用断言（assert）来替代：

```python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
```

assert 的意思是，表达式  $n != 0$  应该是 True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，assert语句本身就会抛出AssertionError:

```txt
$ python3 err.py
Traceback (most recent call last):
...
...
```

```txt
AssertionError: n is zero!
```

程序中如果到处充斥着 assert，和 print()相比也好不到哪去。不过，启动 Python 解释器时可以用 -0 参数来关闭 assert:

```txt
$ python3 -0 err.py
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
```

关闭后，你可以把所有的 assert 语句当成 pass 来看。

- logging

把 print() 替换为 logging 是第 3 种方式，和 assert 比，logging 不会抛出错误，而且可以输出到文件：

```txt
import logging   
s = '0'   
n = int(s)   
logging.info('n = %d' % n)   
print(10 / n)
```

logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？

别急，在importlogging之后添加一行配置再试试：

```python
import logging
loggingisticConfig(level=logging INFO)
```

看到输出了：

```python
$ python3 err.py
INFO:root:n = 0
Traceback (most recent call last):
    File "err.py", line 8, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
```

这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

pdb

第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

```txt
# err.py
s = '0'
n = int(s)
print(10 / n)
然后启动:
$ python3 -m pwd err.py
> /Users/michael/Github/learn-python3/samples debug/err.py(2)<module>()
-> s = '0'
```

以参数-m pdb 启动后，pdb 定位到下一步要执行的代码->s = 'θ'。输入命令1来查看代码：

```txt
(Pdb) 1
1 # err.py
2 -> s = '0'
3 n = int(s)
4 print(10 / n)
```

输入命令  $\mathsf{n}$  可以单步执行代码：

```txt
(Pdb) n  
> /Users/michael/Github/learn-cython3/samples debug/err.py()  
-> n = int(s)  
(Pdb) n  
> /Users/michael/Github/learn-cython3/samples debug/err.py()  
-> print(10 / n)
```

任何时候都可以输入命令p变量名来查看变量：

```txt
(Pdb) p s '0' (Pdb) p n 0
```

输入命令q结束调试，退出程序：

```txt
(Pdb) q
```

这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

```txt
-pdb.set_trace()
```

这个方法也是用pdb，但是不需要单步执行，我们只需要importpdb,然后，在可能出错的地方放一个pdb.set_trace(),就可以设置一个断点：

```python
err.py   
import pdb   
s  $=$  '0'   
n  $=$  int(s)   
pdb.set_trace() # 运行到这里会自动暂停   
print(10/n)
```

运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

```txt
$ python3 err.py
> /Users/michael/GitHub/learn-python3/samples debug/err.py(7)<module>
-> print(10 / n)
(Pdb) p n
0
(Pdb) c
Traceback (most recent call last):
```

```txt
File "err.py", line 7, in <module> print(10 / n) ZeroDivisionError: division by zero
```

这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。

- IDE

如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm: http://www-jetbrains.com/pycharm/

另外，Eclipse加上pydev插件也可以调试Python程序。

小结

写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。

虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。

# 8.3 单元测试

如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不陌生。

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

比如对函数 abs()，我们可以编写出以下几个测试用例：

1 输入正数，比如1、1.2、0.99，期待返回值与输入相同；  
2 输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；  
3 输入0，期待返回0；  
4 输入非数值类型，比如 None、[]、{}，期待抛出 TypeError。

把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。

单元测试通过后有什么意义呢？如果我们对 abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对 abs()函数原有的行为造成影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。

这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。

我们来编写一个 Dict 类，这个类的行为和 dict 一致，但是可以通过属性来访问，用起来就像下面这样：

```txt
>>>d  $=$  Dict(a=1,b=2)   
>>>d['a']   
1   
>>>d.a   
1
```

mydict.py代码如下：

```python
class Dictdict): def __init__(self, \*\*kw): super().__init__(\*\*kw) def __getattr__(self,key): try:
```

```python
return self[key]  
except KeyError:  
    raise ValueError(r'\'Dict' object has no attribute '%s'' % key)  
def __setattr__(self, key, value):  
    self[key] = value
```

为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：

```python
import unittest   
from mydict import Dict   
class TestDict(unittest.TestCase): def test_init(self): d  $=$  Dict(a=1,b  $\equiv$  'test') self.assertEqual(d.a,1) self.assertEqual(d.b,'test') self.assertTrue(isinstance(d,dict)) def test_key(self): d  $=$  Dict() d['key']  $=$  'value' self.assertEqual(d.key,'value') def test_attr(self): d  $=$  Dict() d.key  $=$  'value' self.assertTrue('key'in d) self.assertEqual(d['key'], 'value') def test_keyerror(self): d  $=$  Dict() with self.assertRaises(KeyError): value  $=$  d['empty'] def test_atterror(self): d  $=$  Dict() with self.assertRaises(ATTRIBUTEError): value  $=$  d.empty
```

编写单元测试时，我们需要编写一个测试类，从 unittest.TestCase 继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual():

self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等

另一种重要的断言就是期待抛出指定类型的 Error,比如通过 d['empty'] 访问不存在的 key 时,断言会抛出 KeyError:

```python
with self.assertRaises(KeyError): value  $=$  d['empty']
```

而通过 d.empty 访问不存在的 key 时，我们期待抛出 AttributeError:

```python
with self.assertRaises(ATTRIBUTEError): value  $=$  d.empty
```

# ·运行单元测试

一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：

```python
if __name__ == __main__:
    unittest.main()
```

这样就可以把mydict_test.py当做正常的python脚本运行：

```shell
$ python3 mydict_test.py
```

另一种方法是在命令行通过参数-m unitittest直接运行单元测试：

```txt
$ python3 -m unittest mydict_test
...
...
Ran 5 tests in 0.000s
OK
```

这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。

# - setUp与 TearDown

可以在单元测试中编写两个特殊的 setUp()和 tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

setUp()和 TearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在 setUp()方法中连接数据库，在 TearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

```python
class TestDict(unittest.TestCase): def setUp(self): print('setUp...) def tearDown(self): print('tearDown...')
```

可以再次运行测试看看每个测试方法调用前后是否会打印出 setUp...和 tearDown...。

小结

单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

# 8.4 文档测试

如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。比如re模块就带了很多示例代码：

```coffeescript
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
```

可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。

这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？

答案是肯定的。

当我们编写注释时，如果写上这样的注释：

```python
def abs(n):
    ...
    Function to get absolute value of number.
Example:
>>> abs(1)
1
>>> abs(-1)
1
>>> abs(0)
0
...
return n if n >= 0 else (-n)
```

无疑更明确地告诉函数的调用者该函数的期望输入和输出。

并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

doctest 严格按照 Python 交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。

让我们用 doctest 来测试上次编写的 Dict 类:

```python
mydict2.py   
class Dict(dist): Simple dict but also support access as x.y style.  $\begin{array}{rl} & \mathrm{>>d1 = D�ct()}\\ & \mathrm{>>d1['x'] = 100}\\ & \mathrm{>>d1.x}\\ & \mathrm{100}\\ & \mathrm{>>d1.y = 200}\\ & \mathrm{>>d1['y']}\\ & \mathrm{200}\\ & \mathrm{>>d2 = D�ct(a = 1,b = 2,c = '3')} \end{array}$
```

```python
>>>d2.c   
'3'   
>>>d2['empty']   
Traceback (most recent call last):   
...   
KeyError:'empty'   
>>>d2.empty   
Traceback (most recent call last):   
...   
AttributeError:'Dict' object has no attribute 'empty'   
...   
def __init__(self, \*\*kw): super(Dict,self).__init__(\*\*kw)   
def __getattr__(self,key): try: return self[key] except KeyError: raise ValueError(r'''Dict' object has no attribute '\%s'' %key) def __setattr__(self,key, value): self[key]  $=$  value   
if_name  $\equiv$  main': import doctest doctest.testmod()
```

运行 python3 mydict2.py:

$ python3 mydict2.py

什么输出也没有。这说明我们编写的 doctest 运行都是正确的。如果程序有问题，比如把 __getattr__() 方法注释掉，再运行就会报错：

```txt
$ python3 mydict2.py
**********.
File "/Users/michael/GitHub/learn-python3/samples debug/mydict2.py", line 10, in __main__.Dict
Failed example:
d1.x
Exception raised:
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'x'
**********.
File "/Users/michael/GitHub/learn-python3/samples debug/mydict2.py", line 16, in __main__.Dict
Failed example:
d2.c
Exception raised:
    Traceback (most recent call last):
```

```txt
...
AttributeError: 'Dict' object has no attribute 'c'
**********1 items had failures:
2 of 9 in __main__.Dict
***Test Failed*** 2 failures.
```

注意到最后3行代码。当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行。

·练习

对函数 fact(n) 编写 doctest 并执行：

```python
# -- coding: utf-8 --  
def fact(n):
    ...
    ...
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)
if __name__ == '__main__':
import doittest
doctest.testmod()
```

小结

doctest 非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含 doctest 的注释提取出来。用户看文档的时候，同时也看到了 doctest。

# 9 IO 编程

IO在计算机中指Input/Output，也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。

比如你打开浏览器，访问新浪首页，浏览器这个程序就需要通过网络IO获取新浪的网页。浏览器首先会发送数据给新浪服务器，告诉它我想要首页的HTML，这个动作是往外发数据，叫Output，随后新浪服务器把网页发过来，这个动作是从外面接收数据，叫Input。所以，通常，程序完成IO操作会有Input和Output两个数据流。当然也有只用一个的情况，比如，从磁盘读取文件到内存，就只有Input操作，反过来，把数据写到磁盘文件里，就只是一个Output操作。

IO 编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。Input Stream 就是数据从外面（磁盘、网络）流进内存，Output Stream 就是数据从内存流到外面去。对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。

由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：

第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；

另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为异步IO。

同步和异步的区别就在于是否等待IO执行的结果。好比你去麦当劳点餐，你说“来个汉堡”，服务员告诉你，对不起，汉堡要现做，需要等5分钟，于是你站在收银台前面等了5分钟，拿到汉堡再去逛商场，这是同步IO。

你说“来个汉堡”，服务员告诉你，汉堡需要等5分钟，你可以先去逛商场，等做好了，我们再通知你，这样你可以立刻去干别的事情（逛商场），这是异步IO。

很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。总之，异步IO的复杂度远远高于同步IO。

操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，Python也不例外。我们后面会详细讨论Python的IO编程接口。

注意，本章的IO编程都是同步模式，异步IO由于复杂度太高，后续涉及到服务器端程序开发时我们再讨论。

# 9.1 文件读写

读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

# ·读文件

要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

```txt
>>>f  $\equiv$  open('/Users/michael/test.txt'，'r')
```

标示符'r'表示读，这样，我们就成功地打开了一个文件。

如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：

```txt
>>> f = open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'
```

如果文件打开成功，接下来，调用 read() 方法可以一次读取文件的全部内容，Python 把内容读到内存，用一个 str 对

象表示：

```txt
>>>f.read() 'Hello,world!
```

最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：

```txt
>>>f.close()
```

由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try...finally来实现：

```python
try: f = open('/path/to/file', 'r') print(f.read()) finally: if f: f.close()
```

但是每次都这么写实在太繁琐，所以，Python 引入了 with 语句来自动帮我们调用 close() 方法：

```python
with open('/path/to/file', 'r') as f:  
    print(f.read())
```

这和前面的try...finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

调用 read()会一次性读取文件的全部内容，如果文件有 10G，内存就爆了，所以，要保险起见，可以反复调用 read(size) 方法，每次最多读取 size 个字节的内容。另外，调用 readline()可以每次读取一行内容，调用 readlines()一次读取所有内容并按行返回 list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用 read(size) 比较保险；如果是配置文件，调用 readlines() 最方便：

```python
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
```

# -file-like Object

像 open()函数返回的这种有个 read()方法的对象，在 Python 中统称为 file-like Object。除了 file 外，还可以是内存的字节流，网络流，自定义流等等。file-like Object 不要求从特定类继承，只要写个 read()方法就行。

StringIO 就是在内存中创建的 file-like Object，常用作临时缓冲。

# ·二进制文件

前面讲的默认都是读取文本文件，并且是 UTF-8 编码的文本文件。要读取二进制文件，比如图片、视频等等，用 'rb' 模式打开文件即可：

```txt
>>>f = open('/Users/michael/test.jpg'，'rb')  
>>>f.read()  
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' #十六进制表示的字节
```

# - 字符编码

要读取非 UTF-8 编码的文本文件，需要给 open()函数传入 encoding 参数，例如，读取 GBK 编码的文件：

```txt
>>>f = open('/Users/michael/gbk.txt'，'r'，encoding='gbk')  
>>>f.read()  
'测试'
```

遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

```python
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

# ·写文件

写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

```txt
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
```

你可以反复调用 write() 来写入文件，但是务必要调用 f.close() 来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用 close() 方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用 close() 的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用 with 语句来得保险：

```python
with open('/Users/michael/test.txt', 'w') as f:  
    f.write('Hello, world!')
```

要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。

# 小结

在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。

# 9.2 StringIO 和 BytesIO

# - StringIO

很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO 顾名思义就是在内存中读写 str。

要把 str 写入 StringIO，我们需要先创建一个 StringIO，然后，像文件一样写入即可：

```python
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write('')
1
>>> f.write('world {!}')
6
>>> print(f.getvalue())
hello world!
```

getvalue()方法用于获得写入后的 str。

要读取 StringIO，可以用一个 str 初始化 StringIO，然后，像读文件一样读取：

```python
>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...
    s = f-lines()
...
    if s == ':'
...
    break
```

```txt
print(s.strip())
Hello!
Hi!
Goodbye!
```

# - BytesIO

StringIO 操作的只能是 str，如果要操作二进制数据，就需要使用 BytesIO。

BytesIO 实现了在内存中读写 bytes，我们创建一个 BytesIO，然后写入一些 bytes:

```python
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
```

请注意，写入的不是 str，而是经过 UTF-8 编码的 bytes。

和 StringIO 类似，可以用一个 bytes 初始化 BytesIO，然后，像读文件一样读取：

```python
>>> from io import StringIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
```

# 小结

StringIO 和 BytesIO 是在内存中操作 str 和 bytes 的方法，使得和读写文件具有一致的接口。

# 9.3 操作文件和目录

如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

打开Python交互式命令行，我们来看看如何使用os模块的基本功能：

```txt
>>> import os
>>> os.name # 操作系统类型
'posix'
```

如果是 POSIX，说明系统是 Linux、Unix 或 Mac OS X，如果是 nt，就是 Windows 系统。

要获取详细的系统信息，可以调用 uname()函数：

```python
>>> os uname()
posix uname_result(sysname='Darwin',   nomencl='MichaelMacPro.local',   release='14.3.0',
version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')
```

注意 uname()函数在 Windows 上不提供，也就是说，os 模块的某些函数是跟操作系统相关的。

# ·环境变量

在操作系统中定义的环境变量，全部保存在 os.environ 这个变量中，可以直接查看：

```txt
>>> os.environ
envviron{'VERSIONER_PYTHON=PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...}
```

要获取某个环境变量的值，可以调用os.environ.get('key'):

```txt
>>> os.environ.get('PATH')  
'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'  
>>> osviron.get('x', 'default')  
'default'
```

# - 操作文件和目录

操作文件和目录的函数一部分放在 os 模块中，一部分放在 os.path 模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

```txt
查看当前目录的绝对路径：  
>>> os.path_ABSPath(.')  
'/Users/michael'  
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来：  
>>> os.path.join('/Users/michael', 'testdir')  
'/Users/michael/testdir'  
# 然后创建一个目录：  
>>> os.mkdir('/Users/michael/testdir')  
# 删掉一个目录：  
>>> os.rmdir('/Users/michael/testdir')
```

把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：

```txt
part-1/part-2
```

而Windows下会返回这样的字符串：

```txt
part-1\part-2
```

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

```txt
>>> os.path.split('/Users/michael/testdir/file.txt')  
('/Users/michael/testdir', 'file.txt')
```

os.path.splittext()可以直接让你得到文件扩展名，很多时候非常方便：

```txt
>>> os.path+splits text('/path/to/file.txt')  
('/path/to/file', '.txt')
```

这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

文件操作使用下面的函数。假定当前目录下有一个test.txt文件：

```txt
对文件重命名：  
>>> os.rename('test.txt', 'test.py')  
#删掉文件：
```

```txt
>>> os.remove('test.py')
```

但是复制文件的函数居然在 os 模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

```python
>>> [x for x in os.listdir(['.')] if os.path.isdir(x)] ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
```

要列出所有的.py文件，也只需一行代码：

```python
>>> [x for x in os.listdir('/.') if os.path.isfile(x) and os.path.splittext(x)[1] == '.py'] ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
```

是不是非常简洁？

# 小结

Python 的 os 模块封装了操作系统的目录和文件操作，要注意这些函数有的在 os 模块中，有的在 os.path 模块中。

# ·练习

1. 利用os模块编写一个能实现dir -l输出的程序。  
2. 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

# 9.4 序列化

在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict:

```python
d = dict(name='Bob', age=20, score=88)
```

可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即 unpickling。

Python 提供了 pickle 模块来实现序列化。

首先，我们尝试把一个对象序列化并写入文件：

```python
>>> import pickle
>>> d = dict(name='Bob', age=20, score=88)
>>> pickle>dumps(d)
b'\x80\x03\q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
```

- pickle.dumps()方法把任意对象序列化成一个 bytes，然后，就可以把这个 bytes 写入文件。或者用另一个方法 pickle.dump()直接把对象序列化后写入一个 file-like Object:

```txt
>>>f  $=$  open('dump.txt'，'wb')   
>>> pickle.dump(d,f)   
>>>f.close()
```

看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。

当我们要把对象从磁盘读到内存时，可以先把内容读到一个 bytes，然后用 pickle_load()方法反序列化出对象，也可以直接用 pickle_load()方法从一个 file-like Object 中直接反序列化出对象。我们打开另一个 Python 命令行来反序列化刚才保存的对象：

```txt
>>>f  $=$  open('dump.txt'，'rb')   
>>>d  $=$  pickle.load(f)   
>>>f.close()   
>>>d   
{'age':20,'score':88,'name':'Bob'}
```

变量的内容又回来了！

当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。

Pickle 的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于 Python，并且可能不同版本的 Python 彼此都不兼容，因此，只能用 Pickle 保存那些不重要的数据，不能成功地反序列化也没关系。

- JSON

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

<table><tr><td>JSON 类型</td><td>Python 类型</td></tr><tr><td>{}</td><td>dict</td></tr><tr><td>[]</td><td>list</td></tr><tr><td>&quot;string&quot;</td><td>str</td></tr><tr><td>1234.56</td><td>int 或 float</td></tr><tr><td>true/false</td><td>True/False</td></tr><tr><td>null</td><td>None</td></tr></table>

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON:

```python
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
{'age': 20, 'score': 88, 'name': "Bob"}'
```

dumps()方法返回一个str,内容就是标准的JSON。类似的,dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

```python
>>> json_str = {'"age": 20, "score": 88, "name": "Bob"}
>>> json.loadjson_str
{'age': 20, 'score': 88, 'name': 'Bob'}
```

由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。

JSON进阶

Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：

```python
import json   
class Student(object): def__init__(self，name，age，score): self.name  $=$  name self.age  $=$  age self.score  $=$  score   
s  $=$  Student('Bob'，20,88)   
printjson.dumps(s))
```

运行代码，毫不留情地得到一个 TypeError:

```txt
Traceback (most recent call last):  
...  
TypeError: <__main__.Student object at 0x10603cc50> is not JSONSerializable
```

错误的原因是Student对象不是一个可序列化为JSON的对象。

如果连 class 的实例对象都无法序列化为 JSON，这肯定不合理！

别急，我们仔细看看 dumps()方法的参数列表，可以发现，除了第一个必须的 obj 参数外，dumps()方法还提供了一大堆的可选参数：

https://docs.python.org/3/library/json.html#json.dumps

这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

可选参数 default 就是把任意一个对象变成一个可序列为 JSON 的对象，我们只需要为 Student 专门写一个转换函数，再把函数传进去即可：

```python
def student2dict(std): return { 'name': std.name, 'age': std.age, 'score': std.score }
```

这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON:

```txt
>>> printjson.dumps(s, default  $\equiv$  student2dict)) {"age": 20, "name": "Bob", "score": 88}
```

不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：

```txt
printjson.dumps(s, default  $\equiv$  lambda obj: obj._dict_))
```

因为通常 class 的实例都有一个 __dict__ 属性，它就是一个 dict，用来存储实例变量。也有少数例外，比如定义了 __slots__ 的 class。

同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object hook函数负责把dict转换为Student实例：

```python
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
```

运行结果如下：

```python
>>> json_str = {'age': 20, "score": 88, "name": "Bob'}
>>> printjson.load(str, objectfgets=dict2student())
<__main__.Student object at 0x10cd3c190>
```

打印出的是反序列化的Student实例对象。

# 小结

Python 语言特定的序列化模块是 pickle，但如果要把序列化搞得更通用、更符合 Web 标准，就可以使用 json 模块。

json 模块的 dumps()和 loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。

# 10 进程和线程

很多同学都听说过，现代操作系统比如Mac OS X，UNIX，Linux，Windows等，都是支持“多任务”的操作系统。

什么叫“多任务”呢？简单地说，就是操作系统可以同时运行多个任务。打个比方，你一边在用浏览器上网，一边在听MP3，一边在用Word赶作业，这就是多任务，至少同时有3个任务正在运行。还有很多任务悄悄地在后台同时运行着，只是桌面上没有显示而已。

现在，多核CPU已经非常普及了，但是，即使过去的单核CPU，也可以执行多任务。由于CPU执行代码都是顺序执行的，那么，单核CPU是怎么执行多任务的呢？

答案就是操作系统轮流让各个任务交替执行，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。表面上看，每个任务都是交替执行的，但是，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。

真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。

对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。

有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。

由于每个进程至少要干一件事，所以，一个进程至少有一个线程。当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。

我们前面编写的所有的Python程序，都是执行单任务的进程，也就是只有一个线程。如果我们要同时执行多个任务怎么办？

有两种解决方案：

一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。

还有一种方法是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。

当然还有第三种方法，就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用。

总结一下就是，多任务的实现有3种方式：

- 多进程模式；  
- 多线程模式；  
- 多进程+多线程模式。

同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。

因为复杂度高，调试困难，所以，不是迫不得已，我们也不想编写多任务。但是，有很多时候，没有多任务还真不行。想想在电脑上看电影，就必须由一个线程播放视频，另一个线程播放音频，否则，单线程实现的话就只能先把视频播放完再播放音频，或者先把音频播放完再播放视频，这显然是不行的。

Python既支持多进程，又支持多线程，我们会讨论如何编写这两种多任务程序。

# 小结

线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。

# 10.1 多进程

要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。

Unix/Linux 操作系统提供了一个 fork() 系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是 fork() 调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回 0，而父进程返回子进程的 ID。这样做的理由是，一个父进程可以 fork 出很多子进程，所以，父进程要记下每个子进程的 ID，而子进程只需要调用 getppid() 就可以拿到父进程的 ID。

Python 的 os 模块封装了常见的系统调用，其中就包括 fork，可以在 Python 程序中轻松创建子进程：

```python
import os   
print('Process  $(\% s)$  start...' % os.getpid())   
#Only works on Unix/Linux/Mac:   
pid  $=$  os.fork()   
if pid  $= = 0$  . print('I am child process  $(\% s)$  and my parent is  $\% s$  .  $\%$  (os.getpid(), os.getppid()))   
else: print('I  $(\% s)$  just created a child process  $(\% s)$  .  $\%$  (os.getpid(), pid))
```

运行结果如下：

```txt
Process (876) start...  
I (876) just created a child process (877).  
I am child process (877) and my parent is 876.
```

由于 Windows 没有 fork 调用，上面的代码在 Windows 上无法运行。由于 Mac 系统是基于 BSD（Unix 的一种）内核，所以，在 Mac 下运行是没有问题的，推荐大家用 Mac 学 Python！

有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

# - multiprocessing

如果你打算编写多进程的服务程序，Unix/Linux 无疑是正确的选择。由于 Windows 没有 fork 调用，难道在 Windows 上无法用 Python 编写多进程的程序？

由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：

```python
from multiprocessing import Process  
import os  
# 子进程要执行的代码  
def run_proc(name):  
    print('Run child process %s (%s)...' % (name, os.getpid()))  
if __name__ == '__main__':  
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=['test', ])  
    print('Child process will start.')  
p.start()
```

```txt
p.join()   
print('Child process end.')
```

执行结果如下：

```txt
Parent process 928.   
Process will start.   
Run child process test (929)...   
Process end.
```

创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

- Pool

如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

```python
from multiprocessing import Pool
import os, time, random
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
```

执行结果如下：

```txt
Parent process 669.   
Waiting for all subprocesses done...   
Run task 0 (671)...   
Run task 1 (672)...   
Run task 2 (673)...   
Run task 3 (674)...   
Task 2 runs 0.14 seconds..   
Run task 4 (673)...   
Task 1 runs 0.27 seconds.   
Task 3 runs 0.86 seconds.   
Task 0 runs 1.41 seconds.   
Task 4 runs 1.91 seconds.   
All subprocesses done.
```

代码解读：

对 Pool 对象调用 join()方法会等待所有子进程执行完毕，调用 join()之前必须先调用 close()，调用 close()之后就不能继续添加新的 Process 了。

请注意输出的结果，task 0, 1, 2, 3 是立刻执行的，而 task 4 要等待前面某个 task 完成后才执行，这是因为 Pool 的默认大小在我的电脑上是 4，因此，最多同时执行 4 个进程。这是 Pool 有意设计的限制，并不是操作系统的限制。如果改成：

```txt
p = Pool(5)
```

就可以同时跑5个进程。

由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

# - 子进程

很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

下面的例子演示了如何在Python代码中运行命令nslookupwww.python.org，这和命令行直接运行的效果是一样的：

```python
import subprocess  
print('\\(nslookup www.python.org')  
r = subprocess.call(['nslookup', 'www.python.org'])  
print('Exit code: ', r)
```

运行结果：

```yaml
$ nslookup www.python.org
Server: 192.168.19.4
Address: 192.168.19.4#53
Non-authoritative answer:
www.python.org canonical name = python.map.fastly.net.
Name: python.map.fastly.net
Address: 199.27.79.223
Exit code: 0
```

如果子进程还需要输入，则可以通过communicate()方法输入：

```python
import subprocess  
print('$ nslookup')  
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
output, err = pcommunicate(b'set q=mx\npython.org\nexit\n')  
print(output.decode('utf-8'))  
print('Exit code: ', p.returncode)
```

上面的代码相当于在命令行执行命令nslookup，然后手动输入：

```txt
set q=mx
python.org
exit
运行结果如下:
$ nslookup
```

```txt
Server: 192.168.19.4  
Address: 192.168.19.4#53  
Non-authoritative answer:  
python.org mail exchanger = 50 mail.python.org.  
Authoritative answers can be found from:  
mail.python.org internet address = 82.94.164.166  
mail.python.org has AAAA address 2001:888:2000:d::a6  
Exit code: 0
```

# ·进程间通信

Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的 multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

我们以 Queue 为例，在父进程中创建两个子进程，一个往 Queue 里写数据，一个从 Queue 里读数据：

```python
from multiprocessing import Process, Queue import os, time, random
```

写数据进程执行的代码：

```python
def write(q): print('Process to write:  $\% s$  % os.getpid()) for value in ['A', 'B', 'C']: print('Put %s to queue...' % value) q.put(value) time.sleep(random.random())
```

# 读数据进程执行的代码：

```python
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
```

```python
if __name__ == '__main__':
# 父进程创建 Queue，并传给各个子进程:
q = Queue()
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))
# 启动子进程 pw，写入:
pw.start()
# 启动子进程 pr，读取:
pr.start()
# 等待 pw 结束:
pw.join()
```

```txt
#pr进程里是死循环，无法等待其结束，只能强行终止：prTerminate()运行结果如下：Process to write:50563Put A to queue...Process to read:50564Get A from queue.Put B to queue...Get B from queue.Put C to queue...Get C from queue.
```

在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

# 小结

在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用 multiprocessing 模块。

进程间通信是通过 Queue、Pipes 等实现的。

# 10.2 多线程

多任务可以由多进程完成，也可以由一个进程内的多线程完成。

我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。

由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

启动一个线程就是把一个函数传入并创建 Thread 实例，然后调用 start()开始执行：

```python
import time, threading
# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
            print('thread %s >>> %s' % (threading.current_thread().name, n))
            time.sleep(1)
            print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
```

执行结果如下：

```txt
thread MainThread is running...  
thread LoopThread is running...  
thread LoopThread >>> 1  
thread LoopThread >>> 2  
thread LoopThread >>> 3  
thread LoopThread >>> 4  
thread LoopThread >>> 5  
thread LoopThread ended.  
thread MainThread ended.
```

由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2......

- Lock

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

来看看多个线程同时操作一个变量怎么把内容给改乱了：

```python
import time, threading
# 假定这是你的银行存款:
balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
        global balance
        balance = balance + n
        balance = balance - n
def run_thread(n):
    for i in range(100000):
        change_it(n)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```

我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：

```txt
balance = balance + n
```

也分两步：

1. 计算 balance + n，存入临时变量中；  
2. 将临时变量的值赋给 balance。

也就是可以看成：

```latex
$\mathbf{x} = \mathbf{balance} + \mathbf{n}$  balance  $= x$
```

由于  $\mathbf{x}$  是局部变量，两个线程各自都有自己的  $\mathbf{x}$ ，当代码正常执行时：

```txt
初始值balance  $= 0$
```

```python
t1:  $x1 = \text{balance} + 5 \# x1 = 0 + 5 = 5$   
t1: balance = x1 # balance = 5  
t1:  $x1 = \text{balance} - 5 \# x1 = 5 - 5 = 0$   
t1: balance = x1 # balance = 0  
t2:  $x2 = \text{balance} + 8 \# x2 = 0 + 8 = 8$   
t2: balance = x2 # balance = 8  
t2:  $x2 = \text{balance} - 8 \# x2 = 8 - 8 = 0$   
t2: balance = x2 # balance = 0  
结果 balance = 0
```

但是 t1 和 t2 是交替运行的，如果操作系统以下面的顺序执行 t1、t2：

```txt
初始值 balance = 0  
t1: x1 = balance + 5 # x1 = 0 + 5 = 5  
t2: x2 = balance + 8 # x2 = 0 + 8 = 8  
t2: balance = x2 # balance = 8  
t1: balance = x1 # balance = 5  
t1: x1 = balance - 5 # x1 = 5 - 5 = 0  
t1: balance = x1 # balance = 0  
t2: x2 = balance - 8 # x2 = 0 - 8 = -8  
t2: balance = x2 # balance = -8  
结果 balance = -8
```

究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。

两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。

如果我们要确保 balance 计算正确，就要给 change_it()上一把锁，当某个线程开始执行 change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行 change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由

于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过 threading.Lock()来实现：

```python
balance  $= 0$    
lock  $=$  threading.Lock()   
def run_thread(n): for i in range(100000): # 先要获取锁： lock.acquire() try: # 放心地改吧： change_it(n) finally: #改完了一定要释放锁： lock.release()
```

当多个线程同时执行 lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

# ·多核CPU

如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。

如果写一个死循环的话，会出现什么情况呢？

打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。

我们可以监控到一个死循环线程会  $100\%$  占用一个CPU。

如果有两个死循环线程，在多核CPU中，可以监控到会占用  $200\%$  的CPU，也就是占用两个CPU核心。

要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。

试试用Python写个死循环：

```python
import threading, multiprocessing   
def loop():  $\texttt{x} = 0$  while True:  $\texttt{x} = \texttt{x}\wedge 1$    
for i in range(multiprocessing.cpu_count(): t  $=$  threading.Thread(target  $\coloneqq$  loop) t.start()
```

启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有  $102\%$  ，也就是仅使用了一核。

但是用 C、C++ 或 Java 来改写相同的死循环，直接可以把全部核心跑满，4 核就跑到  $400\%$ ，8 核就跑到  $800\%$ ，为什么 Python 不行呢？

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock,任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指期能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

# ·小结

多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

Python 解释器由于设计时有 GIL 全局锁，导致了多线程无法利用多核。多线程的并发在 Python 中就是一个美丽的梦。

# 10.3 ThreadLocal

在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。

但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：

```python
def processstudent(name):
    std = Student(name)
    # std 是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)
def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)
def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
```

每个函数一层一层调用都这么传参数那还得了？用全局变量？也不行，因为每个线程处理不同的Student对象，不能共享。

如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？

```python
global_dict = {}
def std_thread(name):
    std = Student(name)
    # 把 std 放到全局变量 global_dict 中:
    global_dict[threading.current_thread() ] = std
        do_task_1()
        do_task_2()
    def do_task_1():
```

```javascript
#不传入std，而是根据当前线程查找：std  $=$  global_dict[threading.current_thread()]defdo_task2():#任何函数都可以查找出当前线程的std变量：std  $=$  global_dict[threading.current_thread()]
```

这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。

有没有更简单的方式？

ThreadLocal 应运而生，不用查找 dict，ThreadLocal 帮你自动做这件事：

```python
import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()
def processstudent():
    # 获取当前线程关联的student:
        std = local_school/student
        print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
    # 绑定ThreadLocal的student:
        local_school/student = name
        process/student()
t1 = threading.Thread(target=process_thread, args='Alice', name='Thread-A')
t2 = threading.Thread(target=process_thread, args='Bob', name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
```

执行结果：

```txt
Hello, Alice (in Thread-A)  
Hello, Bob (in Thread-B)
```

全局变量 local_school 就是一个 ThreadLocal 对象，每个 Thread 对它都可以读写 student 属性，但互不影响。你可以把 local_school 看成全局变量，但每个属性如 local_school/student 都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal 内部会处理。

可以理解为全局变量 local_school 是一个 dict，不但可以用 local_school/student，还可以绑定其他变量，如 local_school_teacher 等等。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

# 小结

一个 ThreadLocal 变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal 解决了参数在一个线程中各个函数之间互相传递的问题。

# 10.4 进程 vs 线程

我们介绍了多进程和多线程，这是实现多任务最常用的两种方式。现在，我们来讨论一下这两种方式的优缺点。

首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。

如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。

如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。

多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。

多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。

在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂。

# ·线程切换

无论是多进程还是多线程，只要数量一多，效率肯定上不去，为什么呢？

我们打个比方，假设你不幸正在准备中考，每天晚上需要做语文、数学、英语、物理、化学这5科的作业，每项作业耗时1小时。

如果你先花1小时做语文作业，做完了，再花1小时做数学作业，这样，依次全部做完，一共花5小时，这种方式称为单任务模型，或者批处理任务模型。

假设你打算切换到多任务模型，可以先做1分钟语文，再切换到数学作业，做1分钟，再切换到英语，以此类推，只要切换速度足够快，这种方式就和单核CPU执行多任务是一样的了，以幼儿园小朋友的眼光来看，你就正在同时写5科作业。

但是，切换作业是有代价的，比如从语文切到数学，要先收拾桌子上的语文书本、钢笔（这叫保存现场），然后，打开数学课本、找出圆规直尺（这叫准备新环境），才能开始做数学作业。操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。

所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。

# - 计算密集型 vs. IO 密集型

是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。

计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。

计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，

CPU 效率越高，但也有一个限度。常见的大部分任务都是 IO 密集型任务，比如 Web 应用。

IO 密集型任务执行期间，99%的时间都花在 IO 上，花在 CPU 上的时间很少，因此，用运行速度极快的 C 语言替换用 Python 这样运行速度极低的脚本语言，完全无法提升运行效率。对于 IO 密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C 语言最差。

# ·异步IO

考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。

对应到Python语言，单进程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。我们会在后面讨论如何编写协程。

# 10.5 分布式进程

在 Thread 和 Process 中，应当优选 Process，因为 Process 更稳定，而且，Process 可以分布到多台机器上，而 Thread 最多只能分布到同一台机器的多个 CPU 上。

Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

举个例子：如果我们已经有一个通过 Queue 通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

原有的 Queue 可以继续使用，但是，通过 managers 模块把 Queue 通过网络暴露出去，就可以让其他机器的进程访问 Queue 了。

我们先看服务进程，服务进程负责启动 Queue，把 Queue 注册到网络上，然后往 Queue 里面写入任务：

```python
task/master.py   
import random, time, queue   
from multiprocessing.managers import BaseManager   
#发送任务的队列：   
task_queue  $=$  queueQueue()   
#接收结果的队列：   
result_queue  $\equiv$  queueQueue()   
#从BaseManager继承的QueueManager:   
class QueueManager(BaseManager): pass   
#把两个Queue都注册到网络上，callable参数关联了Queue对象： QueueManager.register('get_task_queue'，callable  $\equiv$  lambda：task_queue) QueueManager.register('get_result_queue'，callable  $\equiv$  lambda：result_queue) #绑定端口5000，设置验证码'abc': manager  $=$  QueueManager(address  $\equiv$  (''，5000)，authkey  $\equiv$  b'abc')
```

```python
# 启动Queue:  
manager.start()  
# 获得通过网络访问的Queue对象：  
task = manager.get_task_queue()  
result = manager.get_result_queue()  
# 放几个任务进去：  
for i in range(10):  
    n = random.randint(0, 10000)  
    print('Put task %d...' % n)  
    task.put(n)  
# 从result队列读取结果：  
print('Try get results...')  
for i in range(10):  
    r = result.get(timeout=10)  
    print('Result: %s' % r)  
# 关闭：  
manager.shutdown()  
print('master exit.')
```

请注意，当我们在一台机器上写多进程程序时，创建的 Queue 可以直接拿来用，但是，在分布式多进程环境下，添加任务到 Queue 不可以直接对原始的 task_queue 进行操作，那样就绕过了 QueueManager 的封装，必须通过 manager.get_task_queue()获得的 Queue 接口添加。

然后，在另一台机器上启动任务进程（本机上启动也可以）：

```python
taskWorker.py   
import time,sys,queue   
from multiprocessing.managers importBaseManager   
#创建类似的QueueManager: class QueueManager(BaseManager): pass   
#由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字： QueueManager.register('get_task_queue') QueueManager.register('get_result_queue')   
#连接到服务器，也就是运行task/master.py的机器： server_addr  $= 127.0.0.1$  print('Connect to server %s...'  $\%$  server_addr) #端口和验证码注意保持与task/master.py设置的完全一致： m  $=$  QueueManager(address=(server_addr，5000)，authkey  $\equiv$  b'abc') #从网络连接：   
m.connect() #获取Queue的对象：   
task  $=$  m.get_task_queue() result  $=$  m.get_result_queue()
```

从task队列取任务，并把结果写入result队列：

```python
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue_empty:
        print('task queue is empty.')
```

任务进程要通过网络连接到服务进程，所以要指定服务进程的 IP。

现在，可以试试分布式进程的工作效果了。先启动 task/master.py 服务进程：

```txt
$ python3 task/master.py
Put task 3411...
Put task 1605...
Put task 1398...
Put task 4729...
Put task 5300...
Put task 7471...
Put task 68...
Put task 4219...
Put task 339...
Put task 7866...
Try get results...
task/master.py 进程发送完任务后,开始等待 result 队列的结果。现在启动 task-worker.py 进程:
$ python3 task-worker.py
Connect to server 127.0.0.1...
run task 3411 * 3411...
run task 1605 * 1605...
run task 1398 * 1398...
run task 4729 * 4729...
run task 5300 * 5300...
run task 7471 * 7471...
run task 68 * 68...
run task 4219 * 4219...
run task 339 * 339...
run task 7866 * 7866...
worker exit.
taskWorker.py 进程结束,在 taskMASTER.py 进程中会继续打印出结果:
Result: 3411 * 3411 = 11634921
Result: 1605 * 1605 = 2576025
Result: 1398 * 1398 = 1954404
Result: 4729 * 4729 = 22363441
```

Result: 5300 * 5300 = 28090000

Result: 7471 * 7471 = 55815841

Result: 68 * 68 = 4624

Result: 4219 * 4219 = 17799961

Result: 339 * 339 = 114921

Result: 7866 * 7866 = 61873956

这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，比如把计算  $n * n$  的代码换成发送邮件，就实现了邮件队列的异步发送。

Queue 对象存储在哪？注意到 task-worker.py 中根本没有创建 Queue 的代码，所以，Queue 对象存储在 task/master.py 进程中：

![](images/d2673283e436a427ece855e474c50a51ee4ceb64ad0be66f77a046aed4ffa2eb.jpg)  
网络

而 Queue 之所以能通过网络访问，就是通过 QueueManager 实现的。由于 QueueManager 管理的不止一个 Queue，所以，要给每个 Queue 的网络调用接口起个名字，比如 get_task_queue。

authkey 有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果 task-worker.py 的 authkey 和 task/master.py 的 authkey 不一致，肯定连接不上。

# 小结

Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

注意 Queue 的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由 Worker 进程再去共享的磁盘上读取文件。

# 11 正则表达式

字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。比如判断一个字符串是否是合法的Email地址，虽然可以编程提取@前后的子串，再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用。

正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

所以我们判断一个字符串是否是合法的Email的方法是：

1. 创建一个匹配Email的正则表达式；  
2. 用该正则表达式去匹配用户的输入来判断是否合法。

因为正则表达式也是用字符串表示的，所以，我们要首先了解如何用字符来描述字符。

在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：

- '00\d'可以匹配'007', 但无法匹配'00A';  
\`d\d'd'可以匹配'010';  
$\cdot$ $\backprime \backslash w\backslash w\backslash d'$  可以匹配'py3';

.可以匹配任意字符，所以：

- 'py.'可以匹配'pyc'、'pyo'、'py!'等等。

要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：

来看一个复杂的例子：\d{3}\s+ \d{3,8}。

我们来从左到右解读一下：

1.  $\backslash d\{3\}$  表示匹配3个数字，例如'010'；  
2. \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' ', ' '等；  
3.  $\backslash d\{3,8\}$  表示 3-8 个数字，例如 '1234567'。

综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。

如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。

但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。

# ·进阶

要做更精确地匹配，可以用[]表示范围，比如：

- [θ-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；  
- [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100', '0_Z', 'Py3000'等等；  
- [a-zA-Z\_] [0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python 合法的变量；  
- [a-zA-Z\_] [0-9a-zA-Z\_] {0, 19} 更精确地限制了变量的长度是 1-20 个字符（前面 1 个字符+后面最多 19 个字符）。

A|B可以匹配A或B，所以(P|p)thon可以匹配'Python'或者'python'。

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束, \d$表示必须以数字结束。

你可能注意到了，py 也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。

# ·re模块

有了准备知识，我们就可以在Python中使用正则表达式了。Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：

s = 'ABC\-\001' # Python 的字符串

对应的正则表达式字符串变成：

```txt
'ABC\-.001'
```

因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：

```python
s = r'ABC\-001' # Python 的字符串
# 对应的正则表达式字符串不变:
# 'ABC\-001'
```

先看看如何判断正则表达式是否匹配：

```txt
>>> import re
>>> re.match(r'^\d{3}\- \d{3,8} $', '010-12345')
<_sre.SRE_MATCH object; span=(0, 9), match='010-12345'>
>>> re.match(r'^\d{3}\- \d{3,8} $', '010 12345')
>>>
```

match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：

```txt
test = '用户输入的字符串'
```

```python
if re.match(r'正则表达式', test): print('ok')   
else: print('failed')
```

# ·切分字符串

用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：

```txt
>>> 'a b c'.split('') ['a', 'b', '','', 'c']
```

嗯，无法识别连续的空格，用正则表达式试试：

```txt
>>> re.split(r'\s+\', 'a b c')  
['a', 'b', 'c']
```

无论多少个空格都可以正常分割。加入，试试：

```txt
>>> re.split(r'[\\s,]+', 'a,b, c d') ['a', 'b', 'c', 'd']
```

再加入；试试：

```txt
>>> re.split(r'[\\s,\;]'+', 'a,b;; c d') ['a', 'b', 'c', 'd']
```

如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组。

# ·分组

除了简单地判断是否匹配之外,正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组(Group)。比如:^(\\d{3})-(\\d{3,8})$分别定义了两个组,可以直接从匹配的字符串中提取出区号和本地号码:

```txt
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object; span=(0, 9), match='010-12345']
>>> m.group(0)
'010-12345'
```

```txt
>>> m.group(1) '010'   
>>> m.group(2) 12345
```

如果正则表达式中定义了组，就可以在 Match 对象上用 group() 方法提取出子串来。

注意到 group(0)永远是原始字符串，group(1)、group(2)……表示第 1、2、……个子串。

提取子串非常有用。来看一个更凶残的例子：

```python
>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9][0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m_groups()
('19', '05', '30')
```

这个正则表达式可以直接识别合法的时间。但是有些时候，用正则表达式也无法做到完全验证，比如识别日期：

```txt
^{\prime\prime}(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$
```

对于'2-30'，'4-31'这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。

# ·贪婪匹配

最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：

```python
>>> re.match(r'^(\d+) (0*)$', '102300').groups()
('102300', '')
```

由于 $\backslash d+$ 采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。

必须让 $\mathsf{d}+$ 采用非贪婪匹配（也就是尽可能少匹配），才能把后面的  $\theta$  匹配出来，加个?就可以让 $\mathsf{d}+$ 采用非贪婪匹配：

```python
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')
```

编译

当我们在Python中使用正则表达式时，re模块内部会干两件事情：

1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；  
2. 用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

```python
>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用:
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
```

编译后生成 Regular Expression 对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。

# 小结

正则表达式非常强大，要在短短的一节里讲完是不可能的。要讲清楚正则的所有内容，可以写一本厚厚的书了。如果你经常遇到正则表达式的问题，你可能需要一本正则表达式的参考书。

# 12 常用内建模块

Python之所以自称“batteriesincluded”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用。

本章将介绍一些常用的内建模块。

# 12.1 datetime

datetime 是 Python 处理日期和时间的标准库。

# - 获取当前日期和时间

我们先看如何获取当前日期和时间：

```txt
>>> from datetime import datetime
>>> now = datetime现已() # 获取当前 datetime
>>> print(now)
2015-05-18 16:28:07.198690
>>> print(type(now))
<class 'datetimedatetime'>
```

注意到 datetime 是模块，datetime 模块还包含一个 datetime 类，通过 from datetime import datetime 导入的才是 datetime 这个类。

如果仅导入 import datetime，则必须引用全名 datetimedatetime。

datetime-now()返回当前日期和时间，其类型是 datetime。

# - 获取指定日期和时间

要指定某个日期和时间，我们直接用参数构造一个 datetime:

```txt
>>> from datetime import datetime
>>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建 datetime
>>> print(dt)
2015-04-19 12:20:00
```

# - datetime转换为timestamp

在计算机中，时间实际上是用数字表示的。我们把1970年1月1日00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

你可以认为：

```txt
timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
```

对应的北京时间是：

```txt
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
```

可见 timestamp 的值与时区毫无关系，因为 timestamp 一旦确定，其 UTC 时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以 timestamp 表示的，因为全球各地的计算机在任意时刻的 timestamp 都是完全相同的（假定时间已校准）。

把一个 datetime 类型转换为 timestamp 只需要简单调用 timestamp() 方法:

# - timestamp 转换为 datetime

要把 timestamp 转换为 datetime，使用 datetime 提供的 fromtimestamp()方法：

```python
>>> from datetime import datetime  
>>> t = 1429417200.0  
>>> print万人次-fromtimestamp(t))
```

```txt
2015-04-19 12:20:00
```

注意到 timestamp 是一个浮点数，它没有时区的概念，而 datetime 是有时区的。上述转换是在 timestamp 和本地时间做转换。

本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：

```txt
2015-04-19 12:20:00  
实际上就是 UTC+8:00 时区的时间：  
2015-04-19 12:20:00 UTC+8:00  
而此刻的格林威治标准时间与北京时间差了 8 小时，也就是 UTC+0:00 时区的时间应该是：  
2015-04-19 04:20:00 UTC+0:00
```

timestamp 也可以直接被转换到 UTC 标准时区的时间：

```txt
>>> from datetime import datetime
>>> t = 1429417200.0
>>> print(dtime.fromtimestamp(t)) # 本地时间
2015-04-19 12:20:00
>>> print(dtime UTCfromtimestamp(t)) # UTC时间
2015-04-19 04:20:00
```

# - str转换为 datetime

很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把 str 转换为 datetime。转换方法是通过 datetimedatetime() 实现，需要一个日期和时间的格式化字符串：

```python
>>> from datetime import datetime
>>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
>>> print(cday)
2015-06-01 18:19:59
```

字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。详细的说明请参考Python文档。

注意转换后的 datetime 是没有时区信息的。

# - datetime转换为str

如果已经有了 datetime 对象，要把它格式化为字符串显示给用户，就需要转换为 str，转换方法是通过 strftime()实现的，同样需要一个日期和时间的格式化字符串：

```txt
>>> from datetime import datetime
>>> now = datetime-now()
>>> print(now strftime("%a, %b %d %H:%M"))  
Mon, May 05 16:28
```

# ·datetime加减

对日期和时间进行加减实际上就是把 datetime 往后或往前计算，得到新的 datetime。加减可以直接用+和-运算符，不过需要导入 timedelta 这个类：

```python
>>> from datetime import datetime, timedelta
>>> now = datetime-now()
>>> now
datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
>>> now + timedelta(hours=10)
datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
>>> now - timedelta(days=1)
datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
```

```txt
>>> now + timedelta(days=2, hours=12)  
datetimedatetime(2015, 5, 21, 4, 57, 3, 540997)
```

可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。

# - 本地时间转换为 UTC 时间

本地时间是指系统设定时区的时间，例如北京时间是 UTC+8:00 时区的时间，而 UTC 时间指 UTC+0:00 时区的时间。

一个 datetime 类型有一个时区属性 tzinfo，但是默认为 None，所以无法区分这个 datetime 到底是哪个时区，除非强行给 datetime 设置一个时区：

```python
>>> from datetime import datetime, timedelta, tzzone
>>> tz_UTC_8 = timezone(timedelta(hours=8)) # 创建时区 UTC+8:00
>>> now = datetime-now()
>>> now
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012)
>>> dt = now.replace(tzinfo=tz_UTC_8) # 强制设置为 UTC+8:00
>>> dt
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=datetime时间和zone景德镇(0, 28800)))
>>>
```

如果系统时区恰好是  $\mathrm{UTC} + 8:00$  ，那么上述代码就是正确的，否则，不能强制设置为  $\mathrm{UTC} + 8:00$  时区。

# ·时区转换

我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：

```txt
拿到UTC时间，并强制设置时区为UTC+0:00：  
>>> utan_dt = datetime.utcnow().replace(tzinfo=timezone.utan)  
>>> print(utan_dt)  
2015-05-18 09:05:12.377316+00:00  
# astimezone()将转换时区为北京时间：  
>>> bj_dt = utan_dt.astimezone(timezone(timedelta(hours=8)))  
>>> print(bj_dt)  
2015-05-18 17:05:12.377316+08:00  
# astimezone()将转换时区为东京时间：  
>>> tokyo_dt = utan_dt.astimezone(timezone(timedelta(hours=9)))  
>>> print(tokyo_dt)  
2015-05-18 18:05:12.377316+09:00  
# astimezone()将bj_dt转换时区为东京时间：  
>>> tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))  
>>> print(tokyo_dt2)  
2015-05-18 18:05:12.377316+09:00
```

时区转换的关键在于，拿到一个 datetime 时，要获知其正确的时区，然后强制设置时区，作为基准时间。

利用带时区的 datetime，通过 astimezone()方法，可以转换到任意时区。

注：不是必须从 UTC+0:00 时区转换到其他时区，任何带时区的 datetime 都可以正确转换，例如上述 bj_dt 到 TOKyo_dt 的转换。

# 小结

datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储 datetime，最佳方法是将其转换为 timestamp 再存储，因为 timestamp 的值与时区完全无关。

# ·练习

假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

```python
# --coding:utf-8 --  
import re  
from datetime import datetime, timezone, timedefla  
def to_timestamp(dt_str, tz_str):  
    pass  
# 测试：  
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')  
assert t1 == 1433121030.0, t1  
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')  
assert t2 == 1433121030.0, t2  
print('Pass')
```

# 12.2 collections

collections 是 Python 内建的一个集合模块，提供了许多有用的集合类。

- namedtuple

我们知道 tuple 可以表示不变集合，例如，一个点的二维坐标就可以表示成：

```txt
>>> p = (1, 2)
```

但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。

定义一个 class 又小题大做了，这时，namedtuple 就派上了用场：

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])  
>>> p = Point(1, 2)  
>>> p.x
1  
>>> p.y
2
```

namedtuple 是一个函数，它用来创建一个自定义的 tuple 对象，并且规定了 tuple 元素的个数，并可以用属性而不是索引来引用 tuple 的某个元素。

这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

可以验证创建的 Point 对象是 tuple 的一种子类:

```txt
>>>isinstance(p,Point)   
True   
>>>isinstance(p,tuple)   
True
```

类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：

```python
namedtuple('名称', [属性List]):  
Circle = namedtuple('Circle', ['x', 'y', 'r'])
```

# deque

使用 list 存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为 list 是线性存储，数据量大的时候，插入和删除效率很低。

deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

```python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])  
>>> q.append('x')  
>>> q.appendleft('y')  
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```

deque 除了实现 list 的 append()和 pop()外，还支持 appendleft()和 popleft()，这样就可以非常高效地往头部添加或删除元素。

# - defaultdict

使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict:

```python
>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1 存在
'abc'
>>> dd['key2'] # key2 不存在，返回默认值
'N/A'
```

注意默认值是调用函数返回的，而函数在创建 defaultdict 对象时传入。

除了在 Key 不存在时返回默认值，defaultdict 的其他行为跟 dict 是完全一样的。

# - OrderedDict

使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

如果要保持 Key 的顺序，可以用 OrderedDict:

```python
>>> from collections import OrderedDict
>>> d = dict(['a', 1], ('b', 2), ('c', 3)]
>>> d # dict 的 Key 是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict(['a', 1], ('b', 2), ('c', 3])
>>> od # OrderedDict 的 Key 是有序的
OrderedDict(['a', 1], ('b', 2), ('c', 3)])
```

注意，OrderedDict 的 Key 会按照插入的顺序排列，不是 Key 本身排序：

```txt
>>> od = OrderedDict()
>>> od['z'] = 1
>>> od['y'] = 2
>>> od['x'] = 3
>>> list(od.keys()) # 按照插入的Key的顺序返回 ['z', 'y', 'x']
```

OrderedDict 可以实现一个 FIFO（先进先出）的 dict，当容量超出限制时，先删除最早添加的 Key:

class LastUpdatedOrderedDict(OrderedDict):  
```python
from collections import OrderedDict
```

```python
def __init__(self, capacity):
    super(LastUpdatedOrderedDict, self).__init__()
    self._capacity = capacity
def __setitem__(self, key, value):
    containsKey = 1 if key in self else 0
    if len(self) - containsKey >= self._capacity:
        last = self.popitem(last=False)
        print('remove: ', last)
    if containsKey:
        del self[key]
        print('set: ', (key, value))
    else:
        print('add: ', (key, value))
    OrderedDict.__setitem__(self, key, value)
```

# Counter

Counter 是一个简单的计数器，例如，统计字符出现的个数：

```python
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
```

Counter 实际上也是 dict 的一个子类，上面的结果可以看出，字符 'g'、'm'、'r' 各出现了两次，其他字符各出现了一次。

# ·小结

collections 模块提供了一些有用的集合类，可以根据需要选用。

# 12.3 base64

Base64是一种用64个字符来表示任意二进制数据的方法。

用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。

Base64 的原理很简单，首先，准备一个包含 64 个字符的数组：

['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']

然后，对二进制数据进行处理，每3个字节一组，一共是  $3 \times 8 = 24$  bit，划为4组，每组正好6个bit：

![](images/8affd88e5516dfa219d8717793ff8a81f2d25177cb7a08fee8a27eb028cdf494.jpg)

这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。

所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加  $33\%$  ，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

Python内置的base64可以直接进行base64的编解码：

```python
>>> import base64
>>> base64.b64encode(b'binary\x00string')
b'YmluYXJ5AHN0cmluZw==''
>>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
b'binary\x00string'
```

由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和：

```python
>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd++//'
>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd--'
>>> base64.urlsafe_b64decode('abcd--')
b'i\xb7\x1d\xfb\xef\xff'
```

还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要。

Base64 是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

Base64 适用于小段内容的编码，比如数字证书签名、Cookie 的内容等。

由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：

```txt
标准Base64: 'abcd' -> 'YWJjZA=': #自动去掉： 'abcd' -> 'YWJjZA'
```

去掉  $=$  后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上  $=$  把Base64字符串的长度变为4的倍数，就可以正常解码了。

# ·小结

Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

# ·练习

请写一个能处理去掉=的base64解码函数：

```python
# -- coding: utf-8 --  
import base64  
def safe_base64 Decode(s):  
    pass  
# 测试：  
assert b'abcd' == safe_base64 Decode(b'YWJjZA=='), safe_base64 Decode('YWJjZA=='')  
assert b'abcd' == safe_base64 Decode(b'YWJjZA'), safe_base64 Decode('YWJjZA')  
print('Pass')
```

# 12.4 struct

准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组  $=$  二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。

在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：

```txt
>>> n = 10240099  
>>> b1 = (n & 0xff00000) >> 24  
>>> b2 = (n & 0xff0000) >> 16  
>>> b3 = (n & 0xff00) >> 8  
>>> b4 = n & 0xff  
>>> bs = bytes([b1, b2, b3, b4])  
>>> bs  
b'\x00\x9c@c'
```

非常麻烦。如果换成浮点数就无能为力了。

好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

struct 的 pack 函数把任意数据类型变成 bytes:

```python
>>> import struct
>>> struct.pack('>I', 10240099)
b'\x00\x9c@c'
```

pack的第一个参数是处理指令，'  $\rightharpoondown$  I'的意思是：

>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

后面的参数个数要和处理指令一致。

unpack把bytes变成相应的数据类型：

```txt
>>> struct unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
(4042322160, 32896)
```

根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。

struct模块定义的数据类型可以参考Python官方文档：

https://docs.python.org/3/library/struct.html#format-characters

Windows 的位图文件 (.bmp) 是一种非常简单的文件格式，我们来用 struct 分析一下。

首先找一个bmp文件，没有的话用“画图”画一个。

读入前30个字节来分析：

```html
>>>s = b '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x36\x00\x00\x00\x00\x00\x02\x00\x00'  
0\x68\x01\x00\x00\x01\x00\x18\x00'
```

BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；一个4字节整数：表示位图大小；一个4字节整数：保留位，始终为0；一个4字节整数：实际图像的偏移量；一个4字节整数：Header的字节数；一个4字节整数：图像宽度；一个4字节整数：图像高度；一个2字节整数：始终为1；一个2字节整数：颜色数。

所以，组合起来用 unpack 读取：

```txt
>>> struct unpack('<ccAAAAAAAAHH', s)
(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
```

结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。

请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。

# 12.5 hashlib

摘要算法简介

Python 的 hashlib 提供了常见的摘要算法，如 MD5，SHA1 等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，你可以一下子指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：

```txt
import hashlib  
md5 = hashlib.md5()  
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))  
print(md5(hexdigest()))  
计算结果如下：  
d26a53750bc40b38b65a520292f69306
```

如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：

```python
import hashlib md5  $=$  hashlib.md5() md5.update('how to use md5 in'.encode('utf-8')) md5.update('python hashlib?'.encode('utf-8')) print(md5(hexdigest()))
```

试试改动一个字母，看看计算的结果是否完全不同。

MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit字节，通常用一个32位的16进制字符串表示。

另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：

```python
import hashlib  
sha1 = hashlibsha1()  
sha1.update('how to use sha1 in '.encode('utf-8'))  
sha1.update('python hashlib?'.encode('utf-8'))  
print(sha1(hexdigest()))
```

SHA1的结果是160bit字节，通常用一个40位的16进制字符串表示。

比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。

有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞，比如 Bob 试图根据你的摘要反推出一篇文章 'how to learn hashlib in python - by Bob'，并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。

# - 摘要算法应用

摘要算法能应用到什么地方？举个常用例子：

任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：

```txt
name | password  
--  
michael | 123456  
bob | abc999  
alice | alice2008
```

如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。

正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：

```txt
username | password  
--  
michael | e10adc3949ba59abbe56e057f20f883e  
bob | 878ef96e86145580c38c87f0410ad153  
alice | 99b1c2188db85afee403b1536010c2c9
```

当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。

# ·练习

根据用户输入的口令，计算出存储在数据库中的MD5口令：

```python
def calc_md5(key): pass
```

存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。

设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回 True 或 False:

```txt
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
```

采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过MD5反推用户的明文口令呢？暴力破解费事费力，真正的黑客不会这么干。

考虑这么个情况，很多用户喜欢用123456，888888，password这些简单的口令，于是，黑客可以事先计算出这些常用口令的MD5值，得到一个反推表：

```python
'e10adc3949ba59abbe56e057f20f883e': '123456'  
'21218cca77804d2ba1922c33e0151105': '888888'  
'5f4dcc3b5aa765d61d8327deb882cf99': 'password'
```

这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。

对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？

由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

```python
def calc_md5(keyword):
    return get_md5(keyword + 'the-Salt')
```

经过 Salt 处理的 MD5 口令，只要 Salt 不被黑客知道，即使用户输入简单口令，也很难通过 MD5 反推明文口令。

但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？

如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

·练习

根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

```python
db = {}
def register username, password):
    db[outname] = get_md5护照 + username + 'the-Salt')
```

然后，根据修改后的MD5算法实现用户登录的验证：

```txt
def login username, password): pass
```

小结

摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。

# 12.6 itertools

Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

首先，我们看看itertools提供的几个“无限”迭代器：

```txt
>>> import itertools
>>> notuals = itertools.count(1)
>>> for n in notuals:
...     print(n)
...
1
2
3
...
```

因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

cycle()会把传入的一个序列无限重复下去：

```python
>>> import itertools
>>> cs = itertools-cycle('ABC')  # 注意字符串也是序列的一种
>>> for c in cs:
...     print(c)
...
'A'
'B'
'C'
'A'
'B'
'C'
```

同样停不下来。

repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

```txt
>>> ns = itertoolsrepeat('A',3)   
>>> for n in ns:   
... print(n)   
A   
A
```

无限序列只有在 for 迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：

```txt
>>> natuals = itertools.count(1)  
>>> ns = itertools.takewhile(lambda x: x <= 10, natuals)  
>>> list(ns)  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

itertools提供的几个迭代器操作函数更加有用：

chain()

chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

```txt
>>>for c in itertools.chain('ABC'，'XYZ'): print(c) #迭代效果：A'B'C'X'Y'Z'
```

groupby()

groupby()把迭代器中相邻的重复元素挑出来放在一起：

```python
>>> for key, group in itertools.groupby('AAABBCCAAA'):  
... print(key, list(group))  
...
```

A ['A', 'A', 'A']

B ['B', 'B', 'B']

C['C'，'C']

A ['A', 'A', 'A']

实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的 key。如果我们要忽略大小写分组，就可以让元素 'A' 和 'a' 都返回相同的 key:

```python
>>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper():
...
...
print(key, list(group))
...
```

A ['A', 'a', 'a']

B ['B', 'B', 'b']

C['c'，‘C']

A ['A', 'A', 'a']

# 小结

itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。

# 12.7 XML

XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。

DOM vs SAX

操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

正常情况下，优先考虑SAX，因为DOM实在太占内存。

在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

举个例子，当SAX解析器读到一个节点时：

```twig
<a href="/\">python</a>
```

会产生3个事件：

1. start_element事件，在读取<a href="/"/>时；  
2. char_data 事件，在读取 python 时；  
3. end_element事件，在读取</a>时。

用代码实验一下：

```python
from xml:parsers.expat import ParserCreate   
class DefaultSaxHandler(object): def start_element(self, name, attributes): print('sax:start_element: %s, attributes:  $\% s^{\prime}$  %(name,str(attributes))) def end_element(self, name): print('sax:end_element:%s' % name) def char_data(self,text): print('sax:char_data:%s' % text) xml  $=$  r'<?xml version="1.0"?> <ol> <li><a href="/python">Python</a></li> <li><a href="/ruby">Ruby</a></li> </ol> handler  $=$  DefaultSaxHandler() parser  $=$  ParserCreate() parser.StartElementHandler  $=$  handler.start_element parser.EndElementHandler  $=$  handler.end_element parser.CharacterDataHandler  $=$  handler.char_data parser.Parse(xm1)
```

需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。

除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：

```txt
L = []
```

```groovy
L.append(r'<?xml version="1.0"?>')  
L.append(r'<root>'')  
L.append encode('some & data'))  
L.append(r'</root>'')  
return '.join(L)
```

如果要生成复杂的XML呢？建议你不要用XML，改成JSON。

小结

解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。

练习

请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取当天和第二天的天气：

```txt
http://weather.yahooapis.com/forecastrss?u=c&w=2151330
```

参数  $w$  是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。

```python
\*- coding:utf-8 \*-   
from xml:parsers.expat import ParserCreate   
class WeatherSaxHandler(object): pass   
def parse/weatherxml): return { 'city': 'Beijing', 'country': 'China', 'today': { 'text': 'Partly Cloudy', 'low': 20, 'high': 33 }, 'tomorrow': { 'text': 'Sunny', 'low': 21, 'high': 34 }
```

# 测试：

```xml
data = r'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>  
<rss version="2.0" xmlns: yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns: geo="http://www.w3.org/2003/01/geo/wgs84_pos#"  
<channel>  
    <title>Yahoo! Weather - Beijing, CN</title>  
    <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>  
    <yweather:location city="Beijing" region="" country="China"/>  
    <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
```

```txt
<weather:wind chill="28" direction="180" speed="14.48" /> <weather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" /> <weather:astronomy sunrise="4:51 am" sunset="7:32 pm"/> <item> <geo:lat>39.91</geo:lat> <geo:long>116.39</geo:long> <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate> <weather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" /> <weather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" /> <weather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" /> <weather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" /> <weather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" /> <weather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" /> </item> </channel> </rss>   
```
weather = parse/weather(data)
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == 20, weather['today']['low']
assert weather['today']['high'] == 33, weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
print('Weather:', str(weather))
```

# 12.8 HTMLParser

如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。

假设第一步已经完成了，第二步应该如何解析 HTML 呢？

HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。

好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：

```python
from html投入到HTMLParser from htmlentitiesimport name2codepoint classMyHTMLParser(HTMLParser):
```

```python
def handle_starttag(self, tag, attrs): print('<%s>' % tag) def handle_endtag(self, tag): print('</%s>' % tag) def handle_startendtag(self, tag, attrs): print('<%s/>' % tag) def handle_data(self, data): print(data) def handle/comment(self, data): print('<!--', data, "-->") def handle_entityref(self, name): print '&%s;%name) def handle_charref(self, name): print '&%s;%name) parser = MyHTMLParser() parser/feed([''<html> <head></head> <body> <!-- test html parser --> <p>Some <a href=\ "#\">html</a> HTML&nbsp;tutorial...<br>END</p> </body></html>'')
```

feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

结

利用HTMLParser，可以把网页中的文本、图像等解析出来。

·练习

找一个网页，例如 https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下 HTML，输出 Python 官网发布的会议时间、名称和地点。

12.9 urllib

urllib提供了一系列用于操作URL的功能。

Get

urllib 的 request 模块可以非常方便地抓取 URL 内容，也就是发送一个 GET 请求到指定的页面，然后返回 HTTP 的响应：

例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：

from urllib import request

```python
with request.urlopen('https://api.douban.com/v2/book/2129650') as f: data = f.read() print('Status: ', f.status, freason) for k, v in f.getheaders(): print('%s:%s' % (k, v)) print('Data: ', datadecode('utf-8'))
```

可以看到 HTTP 响应的头和 JSON 数据：

```txt
Status: 200 OK  
Server:nginx  
Date: Tue, 26 May 2015 10:02:27 GMT  
Content-Type: application/json; charset=utf-8  
Content-Length: 2049  
Connection: close  
Expires: Sun, 1 Jan 2006 01:00:00 GMT  
Pragma: no-cache  
Cache-Control: must-revalidate, no-cache, private  
X-DAE-Node: pid11  
Data: {"rating":"max":10,"numRaters":16,"average":"7.4","min":0}, "subtitle":"","author":[ "廖雪峰编著"], "pubdate":"2007-6", "tags":[ {"count":20,"name":"spring","title":"spring"}...}
```

如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone6去请求豆瓣首页：

```python
from urllib import request   
req  $=$  request.Request('http://www.douban.com/)   
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone;CPU iPhone OS 8_0 like Mac OS X)   
AppleWebKit/536.26 (KHTML,like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')   
with request(urlopen(req) as f: print('Status:  $\cdot _ { \text{一} }$  ,f.status,freason) fork,v in f.getheaders(): print(%s:%s'  $\%$  (k,v)) print('Data:  $\cdot_{\cdot}$  ,f.read().decode('utf-8'))   
#这样豆瓣会返回适合iPhone的移动版网页：   
... <meta name  $=$  "viewport"content  $=$  "width  $\equiv$  device-width，user-scalable=no，initial-scale  $= 1.0$  minimum-scale  $= 1.0$  ，maximum-scale  $= 1.0"$  > <meta name  $=$  "format-detection" content  $=$  "telephone  $\equiv$  no"> <link rel  $=$  "apple-touch-icon" sizes  $=$  "57x57" href  $=$  "http://img4.douban.com/pics/cardkit/loader/57.png" />   
…
```

# Post

如果要以POST发送一个请求，只需要把参数data以bytes形式传入。我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：

```txt
from urllib import request, parse   
print('Login to weibo.cn...')   
email  $=$  input('Email:')   
passwd  $=$  input('Password:')   
login_data  $=$  parse(urleencode([ ('username', email), ('password',passwd), ('entry', 'mweibo'), ('client_id', ')), ('savestate', '1'), ('ec', ')), ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r  $\equiv$  http%3A%2F%2Fm.weibo.cn%2F') ])   
req  $=$  request.Request('https://passport.weibo.cn/sso/login')   
req.add_header('Origin', 'https://passport.weibo.cn')   
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone;CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML,like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25') req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res  $\equiv$  wel&wm  $= 3349\& r =$  http%3A%2F%2Fm.weibo.cn %2F')   
with request(urlopen(req,data  $\equiv$  login_data.encode('utf-8')) as f: print('Status:','f.statusus,freason) for k,v in f.getheaders(): print(%s:%s'  $\%$  (k,v)) print('Data:','f.read().decode('utf-8'))   
如果登录成功，我们获得的响应如下：   
Status:200 OK   
Server:nginx/1.2.0   
...   
Set-Cookie:SSOLoginState  $\coloneqq 1432620126$  ;path=/;domain  $\equiv$  weibo.cn   
...   
Data:{"retcode":20000000,"msg":"","data":{..,"uid":"1658384301"}}
```

# - Handler

如果还需要更复杂的控制，比如通过一个 Proxy 去访问网站，我们需要利用 ProxyHandler 来处理，示例代码如下：

```python
proxy Handler  $\equiv$  urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})   
proxy_authhandler  $=$  urllib.request ProxyBasicAuthHandler()   
proxy.authhandler.add_password('realm', 'host', 'username', 'password')   
opener  $\equiv$  urllib.request.build_openers(proxyhandler, proxy_authhandler)   
with opener.open('http://www.example.com/login.htm1') as f: pass
```

小结

urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。

练习

利用url1ib读取XML，将XML一节的数据由硬编码改为由url1lib获取：

```python
from urllib import request, parse   
def fetchXml(url): pass   
# 测试   
print(fetchXml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330'))
```

# 13 常用第三方模块

除了内建的模块外，Python 还有大量的第三方模块。

基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装。本章介绍常用的第三方模块。

# 13.1 PIL

PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

由于 PIL 仅支持到 Python 2.7，加上年久失修，于是一群志愿者在 PIL 的基础上创建了兼容的版本，名字叫 Pillow，支持最新 Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用 Pillow。

·安装 Pillow

在命令行下直接通过pip安装：

```txt
$ pip install pillow
```

如果遇到 Permission denied 安装失败，请加上 sudo 重试。

- 操作图像

来看看最常见的图像缩放操作，只需三四行代码：

```python
from PIL import Image
# 打开一个.jpg图像文件，注意是当前路径：
im = Image.open('test.jpg')
# 获得图像尺寸：
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im/thumbail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存：
im.save('thumbail.jpg', 'jpeg')
```

其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。

比如，模糊效果也只需几行代码：

```python
from PIL import Image, ImageFilter
```

# 打开一个 jpg 图像文件，注意是当前路径：

```javascript
im = Image.open('test.jpg')
```

应用模糊滤镜：

```txt
im2 = im.filter(ImageFilter.BLUR)
```

```javascript
im2.save('blur.jpg', 'jpeg')
```

![](images/ab68f5b1259b74a7fdc60eafb0b077db5a0709efca8ec4619f59570be98d8c43.jpg)

![](images/d036b42aafb224d36a84ee79c9dbb2cc0efdd535f1827f3aaa3fe87d9c4ed622.jpg)

PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：

```python
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
#随机字母:
defrndChar(   ):
	return chr(random.randint(65, 90))
	#随机颜色1:
 defrndColor(   ):
		return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	#随机颜色2:
 defrndColor2(   ):
		return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
	#  ${240} \times  {60}$  :
 width = 60 * 4
 height = 60
 image = Image.new('RGB', (width, height), (255, 255, 255))
	#创建Font对象:
 font = ImageFont.truetype('Arial.tif', 36)
	#创建Draw对象:
 draw = ImageDraw.Draw(image)
	#填充每个像素:
 for x in range(width):
		for y in range.height):
		 drawn.o point((x, y), fill=rndColor(   ))
	#输出文字:
 for t in range(4):
			p draw.text((60 * t + 10, 10), r ndChar(   ), font=font, fill=rndColor2(   ))
	#模糊:
 image = image.filter(ImageFilter.BLUR)
 image.save('code.jpg', 'jpeg')
```

我们用随机颜色填充背景，再画上文字，最后对图像进行模糊，得到验证码图片如下：

![](images/8976f43c4a89fee30a56cabc5fd4a353e6b3ff4381f603eab505950afd9ec120.jpg)

如果运行的时候报错：

IOError: cannot open resource

这是因为 PIL 无法定位到字体文件的位置，可以根据操作系统提供绝对路径，比如：

'/Library/Fonts/Arial.ttf'

# 13.2 virtualenv

在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。所有第三方的包都会被pip安装到Python3的site-packages目录下。

如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python3。如果应用A需要jinja2.7，而应用B需要jinja2.6怎么办？

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

首先，我们用pip安装virtualenv:

```txt
$ pip3 install virtualenv
```

然后，假定我们要开发一个新的项目，需要一套独立的Python运行环境，可以这么做：

第一步，创建目录：

```txt
Mac:~ michael\( mkdir myproject  
Mac:~ michael\) cd myproject/  
Mac:myproject michael$
```

第二步，创建一个独立的Python运行环境，命名为venv:

```txt
Mac:myproject michael\(\$ 13\)virtualenv --no- site- packages venv  
Using base prefix '/usr/local/...\)/Python-framework/Versions/3.4'  
New python executable in venv/bin/python3.4  
Also creating executable in venv/bin/python  
Installing setuptools, pip, wheel...done.
```

命令virtualenv就可以创建一个独立的Python运行环境，我们还加上了参数--no-site-packages，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境。

新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境：

```txt
Mac:myproject michael $source venv/bin/activate (venv)Mac:myproject michael$
```

注意到命令提示符变了，有个(venv)前缀，表示当前环境是一个名为venv的Python环境。

下面正常安装各种第三方包，并运行python命令：

```txt
(venv)Mac:myproject michael\( pip install jinja2  
...  
Successfully installed jinja2-2.7.3 markupsafe-0.23  
(venv)Mac:myproject michael\) python myapp.py  
...
```

在 venv 环境下，用 pip 安装的包都被安装到 venv 这个环境下，系统 Python 环境不受任何影响。也就是说，venv 环境是专门针对 myproject 这个应用创建的。

退出当前的venv环境，使用deactivate命令：

```txt
(venv)Mac:myproject michael$ deactivate
Mac:myproject michael$
```

此时就回到了正常的环境，现在pip或python均是在系统Python环境下执行。

完全可以针对每个应用创建独立的Python运行环境，这样就可以对每个应用的Python环境进行隔离。

virtualenv 是如何创建“独立”的 Python 运行环境的呢？原理很简单，就是把系统 Python 复制一份到 virtualenv 的环境，用命令 source venv/bin/activate 进入一个 virtualenv 环境时，virtualenv 会修改相关环境变量，让命令 python 和 pip 均指向当前的 virtualenv 环境。

# 小结

virtualenv 为应用提供了隔离的 Python 运行环境，解决了不同应用间多版本的冲突问题。

# 14 图形界面

Python支持多种图形界面的第三方库，包括：

- Tk  
- wXWidgets  
Qt  
GTK

等等。

但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行GUI编程。

# - Tkinter

我们来梳理一下概念：

我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；

Tk 是一个图形库，支持多个操作系统，使用 Tcl 语言开发；

Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。

所以，我们的代码只需要调用Tkinter提供的接口就可以了。

# - 第一个GUI程序

使用Tkinter十分简单，我们来编写一个GUI版本的“Hello,world!”。

第一步是导入Tkinter包的所有内容：

```python
from tkinter import *
```

第二步是从Frame派生一个Application类，这是所有Widget的父容器：

```python
class Application(Frame): def __init__(self, master=None): Frame._init__(self, master) self.pack() self.createWidgets() def createWidgets(self): self.helloLabel = Label(self, text='Hello, world!') self.helloLabel.pack() self.quitButton = Button(self, text='Quit', command= self.quit) self.quitButton.pack()
```

在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。

pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。

在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。

第三步，实例化Application，并启动消息循环：

```python
app = Application()
# 设置窗口标题:
app(master.title('Hello World')
# 主消息循环:
app mainloop()
```

GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线

程中处理。

运行这个GUI程序，可以看到下面的窗口：

![](images/e486c6f6538cc8dfd08025188d68de51f77a4bde0fcc39a8de623df1e3422f05.jpg)

点击“Quit”按钮或者窗口的“x”结束程序。

# ·输入文本

我们再对这个GUI程序改进一下，加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。

```python
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self(alertButton = Button(self, text='Hello', command= self.hello)
        self(alertButton.pack())
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)
app = Application()
# 设置窗口标题:
app(master.title('Hello World')
# 主消息循环:
app mainloop()
```

当用户点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本后，使用tkMessageBox.showinfo()可以弹出消息对话框。

程序运行结果如下：

![](images/fd5a85263baf3fd715a56ab487d6de8fa9b68d1a273fcb7ff442e5ad45b5c0af.jpg)

小结

Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。

# 15 网络编程

自从互联网诞生以来，现在基本上所有的程序都是网络程序，很少有单机版的程序了。

计算机网络就是把各个计算机连接到一起，让网络中的计算机可以互相通信。网络编程就是如何在程序中实现两台计算机的通信。

举个例子，当你使用浏览器访问新浪网时，你的计算机就和新浪的某台服务器通过互联网连接起来了，然后，新浪的服务器把网页内容作为数据通过互联网传输到你的电脑上。

由于你的电脑上可能不止浏览器，还有QQ、Skype、Dropbox、邮件客户端等，不同的程序连接的别的计算机也会不同，所以，更确切地说，网络通信是两台计算机上的两个进程之间的通信。比如，浏览器进程和新浪服务器上的某个Web服务进程在通信，而QQ进程是和腾讯的某个服务器上的某个进程在通信。

# 原来网络通信就是两个进程之间在通信

![](images/4ba44b3c32a121deff7ef2f19ed51e3e4c83544176c5980264ff1cbc809e2f63.jpg)

网络编程对所有开发语言都是一样的，Python也不例外。用Python进行网络编程，就是在Python程序本身这个进程内，连接别的服务器进程的通信端口进行通信。

本章我们将详细介绍Python网络编程的概念和最主要的两种网络类型的编程。

# 15.1 TCP/IP简介

虽然大家现在对互联网很熟悉，但是计算机网络的出现比互联网要早很多。

计算机为了联网，就必须规定通信协议，早期的计算机网络，都是由各厂商自己规定一套协议，IBM、Apple和Microsoft都有各自的网络协议，互不兼容，这就好比一群人有的说英语，有的说中文，有的说德语，说同一种语言的人可以交流，不同的语言之间就不行了。

为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，为了实现互联网这个目标，互联网协议簇（Internet Protocol Suite）就是通用协议标准。Internet是由inter和net两个单词组合起来的，原意就是连接“网络”的网络，有了Internet，任何私有网络，只要支持这个协议，就可以联入互联网。

因为互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议简称TCP/IP协议。

通信的时候，双方必须知道对方的标识，好比发邮件必须知道对方的邮件地址。互联网上每个计算机的唯一标识就是 IP 地址，类似 123.123.123.123。如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个或多个 IP 地址，所以，IP 地址对应实际上是计算机的网络接口，通常是网卡。

IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。

IP地址实际上是一个32位整数（称为IPv4），以字符串表示的IP地址如192.168.0.1实际上是把32位整数按8位分组后的数字表示，目的是便于阅读。

IPv6地址实际上是一个128位整数，它是目前使用的IPv4的升级版，以字符串表示类似于2001:0db8:85a3:0042:1000:8a2e:0370:7334。

TCP 协议则是建立在 IP 协议之上的。TCP 协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。TCP 协议

会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。

![](images/ea1acd226ff39b43580def7c8c5060b797140b80d5c9c77c40f71c7c22f6f48c.jpg)

许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。

一个IP包除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。

端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。一个IP包来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。

一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。

了解了TCP/IP协议的基本概念，IP地址和端口的概念，我们就可以开始进行网络编程了。

# 15.2 TCP 编程

Socket 是网络编程的一个抽象概念。通常我们用一个 Socket 表示“打开了一个网络链接”，而打开一个 Socket 需要知道目标计算机的 IP 地址和端口号，再指定协议类型即可。

# - 客户端

大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

举个例子，当我们在浏览器中访问新浪时，我们自己的计算机就是客户端，浏览器会主动向新浪的服务器发起连接。如果一切顺利，新浪的服务器接受了我们的连接，一个TCP连接就建立起来的，后面的通信就是发送网页内容了。

所以，我们要创建一个基于TCP连接的Socket，可以这样做：

导入socket库：

import socket

创建一个socket:

s = socket(socket(socket.AF_INET, socket.SOCK_STREAM)

建立连接：

s.connect('www.sina.com.cn', 80))

创建 Socket 时，AF_INET 指定使用 IPv4 协议，如果要用更先进的 IPv6，就指定为 AF_INET6。SOCK_STREAM 指定使用面向流的 TCP 协议，这样，一个 Socket 对象就创建成功，但是还没有建立连接。

客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址，但是怎么知道新浪服务器的端口号呢？

答案是作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

因此，我们连接新浪服务器的代码如下：

s.connect('www.sina.com.cn', 80))

注意参数是一个tuple，包含地址和端口号。

建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容：

发送数据：

```javascript
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
```

TCP 连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。例如，HTTP 协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了：

接收数据：

```txt
buffer  $=$  []   
while True: #每次最多接收1k字节： d  $=$  s.recv(1024) ifd: buffer.append(d) else: break data  $=$  b''.join(buffer)
```

接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。

当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了：

关闭连接：

```txt
s.close()
```

接收到的数据包括 HTTP 头和网页本身，我们只需要把 HTTP 头和网页分离一下，把 HTTP 头打印出来，网页内容保存到文件：

```txt
header,html  $\equiv$  data.split(b'\r\n\r\n',1)   
print(headerdecode('utf-8'))   
#把接收的数据写入文件：   
with open('sina.html'，'wb')asf: f.write( html)
```

现在，只需要在浏览器中打开这个sina.html文件，就可以看到新浪的首页了。

# - 服务器

和客户端编程相比，服务器编程就要复杂一些。

服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。

所以，服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。

但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。

我们来编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。

首先，创建一个基于IPv4和TCP协议的Socket：

```python
s = socket(socket(socket.AF_INET, socket.SOCK_STREAM)
```

然后，我们要绑定监听的地址和端口。服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址。127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是说，外部的计算机无法连接进来。

端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：

监听端口：

```txt
s.bind(( '127.0.0.1'，9999))
```

紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：

```python
s.listen(5)
```

```python
print('Waiting for connection...')
```

接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接：

```txt
while True:
```

接受一个新连接：

```python
sock, addr = s.accept()
# 创建新线程来处理TCP连接:
t = threading.Thread(target=tcplink, args=(sock, addr))
t.start()
```

每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：

```python
def tcplink(sock, addr):  
    print('Accept new connection from %s:%s...' % addr)  
    sock.send(b'Welcome!')  
while True:  
    data = sock.recv(1024)  
    time.sleep(1)  
    if not data or data.decode('utf-8') == 'exit':  
        break  
    sock.send('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))  
sock.close()  
print('Connection from %s:%s closed.' % addr)
```

连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接。

要测试这个服务器程序，我们还需要编写一个客户端程序：

```python
s = socket(socket(socket.AF_INET, socket.SOCK_STREAM)
```

建立连接：

```javascript
s.connect((127.0.0.1', 9999))
```

接收欢迎消息：

```lua
print(s.recv(1024).decode('utf-8'))
```

```txt
for data in [b'Michael', b'Tracy', b'Sarah']:
```

发送数据：

```txt
s.send(data)
```

```lua
print(s.recv(1024).decode('utf-8'))
```

```txt
s.send(b'exit')
```

```txt
s.close()
```

我们需要打开两个命令行窗口，一个运行服务器程序，另一个运行客户端程序，就可以看到效果了：

![](images/805754fea5a41006119a01563766476951bdeb00d1eb6d48b8a4d301701e6bdd.jpg)

需要注意的是，客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序。

小结

用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。

同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。

# 15.3 UDP编程

TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。

使用 UDP 协议时，不需要建立连接，只需要知道对方的 IP 地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。

虽然用 UDP 传输数据不可靠，但它的优点是和 TCP 比，速度快，对于不要求可靠到达的数据，就可以使用 UDP 协议。

我们来看看如何通过 UDP 协议传输数据。和 TCP 类似，使用 UDP 的通信双方也分为客户端和服务器。服务器首先需要绑定端口：

```txt
s = socket(socket(socket.AF_INET, socket.SOCK_DGRAM)
```

绑定端口：

```txt
s.bind(( '127.0.0.1'，9999))
```

创建 Socket 时，SOCK_DGRAM 指定了这个 Socket 的类型是 UDP。绑定端口和 TCP 一样，但是不需要调用 listen() 方法，而是直接接收来自任何客户端的数据：

```lua
print('Bind UDP on 9999...')
```

while True:

接收数据：

```txt
data, addr = s.recvfrom(1024)  
print('Received from %s:%s.' % addr)  
s.sendto(b'Hello, %s!' % data, addr)
```

recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。

注意这里省掉了多线程，因为这个例子很简单。

客户端使用 UDP 时，首先仍然创建基于 UDP 的 Socket，然后，不需要调用 connect()，直接通过 sendto()给服务器发数据：

```txt
s = socket(socket(socket.AF_INET, socket.SOCK_DGRAM)
```

```txt
for data in [b'Michael', b'Tracy', b'Sarah']:
```

发送数据：

```txt
s.sendto(data,('127.0.0.1',9999))
```

接收数据：

```lua
print(s.recv(1024).decode('utf-8'))
```

```txt
s.close()
```

从服务器接收数据仍然调用recv()方法。

仍然用两个命令行分别启动服务器和客户端测试，结果如下：

![](images/6f19636aaab2832400b5ffdbc860a32372059879eb67dda49f57a58c82474b03.jpg)

# ·小结

UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。

# 16 电子邮件

Email的历史比Web还要久远，直到现在，Email也是互联网上应用非常广泛的服务。

几乎所有的编程语言都支持发送和接收电子邮件，但是，先等等，在我们开始编写代码之前，有必要搞清楚电子邮件是如何在互联网上运作的。

我们来看看传统邮件是如何运作的。假设你现在在北京，要给一个香港的朋友发一封信，怎么做呢？

首先你得写好信，装进信封，写上地址，贴上邮票，然后就近找个邮局，把信仍进去。

信件会从就近的小邮局转运到大邮局，再从大邮局往别的城市发，比如先发到天津，再走海运到达香港，也可能走京九线到香港，但是你不用关心具体路线，你只需要知道一件事，就是信件走得很慢，至少要几天时间。

信件到达香港的某个邮局，也不会直接送到朋友的家里，因为邮局的叔叔是很聪明的，他怕你的朋友不在家，一趟一趟地白跑，所以，信件会投递到你的朋友的邮箱里，邮箱可能在公寓的一层，或者家门口，直到你的朋友回家的时候检查邮箱，发现信件后，就可以取到邮件了。

电子邮件的流程基本上也是按上面的方式运作的，只不过速度不是按天算，而是按秒算。

现在我们回到电子邮件，假设我们自己的电子邮件地址是me@163.com，对方的电子邮件地址是friend@sina.com（注意地址都是虚构的哈），现在我们用Outlook或者Foxmail之类的软件写好邮件，填上对方的Email地址，点“发送”，电子邮件就发出去了。这些电子邮件软件被称为MUA：Mail User Agent—邮件用户代理。

Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent—邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等。由于我们自己的电子邮件是163.com，所以，Email首先被投递到网易提供的MTA，再由网易的MTA发到对方服务商，也就是新浪的MTA。这个过程中间可能还会经过别的MTA，但是我们不关心具体路线，我们只关心速度。

Email到达新浪的MTA后，由于对方使用的是@sina.com的邮箱，因此，新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent—邮件投递代理。Email到达MDA后，就静静地躺在新浪的某个服务器上，存放在某个文件或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱。

同普通邮件类似，Email不会直接到达对方的电脑，因为对方电脑不一定开机，开机也不一定联网。对方要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上。

所以，一封电子邮件的旅程就是：

发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA<-MUA<-收件人

有了上述基本概念，要编写程序来发送和接收邮件，本质上就是：

1. 编写 MUA 把邮件发到 MTA;  
2. 编写 MUA 从 MDA 上收邮件。

发邮件时，MUA 和 MTA 使用的协议就是 SMTP: Simple Mail Transfer Protocol，后面的 MTA 到另一个 MTA 也是用 SMTP 协议。

收邮件时，MUA 和 MDA 使用的协议有两种：POP：Post Office Protocol，目前版本是 3，俗称 POP3；IMAP：Internet Message Access Protocol，目前版本是 4，优点是不但能取邮件，还可以直接操作 MDA 上存储的邮件，比如从收件箱移到垃圾箱，等等。

邮件客户端软件在发邮件时，会让你先配置SMTP服务器，也就是你要发到哪个MTA上。假设你正在使用163的邮箱，你就不能直接发到新浪的MTA上，因为它只服务新浪的用户，所以，你得填163提供的SMTP服务器地址：smtp.163.com，为了证明你是163的用户，SMTP服务器还要求你填写邮箱地址和邮箱口令，这样，MUA才能正常地把Email通过SMTP协议发送到MTA。

类似的，从MDA收邮件时，MDA服务器也要求验证你的邮箱口令，确保不会有人冒充你收取你的邮件，所以，Outlook之类的邮件客户端会要求你填写POP3或IMAP服务器地址、邮箱地址和口令，这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件。

在使用Python收发邮件前，请先准备好至少两个电子邮件，如xxx@163.com，xxx@sina.com，xxx@qq.com等，注意两个邮箱不要用同一家邮件服务商。

最后特别注意，目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录。

# 16.1 SMTP 发送邮件

SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

首先，我们来构造一个最简单的纯文本邮件：

```python
from emailmime.text import MIMEText  
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
```

注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

然后，通过SMTP发出去：

```python
#输入Email地址和口令：  
from_addr  $=$  input('From:')  
password  $=$  input('Password:'）  
#输入收件人地址：  
to_addr  $=$  input('To:'）  
#输入SMTP服务器地址：  
smtp_server  $=$  input('SMTP server:'）  
import smtplib  
server  $=$  smtplib.SMTP(smtp_server，25)#SMTP协议默认端口是25  
server.setDebuglevel(1)  
server login(from_addr，password)  
server.sendmail(from_addr，[to_addr]，msg.as_string())  
server.quit()
```

我们用 set_DEBUGlevel(1) 就可以打印出和 SMTP 服务器交互的所有信息。SMTP 协议就是简单的文本命令和响应。login() 方法用来登录 SMTP 服务器，sendmail() 方法就是发邮件，由于可以一次发给多个人，所以传入一个 list，邮件正文是一个 str，as_string() 把 MIMEText 对象变成 str。

如果一切顺利，就可以在收件人信箱中收到我们刚发送的Email:

![](images/68ac18a52116b6f5a18297be3752b42dab749e226cc64df7dde73697081b1852.jpg)

仔细观察，发现如下问题：

1. 邮件没有主题；  
2. 收件人的名字没有显示为友好的名字，比如 Mr Green <green@example.com>;  
3. 明明收到了邮件，却提示不在收件人中。

这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEMText中，才是一封完整的邮件：

```python
from email import encoders   
from email.header import Header   
from email.mime.text import MIMEText   
from email.utils import parseaddr, formataddr   
import smtplib   
def _format_addr(s):
```

```python
name, addr = parseaddr(s)  
return formataddr((Header(name, 'utf-8').encode(), addr))  
from_addr = input('From:')  
password = input('Password:')  
to_addr = input('To:')  
smtp_server = input('SMTP server:')  
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')  
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)  
msg['To'] = _format_addr('管理员 <%s>' % to_addr)  
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()  
server = smtplib.SMTP(smtp_server, 25)  
server.setDebuglevel(1)  
serverlogin(from_addr, password)  
server.sendmail(from_addr, [to_addr], msg.as_string())  
server.quit()
```

我们编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。

msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。

再发送一遍邮件，就可以在收件人邮箱中看到正确的标题、发件人和收件人：

# 来自SMTP的问候……

发件人：Python爱好者 <xxxxxxxxx@163.com>

时间：2014年8月14日（星期四）下午3:45

收件人：管理员 <xxxx@qq.com>

hello, send by Python...

你看到的收件人的名字很可能不是我们传入的管理员，因为很多邮件服务商在显示邮件时，会把收件人名字自动替换为用户注册的名字，但是其他收件人名字的显示不受影响。

如果我们查看Email的原始内容，可以看到如下经过编码的邮件头：

From:  $= ?$ utf-8?b?UH10aG9u54ix5aW96ICF?  $=$  <xxxxxxxx@163.com>

To:  $= ?$  utf-8?b?566h55CG5ZGY?  $=$  <xxxx@qq.com>

Subject:  $= ?$  utf-8?b?5p216IeqU01UUOeahOmXruWAmEKApuKApg  $= = ? =$

这就是经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本。如果我们自己来手动构造这样的编码文本，显然比较复杂。

# - 发送 HTML 邮件

如果我们要发送 HTML 邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造 MIMEText 对象时，把 HTML 字符串传进去，再把第二个参数由 plain 变为 html 就可以了：

```html
msg = MIMEText('<html><body><h1>Hello</h1>' +'<p>send by <a href="http://www.python.org">Python</a>....</p>' +'<body></html>'，'html'，'utf-8')
```

再发送一遍邮件，你将看到以 HTML 显示的邮件：

```txt
来自SMTP的问候……  
发件人：Python爱好者 <xxxxxx@163.com> ③  
时间：2014年8月14日（星期四）下午4:06  
收件人：管理员 <xxxxxx@qq.com>
```

# Hello

send by Python...

# - 发送附件

如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：

邮件对象：

```txt
msg = MIMEMultipart()
msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()
```

```python
邮件正文是MIMEText:  
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
```

添加附件就是加上一个MIMEBase，从本地读取一个图片：

```javascript
with open('/Users/michael/Downloads/test.png', 'rb') as f: # 设置附件的MIME和文件名，这里是png类型： mime  $=$  MIMEBase('image'，'png'，filename  $\equiv$  'test.png') # 加上必要的头信息： mime.add_header('Content-Disposition'，'attachment'，filename  $\equiv$  'test.png') mime.add_header('Content-ID'，'<0>） mime.add_header('X-Attachment-Id'，'0') # 把附件的内容读进来： mime.setPGAoyf.read()) # 用Base64编码： encoders.encode_base64(mime) # 添加到MIMEMuLtipart: msg.attach(mime)
```

然后，按正常发送流程把msg（注意类型已变为MIMEMultipart）发送出去，就可以收到如下带附件的邮件：

# 来自SMTP的问候……

发件人：Python爱好者 <xxxxxx@163.com>

时间：2014年8月14日（星期四）下午5:08

收件人：管理员 <xxxx@qq.com>

附件：1个（test.png）

send with file...

# $\mathcal{O}$  附件(1个)

# 普通附件

![](images/428d47dd6b16ba304c6de507c898c20b2f00d6d8058410b438ce1eecc2699ed3.jpg)

test.png (80.13K)

下载预览收藏转存

# ·发送图片

如果要把一个图片嵌入到邮件正文中怎么做？直接在 HTML 邮件中链接图片地址行不行？答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。

要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在 HTML 中通过引用 src="cid:0" 就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的 cid:x 即可。

把上面代码加入MIMEMultipart的MIMText从plain改为html，然后在适当的位置引用图片：

```javascript
msg.attach(MIMEMText('<htm1><body><h1>Hello</h1>' + <p><img src="cid:0"></p>' + </body></htm1>'，'html'，'utf-8'))
```

再次发送，就可以看到图片直接嵌入到邮件正文的效果：

```txt
来自SMTP的问候……  
发件人：Python爱好者 <asklfx@163.com>  
时间：2014年8月14日（星期四）下午5:27  
收件人：Xuefeng<18224514@qq.com>
```

# Hello

![](images/f369da7ef26dad243f67f921dcd069fa4b4195328207a05dcf5bcba41a6ebdd6.jpg)

# - 同时支持 HTML 和 Plain 格式

如果我们发送 HTML 邮件，收件人通过浏览器或者 Outlook 之类的软件是可以正常浏览邮件内容的，但是，如果收件人使用的设备太古老，查看不了 HTML 邮件怎么办？

办法是在发送 HTML 的同时再附加一个纯文本，如果收件人无法查看 HTML 格式的邮件，就可以自动降级查看纯文本邮件。

利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative:

```txt
msg = MIMEMultipart('alternative')  
msg['From'] = ...  
msg['To'] = ...  
msg['Subject'] = ...  
msg.attach(MIMEMText('hello', 'plain', 'utf-8'))  
msg.attach(MIMEMText(['<html><body><h1>Hello</h1></body></html>'', 'html', 'utf-8'))  
# 正常发送 msg 对象...
```

# - 加密 SMTP

使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。

某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。

必须知道，Gmail的SMTP端口是587，因此，修改代码如下：

```python
smtp_server = 'smtp gmail.com'  
smtp_port = 587  
server = smtplib.SMTP(smtp_server,smtp_port)  
server.starttls()  
# 剩下的代码和前面的一模一样：  
server.setDebuglevel(1)
```

只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。后面的代码和前面的发送邮件代码完全一

样。如果因为网络问题无法连接Gmail的SMTP服务器，请相信我们的代码是没有问题的，你需要对你的网络设置做必要的调整。

# ·小结

使用Python的smtpplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。

构造一个邮件对象就是一个Messag对象，如果构造一个MIMEMText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEMBase可以表示任何对象。它们的继承关系如下：

```diff
Message  
+- MIMEBase  
+- MIMEMultipart  
+- MIMENonMultipart  
+- MIMEMessage  
+- MIMEText  
+- MIMEImage
```

种嵌套关系就可以构造出任意复杂的邮件。你可以通过 email mime 文档查看它们所在的包以及详细的用法。

# 16.2 POP3 收取邮件

SMTP用于发送邮件，如果要收取邮件呢？

收取邮件就是编写一个 MUA 作为客户端，从 MDA 把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是 POP 协议，目前版本号是 3，俗称 POP3。

Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。

注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。

要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。

所以，收取邮件分两步：

第一步：用poplib把邮件的原始文本下载到本地；

第二部：用 email 解析原始文本，还原为邮件对象。

# - 通过POP3下载邮件

POP3协议本身很简单，以下面的代码为例，我们来获取最新的一封邮件内容：

```python
import poplib  
# 输入邮件地址，口令和POP3服务器地址：  
email = input('Email:')  
password = input('Password:')  
pop3_server = input('POP3 server:')  
# 连接到POP3服务器：  
server = poplib.pop3(pop3_server)  
# 可以打开或关闭调试信息：  
server.setDebuglevel(1)  
# 可选：打印POP3服务器的欢迎文字：  
print(server.getwelcome().decode('utf-8'))  
# 身份认证：
```

```python
server.user(email)  
server.pass_(password)  
# stat()返回邮件数量和占用空间：  
print('Messages: %s. Size: %s' % server.stat())  
# list()返回所有邮件的编号：  
resp, mails, octets = server.list()  
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]  
print(mails)  
# 获取最新一封邮件，注意索引号从1开始：  
index = len(mails)  
resp, lines, octets = server.retr(index)  
# Lines 存储了邮件的原始文本的每一行，  
# 可以获得整个邮件的原始文本：  
msg_content = b'\r\n'.joinlines).decode('utf-8')  
# 稍后解析出邮件：  
msg = Parser().parsestr(msg_content)  
# 可以根据邮件索引号直接从服务器删除邮件：  
# server.dele(index)  
# 关闭连接：  
server.quit()
```

用POP3获取邮件其实很简单，要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可。真正麻烦的是把邮件的原始内容解析为可以阅读的邮件对象。

# - 解析邮件

解析邮件的过程和上一节构造邮件正好相反，因此，先导入必要的模块：

```python
from emailparser import Parser   
from email.header import decode_header   
from email.utils import parseaddr   
import poplib
```

只需要一行代码就可以把邮件内容解析为 Message 对象：

```txt
msg = Parser().parsestr(msg_content)
```

但是这个 Message 对象本身可能是一个 MIMEMultipart 对象，即包含嵌套的其他 MIMEBase 对象，嵌套可能还不止一层。

所以我们要递归地打印出 Message 对象的层次结构：

```python
#indent 用于缩进显示:
def print_info(msg,indent=0):
    ifindent == 0:
        for header in ['From','To','Subject':
            value = msg.get报告显示，' )
        if value:
            if header=='Subject':
                value = decode_str(value)
```

```python
else: hdr, addr = parseaddr(value) name = decode_str(hr) value  $=$  u'ss'<%s>'  $\%$  (name, addr) print('%s%s'  $\%$  ('\*indent, header, value))   
if (msg.isMULTiarp()): parts  $=$  msg.get_load() for n, part in enumerate-parts): print(%spart  $\%$  (%\*indent, n)) print('%s---------%(%\*indent)) print_info(part,indent + 1)   
else: content_type  $=$  msg.get_content_type() if content_type  $= =$  'text/plain' or content_type  $= =$  'text/html': content  $=$  msg.get_load(decode=True) charset  $=$  guess_charset(msg) if charset: content  $=$  contentdecode(charset) print('%sText:%s'  $\%$  ('\*indent, content + '\...')) else: print('%sAttachment:%s'  $\%$  ('\*indent, content_type))
```

邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode:

```txt
defdecode_str(s): value, charset  $=$  decode_header(s)[0] if charset: value  $=$  value.decode(charset) return value
```

decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。

文本邮件的内容也是 str，还需要检测编码，否则，非 UTF-8 编码的邮件都无法正常显示：

```python
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '') .lower()
        pos = content_type.find('charset')
        if pos >= 0:
            charset = content_type[pos + 8].strip()
    return charset
```

把上面的代码整理好，我们就可以来试试收取一封邮件。先往自己的邮箱发一封邮件，然后用浏览器登录邮箱，看看邮件收到没，如果收到了，我们就来用Python程序把它收到本地：

```txt
用POP3收取邮件  $\text{日}$  0  
发件人：Test<xxxxxx@qq.com>  
收件人：Python爱好者<xxxxxx@163.com>  
时间：2014年08月16日20:53（星期六）  
附件：1个（r.py）查看附件
```

Python可以使用POP3收取邮件……

运行程序，结果如下：

```txt
+OK Welcome to coremail Mail Pop3 Server (163coms[...])  
Messages: 126. Size: 27228317  
From: Test <xxxxxxxx@qq.com>  
To: Python 爱好者 <xxxxxxxx@163.com>  
Subject: 用POP3收取邮件  
part 0  
--  
part 0  
--  
Text: Python 可以使用POP3收取邮件……  
part 1  
--  
Text: Python 可以<a href="..."使用POP3</a>收取邮件……  
part 1  
--  
Attachment: application/occtet-stream
```

我们从打印的结构可以看出，这封邮件是一个MIMEMultipart，它包含两部分：第一部分又是一个MIMEMultipart，第二部分是一个附件。而内嵌的MIMEMultipart 是一个 alternative 类型，它包含一个纯文本格式的 MIMEText 和一个 HTML 格式的 MIMEText。

# ·小结

用Python的poplib模块收取邮件分两步：第一步是用POP3协议把邮件获取到本地，第二步是用email模块把原始邮件解析为Message对象，然后，用适当的形式把邮件内容展示给用户即可。

# 17 访问数据库

程序运行的时候，数据都是在内存中的。当程序终止的时候，通常都需要将数据保存到磁盘上，无论是保存到本地磁盘，还是通过网络保存到服务器上，最终都会将数据写入磁盘文件。

而如何定义数据的存储格式就是一个大问题。如果我们自己来定义存储格式，比如保存一个班级所有学生的成绩单：

<table><tr><td>名字</td><td>成绩</td></tr><tr><td>Michael</td><td>99</td></tr><tr><td>Bob</td><td>85</td></tr><tr><td>Bart</td><td>59</td></tr><tr><td>Lisa</td><td>87</td></tr></table>

你可以用一个文本文件保存，一行保存一个学生，用，隔开：

```csv
Michael,99   
Bob,85   
Bart,59   
Lisa,87
```

你还可以用JSON格式保存，也是文本文件：

```json
[ {"name":"Michael","score":99}, {"name":"Bob","score":85}, {"name":"Bart","score":59}, {"name":"Lisa","score":87} ]
```

你还可以定义各种保存格式，但是问题来了：

存储和读取需要自己实现，JSON还是标准，自己定义的格式就各式各样了；

不能做快速查询，只有把数据全部读到内存中才能自己遍历，但有时候数据的大小远远超过了内存（比如蓝光电影，40GB的数据），根本无法全部读入内存。

为了便于程序保存和读取数据，而且，能直接通过条件快速查询到指定的数据，就出现了数据库（Database）这种专门用于集中存储和查询的软件。

数据库软件诞生的历史非常久远，早在1950年数据库就诞生了。经历了网状数据库，层次数据库，我们现在广泛使用的关系数据库是20世纪70年代基于关系模型的基础上诞生的。

关系模型有一套复杂的数学理论，但是从概念上是十分容易理解的。举个学校的例子：

假设某个 XX 省 YY 市 ZZ 县第一实验小学有 3 个年级，要表示出这 3 个年级，可以在 Excel 中用一个表格画出来：

<table><tr><td>Grade_ID</td><td>Name</td></tr><tr><td>1</td><td>一年级</td></tr><tr><td>2</td><td>二年级</td></tr><tr><td>3</td><td>三年级</td></tr></table>

每个年级又有若干个班级，要把所有班级表示出来，可以在Excel中再画一个表格：

<table><tr><td>Grade_ID</td><td>Class_ID</td><td>Name</td></tr><tr><td>1</td><td>11</td><td>一年级一班</td></tr><tr><td>1</td><td>12</td><td>一年级二班</td></tr><tr><td>1</td><td>13</td><td>一年级三班</td></tr><tr><td>2</td><td>21</td><td>二年级一班</td></tr><tr><td>2</td><td>22</td><td>二年级二班</td></tr></table>

这两个表格有个映射关系，就是根据Grade_ID可以在班级表中查找到对应的所有班级：

![](images/c9cb8866ef82eae8601c2ffb976e9cfe3c7dc3875dd3ad148d6a4265d70ac38f.jpg)

也就是Grade表的每一行对应Class表的多行，在关系数据库中，这种基于表（Table）的一对多的关系就是关系数据库的基础。

根据某个年级的ID就可以查找所有班级的行，这种查询语句在关系数据库中称为SQL语句，可以写成：

```sql
SELECT * FROM classes WHERE grade_id = '1';
```

结果也是一个表：

```txt
grade_id | class_id | name  
1 | 11 | 一年级一班  
1 | 12 | 一年级二班  
1 | 13 | 一年级三班
```

类似的，Class表的一行记录又可以关联到Student表的多行记录：

![](images/1f2e1327e57be526f2bd80a4ba6be6162d9afd0c01c00e7bed79f6918a98b379.jpg)

由于本教程不涉及到关系数据库的详细内容，如果你想从零学习关系数据库和基本的 SQL 语句，如果你想从零学习关系数据库和基本的 SQL 语句，请自行搜索相关课程。

- NoSQL

你也许还听说过NoSQL数据库，很多NoSQL宣传其速度和规模远远超过关系数据库，所以很多同学觉得有了NoSQL是否就不需要SQL了呢？千万不要被他们忽悠了，连SQL都不明白怎么可能搞明白NoSQL呢？

# - 数据库类别

既然我们要使用关系数据库，就必须选择一个关系数据库。目前广泛使用的关系数据库也就这么几种：

付费的商用数据库：

- Oracle，典型的高富帅；  
- SQL Server，微软自家产品，Windows 定制专款；  
DB2，IBM的产品，听起来挺高端；  
- Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。

这些数据库都是不开源而且付费的，最大的好处是花了钱出了问题可以找厂家解决，不过在Web的世界里，常常需要部署成千上万的数据库服务器，当然不能把大把大把的银子扔给厂家，所以，无论是Google、Facebook，还是国内的BAT，无一例外都选择了免费的开源数据库：

- MySQL，大家都在用，一般错不了；  
- PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；  
- sqlite，嵌入式数据库，适合桌面和移动应用。

作为Python开发工程师，选择哪个免费数据库呢？当然是MySQL。因为MySQL普及率最高，出了错，可以很容易找到解决方法。而且，围绕MySQL有一大堆监控和运维的工具，安装和使用很方便。

为了能继续后面的学习，你需要从MySQL官方网站下载并安装MySQL Community Server 5.6，这个版本是免费的，其他高级版本是要收钱的（请放心，收钱的功能我们用不上）。

# 17.1 使用 SQLite

SQLite 是一种嵌入式数据库，它的数据库就是一个文件。由于 SQLite 本身是 C 写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在 iOS 和 Android 的 App 中都可以集成。

Python 就内置了 SQLite3，所以，在 Python 中使用 SQLite，不需要安装任何东西，直接使用。

在使用SQLite前，我们先要搞清楚几个概念：

表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。

要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection;

连接到数据库后，需要打开游标，称之为 Cursor，通过 Cursor 执行 SQL 语句，然后，获得执行结果。

Python 定义了一套操作数据库的 API 接口，任何数据库要连接到 Python，只需要提供符合 Python 标准的数据库驱动即可。

由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

我们在Python交互式命令行实践一下：

```txt
导入SQLite驱动：  
```python
>>> import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建：
>>> conn = sqlite3.connect('test.db')
# 创建一个Cursor:
>>> cursor = conn.cursor()
# 执行一条SQL语句，创建user表：
>>> cursor.exec('create table user (id varchar(20) primary key, name varchar(20))')
<sqlite3.Cursor object at 0x10f8aa260>
# 继续执行一条SQL语句，插入一条记录：
>>> cursor.exec('insert into user (id, name) values ('1', 'Michael')')
<sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数：
>>> cursor.rowcount
1
# 关闭Cursor:
>>> cursor.close()
# 提交事务：
>>> conn.commit()
# 关闭Connection:
>>> conn.close()
```

我们再试试查询记录：

```txt
>>>conn  $=$  sqlite3.connect('test.db')   
>>>cursor  $=$  conn.cursor() #执行查询语句：
```

```python
>>> cursor.exec('select * from user where id=?', ('1',))
<sqlite3.Cursor object at 0x10f8aa340>
# 获得查询结果集:
>>> values = cursor<stdlib(   )
>>> values
[( '1', 'Michael') ]
>>> cursor.close(   )
>>> conn.close(   )
```

使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

使用 Cursor 对象执行 insert, update, delete 语句时，执行结果由 rowcount 返回影响的行数，就可以拿到执行结果。

使用 Cursor 对象执行 select 语句时，通过 featchall()可以拿到结果集。结果集是一个 list，每个元素都是一个 tuple，对应一行记录。

如果 SQL 语句带有参数，那么需要把参数按照位置传递给 execute() 方法，有几个?占位符就必须对应几个参数，例如：cursor.exec('select * from user where name=? and pwd=?', ('abc', 'password'))

SQLite 支持常见的标准 SQL 语句以及几种常见的数据类型。具体文档请参阅 SQLite 官方网站。

# 小结

在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。

要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。

如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:…except:…finally:…的用法。

# ·练习

请编写函数，在Sqlite中根据分数段查找指定的名字：

```python
# --coding: utf-8 --import os,sqlite3
db_file = os.path.join(os.pathdirname(_file_, 'test.db'))
if os.path.isfile(db_file):
    os.remove(db_file)
# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.exec('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.exec(r"insert into user values ('A-001', 'Adam', 95)")
cursor.exec(r"insert into user values ('A-002', 'Bart', 62)")
cursor.exec(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()
def get_score_in(low, high):
```

返回指定分数区间的名字，按分数从低到高排序

# 17.2 使用MySQL

MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。

此外，MySQL 内部有多种数据库引擎，最常用的引擎是支持数据库事务的 InnoDB。

# - 安装 MySQL

可以直接从MySQL官方网站下载最新的CommunityServer5.6.x版本。MySQL是跨平台的，选择对应的平台下载安装文件，安装即可。

安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。

在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。

在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf:

```ini
[client]   
default-character-set  $=$  utf8   
[mysqld]   
default-storage-engine  $=$  INNODB   
character-set-server  $=$  utf8   
collation-server  $=$  utf8_general_ci
```

重启MySQL后，可以通过MySQL的客户端命令行检查编码：

```txt
$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor...
...
mysql> show variables like '%char%';
+
| Variable_name | Value
+---+---+---+
| character_set_client | utf8 | 
| character_set_connection | utf8 | 
| character_set_database | utf8 | 
| character_set_filesystem | binary | 
| character_set_results | utf8 | 
| character_set_server | utf8 | 
| character_set_system | utf8 | 
| character_sets_dir | /usr/local/mysql-5.1.65-osx10.6-x86_64/share/charsets/ |
+---+---+---+
8 rows in set (0.00 sec)
```

看到utf8 字样就表示编码设置正确。

注：如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4，utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。

# - 安装MySQL驱动

由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external:

```txt
$ pip install mysql-connector python --allow-external mysql-connector python
```

我们演示如何连接到MySQL服务器的test数据库：

```python
导入MySQL驱动：  
```python  
>>> import mysqlconnector  
# 注意把password设为你的root口令：  
>>> conn = mysqlconnector.connect(user='root', password='password', database='test')  
>>> cursor = conn.cursor()  
# 创建user表：  
>>> cursor.exec('create table user(id varchar(20) primary key, name varchar(20))')  
# 插入一行记录，注意MySQL的占位符是%s：  
>>> cursor.exec('insert into user(id, name) values(%s, %s)', ['1', 'Michael'])  
>>> cursor.rowcount  
1  
# 提交事务：  
>>> conn.commit()  
>>> cursor.close()  
# 运行查询：  
>>> cursor = conn.cursor()  
>>> cursor.exec('select * from user where id = %s', ('1', ))  
>>> values = cursor_fetchall()  
>>> values  
[(1', 'Michael')]  
# 关闭Cursor和Connection：  
>>> cursor.close()  
True  
>>> conn.close()
```

由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。

小结

- 执行 INSERT 等操作后要调用 commit() 提交事务；  
- MySQL 的 SQL 占位符是%s。

# 17.3 使用SQLAlchemy

数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个list表示多行，list的每一个元素是tuple，表示一行记录，比如，包含id和name的user表：

```txt
[ ('1', 'Michael'), ('2', 'Bob'), ('3', 'Adam') ]
```

Python 的 DB-API 返回的数据结构就是像上面这样表示的。

但是用 tuple 表示一行很难看出表的结构。如果把一个 tuple 用 class 实例来表示，就可以更容易地看出表的结构来：

```python
class User(object): def __init__(self, id, name): self.id = id self.name = name [
```

```python
User('1','Michael'),
User('2','Bob'),
User('3','Adam')
] 这就是传说中的 ORM 技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。是不是很简单？
但是由谁来做这个转换呢？所以 ORM 框架应运而生。
在 Python 中，最有名的 ORM 框架是 SQLAlchemy。我们来看看 SQLAlchemy 的用法。
首先通过 pip 安装 SQLAlchemy：
$ pip install sqlalchemy
然后，利用上次我们在 MySQL 的 test 数据库中创建的 user 表，用 SQLAlchemy 来试试：
第一步，导入 SQLAlchemy，并初始化 DBSession:
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
# 定义 User 对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
# 初始化数据库连接:
engine = create_engine('mysql=mysqlconnector://root:password@localhost:3306/test')
# 创建 DBSession 类型:
DBSession = sessionmaker(bind=engine)
以上代码完成 SQLAlchemy 的初始化和具体每个表的 class 定义。如果有多个表，就继续定义其他 class，例如 School:
class School(Base):
    __tablename__ = 'school'
    id = ...
    name = ...
create_engine()用来初始化数据库连接。SQLAlchemy 用一个字符串表示连接信息：
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
你只需要根据需要替换掉用户名、口令等信息即可。
下面，我们看看如何向数据库表中添加一行记录。
由于有了 ORM，我们向数据库表中添加一行记录，可以视为添加一个 User 对象：
# 创建 session 对象:
session = DBSession()
# 创建新User 对象:
new_user = User(id='5', name='Bob')
```

```python
添加到session:  
session.add(new_user)  
# 提交即保存到数据库：  
session.commit()  
# 关闭session:  
session.close()
```

可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：

```python
# 创建Session:  
session = DBSession()  
# 创建Query 查询，filter 是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行：  
user = session.query(User).filter(User.id=='5').one())  
# 打印类型和对象的name属性：  
print('type:', type(user))  
print('name:", user.name)  
# 关闭Session:  
session.close()
```

运行结果如下：

```yaml
type: <class __main__.User'>  
name: Bob
```

可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。

由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM 框架也可以提供两个对象之间的一对多、多对多等功能。

例如，如果一个User拥有多个Book，就可以定义一对多关系如下：

```python
class User(Base): __tablename__ = 'user' id = Column(String(20), primary_key=True) name = Column(String(20)) #一对多: books = relationship('Book')   
class Book(Base): __tablename__ = 'book' id = Column(String(20), primary_key=True) name = Column(String(20)) #“多”的一方的book表是通过外键关联到user表的: user_id = Column(String(20), ForeignKey('user.id'))
```

当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。

小结

ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。

正确使用 ORM 的前提是了解关系数据库的原理。

# 18 Web 开发

最早的软件都是运行在大型机上的，软件使用者通过“哑终端”登陆到大型机上去运行软件。后来随着PC机的兴起，软件开始主要运行在桌面上，而数据库这样的软件运行在服务器端，这种Client/Server模式简称CS架构。

随着互联网的兴起，人们发现，CS架构不适合Web，最大的原因是Web应用程序的修改和升级非常迅速，而CS架构需要每个客户端逐个升级桌面App，因此，Browser/Server模式开始流行，简称BS架构。

在 BS 架构下，客户端只需要浏览器，应用程序的逻辑和数据都存储在服务器端。浏览器只需要请求服务器，获取 Web 页面，并把 Web 页面展示给用户即可。

当然，Web页面也具有极强的交互性。由于Web页面是用HTML编写的，而HTML具备超强的表现力，并且，服务器端升级后，客户端无需任何部署就可以使用到新的版本，因此，BS架构迅速流行起来。

今天，除了重量级的软件如Office，Photoshop等，大部分软件都以Web形式提供。比如，新浪提供的新闻、博客、微博等服务，均是Web应用。

Web应用开发可以说是目前软件开发中最重要的部分。Web开发也经历了好几个阶段：

1. 静态Web页面：由文本编辑器直接编辑并生成静态的HTML页面，如果要修改Web页面的内容，就需要再次编辑HTML源文件，早期的互联网Web页面就是静态的；  
2. CGI：由于静态Web页面无法与用户交互，比如用户填写了一个注册表单，静态Web页面就无法处理。要处理用户发送的动态数据，出现了Common Gateway Interface，简称CGI，用C/C++编写。  
3. ASP/JSP/PHP: 由于Web应用特点是修改频繁，用C/C++这样的低级语言非常不适合Web开发，而脚本语言由于开发效率高，与HTML结合紧密，因此，迅速取代了CGI模式。ASP是微软推出的用VBScript脚本编程的Web开发技术，而JSP用Java来编写脚本，PHP本身则是开源的脚本语言。  
4. MVC：为了解决直接用脚本语言嵌入HTML导致的可维护性差的问题，Web应用也引入了Model-View-Controler的模式，来简化Web开发。ASP发展为ASP.Net，JSP和PHP也有一大堆MVC框架。

目前，Web开发技术仍在快速发展中，异步开发、新的MVVM前端技术层出不穷。

Python 的诞生历史比 Web 还要早，由于 Python 是一种解释型的脚本语言，开发效率高，所以非常适合用来做 Web 开发。

Python有上百种Web开发框架，有很多成熟的模板技术，选择Python开发Web应用，不但开发效率高，而且运行速度快。

本章我们会详细讨论PythonWeb开发技术。

# 18.1 HTTP协议简介

在Web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来。而浏览器和服务器之间的传输协议是HTTP，所以：

- HTML 是一种用来定义网页的文本，会 HTML，就可以编写网页；  
- HTTP 是在网络上传输 HTML 的协议，用于浏览器和服务器的通信。

在举例子之前，我们需要安装 Google 的 Chrome 浏览器。

为什么要使用 Chrome 浏览器而不是 IE 呢？因为 IE 实在是太慢了，并且，IE 对于开发和调试 Web 应用程序完全是一点用也没有。

我们需要在浏览器很方便地调试我们的Web应用，而Chrome提供了一套完整地调试工具，非常适合Web开发。

安装好 Chrome 浏览器后，打开 Chrome，在菜单中选择“视图”，“开发者”，“开发者工具”，就可以显示开发者工具：

Elements 显示网页的结构，Network 显示浏览器和服务器的通信。我们点 Network，确保第一个小红灯亮着，Chrome 就会记录所有浏览器和服务器之间的通信。

![](images/e4f2e7a23cd5dddaf994a2961c52c1c8752bcfe825ebea6ceee5d197e97879c3.jpg)

当我们在地址栏输入 www.sina.com.cn 时，浏览器将显示新浪的首页。在这个过程中，浏览器都干了哪些事情呢？通过 Network 的记录，我们就可以知道。在 Network 中，定位到第一条记录，点击，右侧将显示 Request Headers，点击右侧的 view source，我们就可以看到浏览器发给新浪服务器的请求：

![](images/2cf0633b7c434ab482e9a6cd77bb8a99bd6195dfe8dfe37df2a085c39c87a34c.jpg)

最主要的头两行分析如下，第一行：

GET / HTTP/1.1

GET表示一个读取请求，将从服务器获得网页数据，/表示URL的路径，URL总是以/开头，/就表示首页，最后的HTTP/1.1指示采用的HTTP协议版本是1.1。目前HTTP协议的版本就是1.1，但是大部分服务器也支持1.0版本，主要区别在于1.1版本允许多个HTTP请求复用一个TCP连接，以加快传输速度。

从第二行开始，每一行都类似于Xxx：abcdefg:

Host: www.sina.com.cn

表示请求的域名是 www.sina.com.cn。如果一台服务器有多个网站，服务器就需要通过 Host 来区分浏览器请求的是哪个网站。

继续往下找到Response Headers，点击view source，显示服务器返回的原始响应数据：

![](images/d21189b7118b42a3f005ddde552e1420f81db8962a8d8da0c6bb82ff0bbb1ad9.jpg)

HTTP响应分为Header和Body两部分（Body是可选项），我们在Network中看到的Header最重要的几行如下：

200 OK

200表示一个成功的响应，后面的OK是说明。失败的响应有404 Not Found：网页不存在，500 Internal Server Error：服务器内部出错，等等。

Content-Type: text/html

Content-Type 指示响应的内容，这里是 text/html 表示 HTML 网页。请注意，浏览器就是依靠 Content-Type 来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠 URL 来判断响应的内容，所以，即使 URL 是 http://example.com/abc.jpg，它也不一定就是图片。

HTTP响应的Body就是HTML源码，我们在菜单栏选择“视图”，“开发者”，“查看网页源码”就可以在浏览器中直接查看HTML源码：

![](images/9def1324d1558ac08c9ecb69f032077cae0e4073f1c391711898fe8cbc107644.jpg)

当浏览器读取到新浪首页的HTML源码后，它会解析HTML，显示页面，然后，根据HTML里面的各种链接，再发送HTTP请求给新浪服务器，拿到相应的图片、视频、Flash、JavaScript脚本、CSS等各种资源，最终显示出一个完整的页面。所以我们在Network下面能看到很多额外的HTTP请求。

# - HTTP 请求

跟踪了新浪的首页，我们来总结一下 HTTP 请求的流程：

步骤1：浏览器首先向服务器发送HTTP请求，请求包括：

方法：GET还是POST，GET仅请求资源，POST会附带用户数据；

路径：/full/url/path;

域名：由 Host 头指定：Host: www.sina.com.cn

以及其他相关的Header;

如果是POST，那么请求还包括一个Body，包含用户数据。

步骤2：服务器向浏览器返回HTTP响应，响应包括：

响应代码：200表示成功，  $3\times x$  表示重定向，  $4\times x$  表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；  
响应类型：由Content-Type指定；

以及其他相关的Header;

通常服务器的 HTTP 响应会携带内容，也就是有一个 Body，包含响应的内容，网页的 HTML 源码就在 Body 中。

步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。

Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，我们只需要在HTTP请求中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，一个HTTP请求只处理一个资源。

HTP协议同时具备极强的扩展性，虽然浏览器请求的是http://www.sina.com.cn/的首页，但是新浪在HTML中可以

链入其他服务器的资源，比如：

<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png>", 从而将请求压力分散到各个服务器上, 并且, 一个站点可以链接到其他站点, 无数个站点互相链接起来, 就形成了 World Wide Web, 简称 WWW。

# - HTTP 格式

每个 HTTP 请求和响应都遵循相同的格式，一个 HTTP 包含 Header 和 Body 两部分，其中 Body 是可选的。

HTTP协议是一种文本协议，所以，它的格式也非常简单。HTTP GET请求的格式：

```txt
GET /path HTTP/1.1  
Header1: Value1  
Header2: Value2  
Header3: Value3
```

每个Header一行一个，换行符是\r\n。

HTTP POST 请求的格式：

```txt
POST /path HTTP/1.1  
Header1: Value1  
Header2: Value2  
Header3: Value3
```

body data goes here...

当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

HTTP响应的格式：

```txt
200 OK  
Header1: Value1  
Header2: Value2  
Header3: Value3
```

body data goes here...

HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。请再次注意，Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。

当存在 Content-Encoding 时，Body 数据是被压缩的，最常见的压缩方式是 gzip，所以，看到 Content-Encoding: gzip 时，需要将 Body 数据先解压缩，才能得到真正的数据。压缩的目的在于减少 Body 的大小，加快网络传输。

# 18.2 HTML简介

网页就是 HTML？这么理解大概没错。因为网页中不但包含文字，还有图片、视频、Flash 小游戏，有复杂的排版、动画效果，所以，HTML 定义了一套语法规则，来告诉浏览器如何把一个丰富多彩的页面显示出来。

HTML长什么样？上次我们看了新浪首页的HTML源码，如果仔细数数，竟然有6000多行！

所以，学HTML，就不要指望从新浪入手了。我们来看看最简单的HTML长什么样：

```html
<html>
<head>
<title>Hello</title>
</head>
<body>
<h1>Hello, world!</h1>
</body>
</html>
```

可以用文本编辑器编写HTML，然后保存为hello.html，双击或者把文件拖到浏览器中，就可以看到效果：

![](images/f23c0e3600b23f26d0479c2491bc47dca4023f71ef33c3eb47f4d5651335e705.jpg)

HTML文档就是一系列的Tag组成，最外层的Tag是<html>。规范的HTML也包含<head>...</head>和<body>...</body>(注意不要和HTTP的Header、Body搞混了)，由于HTML是富文档模型，所以，还有一系列的Tag用来表示链接、图片、表格、表单等等。

·CSS简介

CSS是 Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现，比如，给标题元素 $\langle h1\rangle$ 加一个样式，变成48号字体，灰色，带阴影：

```html
<html>
<head>
<title>Hello</title>
<style>
h1 {
    color: #333333;
    font-size: 48px;
    text-shadow: 3px 3px 3px #666666;
}
</style>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
```

效果如下：

![](images/d9401573fd93670593583ebb127d1c550d8349062ab7499a746ead89cc3237dd.jpg)

- JavaScript 简介

JavaScript 虽然名称有个 Java，但它和 Java 真的一点关系没有。JavaScript 是为了让 HTML 具有交互性而作为脚本语言添加的，JavaScript 既可以内嵌到 HTML 中，也可以从外部链接到 HTML 中。如果我们希望当用户点击标题时把标题

变成红色，就必须通过JavaScript来实现：

```html
<html>
<head>
<title>Hello</title>
<style>
h1 {
    color: #333333;
    font-size: 48px;
    text-shadow: 3px 3px 3px #666666;
}
</style>
<script>
function change() {
    document.getElementsByTagName('h1')[0].style.color = "#ff0000";
}
</script>
</head>
<body>
<h1 onclick="change(){
    Hello, world! </h1>
</body>
</html>
```

点击标题后效果如下：

![](images/18d106fe4d2ffe7f558eac53b831e64b1d426353745299e64bfefcaae977ea0a.jpg)

# ·小结

如果要学习Web开发，首先要对HTML、CSS和JavaScript作一定的了解。HTML定义了页面的内容，CSS来控制页面元素的样式，而JavaScript负责页面的交互逻辑。

讲解 HTML、CSS 和 JavaScript 就可以写 3 本书，对于优秀的 Web 开发人员来说，精通 HTML、CSS 和 JavaScript 是必须的，这里推荐一个在线学习网站 w3schools:

```txt
http://www.w3schools.com/
```

以及一个对应的中文版本：

```txt
http://www.w3school.com.cn/
```

当我们用Python或者其他语言开发Web应用时，我们就是要在服务器端动态创建出HTML，这样，浏览器就会向不同的用户显示出不同的Web页面。

# 18.3 WSGI接口

了解了 HTTP 协议和 HTML 文档，我们其实就明白了一个 Web 应用的本质就是：

1. 浏览器发送一个 HTTP 请求；  
2. 服务器收到请求，生成一个HTML文档；  
3. 服务器把 HTML 文档作为 HTTP 响应的 Body 发送给浏览器；  
4. 浏览器收到 HTTP 响应，从 HTTP Body 取出 HTML 文档并显示。

所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lightpd等这些常见的静态服务器就是干这件事情的。

如果要动态生成 HTML，就需要把上述步骤自己来实现。不过，接受 HTTP 请求、解析 HTTP 请求、发送 HTTP 响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态 HTML 呢，就得花个把月去读 HTTP 规范。

正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是 WSGI: Web Server Gateway Interface。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”:

```python
def application(env, start_response):
    start_response('200 OK', ['Content-Type', 'text/html'])]
    return [b'<h1>Hello, web</h1>]
```

上面的 application()函数就是符合 WSGI 标准的一个 HTTP 处理函数，它接收两个参数：

- environ: 一个包含所有 HTTP 请求信息的 dict 对象;  
- start_response: 一个发送 HTTP 响应的函数。

在application()函数中，调用：

```bazel
start_response('200 OK', ['Content-Type', 'text/html'])
```

就发送了 HTTP 响应的 Header，注意 Header 只能发送一次，也就是只能调用一次 start_response()函数。start_response()函数接收两个参数，一个是 HTTP 响应码，一个是一组 list 表示的 HTTP Header，每个 Header 用一个包含两个 str 的 tuple 表示。

通常情况下，都应该把 Content-Type 头发送给浏览器。其他很多常用的 HTTP Header 也应该发送。

然后，函数的返回值 b'<h1>Hello, web!/h1>'将作为 HTTP 响应的 Body 发送给浏览器。

有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body。

整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了。

不过，等等，这个application()函数怎么调用？如果我们自己调用，两个参数envviron和start_response我们没法提供，返回的bytes也没法发给浏览器。

所以 application()函数必须由 WSGI 服务器来调用。有很多符合 WSGI 规范的服务器，我们可以挑选一个来用。但是现在，我们只想尽快测试一下我们编写的 application()函数真的可以把 HTML 输出到浏览器，所以，要赶紧找一个最简单的 WSGI 服务器，把我们的 Web 应用程序跑起来。

好消息是Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

# ·运行WSGI服务

我们先编写hello.py，实现Web应用程序的WSGI处理函数：

```python
hello.py   
def application(environ, start_response): start_response('200 OK'，['Content-Type'，'text/html']) return [b'<h1>Hello，web</h1>'']
```

然后，再编写一个server.py，负责启动WSGI服务器，加载application()函数：

```python
#server.py  
#从wsgiref模块导入：  
from wsgiref.simple_server import make_server  
#导入我们自己编写的application函数：  
from hello import application  
#创建一个服务器，IP地址为空，端口是8000，处理函数是application：httpd = make_server('', 8000, application)  
print('Serving HTTP on port 8000...')  
#开始监听HTTP请求：  
httpdserve_forever()
```

确保以上两个文件在同一个目录下，然后在命令行输入python server.py来启动WSGI服务器：

![](images/4cd2062d4b194574baa8e054c4640ed7a9196c86cde88eb4618e19fd47e1c002.jpg)

注意：如果8000端口已被其他程序占用，启动将失败，请修改成其他端口。

启动成功后，打开浏览器，输入http://localhost:8000/，就可以看到结果了：

![](images/3283ae31c1ce5613399b57561d86db21528031085e9c780bdc3bf1d5bef7b2cf.jpg)

在命令行可以看到wsgiref打印的log信息：

![](images/74019af223bcdaf43cc0018ee6776edfbe540e52b5c7cf349bbea095c81f78c4.jpg)

按Ctrl+C终止服务器。

如果你觉得这个Web应用太简单了，可以稍微改造一下，从environ里读取PATH_INFO，这样可以显示更加动态的内容：

```python
# hello.py   
def application(envon, start_response): start_response('200 OK', ['Content-Type', 'text/html']) body  $=$  <h1>Hello,  $\% s!$  </h1>'  $\%$  (envviron['PATH_INFO'][1:] or 'web') return [body.encode('utf-8'))
```

你可以在地址栏输入用户名作为URL的一部分，将返回Hello, xxx!：

![](images/382fe760cbc8214189dc26c6242f8d473a63026b3013a320a948cef620d1264f.jpg)

是不是有点Web App的感觉了？

# ·小结

无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。

# 18.4 使用Web框架

了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。

但是如何处理 HTTP 请求不是问题，问题是如何处理 100 个不同的 URL。

每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。

一个最简单的想法是从 environ 变量里取出 HTTP 请求的信息，然后逐个判断：

```python
def application(env, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method == 'GET' and path == '/':
        return handle_home(env, start_response)
    if method == 'POST' and path='/signin':
        return handle_signin(env, start_response)
    ...
```

只是这么写下去代码是肯定没法维护了。

代码这么写没法维护的原因是因为 WSGI 提供的接口虽然比 HTTP 接口高级了不少，但和 Web App 的处理逻辑比，还是比较低级，我们需要在 WSGI 接口之上能进一步抽象，让我们专注于用一个函数处理一个 URL，至于 URL 到函数的映射，就交给 Web 框架来做。

由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接选择一个比较流行的Web框架—Flask来使用。

用 Flask 编写 Web App 比 WSGI 接口简单（这不是废话么，要是比 WSGI 还复杂，用框架干嘛？），我们先用 pip 安装 Flask:

```txt
$ pip install flask
```

然后写一个app.py，处理3个URL，分别是：

- GET /：首页，返回 Home；

- GET /signin: 登录页，显示登录表单；  
- POST /signin: 处理登录表单，显示登录结果。

注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。

Flask 通过 Python 的装饰器在内部自动地把 URL 和函数给关联起来，所以，我们写出来的代码就像这样：

```python
from flask import Flask   
from flask import request   
app  $=$  Flask(_name_)   
@app-route('/',methods=['GET','POST'])   
def home(): return'<h1>Home</h1>'   
@app-route('//signin',methods=['GET'])   
def signin_form(): return'<form action="/signin" method="post"><p><input name  $\coloneqq$  "username></p><p><input name  $\coloneqq$  "password" type  $\coloneqq$  "password></p><p><button type  $\coloneqq$  "submit">Sign In</button></p></form>'   
@app-route('//signin', methods=['POST'])   
def signin(): #需要从request对象读取表单内容： if request.form['username']  $\coloneqq$  'admin' and request.form['password']  $\coloneqq$  'password': return'<h3>Hello,admin!</h3>' return'<h3>Bad username or password.</h3>'   
if_name  $\equiv$  'main': app.run()
```

运行 python app.py，Flask 自带的 Server 在端口 5000 上监听：

```shell
$ python app.py
* Running on http://127.0.0.1:5000/
```

打开浏览器，输入首页地址 http://localhost:5000/：

![](images/e27cb365ad77b4d463fe1154ed725188b38ccb364b0711b37edeb17a935146eb.jpg)

首页显示正确！

再在浏览器地址栏输入 http://localhost:5000/signin，会显示登录表单：

![](images/d1eb70c2a26c232e727e42e0fa984925a7b0a91f8bed1f654938026bb048240f.jpg)

实际的Web App应该拿到用户名和口令后，去数据库查询再比对，来判断用户是否能登录成功。

除了 Flask，常见的 Python Web 框架还有：

Django：全能型Web框架；  
- web.py: 一个小巧的Web框架;  
- Bottle: 和 Flask 类似的 Web 框架;  
- Tornado: Facebook 的开源异步 Web 框架。

当然了，因为开发Python的Web框架也不是什么难事，我们后面也会讲到开发Web框架的内容。

小结

有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。

在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。Flask通过request.form['name']来获取表单的内容。

# 18.5 使用模板

Web 框架把我们从 WSGI 中拯救出来了。现在，我们只需要不断地编写函数，带上 URL，就可以继续 Web App 的开发了。

但是，Web App不仅仅是处理逻辑，展示给用户的页面也非常重要。在函数中返回一个包含HTML的字符串，简单的页面还可以，但是，想想新浪首页的6000多行的HTML，你确信能在Python的字符串中正确地写出来么？反正我是做不到。

俗话说得好，不懂前端的Python工程师不是好的产品经理。有Web开发经验的同学都明白，Web App最复杂的部分就在HTML页面。HTML不仅要正确，还要通过CSS美化，再加上复杂的JavaScript脚本来实现各种交互和动画效果。总之，生成HTML页面的难度很大。

由于在Python代码里拼字符串是不现实的，所以，模板技术出现了。

使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：

这就是传说中的 MVC：Model-View-Controller，中文名“模型-视图-控制器”。

Python处理URL的函数就是C:Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；

包含变量{}name{}的模板就是V:View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。

MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。

![](images/3e9ff45000bda16058fcf33f09babd11e7fb67a8115ad6d5fe827a593a12b72f.jpg)

```yaml
{'name': 'Michael'}
```

只是因为Python支持关键字参数，很多Web框架允许传入关键字参数，然后，在框架内部组装出一个dict作为Model。现在，我们把上次直接输出字符串作为HTML的例子用高端大气上档次的MVC模式改写一下：

```python
from flask import Flask, request, render_template
app = Flask(_name_)
@app.route('/', methods=['GET', 'POST'])
```

Flask 通过 render_template()函数来实现模板的渲染。和 Web 框架类似，Python 的模板也有很多种。Flask 默认支持的模板是 jinja2，所以我们先直接安装 jinja2:

```txt
$ pip install jinja2
```

然后，开始编写jinja2模板：

```txt
- home.html
```

用来显示首页的模板：

```asp
<html>
<head>
<title>Home</title>
</head>
<body>
<h1 style="font-style:italic">Home</h1>
</body>
</html>
```

# -form.html

用来显示登录表单的模板：

```twig
<html>
<head>
<title>Please Sign In</title>
</head>
<body>
{% if message %}
<p style="color:red"><{ message }></p>
{%endif %}
<form action="/signin" method="post">
    <legend>Please sign in:</legend>
    <p><input name="username" placeholder="Username" value="{{ username }}></p>
    <p><input name="password" placeholder="Password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
</form>
</body>
</html>
```

# - signin-ok.html

登录成功的模板：

```txt
<html>
<head>
<title>Welcome, {{ username }}</title>
</head>
<body>
<p>Welcome, {{ username }}! </p>
</body>
</html>
```

登录失败的模板呢？我们在 form.html 中加了一点条件判断，把 form.html 重用为登录失败的模板。

最后，一定要把模板放到正确的 templates 目录下，templates 和 app.py 在同级目录下：

![](images/b0eec5a921ae58757be1f38c9f6b3f3fbbc3db7acc9b4200899fd37603882f06.jpg)

![](images/5260ea77c5fb4cb1999b107c4aefb6bcecd51b42e527012a690d3afd2b228bf0.jpg)

启动pythonapp.py，看看使用模板的页面效果：

通过 MVC，我们在 Python 代码中处理 M: Model 和 C: Controller，而 V: View 是通过模板处理的，这样，我们就成功地把 Python 代码和 HTML 代码最大限度地分离了。

使用模板的另一大好处是，模板改起来很方便，而且，改完保存后，刷新浏览器就能看到最新的效果，这对于调试 HTML、CSS 和 JavaScript 的前端工程师来说实在是太重要了。

![](images/6db4e0a30fa689c7fce91f23ac01286b22b29342480a24629fdd8787a7f9640f.jpg)

在Jinja2模板中，我们用{\name}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用  $\{\% \dots \% \}$  表示指令。

比如循环输出页码：

```txt
$\{\%$  for i in page_list  $\}$  <ahref  $= "$  /page/\{i}  $)\mathbf{\Phi}^{*} > \{\{\textbf{i}\} \} <   / a>$ $\{\%$  endfor  $\}$
```

如果 page_list 是一个 list: [1, 2, 3, 4, 5], 上面的模板将输出 5 个超链接。

除了Jinja2，常见的模板还有：

- Make: 用  $<\%$  ...  $\%\>$  和  $\{\mathbf{x}\mathbf{x}\mathbf{x}\}$  的一个模板;  
- Cheetah: 也是用 $< \%$  …  $9>$ 和 $\$ 1 \{x x x \}$ 的一个模板;  
Django: Django 是一站式框架，内置一个用  $\{\% \dots \% \}$  和  $\{\{xxx\}\}$  的模板。

小结

有了 MVC，我们就分离了 Python 代码和 HTML 代码。HTML 代码全部放到模板里，写起来更有效率。

# 19 异步IO

在IO编程一节中，我们已经知道，CPU的速度远远快于磁盘、网络等IO。在一个线程中，CPU执行代码的速度极快，然而，一旦遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作。这种情况称为同步IO。

在IO操作的过程中，当前线程被挂起，而其他需要CPU执行的代码就无法被当前线程执行了。

因为一个IO操作就阻塞了当前线程，导致其他代码无法执行，所以我们必须使用多线程或者多进程来并发执行代码，为多个用户服务。每个用户都会分配一个线程，如果遇到IO导致线程被挂起，其他用户的线程不受影响。

多线程和多进程的模型虽然解决了并发问题，但是系统不能无上限地增加线程。由于系统切换线程的开销也很大，所以，一旦线程数量过多，CPU的时间就花在线程切换上了，真正运行代码的时间就少了，结果导致性能严重下降。

由于我们要解决的问题是CPU高速执行能力和IO设备的龟速严重不匹配，多线程和多进程只是解决这一问题的一种方法。

另一种解决IO问题的方法是异步IO。当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。

可以想象如果按普通顺序写出的代码实际上是没法完成异步IO的：

```txt
do(Some_code()  
f = open('/path/to/file', 'r')  
r = f.read() # <= 线程停在此处等待 IO 操作结果  
# IO 操作完成后线程才能继续执行：  
do(Some_code(r)
```

所以，同步IO模型的代码是无法实现异步IO模型的。

异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：

```txt
loop  $=$  get_event_loop()   
while True: event  $\equiv$  loop.get_event() process_event(event)
```

消息模型其实早在应用在桌面应用程序中了。一个GUI程序的主线程就负责不停地读取消息并处理消息。所有的键盘、鼠标等消息都被发送到GUI程序的消息队列中，然后由GUI程序的主线程处理。

由于GUI线程处理键盘、鼠标等消息的速度非常快，所以用户感觉不到延迟。某些时候，GUI线程在一个消息处理的过程中遇到问题导致一次消息处理时间过长，此时，用户会感觉到整个GUI程序停止响应了，敲键盘、点鼠标都没有反应。这种情况说明在消息模型中，处理一个消息必须非常迅速，否则，主线程将无法及时处理消息队列中的其他消息，导致程序看上去停止响应。

消息模型是如何解决同步 IO 必须等待 IO 操作这一问题的呢？当遇到 IO 操作时，代码只负责发出 IO 请求，不等待 IO 结果，然后直接结束本轮消息处理，进入下一轮消息处理过程。当 IO 操作完成后，将收到一条“IO 完成”的消息，处理该消息时就可以直接获取 IO 操作结果。

在“发出IO请求”到收到“I0完成”的这段时间里，同步IO模型下，主线程只能挂起，但异步IO模型下，主线程并没有休息，而是在消息循环中继续处理其他消息。这样，在异步IO模型下，一个线程就可以同时处理多个IO请求，并且没有切换线程的操作。对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力。

# 19.1 协程

在学习异步IO模型前，我们先来了解协程。

协程，又称微线程，纤程。英文名 Coroutine。

协程的概念很早就提出来了，但直到最近几年才在某些语言（如 Lua）中得到广泛应用。

子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。

所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。

子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：

```python
def A(: print('1') print('2') print('3')   
def B(): print('x') print('y') print('z')
```

假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：

但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。

看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？

最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

Python对协程的支持是通过generator实现的。

在 generator 中，我们不但可以通过 for 循环来迭代，还可以不断调用 next() 函数获取由 yield 语句返回的下一个值。

但是 Python 的 yield 不但可以返回一个值，它还可以接收调用者发出的参数。

来看例子：

传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。

如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

```python
def consumer():  
    r = ''  
while True:  
    n = yield r  
    if not n:  
        return  
print(['CONSUMER] Consuming %s...' % n)  
r = '200 OK'
```

```python
def produce(c):
    c.send(None)
    n = 0
while n < 5:
    n = n + 1
print(['PRODUCER] Producing %s...' % n)
    r = c.send(n)
print(['PRODUCER] Consumer return: %s' % r)
c.close()
c = consumer()
produce(c)
```

执行结果：

```txt
[PRODUCER] Producing 1...  
[CONSUMER] Consuming 1...  
[PRODUCER] Consumer return: 200 OK  
[PRODUCER] Producing 2...  
[CONSUMER] Consuming 2...  
[PRODUCER] Consumer return: 200 OK  
[PRODUCER] Producing 3...  
[CONSUMER] Consuming 3...  
[PRODUCER] Consumer return: 200 OK  
[PRODUCER] Producing 4...  
[CONSUMER] Consuming 4...  
[PRODUCER] Consumer return: 200 OK  
[PRODUCER] Producing 5...  
[CONSUMER] Consuming 5...  
[PRODUCER] Consumer return: 200 OK
```

注意到consumer函数是一个generator，把一个consumer传入produce后：

1. 首先调用 c.send(None) 启动生成器;  
2. 然后，一旦生产了东西，通过 c.send(n) 切换到 consumer 执行；  
3. consumer 通过 yield 拿到消息，处理，又通过 yield 把结果传回；  
4. produce拿到consumer处理的结果，继续生产下一条消息；  
5. produce 决定不生产了，通过 c.close()关闭 consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。最后套用Donald Knuth的一句话总结协程的特点：

“子程序就是协程的一种特例。”

# 19.2 asyncio

async 是 Python 3.4 版本引入的标准库，直接内置了对异步 IO 的支持。

async 的编程模型就是一个消息循环。我们从 async 模块中直接获取一个 EventLoop 的引用，然后把需要执行的协程扔到 EventLoop 中执行，就实现了异步 IO。

用async实现Helloworld代码如下：

```txt
import asyncio
```

```python
@asynccoroutine   
def hello(): print("Hello world!") #异步调用async.sleep(1):  $r =$  yield fromasync.sleep(1) print("Hello again!")   
#获取EventLoop: loop  $=$  async.get_event_loop() #执行coroutine loop.run_untilcomplete(hello()) loop.close()
```

@async.coroutine 把一个 generator 标记为 coroutine 类型，然后，我们就把这个 coroutine 扔到 EventLoop 中执行。

hello()会首先打印出Hello world!,然后，yield from语法可以让我们方便地调用另一个generator。由于async.sleep()也是一个coroutine，所以线程不会等待async.sleep(),而是直接中断并执行下一个消息循环。当async.sleep()返回时，线程就可以从yield from拿到返回值（此处是None)，然后接着执行下一行语句。

把async.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

我们用 Task 封装两个 coroutine 试试:

```python
import threading   
import asyncio   
@asynccoroutine   
def hello(): print('Hello world!  $(\% s)$  % threading.currentThread()) yield from asyncio.sleep(1) print('Hello again!  $(\% s)$  % threading.currentThread())) loop  $=$  asyncio.get_event_loop() tasks  $=$  [hello(), hello()] loop.run_untilcomplete(asyncio.wait(taskss)) loop.close()
```

观察执行过程：

```txt
Hello world! (<_MainThread(MainThread, started 140735195337472)>)  
Hello world! (<_MainThread(MainThread, started 140735195337472)>)  
(暂停约1秒)  
Hello again! (<_MainThread(MainThread, started 140735195337472)>)  
Hello again! (<_MainThread(MainThread, started 140735195337472)>)
```

由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

如果把async.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。

我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

```typescript
import asyncio @async.coroutine def wget(host):
```

```prolog
print('wget %s...' % host)  
connect = asyncio.open_connection(host, 80)  
reader, writer = yield from connect  
header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host  
writer.write header.encode('utf-8'))  
yield from writer>drain()  
while True:  
    line = yield from reader.Readline()  
    if line == b'\r\n':  
        break  
    print('%s header > %s' % (host, linedecode('utf-8').rstrip()))  
# Ignore the body, close the socket  
writer.close()  
loop = asyncio.get_event_loop()  
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com'])  
loop.run_until_COMPLETE(asyncio.wait(task))  
loop.close()  
执行结果如下:  
wget www.sohu.com...  
wget www.sina.com.cn...  
wget www.163.com...  
(等待一段时间)  
(打印出 sohu 的 header)  
www.sohu.com header > HTTP/1.1 200 OK  
www.sohu.com header > Content-Type: text/html  
...  
(打印出 sina 的 header)  
www.sina.com.cn header > HTTP/1.1 200 OK  
www.sina.com.cn header > Date: Wed, 20 May 2015 04:56:33 GMT  
...  
(打印出 163 的 header)  
www.163.com header > HTTP/1.0 302 Moved Temporarily  
www.163.com header > Server: Cdn Cache Server V2.0
```

可见3个连接由一个线程通过coroutine并发完成。

小结

asyncio提供了完善的异步IO支持；

异步操作需要在coroutine中通过yield from完成；

多个coroutine可以封装成一组Task然后并发执行。

# 19.3 async/await

用async提供的@async.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

为了简化并更好地标识异步IO，从Python3.5开始引入了新的语法async和await，可以让coroutine的代码更简

洁易读。

请注意，async 和 await 是针对 coroutine 的新语法，要使用新的语法，只需要做两步简单的替换：

1. 把@asyncio.coroutine 替换为 async;  
2. 把 yield from 替换为 await。

让我们对比一下上一节的代码：

```txt
@async.coroutine   
def hello(): print("Hello world!") r = yield from asyncio.sleep(1) print("Hello again!")
```

用新语法重新编写如下：

```python
async def hello():  
    print("Hello world!")  
    r = await asyncio.sleep(1)  
    print("Hello again!")
```

小结

Python 从 3.5 版本开始为 asyncio 提供了 async 和 await 的新语法；

注意新语法只能用在Python3.5以及后续版本，如果使用3.4版本，则仍需使用上一节的方案。

练习

将上一节的异步获取sina、sohu和163的网站首页源码用新语法重写并运行。

# 19.4 aiohttp

async 可以实现单线程并发 IO 操作。如果仅用在客户端，发挥的威力不大。如果把 async 用在服务器端，例如 Web 服务器，由于 HTTP 连接就是 IO 操作，因此可以用单线程+coroutine 实现多用户的高并发支持。

async 实现了 TCP、UDP、SSL 等协议，aiohttp 则是基于 async 实现的 HTTP 框架。

我们先安装aiohttp:

```batch
pip install aiohttp
```

然后编写一个 HTTP 服务器，分别处理以下 URL：

- / - 首页返回 b'<h1>Index</h1>'；  
- /hello/{name} - 根据URL参数返回文本hello,%s!。

代码如下：

```python
import asyncio   
from aiohttp import web   
async def index(request): await asyncio.sleep(0.5) return web.Response(body  $\equiv$  b'<h1>Index</h1>'   
async def hello(request): await asyncio.sleep(0.5) text  $=$  <h1>hello, %s!</h1>' % request.match_info['name'] return web.Response(body  $\equiv$  text.encode('utf-8'))   
async def init(loop):
```

```python
app = web.Application(loop=loop)  
app=router.addROUTE('GET', '/', index)  
app=router.addROUTE('GET', '/hello/{name}', hello)  
srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)  
print('Server started at http://127.0.0.1:8000...')  
return svr  
loop = asyncio.get_event_loop()  
loop.run_until_COMPLETE(init(loop))  
loop.run_forever()
```

注意 aiohttp 的初始化函数 init() 也是一个 coroutine，loop.create_server() 则利用 asyncio 创建 TCP 服务。

# 20 实战

由于实战部分涉及的细节太多，复制粘贴成打印版意义不大，建议大家还是根据网上教程一步一步仔细做，遇到不懂的地方再返回来查阅打印版，这样效果也许会好很多。

本想加个封面，后来想想在查看pdf的时候，右下角出现的页码和阅读器上面的页数正好对应也许更方便一点，就没那么做。有什么错误的地方还望指正！！！

我们都是廖雪峰老师 python 教程的受益者，做这个打印版也花了很多时间，无偿分享给大家，希望大家也不要将其用于任何商业用途。

Cameocus.2016