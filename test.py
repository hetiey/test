import tensorflow as tf
import numpy as np
z=np.random.randint(0,10,size=[10])
x=np.random.rand(0,1,size=[10])
y=tf.one_hot(z,10,on_value=1,off_value=None,axis=0)
with tf.Session()as sess:
    print(z)
    print(x)
    print(sess.run(y))