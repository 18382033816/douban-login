# douban-login
豆瓣网验证码识别
1.利用文件保存，手动识别验证码
2.借助各种打码平台
3.借助第三方库
使用图像识别技术来识别图中的信息；
光学字符识别 OCR：OCR（Optical Character Recognition，光学字符识别）是指电子设备（例如扫描仪或数码相机）检查纸上打印的字符，通过检测暗、亮的模式确定其形状，然后用字符识别方法，将形状翻译成计算机文字的过程;
程序处理复杂验证码的方法：
  1．使用Google的开源项目 Tesseract；
安装Tesseract：
Ubuntu中安装：
	sudo apt-get install tesseract-ocr
pip install pytesseract
训练与测试：https://www.cnblogs.com/cnlian/p/5765871.html

简单的Python测试代码：
from PIL import Image
from pytesseract import *
image = Image.open('test1.jpg')
text = image_to_string(image)
print(text)
