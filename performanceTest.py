 # -*- coding: utf-8 -*-

 #测试程序

from core.Gorilla import gorilla
import core.Gorilla.Exhaust



def test1(N=2):
    tr = gorilla.GorilaBasis()
    tr.getTriangle_SingleRow(N)

def test2(N=2):
    core.Gorilla.Exhaust.exhuast(N)

if __name__ == '__main__':
    # from timeit import Timer
    # t1=Timer("test1(1024)","from __main__ import test1")
    # print t1.timeit(1)
    test1(1024)