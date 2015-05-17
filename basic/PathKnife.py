# -*- coding: utf-8 -*-
#
#路径管理类，分析并创建保存生成图片的路径
#如果路径不存在则需要创建。
#路径的命名规则为
#时间---变量
#          |
#         summary
#         |            
#         separate
#             |
#             运算模式()----|
#             |              |         
#             |              P --- sl
#             |              |        |
#             |              X        c
#             |                    |
#             |                    w
#             |                    |
#             |                    f

import os
import time

class PathKnife(object):
    """docstring for DirectoryManager"""
    root_Path = ""#跟路径

    subroot_model = {'separate':'separate','summary':'summary'}
    #叶子目录模板
    leafpath_model = {'sl':'sl','w':'w'}
    #子目录
    subrootpaths = []
    #操作对应的符号
    operation_sign = {'0':'0','1':'1','2':'(-1)','3':'i','4':'(-i)'}
    #存放时间目录
    time_str = ""
    
    def __init__(self,root_Path=None):
        """构造函数"""
        super(PathKnife, self).__init__()
        if root_Path!=None:
            self.root_Path = root_Path
        else:
            self.root_Path = os.path.abspath(".")+"/OutPut/"#默认路径就是当前执行路径的子目录OutPut
        
        #一级子目录的  -根路径/时间/sum or sep/
        time_str = self.get_time()
        self.subrootpaths.append(self.root_Path+time_str+"/"+self.subroot_model['separate']+"/")
        self.subrootpaths.append(self.root_Path+time_str+"/"+self.subroot_model['summary']+"/")
    def set_root_path(self,rootPath):
        """设置跟路径"""
        if len(rootPath)<4:
            print "路径不合法"
            return False
        self.root_Path = rootPath
        return True
    def check_path_exist(self):
        """检查当前根路径是否存在"""
        #让我们查查看以及路径有没有了
        return os.path.exists(self.root_Path)
    def make_top_path(self):
        """创建不包含运算模式及以下路径的顶级路径"""
        if os.path.exists(self.root_Path):
            print "根路径已存在:"+self.root_Path
        else:
            print "根路径不存在"
            os.makedirs(self.root_Path)
            print "根路径创建成功"
    def get_time(self):
         """获取当前时间，次级根目录"""         
         return time.strftime("%y.%m.%d-%H-%M-%S")
    def make_subrootpath(self):
        """用于生成子路径字符串-用于存放结果"""

        if os.path.isdir(self.root_Path) == False:
            self.make_top_path()
        else:
            #开始创建子路径

            #图像是分开的separate
            os.makedirs(self.subrootpaths[0])
            print "路径创建成功" + self.subrootpaths[0]            
            #图像是总和的summary
            os.makedirs(self.subrootpaths[1])
            print "路径创建成功" + self.subrootpaths[1]
    def make_subpath(self, operation=None,mode="X"):
        """用于创建子目录,mode应当是一个数组或一个字符串"""
        
        if isinstance(operation,list):
            #如果operation是个列表，则说明这个b应该要产生多个子目录
            for subrootpath in self.subrootpaths:
                for opstr in operation:
                    #创建操作符的的目录
                    os.makedirs(subrootpath+opstr+self.add_double_slash(mode))
        #判断完成后开始生成子目录
        # if mode != None:
        #     #是多个mode则需循环创建
        #     if isinstance(mode,list):
        #         for x in xrange(1,10):
        #             pass
        #         return True
        #     else:
        #         #只有一个mode的话就创建一个路径了
        #         tempPath = subrootpath + mode
        #         os.makedirs(tempPath)
        #         return True
        # else:
        #     print "mode无输入，暂不创建子目录"
        #     return False

#---------------------------------------------------
#模式需要一个默认值----等待后面再来填写吧
#这个功能先留着，有用没用再说吧
    def get_operation_path(self,model=None):
        """创建操作模式路径"""
        if len(model)<4:
            return
        else:
            #开始处理
            resultstr = ''
            for char in model:
                resultstr = resultstr+operation_sign
#---------------------------------------------------
#这个是输入参数，返回对应存放结果的路径
    def get_path(self,vecLenth,varSize,operation,mode1,mode2,mode3):
        """下面是字符串拼接的路径，感觉不是很好，这种方法"""
        return self.root_Path+self.add_double_slash(str(varSize))+self.add_double_slash(str(operation))+mode1

#---------------------------------------------------
#左右添加两个斜线，构造路径时使用    
    def add_double_slash(self,mystr):
        """左右添加两个斜线，构造路径时使用"""
        return "/"+mystr+"/"
        


if __name__ == '__main__':
    a = PathKnife()
    print a.make_top_path()
    print a.make_subrootpath()
