import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing import image

# _________________ Import moudlues _____________


class ClassifyTarget:
    __class_name = {0: "COVID", 1: "NORMAL", 2: "PNEUMONIA"}
    __prediction_result = None

    def __init__(self, img_url):

        ai_model = tf.keras.models.load_model(
            "F:\Current\Capstone website\model\model4")  # load the model

        img = image.load_img(img_url)
        img_array = image.img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        prediction = ai_model.predict(img_batch)
        self.__prediction_result = self.__class_name[np.argmax(prediction)]

    def get_result(self):
        return self.__prediction_result


# model = ClassifyTarget(
#     "F:\Current\Capstone website\static\img_uploaded\covid.png")
# print(f"\n\n\n{model.get_result()}")
