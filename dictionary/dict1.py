# -*- coding: utf-8 -*-

test_dict_1 = {'YEAR':'2010','MONTH':'1','DAY':'20'}
# 'キー':値 で一つの要素

print(test_dict_1)

print("")

for i in test_dict_1:
    print(i)
    print(test_dict_1[i])
    print('----------------------')

# ループで出力するとキーの取得が出来る
# ディクショナリ[キー]で値を取得出来る
# 関数の使用によって値もしくは両方の取得も出来るように