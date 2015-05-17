# -*- coding: utf-8 -*-
#

import PathKnife 
import XMLConfig


class DirectoryManager(object):
	"""目录管理类，用于根据参数自动创建存放生成结果的
	目录"""
	rootPath = ""
	pk = PathKnife.PathKnife()
	def __init__(self):
		super (DirectoryManager, self).__init__()
	def  _initRootDir(self):
		"""从配置文件当中获取存放结果"""
		self.rootPath = XMLConfig.getRootPath("..")
		print "从配置文件当中获取存放结果" + self.rootPath


	def _getRootPath(self):
		if  len(self.rootPath)>1:
			print "已初始化cfg好：:"+self.rootPath
		else:
			self._initRootDir()
			print "刚刚读取cfg"+self.rootPath


	def _makePath(self, varset=None):
		"""创建所有所有子目录，根据输入的参数类型
		varset是一个结构体，存放各种参数，用于图像命名等"""
		if len(self.rootPath) < 2:
			#如果说根目录尚未创建初始化，则要先初始化
			self._getRootPath()
		self.pk.set_root_path(self.rootPath)
		self.pk.make_subpath(varset)#生成子目录
		pass





if __name__ == '__main__':
	dm = DirectoryManager()
	dm._makePath(["1234","4321"])