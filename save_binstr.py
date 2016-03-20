import core.Gorilla.Exhaust as ex

def SaveBinStr(filename):
    ouputfile = open(filename, "wb")
    res = ex.exhuast_str(N=8)
    for p in res.keys():
        ouputfile.write("p:"+str(p)+"  "+str(res[p]) + "\r\n")
    ouputfile.close()



if __name__ == '__main__':
    SaveBinStr("D:/TestData/vl_binstr_n=8.txt")