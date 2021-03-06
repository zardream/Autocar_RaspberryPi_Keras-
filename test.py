from keras.datasets import mnist
import matplotlib.pyplot as plt  
import keras
#按照顺序连接的神经网络模型
from keras.models import Sequential
#Dense全连接层 Dropout扔掉增加鲁棒性增快速度 Flatten压缩纬度
from keras.layers import Dense, Dropout, Flatten
#二维卷积  按最大值池化
from keras.layers import Conv2D, MaxPooling2D
#引入TensorBoard 通过可视化的直观图来观察
from keras.callbacks import TensorBoard

# step1 #
#数据读入以及预处理
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#展示一张当前数据
plt.figure()
plt.imshow(x_train[30],cmap='gray')
plt.show()
print(y_train.shape)
print(y_train[30])


# step2 #
#下面部分是为了转换数据类型,改变纬度，最后一个1是为了方便卷积核与其进行卷积操作
img_rows, img_cols = 28, 28
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)


# step3 #
#归一化，将数据变到0，1之间方便其他模型使用
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
print('x_train shape:', x_train.shape)

#将标签数据转换成为二进制数组
num_classes = 10
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


# step4 #
#构建序列式神经网络模型
model = Sequential()
#添加第一层：卷积层 32filters 卷积核大小， 激活函数  尺寸只有第一次要管，后面自动
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=input_shape))
#再添加一层卷积层
model.add(Conv2D(64, (3,3), activation='relu'))
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
model.add(Dense(num_classes,activation='softmax'))


# step5 #
#编译神经网络模型
#loss损失函数 optimizer优化器的选择 metrics训练指标列表
model.compile(loss=keras.losses.categorical_crossentropy,
			optimizer=keras.optimizers.Adadelta(),#Adadelta是自适应的学习速率，不需要人为设定
			metrics=['accuracy'])
#打开TensorBoard便于人们观察
tb = TensorBoard(log_dir='./logs',	#将数据存放到相同路径下的logs里
				 histogram_freq=1,	#按什么频率来计算直方图
				 batch_size=128, 	#用多少数据来计算直方图
				 write_graph=True,	#画神经网络结构图
				 write_grads=False,	#画梯度的图
				 write_images=False	#把训练每个阶段的图画出来
				 )
callbacks = [tb]


# step6 #
#训练神经网络模型
model.fit(x_train, y_train,
	batch_size=128, #梯度下降的时候每个batch包含的样本数    理论上选的越大越好，但比较浪费资源和时间，实际选一个小样本数就可以了，确定好了其他参数再用大batch
	epochs=12,		#训练多少轮结束
	verbose=1,		#是否显示训练的时候日志信息
	validation_data=(x_test,y_test),#用来验证的数据集
	callbacks=callbacks#回调，此处使用tensorboard
	)	


# step7 #
#评估神经网络模型
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


# step8 #
#使用神经网络进行预测
prediction = model.predict(x_test[20].reshape(1,28,28,1))#第一个是样本量为多少
#将每个都有值的矩阵转化为唯一解
prediction = prediction.argmax(axis=1)
plt.figure()
plt.imshow(x_test[20].reshape(28,28))
#增加一个标题
plt.text(0,-3,prediction,color='black')
plt.show()


# step9 #
#将模型保存
model.save('my_model.h5')
