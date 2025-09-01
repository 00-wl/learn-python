# 遍历的学习练习
my_list = ["张三", "李四", "王五"]
index =0
while index < len (my_list):
    element = my_list[index]
    print (f"列表元素：{element}")

    index += 1

print("----分割线----")

for element in my_list:
    print(f"列表元素：{element}")



print("-------------------------------")
# 元组tuple的遍历
my_tuple = ("张三", "李四", "王五")
index =0
while index <len(my_tuple):
    element = my_tuple[index]
    print(f"元组元素：{element}")
    index += 1

print("----分割线----")
for element in my_tuple:
    print(f"元组元素：{element}")

print("-------------------------------")


# 字符串内的一些语法
my_str = "hello world "

# relpace 替换
new_my_str= my_str.replace("world","python")
print(new_my_str)

# split 分割(会生成一个列表)
my_str_list = my_str.split("l")
print(my_str_list)

# strip
my_str2 = " 21 hello world 12 "
new_my_str2 = my_str2.strip("12 ")
print(f"去除前后空格前：'{my_str2}'")
print(f"去除前后空格后：'{new_my_str2}'")

 # 遍历
for char in my_str:
    print(f"字符串元素：{char}")

print("-------------------------------")

