# -*- coding: utf-8 -*-

# python3だと出来た
# .lstrip(引数) -> 文字列の先頭から引数までを削除
# 引数なしだと空白のみ除去

print ("----------------------------")

test_str = "　　　python-izm.com"
print (test_str)


test_str = test_str.lstrip()
print (test_str)

test_str = test_str.lstrip("python")
print (test_str)


# .rstrip(引数) -> 文字列の末尾から引数までを削除
# 引数なしだと空白のみ除去

print ("----------------------------")

test_str = "python-izm.com　　　"
print (test_str + "/")

test_str = test_str.rstrip()
print (test_str + "/")

test_str = test_str.rstrip("com")
print (test_str)
