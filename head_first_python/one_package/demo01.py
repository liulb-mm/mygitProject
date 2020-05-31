import datetime
import sys
import os
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
new_plist=''.join(plist[1:3])
new_plist=new_plist+''.join([plist[5],plist[4],plist[7],plist[6]])
print(new_plist)

