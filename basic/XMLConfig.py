# -*- coding: utf-8 -*-
#
#这个文件是用来操作XML配置文件的，
#主要是读写操作。
#
#
#
#
#
#
#
#

from xml.dom import minidom, Node
from xml.dom.minidom import parse,parseString
import os
import sys

def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc


def initConfigFile(cdstr="."):
    #初始化默认配置文件。
    newDoc = minidom.Document()
    newDoc.appendChild(newDoc.createComment('House Young simple xml Configure'))
    #产生第一个跟节点。 这个节点是configure
    configure = newDoc.createElement('configure')#configure下面应该有一个rootPath，和Other的节点。

    #创建rootPath节点
    rootPath = newDoc.createElement('rootPath')
    
    rootPath.appendChild(newDoc.createTextNode((os.path.abspath(cdstr))))
    #将rootPath添加到configure节点上
    configure.appendChild(rootPath)
    #将整棵树添加到文件上。
    newDoc.appendChild(configure)
    
    f = file('config.cfg', 'w')
    f.write(newDoc.toprettyxml().encode("utf-8"))

    print sys.executable


def getRootPath(cdstr="."):
    """参数是一个点. 活着两个点.. 活着是一个
    粗放配置文件目录的绝对路径"""
    #读取配置文件
    #暂时没有异常处理，还要进行修改很多
    configfilePath = os.path.abspath(cdstr)+"\config.cfg"
    dom = parse(configfilePath)
    #config_root = dom.getElementsByTagName("configure") 
    #得到根节点
    rootPath = dom.getElementsByTagName("rootPath")
    #得到的字符串似乎是ascii的，转换下格式
    return getText(rootPath[0].childNodes).encode("utf-8")

def setRootPath(newRootPath, cdstr='.' ):

    """设置新的根目录"""
    configfilePath = os.path.abspath(cdstr)+"\config.cfg"
    dom = parse(configfilePath)
        #得到根节点
    rootPathElement = dom.getElementsByTagName("rootPath")

    rootPathElement[0].childNodes[0].nodeValue = newRootPath
    f = file('config.cfg', 'w')
    f.write(dom.toprettyxml().encode("utf-8"))


    

if __name__ == '__main__':
    # dom1 = parse('config.xml')
    # config_element = dom1.getElementsByTagName("config")[0]
    # servers = config_element.getElementsByTagName("server")
    # for server in servers:
    #     print getText(server.childNodes)

    initConfigFile(".")
    setRootPath("jjjjjjj")
    #print os.getcwd() 
    # get current work directory
    #print os.path.abspath('..')
