# -*- coding: utf-8 -*-

import datetime

def getToday():
    # def 関数を定義する
    
    toDay = datetime.datetime.today()
    value = (toDay.year,toDay.month,toDay.day)
    
    return value
    
    
if __name__ == "__main__":
    
    test_tuple = getToday() #=value
    
    print(test_tuple)
    print(test_tuple[0])
    print(test_tuple[1])
    print(test_tuple[2])