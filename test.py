#导入手写数字数据集
from keras.datasets import mnist
#导入画图包
import matplotlib.pyplot as plt 

#读取数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#画图
#给定一个画出第三十张图片的figure，然后展示不展示给用户看
plt.figure()
plt.imshow(x_train[30], cmap='gray')
plt.show()