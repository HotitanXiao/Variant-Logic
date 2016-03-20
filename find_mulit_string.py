# coding:utf-8
import random

bin_str = open("D:/TestData/quantum_bit/shifted_key_4.char","r").read()
def find_mulit_string(strlen):
    # 随机找几个随机长度的字符串，并在原串中定位子串的个数
    random_num = random.randint(26,10000)
    pattern_str = bin_str[random_num:random_num+strlen]
    if pattern_str in bin_str[random_num+strlen:]:
        print "get multi string len %s --%s, for bin_str len is %s" % (len(pattern_str), random_num, len(bin_str))
        return True
    else:
        return False


if __name__ == '__main__':
    for x in [25,50,100,200,1000,100000]:
        find_mulit_string(x)