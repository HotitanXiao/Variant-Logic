[1mdiff --git a/core/Gorilla/Exhaust.py b/core/Gorilla/Exhaust.py[m
[1mindex 6fd43cc..7366928 100644[m
[1m--- a/core/Gorilla/Exhaust.py[m
[1m+++ b/core/Gorilla/Exhaust.py[m
[36m@@ -1,47 +1,53 @@[m
  # -*- coding: utf-8 -*-[m
[32m+[m[32m# File Name: Exhuast.py[m
[32m+[m[32m# Author   : H.Y[m
[32m+[m[32m# Date     : 2015-4-1[m
[32m+[m
[32m+[m
 def exhuast(N=1):[m
     """设计是两层字典数据结构"""[m
     maxNumber = 2**N[m
     result = {}[m
     binstr_ones = 0[m
     binstr_one_zeros = 0[m
[31m-    for x in xrange(0,maxNumber):[m
[31m-        binstr = bin(x)[2:].zfill(N) #在前方填充使字符串长度到N[m
[31m-        binstr_ones = ones(binstr,N)[m
[31m-        binstr_one_zeros = one_zeros(binstr,N)[m
[31m-        #开始判断操作[m
[31m-        if result.has_key(binstr_ones):[m
[32m+[m[32m    for x in xrange(0, maxNumber):[m
[32m+[m[32m        binstr = bin(x)[2:].zfill(N)  # 在前方填充使字符串长度到N[m
[32m+[m[32m        binstr_ones = ones(binstr, N)[m
[32m+[m[32m        binstr_one_zeros = one_zeros(binstr, N)[m
[32m+[m[32m        # 开始判断操作[m
[32m+[m[32m        if binstr_ones in result:[m
             b = result[binstr_ones][m
[31m-            if b.has_key(binstr_one_zeros):[m
[31m-                #如果有1-0的序列的话就进行自增[m
[32m+[m[32m            if binstr_one_zeros in b:[m
[32m+[m[32m                #  如果有1-0的序列的话就进行自增[m
                 b[binstr_one_zeros] += 1[m
             else:[m
                 b[binstr_one_zeros] = 1[m
         else:[m
[31m-            result[binstr_ones] = {binstr_one_zeros : 1}[m
[32m+[m[32m            result[binstr_ones] = {binstr_one_zeros: 1}[m
 [m
     return result[m
 [m
[31m-def ones(binstr,N):[m
[32m+[m
[32m+[m[32mdef ones(binstr, N):[m
     """根据输入的二进制串计算1的个数"""[m
     count = 0[m
[31m-    if N==1:[m
[32m+[m[32m    if N == 1:[m
         return count[m
[31m-    for x in xrange(0,N):[m
[32m+[m[32m    for x in xrange(0, N):[m
         if binstr[x] == '1':[m
             count = count+1[m
[31m-    [m
     return count[m
 [m
[31m-def one_zeros(binstr,N):[m
[32m+[m
[32m+[m[32mdef one_zeros(binstr, N):[m
     """计算01的个数，需要考虑循环的操作,N表示0-1向量的位长[m
     """[m
     count = 0[m
[31m-    if N==1:[m
[32m+[m[32m    if N == 1:[m
         return count[m
[31m-    for x in xrange(0,N):[m
[31m-        if(binstr[x]=='0' and binstr[(x+1)%N]== '1'):[m
[31m-            count = count +1[m
[32m+[m[32m    for x in xrange(0, N):[m
[32m+[m[32m        if (binstr[x] == '0' and binstr[(x+1) % N] == '1'):[m
[32m+[m[32m            count = count + 1[m
     return count[m
 [m
 [m
[36m@@ -52,4 +58,4 @@[m [mif __name__ == '__main__':[m
     from timeit import Timer[m
     for x in xrange(2,32):[m
         t1=Timer("test1("+str(x)+")","from __main__ import test1")[m
[31m-        print  t1.timeit(1)[m
\ No newline at end of file[m
[32m+[m[32m        print  t1.timeit(1)[m
[1mdiff --git a/core/Gorilla/__init__.pyc b/core/Gorilla/__init__.pyc[m
[1mindex 1b339cf..3343cf0 100644[m
Binary files a/core/Gorilla/__init__.pyc and b/core/Gorilla/__init__.pyc differ
[1mdiff --git a/core/Gorilla/enum.pyc b/core/Gorilla/enum.pyc[m
[1mindex f27170b..fb6ec80 100644[m
Binary files a/core/Gorilla/enum.pyc and b/core/Gorilla/enum.pyc differ
[1mdiff --git a/core/Gorilla/gorilla.pyc b/core/Gorilla/gorilla.pyc[m
[1mindex 88fb78a..cfe338d 100644[m
Binary files a/core/Gorilla/gorilla.pyc and b/core/Gorilla/gorilla.pyc differ
[1mdiff --git a/core/Wave/wave_3dplot.py b/core/Wave/wave_3dplot.py[m
[1mindex 1952705..007430d 100644[m
[1m--- a/core/Wave/wave_3dplot.py[m
[1m+++ b/core/Wave/wave_3dplot.py[m
[36m@@ -17,7 +17,7 @@[m [mdx = 0.5[m
 dy = 0.5[m
 zpos = np.zeros(len(z))[m
 # 下面参数比较坑跌，x，y，z标明画图起始点[m
[31m-#dx dy dz 标明柱状图三位参数长宽高[m
[32m+[m[32m# dx dy dz 标明柱状图三位参数长宽高[m
 ax.bar3d(x, y, zpos, dx, dy, z, color='y', zsort='average')[m
 ax.set_xlabel('p')[m
 ax.set_ylabel('q')[m
[1mdiff --git a/core/Wave/wave_test.py b/core/Wave/wave_test.py[m
[1mindex ca07068..3553c23 100644[m
[1m--- a/core/Wave/wave_test.py[m
[1m+++ b/core/Wave/wave_test.py[m
[36m@@ -4,8 +4,12 @@[m
 # Date     : 2015-11-6[m
 [m
 import os[m
[31m-import struct[m
 import random[m
[32m+[m[32mimport numpy as np[m
[32m+[m[32mfrom .. Gorilla import Exhaust[m
[32m+[m
[32m+[m[32mones = Exhaust.ones[m
[32m+[m[32mone_zeros = Exhaust.one_zeros[m
 [m
 [m
 class Wave(object):[m
[36m@@ -15,15 +19,6 @@[m [mclass Wave(object):[m
         self.cycle = cycle[m
         self.end_round = end_round[m
 [m
[31m-    def square_wave_to_file(self, filename=''):[m
[31m-        i = 0[m
[31m-        out_file = open(filename, 'wb')[m
[31m-        while i < self.end_round:[m
[31m-            out_file.write('1'*self.cycle)[m
[31m-            out_file.write('0'*self.cycle)[m
[31m-            i += 1[m
[31m-        out_file.close()[m
[31m-[m
     def square_wave_to_mem(self, cycle=10, end_round=1000):[m
         i = 0[m
         result_str = ''[m
[36m@@ -39,10 +34,8 @@[m [mclass Wave(object):[m
         while i < end_round:[m
             result_str += '1'*random.randint(random_range[0], random_range[1])[m
             result_str += '0'*random.randint(random_range[0], random_range[1])[m
[31m-            i +=1[m
[32m+[m[32m            i += 1[m
         return result_str[m
[31m-        [m
[31m-        [m
 [m
 [m
 class Tools():[m
[36m@@ -89,7 +82,7 @@[m [mclass Tools():[m
             raise[m
 [m
 [m
[31m-def multi_wave_xor(end_round=100,cycles = [6, 10], a_random=False):[m
[32m+[m[32mdef multi_wave_xor(end_round=100, cycles=[6, 10], a_random=False):[m
     """[m
     多波异或, 最后可以加入一个随机周期的0-1数组异或起来[m
     """[m
[36m@@ -111,10 +104,6 @@[m [mdef multi_wave_xor(end_round=100,cycles = [6, 10], a_random=False):[m
                                     random_wave,[m
                                     min(len(result_wave), len(random_wave)))[m
     return result_wave[m
[31m-    [m
[31m-    [m
[31m-        [m
[31m-[m
 [m
 [m
 def remove_temp_file(filename1='', filename2=''):[m
[36m@@ -126,31 +115,31 @@[m [mdef remove_temp_file(filename1='', filename2=''):[m
     os.remove(filename2)[m
 [m
 [m
[31m-def ones(binstr, N):[m
[31m-    """根据输入的二进制串计算1的个数"""[m
[31m-    count = 0[m
[31m-    if N == 1:[m
[31m-        return count[m
[31m-    for x in xrange(0, N):[m
[31m-        if binstr[x] == '1':[m
[31m-            count = count+1[m
[31m-    return count[m
[31m-[m
[31m-[m
[31m-def one_zeros(binstr, N):[m
[32m+[m[32mdef window_statstic_pjct(window_size=10, strbuffer='',[m
[32m+[m[32m                         offset=1, projection='p'):[m
     """[m
[31m-    计算01的个数，需要考虑循环的操作,N表示0-1向量的位长[m
[32m+[m[32m    这个函数是用于生成一个映射的数据流，就不进行统计，只是标记[m
[32m+[m[32m    这次统计得到的p，或q并加入到result数组中[m
     """[m
[31m-    count = 0[m
[31m-    if N == 1:[m
[31m-        return count[m
[31m-    for x in xrange(0, N):[m
[31m-        if(binstr[x] == '0' and binstr[(x+1) % N] == '1'):[m
[31m-            count = count + 1[m
[31m-    return count[m
[32m+[m[32m    buffer_size = len(strbuffer)[m
[32m+[m[32m    if buffer_size < 2:[m
[32m+[m[32m        return[m
[32m+[m[32m    result = np.array([])  # 存放统计结果的[m
[32m+[m[32m    index = 0[m
[32m+[m[32m    if projection == 'p':[m
[32m+[m[32m        pjctfunc = ones[m
[32m+[m[32m    else:[m
[32m+[m[32m        pjctfunc = one_zeros[m
[32m+[m[32m    while index < buffer_size-window_size:[m
[32m+[m[32m        # 开始判断操作[m
[32m+[m[32m        # pkey 是用于进行映射用的索引标记[m
[32m+[m[32m        pkey = pjctfunc(strbuffer[index:index+window_size], window_size)[m
[32m+[m[32m        result = np.append(result, pkey)[m
[32m+[m[32m        index = index+offset[m
[32m+[m[32m    return result[m
 [m
 [m
[31m-def block_statstic(window_size=10, strbuffer='', offset=1):[m
[32m+[m[32mdef window_statstic(window_size=10, strbuffer='', offset=1):[m
     """[m
     无重叠滑动窗口统计[m
     offset:表示每次窗口滑动的距离[m
[36m@@ -159,11 +148,10 @@[m [mdef block_statstic(window_size=10, strbuffer='', offset=1):[m
     if buffer_size < 2:[m
         return[m
     result = {}  # 存放统计结果的[m
[31m-    n_windows = buffer_size / window_size  # 向下取整的除法， python2 中的截断，python3中的真除法[m
     index = 0[m
[31m-    while index < buffer_size:[m
[32m+[m[32m    while index < buffer_size-window_size:[m
         # 开始判断操作[m
[31m-        print "now is ", strbuffer[index:index+window_size][m
[32m+[m[32m        # 取一个窗口[m[41m [m
         binstr_ones = ones(strbuffer[index:index+window_size], window_size)[m
         binstr_one_zeros = one_zeros([m
             strbuffer[index:index+window_size],[m
[36m@@ -177,33 +165,33 @@[m [mdef block_statstic(window_size=10, strbuffer='', offset=1):[m
                 p[binstr_one_zeros] = 1[m
         else:[m
             result[binstr_ones] = {binstr_one_zeros: 1}[m
[31m-        print index[m
[31m-        index = index+window_size[m
[32m+[m[32m        index = index+offset[m
     return result[m
 [m
 [m
[31m-def main():[m
[31m-    # wave_craetor = Wave(cycle=10, end_round=10000)[m
[31m-    # tools = Tools()[m
[31m-    # sq_wave1 = wave_craetor.square_wave_to_mem([m
[31m-    #     cycle=6,[m
[31m-    #     end_round=64)[m
[31m-    # sq_wave2 = wave_craetor.square_wave_to_mem([m
[31m-    #     cycle=8,[m
[31m-    #     end_round=64)[m
[31m-    # binarystr = tools.xor_str([m
[31m-    #     sq_wave1,[m
[31m-    #     sq_wave2,[m
[31m-    #     min(len(sq_wave1), len(sq_wave2)))[m
[31m-    # result = block_statstic([m
[31m-    #     window_size=6,[m
[31m-    #     strbuffer=binarystr,[m
[31m-    #     buffer_size=len(binarystr))[m
[31m-    # print result[m
[31m-    xorwave = multi_wave_xor(a_random=False)[m
[31m-    result = block_statstic(window_size=6,[m
[31m-                            strbuffer=xorwave, buffer_size=len(xorwave))[m
[31m-    print result[m
[32m+[m[32mdef convert_pos(result):[m
[32m+[m[32m    """[m
[32m+[m[32m    传入一个结果map，将结果map转换为[m
[32m+[m[32m    """[m
[32m+[m[32m    ppos = []  # 1的个数[m
[32m+[m[32m    qpos = []  # 0-1的个数[m
[32m+[m[32m    conpos = []  # 聚类个体数[m
[32m+[m
[32m+[m[32m    for cluster_index in result:[m
[32m+[m[32m        for t in result[cluster_index]:[m
[32m+[m[32m            ppos.append(cluster_index)[m
[32m+[m[32m            qpos.append(t)[m
[32m+[m[32m            conpos.append(result[cluster_index][t])[m
[32m+[m[32m    return (ppos, qpos, conpos)[m
[32m+[m
[32m+[m
[32m+[m[32mdef get_3d_data(end_round=1000, cycles=[12, 8, 2], random=False):[m
[32m+[m[32m    xorwave = multi_wave_xor(end_round, cycles, random)[m
[32m+[m[32m    result = window_statstic_pjct(window_size=6,[m
[32m+[m[32m                                  strbuffer=xorwave,[m
[32m+[m[32m                                  offset=6)[m
[32m+[m[32m    return convert_pos(result)[m
[32m+[m
 [m
 if __name__ == '__main__':[m
[31m-    main()[m
[32m+[m[32m    print "等待测试"[m
[1mdiff --git a/core/plotHist.py b/core/plotHist.py[m
[1mindex 4daf9b3..a15c2ea 100644[m
[1m--- a/core/plotHist.py[m
[1m+++ b/core/plotHist.py[m
[36m@@ -106,7 +106,8 @@[m [mclass PlotHist(GorilaBasis):[m
             plt.ylim(standardAxis[2],standardAxis[3]+2)[m
 [m
         plt.savefig(self.plot_Path+'SL/'+self._getFileName(N,2,power,title,'G','P','null',operation))#保存文件了~走起[m
[31m-        plt.close('all')[m
[32m+[m[32m        plt.close([m
[32m+[m[32m            'all')[m
         # plt.show()[m
         print time.time()-start    [m
     [m
[36m@@ -146,4 +147,4 @@[m [mif __name__ == '__main__':[m
     a = PlotHist()[m
     a._plothist(20,'sl')[m
 [m
[31m-# End of plotHist.py[m
\ No newline at end of file[m
[32m+[m[32m# End of plotHist.py[m
