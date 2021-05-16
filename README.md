# ScreanShot
# Learning points

如上，我们可以看到if __name__ == '__main__'相当于Python模拟的程序入口，Python本身并没有这么规定，这只是一种编码习惯。由于模块之间相互引用，不同模块可能有这样的定义，而程序入口只有一个。到底哪个程序入口被选中，这取决于__name__的值
<https://blog.csdn.net/yjk13703623757/article/details/77918633/>


## Python 利用百度OCR实现截图转文字自动保存为Word文件

<https://blog.csdn.net/mbh12333/article/details/99949059>

申请 百度 API
<https://blog.csdn.net/weixin_42644340/article/details/89303805>

## python 控制鼠标

<https://zhuanlan.zhihu.com/p/147543411>
<https://www.jb51.net/article/186692.htm>

pynput

<https://www.cnblogs.com/tobe-goodlearner/archive/2020/05/17/tutorial-pynput.html>

## Python 关键词汇

with as
<http://blog.kissdata.com/2014/05/23/python-with.html>

## Python 生成exe

### 初始化 安装
pip install pyinstaller

### 生成 exe
pyinstaller -F -w main.py 
--hidden-import=queue
Parameters:--hidden-import=queue -w -F $FileName$

pyinstaller --hidden-import=queue -w -F main.py

pyinstaller --hidden-import=pkg_resources -F main.py

### 注意项
main.py 可变..需注意指定文件夹 cd到实际文件的文件夹

！！！关闭安全卫士！！
<https://blog.csdn.net/qq_32939413/article/details/86564611>

#### exe 太大的解决办法
<https://www.zhihu.com/question/281858271/answer/1548304414>
<https://blog.csdn.net/weixin_42277380/article/details/112648319>

创建虚拟环境
conda create -n MS_Py_Creation python==3.6  #创建虚拟环境

conda activate MS_Py_Creation               #激活虚拟环境

conda deactivate                          #退出虚拟环境

#### uctbase.dll 报错
网上下载
ucrtbase.dll 放到报错路径

<https://blog.csdn.net/weixin_42646103/article/details/101794074>

MS 测试无效：
重装uninstall pyinstaller 
pip uninstall pyinstaller 
！！！关闭安全卫士！！
升级pip

#### 生成exe 报Failed to execute script main解决

调试时增加 try: except 报错信息
pyinstaller 去掉-w  显示命令窗口运行exe, 会出现报错信息，然后根据信息查找问题

用到 pynput 时, MS 测试有效：
pip install pynput==1.6.8 ///打包成功

以下无效，但注意：

文件中使用了第三方库的打包方式
在打包之前务必找到第三方库的包，把包复制到到跟myfile.py同目录下，然后再使用以上2种方式打包，否则会打包失败或者即使打包成功，程序也会闪退。

下面演示一下使用了第三方库的打包方式
