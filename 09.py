# 切片

print(f'\n{"*" * 20}')
# 正向切片
cust_str = 'hello world'
# 使用正索引
print(f'{cust_str[:]}')     # hello world
print(f'{cust_str[0:5]}')   # hello
print(f'{cust_str[6:]}')    # world
print(f'{cust_str[6:11]}')  # world
print(f'{cust_str[6:99]}')  # world
# 使用负索引，使用负索引的时候，结束位置如果设定，则总会丢失一个，最好不设定
print(f'{cust_str[-11:]}')  # hello world
print(f'{cust_str[-11:-6]}')    # hello
print(f'{cust_str[-5:]}')    # world
# 使用步长
cust_str = '0123456789'
print(f'{cust_str[::2]}')    # 02468
print(f'{cust_str[1::]}')

print(f'\n{"*" * 20}')
# 负向切片
cust_str = '0123456789'
print(f'{cust_str[::-1]}')  # 9876543210
print(f'{cust_str[::-2]}')  # 97531


print(f'{"-" * 5}') # -----