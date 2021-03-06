import tensorflow as tf  
#our NN's output  
logits=tf.constant([[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0]])  
#step1:do softmax  
y=tf.nn.softmax(logits)  
#true label  
t = 1 - y
tt = t * t
y_=tf.constant([[0.0,0.0,1.0],[0.0,0.0,1.0],[0.0,0.0,1.0]])  
#step2:do cross_entropy  
t1 = y_ * tf.log(y)
t2 = tt * y_ * tf.log(y)
cross_entropy = -tf.reduce_sum(y_*tf.log(y))  
#do cross_entropy just one step  
#cross_entropy2=tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits, y_))#dont forget tf.reduce_sum()!!  
  
with tf.Session() as sess:  
    softmax=sess.run(y)
    ob1 = sess.run(t1)
    ob2 = sess.run(t2)
    c_e = sess.run(cross_entropy)  
    #c_e2 = sess.run(cross_entropy2)  
    print("step1:softmax result=")  
    print(softmax)  
    print("step2:cross_entropy result=")  
    print(c_e)  
    print(ob1)
    print(ob2)
    #print("Function(softmax_cross_entropy_with_logits) result=")  
    #print(c_e2)  
