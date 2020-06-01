import datetime
import os
import sys
import time

# 查看环境变量

print(os.environ)
print(os.getenv('HOME'))

# sys查看解释器运行的系统
print(sys.platform + sys.version)

# 查看日期&时间
print(datetime.date.today())  # 查看今日日期
print(datetime.date.today().year)  # 访问today具体属性
print(time.strftime("%H:%M:%S"))

# for循环的使用
for i in range(5):
    print(("你好啊" + str(i)))

# test打印word中的不重复元音
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
# word =input("请输入一个英文单词")
out = []
for i in word:
    if i in vowels:
        if i not in out:
            out.append(i)
for s in out:
    print(s)

print("-----------------第二个练习-------------------------------")

# on tap
# phrase = "Dont't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)
# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.pop(3)
# plist.remove("t")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
# print(("dddddd"))
# print(plist)
# new_plist = ''.join(plist)
# print(new_plist)


# on tap
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
new_plist = ''.join(plist[1:3])
new_plist = new_plist + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(new_plist)

# 字典
dict = {'a': 1, 'b': '可以啊', '姓名': '练习册', '可以': 33}
# 遍历字典
# for k in dict:
#     print(k,dict[k])
# 按照升序顺序遍历
for k in sorted(dict):
    print(k, dict[k])
# 常用遍历字典的方法，dict.items()
for k, v in dict.items():
    print(k, v)

fruits = {}
fruits["apple"] = 2
if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1
print(fruits)

for k, v in fruits.items():
    print(k, v)

# 集合set，集合的合并用union,sorted是对集合进行升序排序 >并集
set_1 = {'a', 'e', 'i', 'o', 'u'}
set_2 = {'a', 'b', 'c', 'd', 'e'}
set_all = sorted(set_1.union(set_2))
print(set_all)
word = "hahahahnihaoha"
set_all = set_1.union(set(word))
print(set_all)
# 使用difference查看不是共有元素 >差集
set_diff = set_1.difference(set_2)
print(set_diff)

# 使用intersection查询共同对象 >交集
set_same = set_1.intersection(set_2)
print(set_same)


# 告诉传入参数需要哥字符串类型，返回字符串类型
def zhujie(word: str) -> str:
    return word


zhujie("你好啊")

#取两个字符串的交集，返回一个集合类型，设置leetter的默认值为'aeiou'
def search(phrase: str, leetter: str='aeiou') -> set:
    return set(leetter).intersection(set(phrase))

