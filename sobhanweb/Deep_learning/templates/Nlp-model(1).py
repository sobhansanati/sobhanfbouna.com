import keras
import tensorflow as tf 




model = tf.keras.Sequential([
    tf.keras.layers.Embedding(toknize.vocab_size,64),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tk.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(64,activation='sigmoid'),
])