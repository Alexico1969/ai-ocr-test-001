import cv2 as cv
import keras_ocr
from matplotlib import pyplot as plt
import glob

pipeline = keras_ocr.pipeline.Pipeline()

files = [f for f in glob.glob("*.png")]
images = list(map(cv.imread, files))
prediction_groups = pipeline.recognize(images)

fig, axs = plt.subplots(nrows=len(images), figsize=(30,30))
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)

index = 0
for predicted_image in prediction_groups:
    for text, box in predicted_image:
        if text:
            print(f"Word found in {files[index]} : {text}")
        else:
            print(f"No words found in {files[index]}")
    index += 1