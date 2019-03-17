import keras
import numpy
from keras.datasets import mnist
# 这个数据集已经包含进去了,但是里面的是链接，还要下载
from keras.models import Sequential
# 用的是序贯模型，通过顺序的方式叠加神经网络层
from keras.layers import Dense, Dropout, Flatten
# 用于防止过拟合的
from keras.layers import Conv2D, MaxPooling2D
# 前面的是卷积层，后面的是池化层
from keras import backend as K
# 这个是后台架构
batch_size = 128
# 一批喂给模型多少张图片，这是一共60000张，分批只是给其中的128张，每一批进行一次损失函数的估计
num_classes = 10
# 因为是数字，所以分类0到9，一共10类
epochs = 10
# 迭代多少次，多了电脑卡了，而且太多了会把过多特征全部提取出来，导致过拟合，就是提取的太细了，换成其他数据集可能就没那么好了
img_rows, img_cols = 28, 28
# 图片是28*28的灰度图，不是彩色图，彩色图是32*32
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 加载数据集

# 判断backend，theano，tensorflow三个后台，根据通道来区分
# 'backend'是后端函数，keras通过它来操作其他的后端执行代码

if K.image_data_format() == 'channels_first':
    # 区分后台是根据通道来的
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
#     (60000,1,28,28)，通道放中间的就是theano，这个是什么自己百度去
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    # 通道放在最后一个就是TensorFlow，就是这个1
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)


# 数据处理
x_train = x_train.astype(numpy.float32)
# 更改类型,别打错字了
x_test = x_test.astype(numpy.float32)
x_train /= 255
# 归一化处理，全部变成0到1之间的数
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# 处理标签
y_train = keras.utils.to_categorical(y_train, num_classes)
# 可以把5这个标签变成0000010000，就是数从前往1的0的个数，便于后面做比较
# 把2这个标签变成0010000000
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
# 选择模型，因为卷积神经网络是一层层的
model.add(Conv2D(32, kernel_size=(3, 3),
                 # 32个卷积和，每一个大小3*3
                 activation='relu',
                 # 激活函数
                 input_shape=input_shape))
# 输入
# 卷积层1
model.add(Conv2D(64, (3, 3), activation='relu'))
# 卷积层2
model.add(MaxPooling2D(pool_size=(2, 2)))
# 池化层的大小2*2，默认步长是1
# 池化，卷积和池化的位置不是绝对的
model.add(Dropout(0.25))
# 断开一部分连接，怕提取的太细致，扔掉百分之25的神经元
# 防止过拟合
model.add(Flatten())
# 压平，变成一维的
model.add(Dense(num_classes, activation='relu'))
# 全连接
model.add(Dropout(0.5))
# 还是为了防止过拟合
model.add(Dense(num_classes, activation='softmax'))
# 这个全连接是用来分类
# 这个激活函数就是用来做多分类的
# 全连接就是所有的卷积层之间互相都是连接的
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
# 定义损失函数和优化器
# 用什么评估模型
# 构建完之后进行编译
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1)
# 开始训练
score = model.evaluate(x_test, y_test, verbose=0)
# 进行测试
print('test loss:', score[0])
print('test accuracy:', score[1])
model.save('C:\\python_code\\20190316\\handwritingrecusingcnn.model')
