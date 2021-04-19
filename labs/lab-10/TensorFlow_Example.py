# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100*np.max(predictions_array),
                                         class_names[true_label]),
               color=color)

def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

print(tf.__version__)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Download dataset
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Setup new test image
new_image_name = "test_image_3.PNG"
new_image_type = 8
new_image_labels = np.array([new_image_type])
new_image = Image.open(new_image_name);
new_image = ImageOps.grayscale(new_image)
new_image = ImageOps.invert(new_image)
new_image = new_image.resize((28, 28))

# Save image for lab notebook
new_image.save('scaled_' + new_image_name)

# Finish converting image
new_image = np.array(new_image) / 255
new_image = (np.expand_dims(new_image, 0))

print(test_labels[0])
print(new_image_labels[0])

# Convert dataset into 255 color images
train_images = train_images / 255.0
# test_images = test_images / 255.0

# Setup training model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# Compile training model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train on the model for x epochs
model.fit(train_images, train_labels, epochs=10)

# Evaluate test images
test_loss, test_acc = model.evaluate(new_image,  new_image_labels, verbose=2)
print('\nTest accuracy:', test_acc)

# With the model trained, setup a prediction model
probability_model = tf.keras.Sequential([model,
                                         tf.keras.layers.Softmax()])
predictions = probability_model.predict(new_image) # Predict images

# Plot Predictions
# num_rows = 5
# num_cols = 3
# num_images = num_rows*num_cols
# plt.figure(figsize=(2*2*num_cols, 2*num_rows))
# for i in range(num_images):
#     plt.subplot(num_rows, 2*num_cols, 2*i+1)
#     plot_image(9000 + i, predictions[9000 + i], test_labels, test_images)
#     plt.subplot(num_rows, 2*num_cols, 2*i+2)
#     plot_value_array(9000 + i, predictions[9000 + i], test_labels)
# plt.tight_layout()
# plt.show()

# Plot Single Prediction
i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], new_image_labels, new_image)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  new_image_labels)
plt.show()