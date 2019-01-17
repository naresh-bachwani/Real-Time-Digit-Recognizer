# Digit Recognizer

This is a deep neural network model for identifying images of handwritten digits. The model is trained on a set of 42000 images taken from Kaggle. It supports real time digit recognition using an drawing tool made using OPENCV. 

The data is taken from the MNIST dataset ("Modified National Institute of Standards and Technology"), which is the de facto “hello world” dataset of computer vision. Since its release in 1999, this classic dataset of handwritten images has served as the basis for benchmarking classification algorithms. As new machine learning techniques emerge, MNIST remains a reliable resource for researchers and learners alike.

Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. Each pixel has a single pixel-value associated with it, indicating the lightness or darkness of that pixel, with higher numbers meaning darker. This pixel-value is an integer between 0 and 255, inclusive.

Files model.json and model.h5 contains the weights of model already trained on my PC.

# Features 

-Real time digit recognition using  an interactive drawing tool

### Requirements
*   [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
*   [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation
*   [Kivy](https://kivy.org/doc/stable/) - for GUI
*   Data visualisation libraries such as Seaborn and Matplotlib.
*   Data processing library - Pandas
*   Keras 
*   Tensorflow

