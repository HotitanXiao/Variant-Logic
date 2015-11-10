from core.Wave import wave_projection

def house():
    end_round_set = [10000, 20000]
    cycles_set = [[1], [2], [1, 2], [10], [20], [10, 20]]
    random_flag = [False, True]
    window_size_set = [2, 6, 8, 20]
    offset_set = [2, 4, 6, 8, 10, 40]
    for end_round in end_round_set:
        for cycles in cycles_set:
            for random in random_flag:
                for window_size in window_size_set:
                    for offset in offset_set:
                        wave_projection.process(end_round, cycles,
                                                random, window_size,
                                                offset, 'q')

if __name__ == '__main__':
    house()