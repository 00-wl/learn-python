###文件的读取练习
f = open ('D:\learn.py',"r",encoding='utf-8')



#for line in f:
   # print(f"每一行内容是{line}")



#小练习
number = f.read().count('we')
print(f"we出现的次数是{number}")
f.close()

#小练习：找出一百以内的偶数
i=0
for i in range(1,101):
    if i%2==0:
        print(i)

#小练习：找出一百以内的奇数
i=0
for i in range(1,101):
    if i%2!=0:
        print(i)

#小练习：判断一个数是不是素数



