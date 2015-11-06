# -*-coding:utf-8 -*-
import os
import struct


class Wave():
    def __init__(self, cycle=10, end_round=10000):
        self.cycle = cycle
        self.end_round = end_round

    def square_wave(cycle=2, end_round=100, filename=''):
        i = 0
        out_file = open(filename, 'wb')
        while i < end_round:
            out_file.write('1' * cycle)
            out_file.write('0' * cycle)
            i += 1
        out_file.close()



