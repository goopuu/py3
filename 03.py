# 数据类型基础

# 使用 id() 获取内存地址，type() 获取数据类型
print('\n1--------------')
print(hex(id(100)))         # 0x9526a8
print(type('hello world'))  # <class 'str'>

# 不可变类型，可以计算 哈希值


# 可变类型，不可以计算 哈希值
# 从这个示例中可以看到，不可变类型：整数，当修改操作时，其实并不是真的修改，而是删除原来的数据后，创建了新的数据，因为内存地址都发生变化了
print('\n2--------------')
cust_num = 100
print(hex(id(cust_num)))         # 0x9526a8
num = 100100
print(hex(id(cust_num)))         # 0x723a5211bd90
# 不可变类型，可以计算 哈希值
csut_str = 'hello world'
print(hash(csut_str))            # 5008393734156075680

print('\n3--------------')
# 可变类型，可以修改数据，可以看到，即使修改了列表的值，但是它的内存地址没有任何变化
cust_list = ['a', 2, 3]
print(hex(id(cust_list)))        # 0x7c58303ac9c0
cust_list[0] = 1
print(hex(id(cust_list)))        # 0x7c58303ac9c0

print('\n4--------------')
# print(hash(cust_list))           # 报错