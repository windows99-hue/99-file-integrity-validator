# 99 文件完整性验证器

> DJI flip! 好耶！

这是一个可以验证文件夹中的文件完整性的小工具，很适合大项目拷贝，尤其是照片类

![python: 3.13](https://img.shields.io/badge/python-3.13-blue)

## 安装

~~~shell
pip install -r requirements.txt
~~~

## 使用

~~~shell
python main.py
~~~

按照程序要求选择源文件夹和目标文件夹，程序会对比两文件夹中名字一样的所有文件的MD5

程序运行完成后，会显示核对情况

![error information](https://github.com/windows99-hue/99-file-integrity-validator/blob/main/images/4091e43c4ad813129b8006053f682485.png?raw=true)

全部文件完整则显示

`所有文件 MD5 匹配!`

## 写在后面

本程序使用MIT协议，如果您对程序有任何建议或者bug反馈，请fork我的仓库或者向我提出Issue

祝您使用愉快！
