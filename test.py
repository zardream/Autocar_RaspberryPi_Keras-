from keras.datasets import mnist
import matplotlib.pyplot as plt 
import numpy as np 
import keras
#按照顺序连接的神经网络模型
from keras.models import Sequential
#Dense全连接层 Dropout扔掉增加鲁棒性增快速度 Flatten压缩纬度
from keras.layers import Dense, Dropout, Flatten
#二维卷积  按最大值池化
from keras.layers import Conv2D, MaxPooling2D

#构建序列式神经网络模型
model = Sequential()
#添加第一层：卷积层 32filters 卷积核大小， 激活函数  尺寸只有第一次要管，后面自动
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=input_shape))
#再添加一层卷积层
model.add(Conv2D(64, (3,3), activation=(2,2)))
#池化,缩小图片
model.add(MaxPooling2D(pool_size=(2,2)))
#随机丢掉一点数据
model.add(Dropout(0.25))
#降低维度压扁成一维
model.add(Flatten())
#全连接层,人为设定128
model.add(Dense(128, activation='relu'))
#随机丢掉一点数据
model.add(Dropout(0.5))
#最终全连接到输出层
model.add(Dense(num_classes,activation='relu'))
(x_train, y_train), (x_test, y_test) = mnist.load_data()

img_rows, img_cols = 28, 28
#reshape来自numpy，下面部分是为了转换数据类型并改变纬度，最后一个1是为了方便卷积核与其进行卷积操作
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

#归一化，将数据变到0，1之间方便其他模型使用
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

#将标签数据转换成为二进制数组
num_classes = 10
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print(y_test[5], 'result')