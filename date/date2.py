# -*- coding: utf-8 -*-
# 日付の計算 timedelta

import datetime

if __name__ == "__main__":
    
    today    =    datetime.datetime.today()
    
    # 今日の日付
    print(today)
    
    # 明日の日付
    # timedelta(days=進めたい日数)
    print(today + datetime.timedelta(days=1))
    
    
    newyear   =   datetime.datetime(2010,1,1)
    
    # 2010年1月1日の一週間後
    print(newyear + datetime.timedelta(days=7))
    
    # 2010年1月1日から今日までの日数
    calc   =   today - newyear
    # 計算結果の返り値は「timedelta」
    print(calc.days)