from keras.datasets import mnist
import matplotlib.pyplot as plt 
import numpy as np 

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