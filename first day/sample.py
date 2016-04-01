# -*- coding: utf-8 -*-

def main():
    for i in range (1,6):
        if i % 2 == 0:
            print("%sは偶数です。" % i)
        else:
            print("%sは奇数です." % i)
            
if __name__ == '__main__':
    main()