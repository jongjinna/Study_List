import tensorflow as tf

# Data
x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

# W, b initialize
W = tf.Variable(2.9)
b = tf.Variable(0.5)

learning_rate = 0.01

for i in range(1000):
  # Gradient descent
  with tf.GradientTape() as tape:
    hypothesis = W*x_data + b
    cost = tf.reduce_mean(tf.square(hypothesis-y_data))
  W_grad, b_grad = tape.gradient(cost, [W,b])
  W.assign_sub(learning_rate * W_grad)
  b.assign_sub(learning_rate * b_grad)
  # assign_sub 는 python의 a -= b 와 같은 역할
  if i % 10 == 0:
    print("{:5}|{:10.4}|{:10.4}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))
    
print(W*5+b)
print(W*2.5+b)