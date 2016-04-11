# -*- coding: utf-8 -*-

test_dict_1 = {'YEAR':'2010','MONTH':'1','DAY':'20'}

print(test_dict_1)

print("")


print(test_dict_1['YEAR'])
# print(test_dict_1['MOGU'])

print("---------------------------")

print(test_dict_1.get('YEAR'))
print(test_dict_1.get('MOGU'))

print("---------------------------")
print(test_dict_1.get('YEAR','NOT FOUND'))
print(test_dict_1.get('MOGU','NOT FOUND'))

# get関数を使用すれば、存在しないキーを引数にしても
# エラーしない(Noneとなる)
# また、キーが存在しなかった場合のデフォルト値を設定可能

