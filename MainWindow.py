# -*- coding: utf-8 -*-
#
#
# 要想界面搞得好
# 自己动手少不了
#
#
import sys
import PySide
from PySide.QtGui import (QApplication, QDialog, QMessageBox,QMainWindow,QMdiSubWindow,QIntValidator,QRegExpValidator)
from PySide.QtCore import (Qt, QRegExp)
from PySide.QtGui import QHBoxLayout

from guiBasis.GorillaWindow import Ui_Dialog_pascal
from guiBasis.MainWindowUI import Ui_MainWindow
from guiBasis.about import Ui_Form
from guiBasis.SettingWindow import Ui_Setting
from core.plotHist import PlotHist
import basic.XMLConfig as xmlcfg
import basic.PathKnife as ptknife



__version__ = '3.1.0' 

class PascalWindow(QDialog,Ui_Dialog_pascal):  

    def __init__(self, parent=None):       
        super(PascalWindow, self).__init__(parent)
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.createHist)
        self.pushButton.clicked.connect(self.createHist)
        #限制长度
        self.lineEdit.setValidator(QIntValidator(10,999999,self))
        self.lineEdit_operation.setValidator(QRegExpValidator(QRegExp("([0-4]{4})|([0-4]{4}-[0-4]{4})"),self))


    def createHist(self,N=100,SortGroup='sl'):
        """
        函数名：createHist
        参数:
        返回值：没有
        说明：产生各种各样的图样

        """
        #获取长度N
        newN = int(str(self.lineEdit.text()))
        #获取选择的排序方式
        selectedSortGroup = str(self.comboBox.itemText(self.comboBox.currentIndex()))
        power = int(self.spinBox.text())
        print selectedSortGroup
        if newN>1:
            N = newN

        if self.varSelectedCheck():    
            a = PlotHist()
            for opcode in self.operationParser():
                a._plothist(N,selectedSortGroup,power,opcode)

    def operationParser (self):
        """
        函数名:operationParser
        参数：无
        返回值： 位于范围内的操作符，类型为List
        说明：用于解析从UI中获取到的操作符范围，然后根据
        该范围返回一个List，List中包含所有范围内的操作符
        """
        import re
        pattern1 = re.compile(r'([0-4]{4})')
        pattern2 = re.compile(r'([0-4]{4}-[0-4]{4})')
        match = pattern1.match(self.lineEdit_operation.text())

        if pattern2.match(self.lineEdit_operation.text()) != None:
            opcode = pattern2.match(self.lineEdit_operation.text()).group()
            twoString = opcode.split('-')
            if int(twoString[0])>=int(twoString[1]):
                return [opcode]
            else:
                numberArray = self.covertToArray(int(twoString[0]))
                end = int(twoString[1])
                result = []
                temp = '0'
                result.append(twoString[0])
                while int(temp) < end:
                    temp = ''.join(str(v) for v in self.fiveAdd(numberArray))
                    result.append(temp)
                return result
        if match != None:
            opcode = match.group(0)
            print opcode
            print match.groups()
            print self.lineEdit_operation.text()
            if opcode.find('-') == -1:
                return [opcode]        
    def covertToArray(self,inputNumber):
        """
        说明：将数字转换为数组
        """
        array = [0,0,0,0]
        for x in xrange(0,4):
            array[x] = inputNumber/(10**(3-x))
            inputNumber = inputNumber - array[x]*10**(3-x)
            print inputNumber
        return array

    def fiveAdd(self,numberArray,mode=2):
        """
        说明：三/五进制加法
        """
        if numberArray[3] <mode:
            numberArray[3] +=1
        else: 
            numberArray[3] += 1 
            for x in xrange(0,3):
                if numberArray[3-x] > mode:
                    numberArray[3-x] = 0
                    numberArray[3-x-1] +=1
        if numberArray[0] > mode:
            numberArray[0]=0
        return numberArray
                
    def functionTest(self):
        print self.operationParser()     

    def varSelectedCheck(self):
        """
        说明：判断需要输入的参数是否都输入完毕
        """
        if len(self.lineEdit_operation.text()) <4:
            print len(self.lineEdit_operation.text())
            QMessageBox.information(self, QApplication.translate("Error", "错误:", None, QApplication.UnicodeUTF8),
                QApplication.translate("Error", "请检查你的参数是否输入正确", None, QApplication.UnicodeUTF8)
                )    
        else:
            return True

class AboutWidnow(QDialog,Ui_Form):
    def __init__(self, parent=None):
        super(AboutWidnow, self).__init__(parent)
        self.setupUi(self)
class SettingWindow(QDialog,Ui_Setting):
    """docstring for SettingWindow"""
    def __init__(self, parent=None):
        super(SettingWindow, self).__init__(parent)
        self.setupUi(self)
        # 获取文件保存根路径
        rootpathstr = xmlcfg.getRootPath()
        # 将得到的内容显示到界面上
        self.lineEdit_rootPath.setText(rootpathstr)

    def save(self):
        # 保存配置文件
        pass
        
    def RSConfig(self):
        #读取配置文件并呈现信息
        pass

    def checkPath(self):
        #检查路径是否存在
        pass

    def createPath(self):
        pass


from guiBasis.index import Ui_Index
class IndexWindow(QDialog,Ui_Index):
    """docstring for IndexWindow"""
    def __init__(self, parent=None):
        super(IndexWindow, self).__init__(parent)
        self.setupUi(self)
        self.layout  = QHBoxLayout()
        from PySide.QtGui import QLabel
        self.label = QLabel("House")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


from guiBasis.TriangularNumber import Ui_TriangularNumber
from PySide.QtCore import QObject
from PySide.QtCore import SIGNAL

class TriangularNumberWindow(QDialog,Ui_TriangularNumber):
    """docstring for TriangularNumberWindow"""
    def __init__(self,parent=None):
        super(TriangularNumberWindow, self).__init__(parent)
        self.setupUi(self)

        self.checkBox_triangularNumber.clicked.connect(self._set_GTNListcheckBox)
        self.checkBox_triangular.clicked.connect(self._set_GTNcheckBox)
        QObject.connect(self.buttonBox, SIGNAL("accepted()"), self._Proccessor)


    def _set_GTNListcheckBox(self):
        """该功能主要针对界面里的和堆垒三角数相关的几个控件
        设置其的可用性"""
        #判断下按钮是否被选中
        checkState = self.checkBox_triangularNumber.checkState()
        trueOrFalse = False
        print trueOrFalse
        if checkState == Qt.Checked:
            trueOrFalse = True
        self.checkBox_evenSeq.setEnabled(trueOrFalse)
        self.checkBox_pascal.setEnabled(trueOrFalse)
        self.checkBox_LongSeq.setEnabled(trueOrFalse)
        self.checkBox_sortSeq.setEnabled(trueOrFalse)

    def _set_GTNcheckBox(self):
        """该功能是针对界面里的和堆垒三角相关的几个控件
        设置其可用性"""
        checkState = self.checkBox_triangular.checkState()
        trueOrFalse = False
        print trueOrFalse
        if checkState == Qt.Checked:
            trueOrFalse = True

        self.checkBox_HLayout.setEnabled(trueOrFalse)
        self.checkBox_VLayout.setEnabled(trueOrFalse)
#这个是个用于产生一个时间目录的
    def get_time(self):
         """获取当前时间，次级根目录""" 
         import time        
         return time.strftime("%y.%m.%d-%H-%M")
    def _createFileName(self,gtntype,N):
        """生成三角形文件名
            gtntype是输出类型"""
        result = self.get_time()
        result = result+'_'+gtntype
        result = result+'_N='+str(N)

        return result

    def _Proccessor(self):
        """开始生成所需要要生成的
        三角形内容"""
        import basic.XMLConfig
        from core import plotTriangle
        if len(str(self.lineEdit_Number.text()))<1:
            msg = QMessageBox()
            msg.setText(QApplication.translate("Cannot get N", "N未输入", None, QApplication.UnicodeUTF8))
            msg.setWindowTitle(QApplication.translate("Error", "错误", None, QApplication.UnicodeUTF8))
            msg.show()
            
        else:
            MaxLen =  int(str(self.lineEdit_Number.text()))
            print MaxLen
            #首先判断选择
            rootPath = basic.XMLConfig.getRootPath()
       
            if rootPath[len(rootPath)-1] != '\\':
                rootPath = rootPath + '\\'
            print rootPath
            tr = plotTriangle.CreateGTNTriangel()
            tr._set_root_path(rootPath)
            if self.checkBox_triangular.isChecked() == True:
                """要对外生成堆垒三角了"""           
                print "----堆垒三角处理开始-----"  
                if self.checkBox_VLayout.isChecked() == True:
                    #要生成垂直三角                
                     for x in xrange(1,MaxLen):
                        tr.oneRow_with_Sum_verticalV3(' ',True,x,self._createFileName('GTN_VLayout',MaxLen))

                if self.checkBox_HLayout.isChecked() == True:
                    #要生成水平三角
                    for x in xrange(1,MaxLen):
                        tr.oneRow_with_Sum(x,self._createFileName('GTN_HLayout',MaxLen))                 
                print "----堆垒三角处理结束-----"  
            if self.checkBox_triangularNumber.isChecked() == True:
                #这边是列出内容的
                #列出方法是，水平优先，垂直优先，
                print "----堆垒三角值处理开始-----"  
                if self.checkBox_pascal.isChecked()==True:
                    #pascal 一一水平投影
                    tr._PascalTriangle_List(MaxLen,self._createFileName('P',MaxLen))

                if self.checkBox_evenSeq.isChecked()==True:
                    tr._Projection_EvenSeq(MaxLen,self._createFileName('E',MaxLen))

                    #垂直投影
                if self.checkBox_LongSeq.isChecked()==True:
                    tr._MetaLongSeq(MaxLen,self._createFileName('L',MaxLen))
                if self.checkBox_sortSeq.isChecked()==True:
                    tr._MetaShortSeq(MaxLen,self._createFileName('S',MaxLen))
                print "----堆垒三角值处理结束-----"  

class MainWindow(QMainWindow,Ui_MainWindow):
    """docstring for MainWindow--这个是主界面的类"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.passcal = PascalWindow()
        self.About = AboutWidnow()
        self.Setting = SettingWindow()
        self.GTNWindow = TriangularNumberWindow()
        self.setupUi(self)
        self.actionSouq.triggered.connect(self.show_passcal)
        self.actionAbout.triggered.connect(self.about)
        self.actionStt.triggered.connect(self.setting)
        self.action_gtn.triggered.connect(self.show_gtnWindow)
        self.indexPage = IndexWindow()
        self.subWindow_Index = self.mdiArea.addSubWindow(self.indexPage)
        self.subWindow_Index.showMaximized()
    def show_passcal(self):
        """显示计算堆垒三角相关计算界面-生成图像的"""
        self.passcal = PascalWindow()
        subWindow2 = self.mdiArea.addSubWindow(self.passcal)
        subWindow2.resize(300,370) #定制窗口大小
        #应该要限制下窗口大小
        
        self.passcal.show()
    def show_gtnWindow(self):
        """显示堆垒类三角值的生成窗口"""
        self.GTNWindow = TriangularNumberWindow()
        subWindow3 = self.mdiArea.addSubWindow(self.GTNWindow)
        subWindow3.show()
        subWindow3.resize(490,320) 
        #定制窗口大小

    def about(self):
        self.About.show() 

    def setting(self):
        self.Setting.show()
           
    
if __name__ == '__main__':    
    app = QApplication(sys.argv)    
    # form = LoginForm()    
    # form.show() 
    _MainWindow = MainWindow()
    _MainWindow.show()
    # a = IndexWindow()
    # a.show()     
    sys.exit(app.exec_())
