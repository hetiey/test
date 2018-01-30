import tensorflow as tf
import numpy as np
z=np.random.randint(0,10,size=[10])
a = tf.Variable(tf.random_normal([10,1],seed=1))
y=tf.one_hot(z,10,on_value=1,off_value=None,axis=0)
aa = 1-a
aaa = aa*aa
yy = y*a
yyy = aaa * y * a
init = tf.global_variables_initializer()
sess.run(init)
with tf.Session()as sess:
    print(z)
    print(sess.run(a))
    print(sess.run(aa))
    print(sess.run(aaa))        
    print(sess.run(y))
    print(sess.run(yy))
    print(sess.run(yyy))