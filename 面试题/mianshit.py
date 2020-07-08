# 1、一行代码实现1—100之和
"""
print(sum(range(1, 101)))

sum =0
i=1
while i <=100:
    sum=sum+i
    i+=1
print(sum)
"""
# 2、如何在一个函数内部修改全局变量
import datetime
import math
import os
import sys
from re import split
# import xlrd as xlrd
"""
使用global 修饰需求修改的变量   global test_xxx
"""
# 3、列出5个python标准库
"""
os：提供了不少与操作系统相关联的函数
sys:   通常用于命令行参数
re:   正则匹配
math: 数学运算
datetime:处理日期时间
"""
# 4、字典如何删除键和合并两个字典
"""
dict_a ={"a":1,"b":2,"c":"cccc"}
dict_b={"d":4,"e":5,"f":"你"}
print(dict_a["a"])
del dict_a["a"] #删除字典中的值
dict_b={"d":4,"e":5,"f":"你"}
dict_b.pop()
print(dict_a)
dict_a.update(dict_b) #合并字典
print(dict_a)
"""

# 5、谈下python的GIL
"""
GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。
所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。

多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大
"""
# 6、python实现列表去重的方法
"""
使用set集合去重，
goods = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子","雪纺衫", "裤子", "高跟鞋", "袜子","雪纺衫", "裤子", "高跟鞋", "袜子""雪纺衫", "裤子", "高跟鞋", "袜子"]
list(set(goods))

字典去重
goods = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子","雪纺衫", "裤子", "高跟鞋", "袜子","雪纺衫", "裤子", "高跟鞋", "袜子""雪纺衫", "裤子", "高跟鞋", "袜子"]
dict ={}.fromkeys(goods)
print(dict.keys())
"""
# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
"""
*args 用来将参数打包成tuple给函数体调用
**kwargs 打包关键字参数成dict给函数体调用
注意点：参数arg、*args、**kwargs三个参数的位置必须是一定的。必须是(arg,*args,**kwargs)这个顺序，否则程序会报错。
"""
# 8、python2和python3的range（100）的区别
"""
python2返回列表，python3返回迭代器，节约内存
迭代器（iterator）：
迭代器是一个对象。
是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前不会后退。
创建迭代器：字符串，列表或元组对象都可用于创建迭代器
迭代器有两个基本的方法：iter() 和 next()

"""


# def openExcel(path):
#     excel = xlrd.open_workbook(path)
#     sheet = excel.sheet_by_name()
#     sheet.nrows
#
#
# dict = {"a": 1, "b": 2, "v": 3}
# s = dict.items()
# 9、一句话解释什么样的语言能够用装饰器?
"""
函数可以作为参数传递的语言，可以使用装饰器
Python装饰器看起来类似Java中的注解
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
"""
# 10、python内建数据类型有哪些
"""
整型--int
布尔型--bool
字符串--str
列表--list
元组--tuple
字典--dict
"""
# 11、简述面向对象中__new__和__init__区别
"""
__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。
也就是，__new__在__init__之前被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
"""
# 12、简述with方法打开处理文件帮我我们做了什么？
"""
with open('./1.text','w',encoding='utf-8')as fp:
    fp.write('hello')
使用with帮我们实现了文件关闭
"""
#
# 13、表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
"""
map函数，map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
def cheng(x):
    return x**2
a=[1,2,3,4,5]
b=map(cheng,a)
c=[]
for i in b:
    if i>10:
        c.append(i)
print(c)
"""

# 14、python中生成随机整数、随机小数、0—1之间小数方法
"""
import random
s =random.randint(1,10)
s =random.uniform(1,9)
a =random.random()
"""
# 15、避免转义给字符串加哪个字母表示原始字符串？
"""
r"e:\ttest"
"""
#
16、 < div


class ="nam" > 中国 < / div > ，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的


"""

"""
#
# 17、python中断言方法举例
"""
assert xxx == xxx
"""
#
# 18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
"""
select distinct name from student
"""
#
# 19、10个Linux常用命令
"""
tail -f     grep    more   vim    netstat  cat   df rm -rf   mkdir  mv  cp   
"""
#
# 20、python2和python3区别？列举5个
"""
python3中只有range()
print()变成了函数
不相等操作符"<>"被 Python3 废弃，统一使用"!="
raw_input 函数被 Python3 废弃，统一使用 input 函数
long 整数类型被 Python3 废弃，统一使用 int

"""
#
# 21、列出python中可变数据类型和不可变数据类型，并简述原理
"""
可变数据类型：dict、list、set
可变类型（mutable）：变量进行append、+=等这种操作后 == 改变了变量的值，而不会新建一个对象，
变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，
相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象

不可变数据类型：tuple
不可变类型（immutable）：改变了变量的值 == 新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址）
"""
#
# 22、s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”
"""
s = "dajldjlajfdljfddd"
ss =list(set(s))
ss.sort()
"""
#
# 23、用lambda函数实现两个数相乘
"""
f = lambda x,y:x*y
print(f(5,6))
"""
#
# 24、字典根据键从小到大排序dict={“name”:”zs”,”age”:18,”city”:”深圳”,”tel”:”1362626627”}
"""
dic = {"name": "zs", 'age': 18, 'city': "深圳", 'tel': "1362626627"}
print(dic.items())
l = sorted(dic.items(), key=lambda i:i[0], reverse=False)
print(l)
"""
#
# 25、利用collections库的Counter方法统计字符串每个单词出现的次数”kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h”
"""
from collections import Counter
... a = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
... res = Counter(a)
... print(res)
"""
#
26、字符串a = “not 404
found
张三
99
深圳”，每个词中间是空格，用正则过滤掉英文和数字，最终输出”张三  深圳”
"""

"""

#
# 27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
filter函数作用：函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，
最后将返回 True 的元素放到新列表中
def s(n):
...     return n % 2 == 1
... a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
... tmplist=filter(s,a)
... print(list(tmplist))
[1, 3, 5, 7, 9]
"""

#
# 28、列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s =[]
for i in a:
    if i%2==1:
        s.append(i)
print(s)
a = [1,2,3,4,5,6,7,8,9,10]
b = [i for i in a if i%2 != 0]
print(b)
"""
#
29、正则re.complie作用
#
# 30、a=（1，）b=(1)，c=(“1”) 分别是什么类型的数据？
"""
a=（1，） :tuple
b=(1) :int
c=(“1”)  :str
"""
#
# 31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
"""
s =[1,5,7,9]
b=[2,2,6,8]
s.extend(b)
print(sorted(s))
"""
#
# 32、用python删除文件和用linux命令删除文件方法
"""
python: os.remove(file_name)
linux: rm file_name
"""
#
# 33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
"""
import datetime
print(datetime.datetime.today())
print(datetime.datetime.now())
"""
#
# 34、数据库优化查询方法
"""
外键、索引、联合查询、选择特定字段等等
"""
#
# 35、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
"""
allure
"""
#
# 36、写一段自定义异常代码
"""
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
try:
    raise MyError("你错了")
except MyError as e:
    print(e)
"""
#
#37、正则表达式匹配中，（.）和（.?）匹配区别？
"""
'.'是匹配除了'\n'之外的任意一个字符
'?'是匹配前一个字符1次或0次
"""
#
# 38、简述Django的orm
"""

"""
#
# 39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
"""
s =[[1,2],[3,4],[5,6]]
b=[]
for i in s:
    for j in i :
        b.append(j)
print(b)
"""
#
# 40、x=”abc”,y=”def”,z=[“d”,”e”,”f”],分别求出x.join(y)和x.join(z)返回的结果
"""
x = "123"
y = "def"
z = ["d", "e", "f"]
print(x.join(y))
print(x.join(z))

d123e123f
d123e123f
"""
#
# 41、举例说明异常模块中try except else finally的相关意义
"""
try...except...else 没有捕获到异常，执行else语句
try...except...finally 不管有没有捕获到异常，都执行finally语句
"""
#
# 42、python中交换两个数值
"""
a,b=b,a
"""
#
# 43、举例说明zip（）函数用法
"""
zip()函数在运算时，会以一个或多个序列(可迭代对象)作为参数，返回一个元组的列表，同时将这些序列中对应的元素配对
#当两个参数的长度不同时，zip会以最短序列长度为基准截取，获得元组。
a = [1,2]
b = [3,4]
res = [i for i in zip(a,b)]
print(res) # [[1,3],[2,4]]

a = (1,2)
b = (3,4)
res = [i for i in zip(a,b)]
print(res) # [(1,3),(2,4)]

a = "ab"
b = "xyz"
res = [i for i in zip(a,b)]
print(res) # [('a','x'),('b','y')]
"""
#
44、a=”张明 98分”，用re.sub，将98替换为100
"""

"""
#
# 45、写5条常用sql语句
"""
select * from table
inster into table （列明，列名）values(值1，值2)
update table set 列名=值1，列名=值2 where 列名=值3
delete from table where 列名=值
show databases
show tables
"""
#
# 46、a=”hello”和b=”你好”编码成bytes类型
"""
a.encode()
b.encode()
"""
#
# 47、[1,2,3]+[4,5,6]的结果是多少？
"""
[1,2,3,4,5,6]
"""
#
# 48、提高python运行效率的方法
"""
1、使用生成器，因为可以节约大量内存
2、循环代码优化，避免过多重复代码的执行
3、核心模块用Cython、PyPy等，提高效率
4、多进程、多线程、协程
5、多个if else条件判断，可以把最有可能发生的条件放在前面写，这样可以减少程序的判断次数，提高效率
"""
#
# 49、简述mysql和redis区别
"""
redis: 内存型非关系数据库，数据保存在内存中，速度快
mysql: 关系型数据库，数据保存在磁盘中，速度相对慢
"""
#
# 50、遇到bug如何处理
"""
1、细节上的错误，通过print()打印，能执行到print()说明一般上面的代码没什么问题，分段检测程序是否有问题，如果是js的话使用alert或console.log
2、如果涉及一些第三方框架的话，查官方文档或技术博客
3、对于bug的管理和归类总结
"""
#
# 51、1、正则匹配，匹配日期2018-03-20
# url=’https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462‘
#
# 52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
"""
list=[2,3,5,4,9,6]
for i in range(len(list)):
    if i+1<6:
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
print(list)
"""



#
# 53、写一个单列模式
"""
class DanLi():
    def dan(self):
        pass

danli=DanLi()
from DanLi.mydanli import danli
"""
#
# 54、保留两位小数
# 题目本身只有a=”%.03f”%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数）
#
# 55、求三个方法打印结果
"""

"""
#
# 56、列出常见的状态码和意义
"""
200 OK: 请求正常处理完毕
204 No Content: 请求成功处理，没有实体的主体返回
206 Partial Content: GET范围请求已成功处理
301 Moved Permanently: 永久重定向，资源已永久分配新URI
302 Found: 临时重定向，资源已临时分配新URI
303 See Other: 临时重定向，期望使用GET定向获取
304 Not Modified: 发送的附带条件请求未满足
307 Temporary Redirect: 临时重定向，POST不会变成GET
400 Bad Request: 请求报文语法错误或者参数错误
401 Unauthorized: 需要通过HTTP认证，或认证失败
403 Forbidden: 请求资源被拒绝
404 Not Found: 无法找到请求资源(服务器无理由拒绝)
500 Internal Server Error: 服务器故障或Web应用故障
503 Service Unavailable: 服务器超负载或停机维护
"""
#
# 57、分别从前端、后端、数据库阐述web项目的性能优化
"""
前端优化：
(1)减少http请求、例如制作精灵图
(2)html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差
后端优化：
(1)缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。
(2)异步方式，如果有耗时操作，可以采用异步，比如celery
(3)代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况
数据库优化：
(1)如有条件，数据可以存放于redis，读取速度快
(2)建立索引、外键等
"""
#
# 58、使用pop和del删除字典中的”name”字段，dic={“name”:”zs”,”age”:18}
"""
dic ={"name":"ddd","age":18}
dic.pop("name")

dic ={"name":"ddd","age":18}
del dic["name"]
"""
#
# 59、列出常见MYSQL数据存储引擎
"""
InnoDB
MyISAM
MEMORY
"""
#
# 60、计算代码运行结果，zip函数历史文章已经说了，得出[(“a”,1),(“b”,2)，(“c”,3),(“d”,4),(“e”,5)]
"""
m =["a","b","c","d","e"]
n=[1,2,3,4,5]
k=[]
for i in zip(m,n):
    k.append(i)
print(k)

m =["a","b","c","d","e"]
n=[1,2,3,4,5]
c=[i for i in zip(m,n)]
print(c)
"""
#
# 61、简述同源策略
"""
同源策略需要同时满足以下三点要求：
1、协议相同
2、域名相同
3、端口相同

ex:
http:www.test.com与https:www.test.com 协议不同
http:www.test.com与http:www.admin.com域名不同
http:www.test.com与http:www.test.com:8081 端口不同
只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”
"""
#
# 62、简述cookie和session的区别
"""
1、session在服务器端，cookie在客户端(浏览器)
2、session的运行依赖seesion id，而session id 是存在cookie中的，也就是说，如果浏览器禁用cookie，
同时session也会失效，存储session时，键与cookie中的sesson id相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
3、cookie安全性比session差
"""
#
# 63、简述多线程、多进程
"""
进程：
1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限

线程：
1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能够独立运行的基本单位，一个进程下的多个进程可以共享该进程的所有资源
2、如果IO操作密集，则可以多个线程运行，效率高，缺点是如果一个线程崩溃，就会造成进程崩溃

应用：
IO密集的用多线程，在用户输入sleep的时候，可以切换到其它线程执行，减少等待时间
CPU密集的用多进程，如果IO操作少，勇夺线程的话，因为线程共享	一个全局解释器锁，当前运行的线程会霸占DIL，其他线程没有DIL，
就不能充分利用多核CPU的优势
"""
#
# 64、简述any()和all()方法
"""
any(): 只要迭代器中有一个元素为真就为真
all(): 迭代器中所有的判断项返回都是真，结果才是真
python中为假的元素：0、空字符串、空列表、空元组、None、False
"""
#
# 65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
"""
IOError: 输入输出异常
AttributeError: 试图访问一个对象没有的属性
ImportError: 无法引入模块或包，基本是路径问题
IndentationError: 语法错误，代码没有正确的对齐
IndexError: 下标索引超出序列边界
KeyError: 试图访问你字典里不存在的键
SyntaxError: Python代码逻辑语法出错，不能执行
NameError: 使用一个还未赋予对象的变量
"""
#
# 66、python中copy和deepcopy区别
"""
1、当复制不可变数据类型时(数值、字符串、元组)
不管是copy还是deepcopy，都和赋值的情况一样，对象的id和原来的值一样，都指向同一块内存地址
2、当复制可变的数据类型时(列表、字典)
对于浅拷贝copy来说，分两种情况
	第一种情况，当复制的对象中无复杂的子对象时，原来值的改变并不会影响浅复制的值的改变，浅复制的值的改变也不会影响原来的值，
	浅复制的id和原来的id不同
	第二种情况，当复制的对象中有复杂的子对象时，改变原来值中的复杂子对象的值，会影响浅复制的值，原来的id和浅拷贝的id相同
对于深拷贝deepcopy来说，完全复制独立，包括内层列表和字典
"""
#
# 67、列出几种魔法方法并简要介绍用途
"""
__init__ 对象初始化的方法
__new__ 创建对象会执行的方法，单例模式会用到
"""
#
# 68、C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？
"""
得到一个列表
"""
#
# 69、请将[i for i in range(3)]改成生成器
"""
g = (i for i in range(3))
"""
#
# 70、a = “  hehheh  “,去除收尾空格
"""
a = " hehheh "
a.strip()
"""
#
# 71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
"""
list.sort()
sorted(list)
"""
#
# 72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
"""
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
ss=sorted(foo,key=lambda x:x)
print(ss)
"""
#
73、使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为
[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
"""

"""
#
# 74、列表嵌套字典的排序，分别根据年龄和姓名排序
"""
lambda中，字典取key
list=[{"name":"liu","age":19},{"name":"mu","age":20}]
a=sorted(list,key= lambda x:x["name"] ,reverse=True)#姓名 从大到小
b=sorted(list,key=lambda y:y["age"])#年龄从小打到
print(a)
print(b)
"""
#
# 75、列表嵌套元组，分别按字母和数字排序
"""
lambda中，元祖取索引
list = [("liu",19),("mu",20),("li",31),("haha",33)]
a =sorted(list, key=lambda x:x[0],reverse=True)
b=sorted(list,key=lambda y:y[1])
print(a)
print(b)
"""
#
# 76、列表嵌套列表排序，年龄数字相同怎么办？
"""
lambda 写两个条件，如果第一个相等，就用第二个排序
foo = [['zs', 19], ['li', 54],
        ['wa', 17], ['df', 23], ['as', 17]]
a = sorted(foo, key=lambda x:(x[1], x[0]))
print(a)
"""
#
# 77、根据键对字典排序（方法一，zip函数）
"""
dic = {"name": "zs", "sex": "man", "city": 'bj'}
b =zip(dic.keys(),dic.values())
c =sorted(b,key=lambda x:x[0])
print(c)
"""
#
# 78、根据键对字典排序（方法二,不用zip)
#
# 79、列表推导式、字典推导式、生成器
"""

"""
#
# 80、最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
"""
s = ['ab', 'sbc', 'a', 'sdfg']
a=sorted(s,key=lambda x:len(x))
print(a)
"""
#
# 81、举例说明SQL注入和解决办法
"""
"Select * from users where name='"+uName+"' and pwd='"+uPwd+"' " 
如用户在t_name中输入tom’ or 1=‘1 就可以进入系统了。
生成语句：
Select * from users where name = ‘tom’ or 1=‘1’ and pwd=‘123’
防止sql注入的方法有如下几点：
使用参数化过滤语句
在web应用程序的开发过程中所有阶段实施代码安全检察
使用存储过程
"""
#
# 82、s=”info:xiaoZhang 33 shandong”,用正则切分字符串输出[‘info’, ‘xiaoZhang’, ‘33’, ‘shandong’]
#
# 83、正则匹配以163.com结尾的邮箱
#
# 84、递归求和
"""
def digui(i):
    if i >= 1:
        res = i + digui(i - 1)
    else:
        res=0
    return res

print(digui(100))

sum =0
i =100
while i>0:
    sum+=i
    i-=1
print(sum)

"""
#
# 85、python字典和json字符串相互转化方法
"""
json.dumps() 将字典转化为字符串
json.loads() 将字符串转化为字典
"""
#
# 86、MyISAM 与 InnoDB 区别：
#
# 87、统计字符串中某字符出现次数
"""
str = "张三 李四 王五 张三 张三张三李四"
res = str.count("李四")
print(res)
"""
#
# 88、字符串转化大小写
"""
s="sdafasdfsdaSDFAF"
s.lower()
s.upper()
"""
#
# 89、用两种方法去空格
"""
s="hello adfas sdfsadf asdfsadf asdfasd "
d=s.replace(" ","")
print(d)
str = "hello world hello world"
res = str.replace(" ", "")
print(res)

str2 = "hello world hello world"
res2 = str2.split(" ")
r = "".join(res)
print(r)
"""
#
# 90、正则匹配不是以4和7结尾的手机号
#
# 91、简述python引用计数机制
"""

"""
#
# 92、int(“1.4”),int(1.4)输出结果？
"""
int("1.4")报错，因为"1.4"是str类型
int(1.4)输出是1 int是整数
"""
#
# 93、列举3条以上PEP8编码规范
"""
变量命名规则：
　　不能与关键字重名，必须以数字字母下划线组成，且不能以数字开头
3.缩进
　　每一级使用四个空格缩进，要么都是用空格，要么都是用tab键，不要空格和tab键混用
4.每行最大字符限时为79个，除了长导包语句，和url地址
5.多个变量，之间使用逗号分隔，逗号与前变量相邻，与后变量之间空一格。
6.# TODO
"""
#
# 94、正则表达式匹配第一个URL
#
# 95、正则匹配中文
#
# 96、简述乐观锁和悲观锁
"""
悲观锁，就是很悲观，每次去拿数据的时候都认为别人会修改，所以每一次在拿数据的时候都会上锁，这样别人想拿这个数据就会block直到它拿到锁。
    传统的关系型数据库里面就用到了很多这种锁机制，比如行锁、表锁、读锁、写锁等，都是在做操作之前先上锁。
乐观锁，就是很乐观，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，
    可以使用版本号等机制，乐观锁适合于多读的应用类型，这样可以提高吞吐量
"""
#
# 97、r、r+、rb、rb+文件打开模式区别
"""
r: 以只读方式打开文件。文件的指针将放在文件的开头。这是默认模式。
w: 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果文件不存在，创建新文件。
a: 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果文件不存在，创建新的文件进行写入。	
rb: 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
wb: 以二进制格式打开一个文件只用于写入。如果文件已存在则将其覆盖。如果文件不存在，创建新文件。
ab: 以二进制格式打开一个文件用于追加。如果文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容会被写入到已有内容之后。如果文件不存在，创建新文件进行写入。
r+: 打开一个文件用于读写。文件指针将会放在文件开头。
w+: 打开一个文件用于读写。如果文件已存在则将其覆盖。如果文件不存在，创建新文件。
a+: 打开一个文件用于读写。如果文件已存在，文件指针将会放在文件结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
rb+: 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
wb+: 以二进制格式打开一个文件用于读写。如果文件已存在则将其覆盖。如果文件不存在，创建新文件。
ab+: 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""
#
# 98、Linux命令重定向 > 和 >>
"""
linux允许将命令执行结果，重定向到一个文件
将本应显示在终端上的内容，输出/追加到指定文件中
>表示输出，会覆盖文件原来的内容
>>表示追加，会将内容追加到已有文件的末尾
用法示例：
	将 echo 输出的信息保存到 1.txt 里：echo Hello Python > 1.txt
	将 tree 输出的信息追加到 1.txt 文件的末尾：tree >> 1.txt
"""
#
# 99、正则表达式匹配出 <html><h1>www.itcast.cn</h1></html>
#
# 100、python传参数是传值还是传址？
"""
python中函数参数是引用传递(注意不是值传递)。对于不可变类型(数值型、字符串、元组)，因变量不能修改，所以运算不会影响到变量自身；
而对于可变类型(列表、字典)来说，函数体运算可能会更改传入的参数变量。

def selfAdd(a):
    a += a

x = 1 # 不可变
selfAdd(x)
print(x)
l = [1,2] # 可变
selfAdd(l)
print(l)
"""
#
#
# 101、求两个列表的交集、差集、并集
"""
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
a1 = set(a)
b1 = set(b)
c = list(a1 & b1)  # 交集
print(c)
c = list(a1 - b1)  # 差集
print(c)
c = list(a1 | b1)  # 并集
print(c)
"""
#
# 102、生成0-100的随机数
"""
import random

s=random.random()
print(s)
res1 = 100*random.random()
res2 = random.choice(range(0,101))
res3 = random.randint(0,100)
print(res1, res2, res3)
"""
#
# 103、lambda匿名函数好处
"""
精简代码，lambda省去了定义函数
"""
#
# 104、常见的网络传输协议
"""
tcp/udp/ftp/http/smtp
"""
#
# 105、单引号、双引号、三引号用法
"""
1、单引号和双引号没有什么区别，不过单引号不用按shift键，打字稍微快一点。表示字符串的时候，单引号里面可以用双引号，而不用转义字符，反之亦然。
2、但是如果直接用单引号括住单引号，则需要转义
3、三引号可以直接书写多行，通常用于大段，大篇幅的字符串
"""
#
# 106、python垃圾回收机制
"""
python垃圾回收主要以引用计数为主，标记-清除和分代回收为辅的机制
"""
#
# 107、HTTP请求中get和post区别
"""
1、GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，我们是无法直接看到的
2、少量的数据提交用GET，大量的数据提交用POST。GET提交的数据大小的限制，一般不超过1024个字节，而这种说法不完全正确，
HTTP协议并没有设定URL字节长度的上限，而浏览器做了些处理，所有长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，
一般来说是没有设置限制的，但是实际上浏览器也有默认值。
3、GET请求的数据参数是直接显示在URL中的，可以直接看到的，POST请求的数据参数放在请求头中，所以安全度比GET高一点，但是两者都是不安全的，
数据参数都是可以被提取出来的。在实际中，涉及登录操作的时候，尽量使用HTTPS请求，安全性更好。
"""
#
# 108、python中读取Excel文件的方法
"""
import pandas as pd # 应用数据分析库pandas
df = pd.read_excel("1.xlsx")
print(df)
"""
#
# 109、简述多线程、多进程
"""
进程：
1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制
线程：
1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
2、如果IO操作密集，则可以用多进程，运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃
应用：
IO密集的用多线程，在用户输入，sleep的时候，可以切换到其它线程执行，减少等待时间
CPU密集的用多进程，因为如果IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，其它线程没有GIL，
就不能充分利用多核CPU的优势
"""
#
# 110、python正则中search和match

# 华为编程题：
# 写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
"""
str1 = input().lower()
str2 = input().lower()
print(str1.count(str2))
"""
# 明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
# 对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。
# 然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。
# 请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。
"""
while True:
    try:
        a = int(input())
        res = set()
        for i in range(a):
            res.add(int(input()))
        for i in sorted(res):
            print(i)
    except:
        break
"""


# str1 = input()
# str2 = input()
#
#
# def string_out(str):
#     if len(str) <= 8:
#         print(str + "0" * (8 - len(str)))
#     else:
#         while len(str) > 8:
#             print(str[:8])
#             str = str[8:]
#         print(str + "0" * (8 - len(str)))
#
# string_out(str1)
# string_out(str2)

        #continue  # 上面的条件都不满足就跳过，进行下一次循环

# leetcode
# 1、给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final_len=[]
        for i in range(len(s)):
            data = s[i]
            for j in range(i+1,len(s)):
                if s[j] not in data:
                    data = data+ s[j]
                else:
                    break
            final_len.append(len(data))
        if final_len ==[]:
            if s =='':
                final_len.append(0)
            else:
                final_len.append(1)
        return max(final_len)

# 2、给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums)<2:
            return print("无法计算")

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]



