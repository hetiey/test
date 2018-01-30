import tensorflow as tf
import numpy as np
z=np.random.randint(0,10,size=[10])
x=np.random.rand(10)
xx = 1-x
xxx = xx*xx
y=tf.one_hot(z,10,on_value=1,off_value=None,axis=0)
with tf.Session()as sess:
    print(z)
    print(x)
    print(xx)
    print(xxx)
    print(sess.run(y))