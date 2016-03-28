# -*- cording: utf-8 -*-

# .rjust(第一引数,第二引数) ->
# 第一引数で指定した桁数になるまで
# 第二引数で文字列の左を埋める

test_str = "1234"

print (test_str.rjust(10,"0"))
print (test_str.rjust(10,"!"))

# .zfill(第一引数) ->
# 第一引数で指定した桁数になるまで0で埋める
print (test_str.zfill(10))
print (test_str.zfill(3))
