[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/abdassalamahmad/gender-classification/main/multiplefaces.py)

# Face-Detection & Gender-Classification
Face detection using MTCNN library by drawing a rectangle on every face, <br> then running Xception pre-trained model on that face to classify the gender.<br>
You can use it directly from your camera or from any picture stored on your device.

## Model Demo
![Model Demo](https://github.com/AbdassalamAhmad/Predicting-Clothing-Types/blob/main/predicting-clothing-types.gif)

## About the Dataset
#### Data Source
I've used 2 datasets:
* https://www.kaggle.com/ashishjangra27/gender-recognition-200k-images-celeba
* https://www.kaggle.com/cashutosh/gender-classification-dataset

#### Dataset Information
The first dataset contatins over 47K images of males and females with over cropped faces<br>
![1st dataset example](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/Dataset_examples/1st.jpg)<br>
The second dataset contains over 200K images of males and females without over cropping faces<br>
![2nd dataset example](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/Dataset_examples/2nd.jpg)<br>


## Short Description of the Files
1. [Training_the_model](https://github.com/AbdassalamAhmad/Gender-Classification/tree/main/Training_the_model) folder has
 [face-detection-gender-classification-94%25.ipynb](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/Training_the_model/face-detection-gender-classification-94%25.ipynb) : **Training the model on two different datasets to get the best results.**
* Used transfer learning to get Xception model pretrained on Imagnet.
* Freeze its CNN layers and re-train the dense layers.
* Used callbacks to save the best model.
* Did some data augmentation to prevent overfitting and generalize our model.
* Evalutaing the model, Aciheved 94% accuracy.


2. [multiplefaces.py](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/multiplefaces.py) : **predict gender of every face detected.**
* Used MTCNN library to detect faces.
* Used matplotlib to draw a blue rectangle on every male face and red one on every female face.
* Get the cropped face and feed it to the Xception pre-trained model to predict the gender.
* Count the number of male and female faces in the picture
* It deploy the trained model to streamlit cloud.
* you can test the model after depoyment to streamlit directly from your phone/laptop camera or from any picture stored on your device. 

3. hgjadj














## Resources and Note
I have used these resources to build my project
* https://www.kaggle.com/dipeshmalhotra/gender-classification-96-accuracy (gender classification)
* https://machinelearningmastery.com/how-to-perform-face-detection-with-classical-and-deep-learning-methods-in-python-with-keras (Face detection)

It took me a while to combine these resourses (and find them in the first place) to build this project.<br>

If you like this project, I appreciate you starring this repo.<br>
Please feel free to fork the content and contact me on my [LinkedIn account](https://www.linkedin.com/in/abdassalam-ahmad/) if you have any questions.
