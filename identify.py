from PIL import Image
from pytesseract import *
# 加载图片
image = Image.open('v.jpg')
# 识别过程
text = image_to_string(image)
print(text)