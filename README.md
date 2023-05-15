# Python

快速巩固要点，并进行针对性面试复习而开仓。

*born 2023.05.15*

---

### 数字、字符串、列表

#### 运算符:`+ - * / **`

特别地,

1. `_`:下划线，记录上一次的输出结果

2. `未赋值`:未定义会报错

#### 字符串

- 单行:`'',""`

- 多行:`""" """`

特别地,

1. `+`:合并字符串

2. `*`:重复字符串

支持索引访问,`string_list = "asbs",string_list[0] = "a"` 

索引可以为负数,从末尾进行访问

支持切片访问,`string_list[开始下标:结束下标]`

`len(字符串) 返回字符串长度`

#### 列表

`list_abb = [1,2,3,4]`

支持切片、索引访问、合并

- `list_abb[:2] = [1,2]`

- `list_abb[0] = [1]`

- `list_abb[0] + list_abb[1] = [1,2]`

支持`len() 返回长度,append() 末尾添加元素`

#### 案例-斐波那契数列

```python
a,b = 0,1;
while (a<100):
    print(a,end=",");
    a,b = b,a+b;
```

---

### 控制流程

#### if语句

```python
x = int(input("Enter a number : "));
if (x<0):
    x = 0;
    print("The min number is zero");
elif (x == 0):
    print("the number is : ",x);
elif (x == 1):
    print("the number is : ",x);
else:
    print("the number is bigger than 1");
```

#### for语句

```python
words = ['cat', 'window', 'defenestrate'];
for w in words:
    print(w, len(w));
```

#### range函数

遍历数字序列

```python
for i in range(5):
    print(i)

0
1
2
3
4


list(range(0, 10, 3))
[0, 3, 6, 9]
```

#### 循环中的 `break`、`continue` 语句及 `else` 子句

略

### pass语句

不执行任何操作

#### match语句

类似于`switch语句`

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet" 


class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

#### 定义函数

```python
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
```

**重要警告：** 默认值只计算一次。

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3)) 

[1]
[1,2]
[1,2,3]
```

---

## 数据结构

列表常用方法

1. list.append(*x*)

在列表末尾添加一个元素，相当于 `a[len(a):] = [x]` 。

2. list.extend(*iterable*)

用可迭代对象的元素扩展列表。字符串合并`+` 。

3. list.insert(*i*, *x*)

在指定位置插入元素。第一个参数是插入元素的索引，因此，`a.insert(0, x)` 在列表开头插入元素， `a.insert(len(a), x)` 等同于 `a.append(x)` 。

4. list.remove(*x*)

从列表中删除第一个值为 *x* 的元素。未找到指定元素时，触发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError "ValueError") 异常。

5. list.pop([*i*])

删除列表中指定位置的元素，并返回被删除的元素。未指定位置时，`a.pop()` 删除并返回列表的最后一个元素。（方法签名中 *i* 两边的方括号表示该参数是可选的，不是要求输入方括号。这种表示法常见于 Python 参考库）。

6. list.clear()

删除列表里的所有元素，相当于 `del a[:]` 。

7. list.index(*x*[, *start*[, *end*]])

返回列表中第一个值为 *x* 的元素的零基索引。未找到指定元素时，触发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError "ValueError") 异常。

可选参数 *start* 和 *end* 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 *start* 参数。

8. list.count(*x*)

返回列表中元素 *x* 出现的次数。

9. list.sort(***, *key=None*, *reverse=False*)

就地排序列表中的元素（要了解自定义排序参数，详见 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted "sorted")）。

10. list.reverse()

翻转列表中的元素。

11. list.copy()

返回列表的浅拷贝。相当于 `a[:]` 。

#### del语句

```python
a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
[1, 66.25, 333, 333, 1234.5]

del a[2:4]
[1, 66.25, 1234.5]

del a[:]    #等价于 del a
[]
```

#### 元组与序列

```python
t = 12345, 54321, 'hello!'
t[0]
12345
t
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
([1, 2, 3], [3, 2, 1])
```

#### 集合

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # fast membership testing
True
'crabgrass' in basket
False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

#### 字典

```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
4098
del tel['sape']
tel['irv'] = 4127
tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
['jack', 'guido', 'irv']
sorted(tel)
['guido', 'irv', 'jack']
'guido' in tel
True
'jack' not in tel
False 


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098} 


dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

---

## 模块

模块是包含 Python 定义和语句的文件

```python
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

#### 包

包是一种用“点式模块名”构造 Python 模块命名空间的方法。

---

## 输入与输出

#### 使用 `json`保存结构化数据

```python
import json
x = [1, 'simple', 'list']
json.dumps(x)
'[1, "simple", "list"]'
```

> 备注:
> 
> JSON文件必须以UTF-8编码。当打开JSON文件作为一个 `text file`用于读写时，使用 `encoding="utf-8"` 。

---

## 语法错误与异常

#### 语法错误

句法错误又称解析错误

#### 异常

即使语句或表达式使用了正确的语法，执行时仍可能触发错误。执行时检测到的错误称为 *异常*，异常不一定导致严重的后果

---

## 类

#### 概念

- 类把数据与功能绑定在一起。

- 创建新类就是创建新的对象 **类型**，从而创建该类型的新 **实例** 。

- 类实例支持维持自身状态的属性，还支持（由类定义的）修改自身状态的方法

#### 名称和对象

对象之间相互独立，多个名称（在多个作用域内）可以绑定到同一个对象

#### 定义方法

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

> 常见内容总结完毕
> 
> 记录于 2022.05.15
> 
> 接下来进行算法训练
