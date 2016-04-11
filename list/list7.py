# -*- coding: utf-8 -*-


test_list_1 = ['100','200','300','200','100']

print(test_list_1.count('200'))

print("")

number = test_list_1.count('200')

for i in range(number):
    test_list_1.remove('200')
    
print(test_list_1)

for i in range(5):
    print("mogu")