# -*-coding:utf-8 -*-
# File Name: wave_projection.py
# Author   : H.Y
# Date     : 2015-11-10

import numpy as np
import matplotlib.pyplot as plt
import wave_test


def _getFileName(round, cycles, random, window_size, offset, projecttype):
    return "pt=" + projecttype +\
        "_r=" + str(round) +\
        "_c=" + str(cycles) + \
        "_rdm=" + bin(random)[2:] + \
        "_ws="+str(window_size) + \
        "_offset=" + str(offset)


def projection(end_round=1000, cycles=[12, 8, 2], random=False,
               window_size=10, offset=6, projecttype='p'):
    """
    用于生成映射的数据，可选按p和按q映射
    """
    xorwave = wave_test.multi_wave_xor(end_round, cycles, random)
    return wave_test.window_statstic_pjct(window_size, xorwave,
                                          offset, projection=projecttype)


def process(end_round=1000, cycles=[12, 8, 2], random=False,
            window_size=10, offset=6, projecttype='p'):
    data = projection(end_round, cycles, random,
                      window_size, offset, projecttype)
    filename = _getFileName(end_round, cycles, random,
                            window_size, offset, projecttype)
    plt.xlabel(projecttype)
    plt.ylabel('count')
    plt.hist(data, facecolor='green')
    plt.savefig(filename)  # 保存文件了~走起
    plt.close('all')


if __name__ == '__main__':

    end_round_set = [5000, 10000]
    cycles_set = [[1], [2], [1, 2], [10], [15], [10, 15]]
    random_flag = [True, False]
    window_size_set = [2, 6, 8, 14, 20]
    offset_set = [1, 3, 7, 20, 25]
    projc_set = ['p', 'q']
    for end_round in end_round_set:
        for cycles in cycles_set:
            for random in random_flag:
                for window_size in window_size_set:
                    for offset in offset_set:
                        for p in projc_set:
                            process(end_round, cycles, random,
                                    window_size, offset, p)
