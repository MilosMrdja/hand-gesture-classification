# 1. Mount to google colab

# from google.colab import drive
# import os
#
# drive.mount('/content/drive')
#
# !unzip -q "/content/drive/MyDrive/handgesture.zip" -d /content/dataset
#
# print("Unzipping complete!")

# 2. Preprocess - loading dataset, create labels and batches for train
# import tensorflow as tf
# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.metrics import classification_report, accuracy_score, precision_recall_fscore_support
#
# TRAIN_DIR = '/content/dataset/train/train'
# TEST_DIR = '/content/dataset/test/test'
#
# IMG_SIZE = (224, 224)
# BATCH_SIZE = 32
#
# print("Loading datasets...")
# train_ds = tf.keras.utils.image_dataset_from_directory(
#     TRAIN_DIR, shuffle=True, batch_size=BATCH_SIZE, image_size=IMG_SIZE
# )
#
# test_ds = tf.keras.utils.image_dataset_from_directory(
#     TEST_DIR, shuffle=False, batch_size=BATCH_SIZE, image_size=IMG_SIZE
# )
#
# class_names = train_ds.class_names
# print(f"Detected Classes: {class_names}")

# 3.
# data_augmentation = tf.keras.Sequential([
#     layers.RandomFlip("horizontal"),  # Hand can be left or right
#     layers.RandomRotation(0.15),      # Hand isn't always perfectly vertical
#     layers.RandomZoom(0.15),          # Hand distance varies
#     layers.RandomTranslation(0.1, 0.1) # Hand moves around the frame
# ])

# base_model = tf.keras.applications.MobileNetV2(
#     input_shape=IMG_SIZE + (3,),
#     include_top=False,
#     weights='imagenet',
#     alpha=0.35 # low capacity
# )
# base_model.trainable = False
#
# inputs = tf.keras.Input(shape=IMG_SIZE + (3,))
# x = data_augmentation(inputs)
# x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
# x = base_model(x, training=False)
# x = tf.keras.layers.GlobalAveragePooling2D()(x)
# x = tf.keras.layers.Dropout(0.5)(x) # master memorizes, killing 50% neurons
#
# outputs = tf.keras.layers.Dense(len(class_names), activation='softmax')(x)
#
# model = tf.keras.Model(inputs, outputs)
#
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
# # --- 3. TRAINING ---
# print("Starting training with Augmentation and Alpha=0.35...")
# # Increased epochs to 15 because Augmentation makes it harder to learn
# history = model.fit(train_ds, validation_data=test_ds, epochs=15)