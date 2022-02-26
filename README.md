[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/abdassalamahmad/gender-classification/main/multiplefaces.py)
<a href="https://www.kaggle.com/abdassalamahmad/gender-classification-94"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>
# Face-Detection & Gender-Classification
Face detection using MTCNN library by drawing a rectangle on every face, <br> then running Xception pre-trained model on that face to classify the gender.<br>
You can use it directly from your camera or from any picture stored on your device **by clicking the streamlit badge in the top.**

## Model Demo

https://user-images.githubusercontent.com/83673888/155728628-63d45522-2f6e-4e01-8595-3a4214885a34.mp4

<br>**Try the model yourself from [here](https://share.streamlit.io/abdassalamahmad/gender-classification/main/multiplefaces.py)**

## About the Dataset
#### Data Source
I've used 2 datasets:
* https://www.kaggle.com/cashutosh/gender-classification-dataset
* https://www.kaggle.com/ashishjangra27/gender-recognition-200k-images-celeba

#### Dataset Information
The first dataset contatins over 47K images of males and females with over cropped faces<br>
![1st dataset example](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/Dataset_examples/1st.jpg)<br>
The second dataset contains over 200K images of males and females without over cropping faces<br>
![2nd dataset example](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/Dataset_examples/2nd.jpg)<br>


## Short Description of the Files
1. [gender_classification_training_94%.ipynb](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/gender_classification_training_94%25.ipynb) : **Training the model on two different datasets to get the best results.**
* Used transfer learning to get Xception model pretrained on Imagnet.
* Freeze its CNN layers and re-train the dense layers.
* Used callbacks to save the best model.
* Did some data augmentation to prevent overfitting and generalize the model.
* Evalutaing the model, Achieved 94% accuracy.


2. [multiplefaces.py](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/multiplefaces.py) : **Predict gender of every face detected.**
* Used MTCNN library to detect faces.
* Used matplotlib to draw a blue rectangle on male faces and red one on female faces.
* Get the cropped face and feed it to the Xception pre-trained model to predict the gender.
* **Count the number of male and female faces in the picture.**
* It deploy the trained model to streamlit cloud.
* You can test the model after depoyment to streamlit directly from your phone/laptop camera or from any picture stored on your device. 

3. [xception_v5_03_0.939.h5](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/xception_v5_03_0.939.h5) : **Best model from training saved in this binary format to load it easily.**
4. [requirements.txt](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/requirements.txt) : **Virtual environment setup** 
5. [packages.txt](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/packages.txt) : **To handle an error when deploying to streamlit**

## How to reproduce this model
1. clone this repo to get all the code and pre-trained model.
2. (optional if you want to retrain the model) download the 2 datasets from here [1st](https://www.kaggle.com/cashutosh/gender-classification-dataset/download) and [2nd](https://www.kaggle.com/ashishjangra27/gender-recognition-200k-images-celeba/download), **OR** you can use the notebook I edited on kaggle from [here](https://www.kaggle.com/abdassalamahmad/gender-classification-94) and it will automatically download these two datasets.
3. make sure you are on the cloned repo folder, then run this command to install all requirements.
```py
pip install -r requirements.txt
```
4. (optional) you can open the [training file](https://github.com/AbdassalamAhmad/Gender-Classification/blob/main/gender_classification_training_94%25.ipynb) and retrain for longer time to get better accuracy or you can explore the dataset. 
5. open your terminal and cd to project folder and run this command to run the **detection and classification program** locally
```py
streamlit run multiplefaces.py
```
6. Now, you can test the model, you can take photos from your device camera or upload a picture from your device.<br>
then the prgram will output a picture with the detected faces (**blue for males, red for females**) and the count of faces in the picture.


## Resources and Note
I have used these resources to build my project
* https://www.kaggle.com/dipeshmalhotra/gender-classification-96-accuracy (gender classification)
* https://machinelearningmastery.com/how-to-perform-face-detection-with-classical-and-deep-learning-methods-in-python-with-keras (Face detection)

It took me a while to combine these resourses (and find them in the first place) to build this project.<br>

If you like this project, I appreciate you starring this repo.<br>
Please feel free to fork the content and contact me on my [LinkedIn account](https://www.linkedin.com/in/abdassalam-ahmad/) if you have any questions.
