import tensorflow as tf

# Check the number of available GPUs
gpus = tf.config.list_physical_devices('GPU')
num_gpus = len(gpus)
print(num_gpus)

cifar = tf.keras.datasets.cifar100

# Enter input shape into model, will resize the cifar100 input shape
new_input_shape = (32, 32, 3)

# Load CIFAR-100 data
(x_train, y_train), (x_test, y_test) = cifar.load_data()

# Resize images to the new input dimensions
x_train_resized = tf.image.resize(x_train, new_input_shape[:2])
x_test_resized = tf.image.resize(x_test, new_input_shape[:2])

# Create the ResNet50 model
model = tf.keras.applications.ResNet50(
        include_top=True,
        weights=None,
        input_shape=new_input_shape,
        classes=100,  # CIFAR-100 has 100 classes
)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

# Train the model, change batch_size as desired
model.fit(x_train_resized, y_train, epochs=1, batch_size=128)