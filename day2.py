# 打印乘法口诀表，使用while循环
i =0
while i < 10:
    j = 0
    while j <= i:
        print(f"{j}*{i}={i*j}", end="\t")
        j += 1
    i += 1   
    print()

# 打印乘法口诀表，使用for循环
i=0
for i in range (10):
    j = 0
    for j in range (i+1):
        print(f"{j}*{i}={i*j}", end="\t")
    print()
    i += 1

    
# 循环综合练习：发工资
money = 10000

person = 1
print(f"今天是发工资的日子，公司有20个员工,现在账户余额{money}元")
for person in range(1,21):
    import random
    num = random.randint(1,10)

    if num < 5:
       print(f"员工{person},绩效分小于5,没有工资")
       print("当前账户还剩余",money,"元")
    else:
       print(f"员工{person},绩效分大于等于5,发工资1000元")
       money -= 1000
       print("当前账户还剩余",money,"元")
    

    if money < 1000:

        print("账户余额不足，停止发工资")
        break


# 循环综合练习：发工资中使用continue和break
money = 10000
person = 1


print(f"今天是发工资的日子，公司有20个员工,现在账户余额{money}元") 
for person in range(0,21):
    import random
    num = random.randint(1,10)
    
    if num < 5:
         print(f"员工{person},绩效分小于5,没有工资,继续下一个员工")
         continue
    
    if money < 1000:
            print("账户余额不足，停止发工资")
            break
    else:
         money -= 1000
         print(f"员工{person},满足条件,发工资1000元")
         print("当前账户还剩余",money,"元")
         

# ATM机取款练习 


money = 50000000
print("欢迎使用ATM取款机")
name = input("请输入您的姓名：")
i = True
while i:
  if  name == "小帅":
    print(f"尊敬的{name}，您好！")
    print("您可以查询余额，取款，存款")
    action = input("请输入您要办理的业务（查询余额，取款，存款）：")
    def query():
        print(f"您的账户余额为{money}元")
    def withdraw():
        global money
        amount = int(input("请输入取款金额："))
        if amount > money:  
            print("余额不足，无法取款")
        else:
            money -= amount
            print(f"取款成功，当前余额为{money}元")
    def deposit():
        global money
        amount = int(input("请输入存款金额："))
        money += amount
        print(f"存款成功，当前余额为{money}元")
    if action == "查询余额":
        query()
        
    elif action == "取款":  
        withdraw()
        
    elif action == "存款":
        deposit()  
        
    elif action == "退出":
        print("感谢使用ATM取款机，欢迎下次光临！")
        break
    else:
        print("输入有误")
        break
  else:
    print("用户名错误，请重新输入")

    i = False
    
        
    

        






    
    




