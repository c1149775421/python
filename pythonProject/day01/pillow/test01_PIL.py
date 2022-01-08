from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
m=Image.open("涛生02.jpg")
print(m.format,m.size,m.mode)
size=(1080,1440)

m.thumbnail(size)#缩略图
m.save("02.jpg")
