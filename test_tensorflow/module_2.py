import tensorflow as tf


# Rank 0 - no dimensions
# Shape of 1, scalar
# Create a tensorflow variable here. Value, data type
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

# // Rank 1 tensors
rank1_tensor = tf.Variable(["Test"], tf.string)
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)
