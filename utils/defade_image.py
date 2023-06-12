# Import the helper functions to be used in program
import tensorflow as tf
import cv2
from defade_backend.settings import BASE_DIR

# Load the trained saved model
model = tf.keras.models.load_model(BASE_DIR / "utils" / "defade_image_model")
class_names = ["fake", "real"]

# Create a helper function to import an image and resize it to be able to be used with our trained model


def load_and_prepare_image(filename, img_shape=224):
    """
    Reads an image from filename, turns it into a tensor and reshapes it to
    (img_shape, img_shape, color_channels).
    """

    # Read in the image
    img = tf.io.read_file(filename)
    # Decode the read file into a tensor
    img = tf.image.decode_image(img)
    # Resize the image
    img = tf.image.resize(img, size=[img_shape, img_shape])
    # Rescale the image (get all values between 0 and 1)
    img = img / 255.

    return img


def pred_and_plot(model, filename, class_names=class_names):
    """
    Imports an image located at filename, makes a prediction with model
    and plots the image with the predicted class as the title.
    """

    # Import the target image and preprocess it
    image = load_and_prepare_image(filename)

    # Make a prediction on our image
    prediction = model.predict(tf.expand_dims(image, axis=0))

    # Add a logic for multiclass and get pred_class name
    if len(prediction[0]) > 1:
        prediction_class = class_names[tf.argmax(prediction[0])]
    else:
        # Select the prediction class from our list of class names
        prediction_class = class_names[int(tf.round(prediction))]

    return prediction_class


def check_image(image):
    prediction = pred_and_plot(model, image)
    return prediction