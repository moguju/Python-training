# -*- coding: utf-8 -*-

# .startswith(第一引数) ->
# 文字列の先頭が第一引数と一致すればTrue
# 不一致ならばFalse 返り値？

test_str = "python-izm"

print (test_str.startswith("python"))
print (test_str.startswith("izm"))

# 第一因数 in 文字列 ->
# 文字列中に第一引数が含まれていればTrue
# 含まれていなければFalse

print ("z" in test_str)
print ("s" in test_str)
