import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns


from keras.models import model_from_json
import tensorflow as tf
import cv2

# sns.set(style='white', context='notebook', palette='deep')



def process(img_path):
    img=cv2.bitwise_not(cv2.imread(img_path,0))
    img=img/255.0
    resize_img = cv2.resize(img  , (28 , 28))
    
    
    #plt.imshow(img)
    
    X=resize_img.reshape(-1,28,28,1)
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    a=[1,2,3,4,5,6,7,8,9,10]
    Y_pred1=loaded_model.predict(X)
#     a = enumerate(Y_pred1[0])
    Y_pred1_classes=np.argmax(Y_pred1,axis=1)
    pred=Y_pred1_classes[0]
#     pred11=a[0]
    pred_image=cv2.imread(('Images/'+str(pred)+'.jpg'),1)
    #print(pred_image);
    
    #plt.subplots(figsize=(15,15))
    #`fig = plt.figure(figsize=(15,15))
    gs = gridspec.GridSpec(2, 2) 
    #plt.subplot(2, 2, 1)
    ax0 = plt.subplot(gs[0,0])
    ax0.imshow(img)
    plt.title("Original Image")
    
    #plt.subplot(2, 2, 2)
    ax1 = plt.subplot(gs[0,1])
    ax1.imshow(pred_image)
    plt.title("Predicted Digit")
        
    #plt.subplot(2, 2, 4)
    ax4 = plt.subplot(gs[1,:])
    #plt.subplots(figsize=(10,10))
    colors=['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe']
    ax4.bar(x=np.arange(10),height=Y_pred1[0],color=colors,tick_label=[0,1,2,3,4,5,6,7,8,9])
    plt.ylabel('Probability')
    plt.title("Probability of each digit",y=-0.30);
    
    plt.show()
    print("The digit given in picture is==> ",pred)
