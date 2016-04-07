# -*- coding: utf-8 -*-


test_list_1 = ['100','200','300','200','100']

print(test_list_1.count('200'))

print("")


number = test_list_1.count('200')
test_list_2 = range(number)
print(test_list_2)

for i in [0, 1]:
    test_list_1.remove('200')
    print(test_list_1)
    
# print(test_list_1)