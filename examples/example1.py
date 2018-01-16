import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.2)
node3 = tf.add(node1, node2)
# node3 = node1 + node2

sess = tf.Session()
print("node1:", node1, "node2:", node2)
print("node3:", node3)

print("sess.run(node1, node2)", sess.run([node1, node2]))
print("sess.run(node3)", sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
print(sess.run(adder_node, feed_dict={a: [1, 2], b: [2.2, 5.6]}))

add_and_triple = adder_node * 3
print(sess.run(add_and_triple, feed_dict={a: 3.0, b: 2.1}))

