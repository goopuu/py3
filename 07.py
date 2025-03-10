# 字符串

# 转义字符
print(f'\n1-------------------')
print('\\') # \
print('\\\\') # \\
print('I\'m goopuu') # \\ I'm goopuu
print("I say: \"No!\"") # I say: "No!"
print('床前明月光，疑是地上霜。\n举头望明月，低头思故乡。')   # 床前明月光，疑是地上霜。
                                                     # 举头望明月，低头思故乡。
print('goopuu\t100分') # goopuu	100分
print('123\xff')    # 123ÿ
print('\u4e2d\u56fd')   # 中国

# 格式化字符串，format()
print(f'\n2-------------------')

# 格式化字符串，f字符串
print(f'\n3-------------------')

# 字符串长度
print(f'\n4-------------------')
cust_str = 'hello中国'
print(len(cust_str))

# 索引操作
print(f'\n5-------------------')
cust_str = 'hello world'
print(cust_str[0], cust_str[6], cust_str[-1], cust_str[-7]) # h w d o
# cust_str[1] = 'H'   # 报错

# 切片
print(f'\n6-------------------')
