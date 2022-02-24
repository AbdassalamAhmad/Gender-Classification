import tensorflow as tf
#from tensorflow import keras
from mtcnn import MTCNN
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import streamlit as st
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from PIL import Image# to read & resize the image 

#declaring variables
size = 249 
target_size = (size,size)
crop_img = []
coords = [] #coordinates of the rectangle
male = [] # number of males in pic
female = [] # number of females in pic
predictions = []
result = []

#Load the model
model  = tf.keras.models.load_model("xception_v5_03_0.939.h5")

def main():
    st.title("Gender Classification")
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose the app mode",
    ["Predict gender from image", "Predict gender from camera"])

    if app_mode == "Predict gender from image":
        uploaded_file = st.file_uploader("Upload a picture of a person to predict its gender", type=['jpg', 'jpeg', 'png'])
        if uploaded_file is not None:
            st.title("Here is the picture you've uploded")
            
            image = Image.open(uploaded_file)
            pixels = img_to_array(image)
            # create the detector, using default weights
            detector = MTCNN()
            # detect faces in the image
            faces = detector.detect_faces(pixels)
            # get faces coordinates
            croped_img, coords= get_face_coords(uploaded_file, faces)

            #output the prediction
            result, predictions= predict_img(croped_img)
            # draw rectangle on every face
            draw_rect(coords, predictions)
            
            st.write(result)
            st.write("Males count:",len(male))
            st.write("Females count:",len(female))
            st.write("Faces count:",len(male)+len(female))
    elif app_mode == "Predict gender from camera":
        #take a picture from your camera
        picture = st.camera_input("Take a picture")
        if picture is not None:
            st.title("Here is the picture you've taken")
            image = Image.open(picture)
            #st.image(image)
            pixels = img_to_array(image)
            # create the detector, using default weights
            detector = MTCNN()
            # detect faces in the image
            faces = detector.detect_faces(pixels)
            # display faces on the original image
            croped_img, coords= get_face_coords(picture, faces)
            
            result, predictions= predict_img(croped_img)#output the prediction
            # show the plot (face detected)
            draw_rect(coords, predictions)
            
            st.write(result)
            st.write("Males count:",len(male))
            st.write("Females count:",len(female))
            st.write("Faces count:",len(male)+len(female))

# draw an image with detected objects
def get_face_coords(uploaded_file, result_list):
  # load the image
  data = pyplot.imread(uploaded_file)
  # plot the image
  pyplot.imshow(data)
  for result in result_list:
    # get coordinates
    #st.write(result['confidence'])
    if result['confidence'] > 0.96:
      x1, y1, width, height = result['box']
      x2, y2 = x1 + width, y1 + height
      coords.append([x1,y1,x2,y2,width,height])
      crop_img.append(data[y1:y2,x1:x2])
  return crop_img, coords


def predict_img(croped_img):
  for crop in croped_img:     
    #preprocess Image
    img = Image.fromarray(crop, 'RGB')
    img = img.resize(target_size)
    img = img_to_array(img)
    img = img/255.0
    img=img.reshape(1, size, size, 3)

    #Prediction
    pred = model.predict(img)
    pred = pred[0][0]
    predictions.append(pred)  
    if pred>=0.5:
      male.append(1)
      result.append("Male, Confidence is {:.2f}".format(pred))
    else:
      female.append(1)
      pred = 1-pred
      result.append("Female, Confidence is {:.2f}".format(pred))
  return result, predictions


def draw_rect(coords, predictions):
    ax = pyplot.gca()
    for i,coord in enumerate(coords):
        if predictions[i] >= 0.5:
          color = 'b'
        else:
          color = 'r'
        # create the shape
        rect = Rectangle((coord[0], coord[1]), coord[4], coord[5], gid="one", fill=False, color=color)
        ax.annotate(i, (coord[2], coord[1]), color='w', weight='bold', fontsize=7, ha='center', va='center')
        # draw the box
        ax.add_patch(rect)
    pyplot.axis('off')
    st.pyplot()

#error handler
st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__=='__main__':
    main()
