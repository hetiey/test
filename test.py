import tensorflow as tf
import numpy as np
z=np.random.randint(0,10,size=[10])
x=np.random.rand(10)
xx = 1-x
xxx = xx*xx
y=tf.one_hot(z,10,on_value=1,off_value=None,axis=0)
yy = y*x
yyy = xxx*y*x
with tf.Session()as sess:
    print(z)
    print(x)
    print(yy)
    print(sess.run(y))
    print(sess.run(yy))
    print(sess.run(yyy))