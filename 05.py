# 浮点型

# 科学计数法

# 基于浮点型的计算，有精度问题
print('\n2-------------')
print(0.1 + 0.2) # 0.30000000000000004

# 特殊的浮点型
print('\n3--------------')
print(float('nan'), type(float('nan'))) # nan <class 'float'>
print(float('inf'), type(float('inf'))) # inf <class 'float'>
print(float('-inf'), type(float('-inf'))) # -inf <class 'float'>

# 转换为浮点数
print('\n4--------------')
cust_num = 100
cust_float = float(cust_num)
print(cust_float, type(cust_float)) # 100.0 <class 'float'>