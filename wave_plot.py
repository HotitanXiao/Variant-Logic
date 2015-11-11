# File Name: wave_plot.py
# Author   : H.Y
# Date     : 2015-11-11

from core.Wave import wave_projection, wave_test


def house():
    end_round_set = [10000]
    cycles_set = [[20]]
    random_flag = [False]
    window_size_set = [20]
    offset_set = [1, 6, 20]
    for end_round in end_round_set:
        for cycles in cycles_set:
            for random in random_flag:
                for window_size in window_size_set:
                    for offset in offset_set:
                        wave_projection.process(end_round, cycles,
                                                random, window_size,
                                                offset, 'q')


# def wave_xor_test():
#     wave_creator = wave_test.Wave()
#     tool = wave_test.Tools()
#     w3 = wave_test.multi_wave_xor(100, [1, 3])
    # w1 = wave_creator.square_wave_to_mem(end_round=100, cycle=1)
    # w2 = wave_creator.square_wave_to_mem(end_round=100, cycle=)
    # w3 = tool.xor_str(w1, w2, compare_len=min(len(w1), len(w2)))

if __name__ == '__main__':
    house()
