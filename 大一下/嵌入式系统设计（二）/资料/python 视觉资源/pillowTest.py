from PIL import Image
im = Image.open('dog.jpg')
print(im)
print(im.format,im.size,im.mode)
im.show()    #显示图片
im.save('dog.BMP')  #保存图片

#设置要拷贝的区域  
box = (100, 100, 500, 500)
# 将im表示的图片对象拷贝到region中，大小为(400*400)像素。
# 这个region可以用来后续的操作(region其实就是一个Image对象)，
# box变量是一个四元组(左，上，右，下)。  
region  = im.crop(box)

# 从字面上就可以看出，先把region中的Image反转180度，然后再放回到region中。  
region = region.transpose(Image.ROTATE_90)
#粘贴box大小的region到原先的图片对象中。  
im.paste(region, box)
im.save('dogA.jpg')

r,g,b = im.split()#分割成三个通道  
im = Image.merge("RGB", (b, g, r))  #将b,r两个通道进行翻转。 
im.save('rgb.jpg')


#几何转变
out = im.resize( ( 128,128))
out = im.rotate(45)
out.show()

# 左右翻转
out = im.transpose(Image.FLIP_LEFT_RIGHT)
# 上下反向
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out = im.transpose(Image.ROTATE_90)
out.show()


#模式转换
# 黑白
am = im.convert('L')
am.show()


#图像增强
#1.滤镜 
out = im.filter(ImageFilter.DETAIL)     #detail滤镜
out.show()


#2.直接操作像素点
out = im.point(lambda i : i *1.2)  #每个像素点亮度增20
out.show()








