# coding=utf-8
import tensorflow as tf
# tf对数据类型要求比python高许多，就要定义 清楚才行
v_one = tf.Variable(3)
# 这个是变量
c_two = tf.constant(1)
# 这个是常量1，而且 这个变量必须要给值，不行的话就给placeholder并且给出类型
input1 = tf.placeholder(tf.int32)
input2 = tf.placeholder(tf.int32)
print(v_one)
# tf里面的都是张量，可以打印出来看看
# tf读多维的从外往里面 读，然后shape显示是从左到右

output = tf.matmul(input1, input2)
# 两个tensor叉乘，tensorflow里面一切都是tensor
sess = tf.Session()
# print(sess.run(v_one.initializer.run()))

rst = sess.run(output, feed_dict={input1:[[1, 2]], input2:[[3], [1]]})
print(rst)
# 这样子就能显示出来结果5
# sess.close()
# 或者用with来打开session,不关也无所谓了
# g = tf.Graph()
# # 这个就是图，只认识图里面的数据，不认识图外面的数据，当然图外面也不认识图里面的数据
# with g.as_default():
#     sess = tf.Session()
#     print(sess.run(v_one))
# #     这个是会报错显示不出来的

sess.run(tf.global_variables_initializer())
print(sess.run(v_one))
# 这个就不会显示shape这些了，只显示数值
