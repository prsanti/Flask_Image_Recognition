"""
Model Functions for Image Preprocessing and Prediction
"""

from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

# Loading model
model = load_model("digit_model.h5")

# Preparing and pre-processing the image
def preprocess_img(img_path):
    """
    Load an image from a filesystem path or a file-like object, resize to 224x224 RGB,
    normalize to [0, 1], and add a batch dimension.

    Args:
        img_path (str): string

    Returns:
        img_shape: array of shape (1, 224, 224, 3)
    """
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 224, 224, 3)
    return img_reshape


# Predicting function
def predict_result(predict):
    """
    Run model prediction and return the argmax class for the first item in the batch.

    Args:
        predict (batch): a numpy array of shape (N, 224, 224, 3)

    Returns:
        int: predicted class index for the first element
    """
    pred = model.predict(predict)
    return np.argmax(pred[0], axis=-1)
