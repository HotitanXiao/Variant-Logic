# -*-coding:utf-8 -*-
# File Name: wave_3dplot.py
# Author   : H.Y
# Date     : 2015-11-7

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from core.Wave import wave
from core.Gorilla import Exhaust
from core.Gorilla import gorilla
from core.Gorilla import basic

def convert_vlt_pos(vlt, N):
    """
        将变值三角的一个横行的数据转换为p，q两个数组
    """
    p_set=[]
    q_set=[]
    c_set=[]
    print vlt
    p_set.append(0)
    q_set.append(0)
    c_set.append(1)
    for p_index in range(1, N):
        for q in range(0, min(p_index, N - p_index)):
            p_set.append(p_index)            
            q_set.append(q+1)
            c_set.append(vlt[p_index][q])
    p_set.append(N)
    q_set.append(0)
    c_set.append(1)
    return (p_set, q_set, c_set)



def StandardVLTriangle3D(windowSize):
    """
    将编制三角形在三维空间中显示
    """
    g = gorilla.GorilaBasis()
    tri = g.getTriangle_SingleRow(windowSize)
    (p, q, c) = convert_vlt_pos(tri,windowSize)
    n=range(0,windowSize)
    fig = plt.figure()
    axall = fig.add_subplot(111, projection="3d")
    axall.set_title("All ws=%s" % windowSize)
    axall.scatter(p,q,c,c='r', marker='o')
    axall.set_xlabel('p')
    axall.set_ylabel('q')
    axall.set_zlabel('sum')
    plt.show()


def BinaryString3D_file(filename1,file1Title, filename2, file2Title,windowSize=32):
    """
    从文件中读取二进制字符串，只读一行
    然后进行p and q的统计。
    """
    # if len(filenamelist) < 1:
    #     print "请输入至少一个有效的文件名"
    #     return
    
    # for filename in filenamelist:
    #     if len(filename) < 3:
    #         print "文件名长度不足"
    #         continue
    #     else:
    #         inputFile = open(filename, 'rb')
    #         binstr = inputFile.readline()
    #         result = basic.window_statstic(window_size=32, strbuffer=binstr,
    #                                        offset=32)
    #         (p, q, count) = basic.convert_pos(result)
    #         fig = plt.figure()
    #         ax = fig.add_subplot(111, projection="3d")
    #         ax.scatter(p, q, count, c='r', marker='o')
    if len(filename1) < 3 or len(filename2) < 3:
        print "文件名长度不足"
        return
    else:
        inputFile = open(filename1, 'rb')
        binstr = inputFile.readline()
        result = basic.window_statstic(window_size=windowSize,
                                       strbuffer=binstr,
                                       offset=windowSize)
       
        fig = plt.figure()

        # 变值三角的图像
        g = gorilla.GorilaBasis()
        tri = g.getTriangle_SingleRow(windowSize)
        (p_vlt, q_vlt, c_vlt) = convert_vlt_pos(tri,windowSize)
        n=range(0,windowSize)
        ax = fig.add_subplot(221, projection="3d")
        ax.set_title("All ws=%s" % windowSize)
        ax.scatter(p_vlt,q_vlt,c_vlt,c='g', marker='o')
        ax.set_title('vlt')       
        # 两个流密码的
        (p, q, count) = basic.convert_pos(result)      
        ax = fig.add_subplot(224, projection="3d")
        ax.scatter(p, q, count, c='r', marker='o')
        ax.set_title("%s ws=%s" % (file1Title,windowSize))
        axall = fig.add_subplot(222, projection="3d")
        axall.scatter(p, q, count, c='r', marker='o')
        # ax.scatter(p_vlt,q_vlt,c_vlt,c='g', marker='o')

        # 画第二个文件的结果
        inputFile = open(filename2, 'rb')
        binstr = inputFile.readline()
        result = basic.window_statstic(window_size=windowSize,
                                       strbuffer=binstr,
                                       offset=windowSize)
        (p, q, count) = basic.convert_pos(result)
        ax = fig.add_subplot(223, projection="3d")
        ax.scatter(p, q, count, c='b', marker='^')
        ax.scatter(p_vlt, q_vlt, c_vlt, c='g', marker='o')
        ax.set_title("%s ws=%s" % (file2Title,windowSize))
        axall.scatter(p, q, count, c='b', marker='^')


        # 绘制标准的变值三角的图样
        # gorrilaBasic = gorilla.GorilaBasis()
        # tri = gorrilaBasic.createBasis(32)
        # (p, q, count) = basic.convert_pos(tri)
        # ax = fig.add_subplot(221, projection="3d")
        # ax.scatter(p, q, count, c='r', marker='o')
        plt.show()

if __name__ == '__main__':
    # StandardVLTriangle3D(32)

    BinaryString3D_file("d:/TestData/StreamCipher/VLRC4.txt","VLRC4",
                        "d:/TestData/StreamCipher/rc4.txt","rc4",
                        16
                        )
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# (x, y, z) = wave_test.get_3d_data(end_round=1000,
#                                   cycles=[6, 20])
# hist, xedges, yedges = np.histogram2d(x, y, bins=4)


# dx = 0.5
# dy = 0.5
# zpos = np.zeros(len(z))
# # 下面参数比较坑跌，x，y，z标明画图起始点
# # dx dy dz 标明柱状图三位参数长宽高
# ax.bar3d(x, y, zpos, dx, dy, z, color='y', zsort='average')
# ax.set_xlabel('p')
# ax.set_ylabel('q')
# ax.set_zlabel('sum')

# plt.show()
