# -*- coding: utf-8 -*-


import datetime
if __name__ == "__main__":
    
    today        =    datetime.date.today()
    todaydetail  =    datetime.datetime.today()
    
    # 今日の日付
    print("-----------------------------------")
    print(today)
    print(todaydetail)
    
    # 今日に日付：それぞれの要素値
    print("-----------------------------------")
    print(today.year)
    print(today.month)
    print(today.day)
    print(todaydetail.year)
    print(todaydetail.month)
    print(todaydetail.day)
    print(todaydetail.hour)
    print(todaydetail.minute)
    print(todaydetail.second)
    print(todaydetail.microsecond)
    
    # 日付のフォーマット
    print("-----------------------------------")
    print(today.isoformat())
    print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))
    
    
    
    