# -*- coding: utf-8 -*-  
import cv2
# from matplotlib import pyplot as plt
from pylab import *
 
# 添加中文字体支持
from matplotlib.font_manager import FontProperties
#font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc",size = 14)
 
# 载入图像
im = cv2.imread('cat.jpg')
 
# 颜色空间转换
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
 
# 显示原始图像
fig = plt.figure()
subplot(121)
plt.gray()
imshow(im)
title(u'彩色图')
axis('off')
# 显示灰度化图像
plt.subplot(122)
plt.gray()
imshow(gray)
title(u'灰度图')
axis('off')
 
show()
