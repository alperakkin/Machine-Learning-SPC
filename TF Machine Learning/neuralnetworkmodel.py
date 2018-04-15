import tensorflow as tf
import numpy as np


x_data= np.array([[0,0],[0,1],[1,0],[1,1]])
y_data= np.array([[1],[0],[0],[1]])

n_input=2
n_hidden=10
n_output=1

learning_rate=0.1
epochs=10000


x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)

#weights

w1=tf.Variable(tf.random_uniform([n_input,n_hidden],-1.0,1.0))
w2=tf.Variable(tf.random_uniform([n_hidden,n_output],-1.0,1.0))

# Bias

b1= tf.Variable(tf.zeros([n_hidden]),name='Bias1')
b2= tf.Variable(tf.zeros([n_output]),name='Bias2')


l2=tf.sigmoid(tf.matmul(x,w1)+b1)
hy=tf.sigmoid(tf.matmul(l2,w2)+b2)


cost=tf.reduce_mean(-y*tf.log(hy)-(1-y)*tf.log(1-hy))
optimizer= tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)



init=tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init)

    for step in range(epochs):
        session.run(optimizer,feed_dict={x: x_data, y: y_data})


        if step % 1000 ==0:
            print(session.run(cost,feed_dict={x:x_data , y: y_data}))


    answer=tf.equal(tf.floor(hy+0.5),y)
    accuracy=tf.reduce_mean(tf.cast(answer,'float'))

    print(session.run([hy],feed_dict={x: x_data, y:y_data}))
    print('Accuracy: ', accuracy.eval({x: x_data,y: y_data }))

    #Tahmin
    test_data=[[0.12,0.76]]
    predicted = session.run([hy], feed_dict={x: test_data})
    print(predicted)
    print('Accuracy: ', accuracy.eval({x: x_data, y: y_data}))