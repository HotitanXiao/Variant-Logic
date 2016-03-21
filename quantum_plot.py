#coding:utf-8
from core.Wave import wave_projection, wave
from core.Gorilla import basic
import matplotlib.pyplot as plt
import numpy as np
import os

import operator
import platform

system_type = platform.system()
if system_type == "Linux":
    output_filename_base = "/home/dm007/TestData/quantum_bit/output/shifted_key4/"
    input_dir = "/home/dm007/TestData/quantum_bit/source_char/"
    result_output = "/home/dm007/result_output.txt" 
else:
    output_filename_base = "D:/TestData/quantum_bit/quantum_bit/output/shifted_key4/"
    input_dir = "D:/TestData/quantum_bit/source_char/"
    result_output = "d:/result_output.txt"
     
file_list = os.listdir(input_dir+"secure_key4/")



def log_stastic_result():
    log_file = open(output_filename_base+"log_file.txt","w")
    window_size_set = [4096]
    projection_set = ['p','q']
    offset_set = [8]
    xtickets = []
    ytickets = []

    ones = 0
    zeros = 0
    p = 0
    p_count = 0

    q = 0
    q_count = 0

    for file in file_list:
        # print "now is %s" % file
        quantum_binstr_secure = open(input_dir+file,'rb').read()
        for window_size in window_size_set:
            for offset in offset_set:

                (ones_t,zeros_t,data) = basic.quantum_statstic_pjct(window_size=window_size, strbuffer=quantum_binstr, offset=window_size, projection='p')
                (x,y) = np.unique(data,return_counts=True)
                x_range = window_size/2

                # p_index, p_value = max(enumerate(x), key=operator.itemgetter(1))
                index = y.argmax()
                p_count = y[index]
                p = x[index]

                (ones_t,zeros_t,data) = basic.quantum_statstic_pjct(window_size=window_size, strbuffer=quantum_binstr, offset=window_size, projection='q')
                (x,y) = np.unique(data,return_counts=True)
                x_range = window_size/2
                
                index = y.argmax()
                q_count = y[index]
                q = x[index]

                

                print "ones:%s--zeros:%s---p:%s(position:%s)---q:%s(position:%s)" % (ones,zeros,p_count,p,q_count,q)
                log_file.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (ones,zeros,p_count,p,q_count,q))

                    # output_filename = output_filename_base + "%s_ws=%s_offest=%s_ptype=%s.PNG" % (title_pattern,window_size, window_size, projection)
                    # plt.title("%s len %s" % (title_pattern,len(quantum_binstr)))
                    # plt.xlabel(projection)
                    # plt.ylabel('count')
                    # plt.bar(x,y,linewidth=0.5, facecolor='green')
                    # plt.tight_layout()
                    # # plt.hist(data,4,align='left',rwidth=0.2,histtype='bar',facecolor='green')
                    # plt.savefig(output_filename)
                    # plt.close()

def log_stastic_result_plot():
    fileindex = 4
    choice = "p_p"
    log_file = open(output_filename_base+"log_file.txt","w")
    center_position = 2048
    window_size = 4096
    projection_set = ['p','q']
    offset_set = [8]
    xtickets = []
    ytickets = []



    ones = 0
    zeros = 0
    p = 0
    p_count = 0

    q = 0
    q_count = 0

    one_zero_rate_array = []
    p_array = []
    p_count_array = []
    q_array = []
    q_count_array = []


    onesshifted_ = 0
    zerosshifted_ = 0
    pshifted_ = 0
    p_countshifted_ = 0

    qshifted_ = 0
    q_countshifted_ = 0

    one_zero_rate_shifted_array = []
    p_shifted_array = []
    p_count_shifted_array = []
    q_shifted_array = []
    q_count_shifted_array = []
    
    p_position_table = {} # 用来存放
    p_position_shifted_table = {}

    for file in file_list[1:1000]:
        # print "now is %s" % file
        quantum_binstr_secure = open(input_dir+"secure_key4/"+file,'rb').read()


        split_index = file.split("_")[4]

        shifted_file = "/shifted_key4/shifted_key_%s.bin_split_%s" % (fileindex, split_index)
        quantum_binstr_shifted = open(input_dir+shifted_file,'rb').read()


        (ones_t,zeros_t,data) = basic.quantum_statstic_pjct(window_size=window_size, strbuffer=quantum_binstr_secure, offset=window_size, projection='p')
        (x,y) = np.unique(data,return_counts=True)
        x_range = window_size/2

        # p_index, p_value = max(enumerate(x), key=operator.itemgetter(1))
        index = y.argmax()
        p_count = y[index]
        p = x[index]
        p_array.append(p-center_position)
        p_count_array.append(p_count)
        
        if p_position_table.get(p):
            p_position_table[p] += p_count
        else:
            p_position_table[p] = p_count
            


        (ones_t,zeros_t,data) = basic.quantum_statstic_pjct(window_size=window_size, strbuffer=quantum_binstr_shifted, offset=window_size, projection='p')
        (x,y) = np.unique(data,return_counts=True)
        index = y.argmax()
        p_count = y[index]
        p = x[index]
        p_shifted_array.append(p-center_position)
        p_count_shifted_array.append(p_count)
        if p_position_shifted_table.get(p):
            p_position_shifted_table[p] += p_count
        else:
            p_position_shifted_table[p] = p_count



        (ones_t,zeros_t,data) = basic.quantum_statstic_pjct(window_size=window_size, strbuffer=quantum_binstr_secure, offset=window_size, projection='q')
        (x,y) = np.unique(data,return_counts=True)
        x_range = window_size/2
        
        index = y.argmax()
        q_count = y[index]
        q = x[index]
        q_count_array.append(q_count)
        q_array.append(q)
        one_zero_rate_array.append(float(ones_t)/float(zeros_t))



        (ones_t,zeros_t,data) = basic.quantum_statstic_pjct(window_size=window_size, strbuffer=quantum_binstr_shifted, offset=window_size, projection='q')
        (x,y) = np.unique(data,return_counts=True)
        x_range = window_size/2
        
        index = y.argmax()
        q_count = y[index]
        q = x[index]
        q_count_shifted_array.append(q_count)
        q_shifted_array.append(q)
        one_zero_rate_shifted_array.append(float(ones_t)/float(zeros_t))



    # for (x,y) in zip(q_count_shifted_array,q_count_array):
    #     print '%s--------------%s' % (x,y)

        # log_file.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (ones_t,zeros_t,p_count,p,q_count,q))
    n_bins = len(q_count_array)
    width = 0.25
    x = np.arange(1,n_bins+1)
    fig, axes = plt.subplots(nrows=2, ncols=1)
    ax0, ax1 = axes.flat
    colors = ['red', 'green']
    label = ["shited","secure"]
    # ax0.set_title("p_count")   
    # ax0.bar(x, p_count_shifted_array, width)
    # ax0.bar(x + width, p_count_array, width, color=plt.rcParams['axes.color_cycle'][1],label=label)
    # ax0.set_xticks(x)
    if choice == "position":
        ax0.set_title("p_position_shifted")   
        ax0.bar(x, p_shifted_array, width)
        ax0.set_xticks(x)

        ax1.set_title("p_position_secure")   
        ax1.bar(x, p_array, width)
        ax1.set_xticks(x)
    
    if choice == "rate":
        ax0.set_title("rate_shifted")   
        ax0.plot(x, one_zero_rate_shifted_array)
        ax0.set_xticks(x)

        ax1.set_title("rate_secure")   
        ax1.plot(x, one_zero_rate_array)
        ax1.set_xticks(x)
    if choice == "p_p":
        x = p_position_shifted_table.keys()
        y = []
        for key in x :
            y.append(p_position_shifted_table[key])
        ax0.set_title("position and count shifted")
        ax0.bar(x,y)
        
        x = p_position_table.keys()
        y = []
        for key in x :
            y.append(p_position_table[key])
        
        ax1.set_title("position and count secure")
        ax1.bar(x, y)
    # ax1.plot(x,p_shifted_array,color="red",linewidth=2)
    # ax1.plot(x,p_array,color="green",linewidth=3)
    # ax1.plot([1,len(p_shifted_array)],[2048,2048])

    # ax2.set_title("q count")   
    # ax2.bar(x, q_count_shifted_array, width)
    # ax2.bar(x + width, q_count_array, width, color=plt.rcParams['axes.color_cycle'][1],label=label)
    # ax2.set_xticks(x)

    # ax3.set_title("q position")   
    # ax3.bar(x, q_count_shifted_array, width)
    # ax3.bar(x + width, q_count_array, width, color=plt.rcParams['axes.color_cycle'][1],label=label)
    # ax3.set_xticks(x)

    # ax4.set_title("1/0 rate")   
    # ax4.bar(x, one_zero_rate_shifted_array, width)
    # ax4.bar(x + width, one_zero_rate_array, width, color=plt.rcParams['axes.color_cycle'][1],label=label)
    # ax4.set_xticks(x)



    # # Make a multiple-histogram of data-sets with different length.
    # ax3.hist([q_shifted_array,q_array], n_bins, normed=1, histtype='bar', color=colors, label=label)
    # ax3.set_title('q position')


    # ax4.hist([one_zero_rate_shifted_array,one_zero_rate_array], n_bins, normed=1, histtype='bar', color=colors, label=label)
    # ax3.set_title('ones/zeros rate')

    plt.tight_layout()
    plt.show()

    # output_filename = output_filename_base + "%s_ws=%s_offest=%s_ptype=%s.PNG" % (title_pattern,window_size, window_size, projection)
    # plt.title("%s len %s" % (title_pattern,len(quantum_binstr)))
    # plt.xlabel(projection)
    # plt.ylabel('count')
    # plt.bar(x,y,linewidth=0.5, facecolor='green')
    # plt.tight_layout()
    # # plt.hist(data,4,align='left',rwidth=0.2,histtype='bar',facecolor='green')
    # plt.savefig(output_filename)
    # plt.close()



def go():

    # quantum_binstr = open("d:/TestData/quantum_bit/secure_key_4_split0.char","rb").read()
    # quantum_binstr = open("d:/TestData/quantum_bit/shifted_key_4.char","rb").read()
    # title_pattern = "%s-%s"

    quantum_binstr = open("d:/TestData/VLRC4_for_nist_128.txt","rb").read()
    window_size_set = [4096]
    projection_set = ['p','q']
    offset_set = [8]
    xtickets = []
    ytickets = []

    for file in file_list:
        print "now is %s" % file
        quantum_binstr = open(input_dir+file,'rb').read()
        for window_size in window_size_set:
            for offset in offset_set:
                for projection in projection_set:
                    title_pattern = "%s-%s" % (file,window_size)
                    data = basic.window_statstic_pjct(window_size=window_size, strbuffer=quantum_binstr, offset=window_size, projection=projection)
                    (x,y) = np.unique(data,return_counts=True)
                    x_range = window_size/2

                    output_filename = output_filename_base + "%s_ws=%s_offest=%s_ptype=%s.PNG" % (title_pattern,window_size, window_size, projection)
                    plt.title("%s len %s" % (title_pattern,len(quantum_binstr)))
                    plt.xlabel(projection)
                    plt.ylabel('count')
                    plt.bar(x,y,linewidth=0.5, facecolor='green')
                    plt.tight_layout()
                    # plt.hist(data,4,align='left',rwidth=0.2,histtype='bar',facecolor='green')
                    plt.savefig(output_filename)
                    plt.close()
    
    # plt.show()
    # outfile = open(result_output,"w")
    # for data_item in data:
    #     outfile.write(str(data_item))

if __name__ == '__main__':
    # file_list = os.listdir("d:/TestData/quantum_bit/")
    # for x in xrange(1,10):
    #     print file_list[x]
    log_stastic_result_plot()
