# -*- coding: utf-8 -*-


test_list_1 = ['python','izm','com']
print(test_list_1)

print("")

test_list_1.insert(1,'-')
test_list_1.insert(3,'.')

print(test_list_1)

test_list_1.insert(0,'http://www.')

print(test_list_1)

for i in test_list_1:
    print(i, end = "")