# -*- coding: utf-8 -*-


test_list_1 = ['1','2','3','2','1']
print (test_list_1)

print ('')

# 指定したインデックスの値を取り出し削除
# 引数なしだと末尾

print (test_list_1.pop(1))
print (test_list_1)

print (test_list_1.pop())
print (test_list_1)

result = test_list_1.pop()