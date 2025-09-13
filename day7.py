#继昨天的练习
#素数的判断
a=100
flag = False
for i in range(2,a):
    if a%i==0:
        flag=True
        break
if flag:
    print(f"{a}不是素数")
else:
    print(f"{a}是素数")

#输出100以内的素数

for num in range(2,101):
    flag = False
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
    if not flag:
        print(num,end=" ")

    
# 求阶乘
# 非递归
n=5
num=1
for i in range(1,n+1):
    num=num*i
print(f"{n}的阶乘是{num}")
# 递归
def jiecheng(n):
    if n ==1:
        return 1
    else:
        return n*jiecheng(n-1)
print(f"{n}的阶乘是{jiecheng(n)}")
jiecheng(5)


# 求圆的周长
def zhong_chang(r):
    pi = 3.14
    print(f"半径为{r}的圆的周长是{2*pi*r}")
    return 2*pi*r
zhong_chang(5)

# 求圆的面积
def mian_ji(r):
    pi = 3.14
    print(f"半径为{r}的圆的面积是{pi*r*r}")
    return pi*r*r
mian_ji(5)

#求直角三角形斜边长
def xie_bian(a,b):
    
    c = (a**2 + b**2)**0.5
    print(f"直角三角形的斜边长是{c}")

xie_bian(3,4)
xie_bian(5,12)

# 比较三个数的大小
#简单繁琐版
num=input("请输入三个不相同的数，用逗号隔开")
a,b,c = num.split(",")
if a>b:
    if a>c:
        print(f"{a}最大")
        if b>c:
            print(f"{b}第二大")
            print(f"{c}最小")
        else:
            print(f"{c}第二大")
            print(f"{b}最小")
    else:
        print(f"{c}最大")
        print(f"{a}第二大")
        print(f"{b}最小")
else:
    if b>c:
        print(f"{b}最大")
        if a>c:
            print(f"{a}第二大")
            print(f"{c}最小")
        else:
            print(f"{c}第二大")
            print(f"{a}最小")
    else:
        print(f"{c}最大")
        print(f"{b}第二大")
        print(f"{a}最小")

#简洁版
def compare_num(a,b,c,):
    if a>=b and a>=c:
        print(f"{a}最大")
        if b>=c:
            print(f"{b}第二大")
            print(f"{c}最小")
        else:
            print(f"{c}第二大")
            print(f"{b}最小")
    elif b>=a and b>=c:
        print(f"{b}最大")
        if a>=c:
            print(f"{a}第二大")
            print(f"{c}最小")
        else:
            print(f"{c}第二大")
            print(f"{a}最小")
    else:
        print(f"{c}最大")
        if a>=b:
            print(f"{a}第二大")
            print(f"{b}最小")
        else:
            print(f"{b}第二大")
            print(f"{a}最小")   

compare_num(3,5,2)

#将三个数字从小到大排列（会使用sorted函数）
def sort_num(a,b,c):
    list1 = [a,b,c]
    list2 = sorted(list1)
    print(f"从小到大排列是{list2}")

sort_num(3,5,2)

    










    