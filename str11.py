# -*- coding: utf-8 -*-
# 出来ないぞ！！！

print ("----------------------------")

test_str = "　　　python-izm.com"
print (test_str)


test_str = test_str.lstrip()
print (test_str)

test_str = test_str.lstrip("python")
print (test_str)


print ("----------------------------")

test_str = "python-izm.com　　　"
print (test_str + "/")

test_str = test_str.rstrip()
print (test_str + "/")

test_str = test_str.rstrip("com")
print (test_str)
