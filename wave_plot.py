# -*- coding:utf-8 -*-
# File Name: wave_plot.py
# Author   : H.Y
# Date     : 2015-11-11

from core.Wave import wave_projection
from core.Wave import wave
from core.Gorilla import basic
from basic import XMLConfig
import numpy as np
import matplotlib.pyplot as plt
# import numpy as np    


def main(end_round_set=1000, cycles_set=[[1]], random_flag=[False],
         window_size_set=[[5]], offset_set=[1], projections=['p', 'q']):
    print XMLConfig.getRootPath()


def house():
    end_round_set = [1000]
    cycles_set = [[]]
    pattern_set = [['1011001'], ['11010'], ['1011001', '11010']]
    random_flag = [False]
    window_size_set = range(1, 100, 10)
    offset_set = [1, 11]
    projections = ['p', 'q']
    for end_round in end_round_set:
        for cycles in cycles_set:
            print "out loop cycles %s" % cycles
            for random in random_flag:
                for window_size in window_size_set:
                    for projection in projections:
                        for offset in offset_set:
                            for patterns in pattern_set:
                                wave_projection.process(end_round=end_round,
                                                        cycles=cycles,
                                                        random=random,
                                                        patterns=patterns,
                                                        window_size=window_size,
                                                        offset=offset,
                                                        projecttype=projection)
                        wave_projection.process(end_round=end_round,
                                                cycles=cycles,
                                                patterns=patterns,
                                                random=random,
                                                window_size=window_size, 
                                                offset=window_size,
                                                projecttype=projection)

def house2():
    end_round_set = [1000]
    cycles_set = [[]]
    pattern_set = [['1011001'], ['11010'], ['1011001', '11010']]
    random_flag = [False]
    window_size_set = range(2, 100, 9)
    offset_set = [1, 11]
    projections = ['p', 'q']
    for end_round in end_round_set:
        for cycles in cycles_set:
            print "out loop cycles %s" % cycles
            for random in random_flag:
                for window_size in window_size_set:
                    for projection in projections:
                        for patterns in pattern_set:
                            wave_projection.process(end_round=end_round,
                                                    cycles=cycles,
                                                    random=random,
                                                    patterns=patterns,
                                                    window_size=window_size,
                                                    offset=window_size,
                                                    projecttype=projection)


def wave_plot_3d_point(end_round=1000, pattern_set=[['1011001', '11010']]):
    """
    三维空间上的点的打印
    """
    result_set = wave.get_3d_data()
    print result_set
# def wave_xor_test():
#     wave_creator = wave_test.Wave()
#     tool = wave_test.Tools()
#     w3 = wave_test.multi_wave_xor(100, [1, 3])
    # w1 = wave_creator.square_wave_to_mem(end_round=100, cycle=1)
    # w2 = wave_creator.square_wave_to_mem(end_round=100, cycle=)
    # w3 = tool.xor_str(w1, w2, compare_len=min(len(w1), len(w2)))

def rc4_xor_wave(filename="D:/TestData/StreamCipher/VLRC4.txt"):
    output_filename_base = "D:/development/pythonCode/Variant-Logic/Variant-Logic/output/"
    end_round_set = [1000]
    cycles_set = [[]]
    pattern_set = ['1011001', '11010']
    random_flag = [False]
    window_size_set = range(2, 100, 6)
    offset_set = [1, 8, 11]
    projections = ['p', 'q']
    wave_creator = wave.Wave()
    tool = wave.Tools()
    for end_round in end_round_set:
        for pattern in pattern_set:
            rc4_string = open(filename, 'rb').read(len(pattern)*end_round)
            for offset in offset_set:
                for projecttype in projections:
                    for window_size in window_size_set:
                        wavestr = wave_creator.complex_square_wave_to_mem(pattern, end_round)
                        result_str = tool.xor_str(rc4_string, wavestr,min(len(rc4_string), len(wavestr))) 
                        
                        data = basic.window_statstic_pjct(window_size=window_size,strbuffer=result_str, offset=offset, projection=projecttype)
                        output_filename = output_filename_base + "rc4&wave_%s_ws=%s_offset=%s_type=%s.png" % (pattern, window_size, offset, projecttype)
                        plt.title("RC4&%s_len=%s" % (pattern, len(wavestr)))
                        plt.xlabel(projecttype)
                        plt.ylabel('count')
                        plt.hist(data, facecolor='green')
                        plt.savefig(output_filename)  # 保存文件了~走起
                        plt.close('all')


                        # 单个的图
                        # rc4 
                        data = basic.window_statstic_pjct(window_size=window_size,strbuffer=rc4_string, offset=offset, projection=projecttype)
                        # print data
                        output_filename = output_filename_base + "rc4_pt=%s_ws=%s_offset=%s.png" % (projecttype ,window_size, offset)
                        plt.title("VRC4_offset=%s_len=%s_ws=%s" % (offset, len(rc4_string), window_size))
                        plt.xlabel(projecttype)
                        plt.ylabel('count')
                        plt.hist(data, facecolor='green')
                        plt.savefig(output_filename)  # 保存文件了~走起
                        plt.close('all') 


                        data = basic.window_statstic_pjct(window_size=window_size,strbuffer=wavestr, offset=offset, projection=projecttype)
                        output_filename = output_filename_base + "wave_pt=%s_pattern=%s_ws=%s_offset=%s.png" % (projecttype,pattern, window_size, offset)
                        plt.title("wave%s_offset=%s_len=%s" % (pattern, offset ,len(wavestr)))
                        plt.xlabel(projecttype)
                        plt.ylabel('count')
                        plt.hist(data, facecolor='green')
                        plt.savefig(output_filename)  # 保存文件了~走起
                        plt.close('all')










if __name__ == '__main__':
    rc4_xor_wave()
