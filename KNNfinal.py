#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import librosa
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Define the genres and their corresponding label
genres = {
    'blues': 0,
    'classical': 1,
    'country': 2,
    'disco': 3,
    'hiphop': 4,
    'jazz': 5,
    'metal': 6,
    'pop': 7,
    'reggae': 8,
    'rock': 9
}

# Define the directory path of the dataset
dataset_path = r'C:\Users\Apurva\Downloads\Genere\Data\genres_original'

# Initialize empty lists to store the features and labels
X = []
y = []

# Loop through each folder in the dataset
for folder in os.listdir(dataset_path):
    # Get the label of the genre
    label = genres[folder]
    # Loop through each WAV file in the folder
    for filename in os.listdir(os.path.join(dataset_path, folder)):
        # Load the WAV file and extract its features
        filepath = os.path.join(dataset_path, folder, filename)
        y_, sr = librosa.load(filepath, duration=30)  # Load the WAV file and limit the duration to 30 seconds
        mfcc = librosa.feature.mfcc(y=y_, sr=sr, n_mfcc=20)  # Extract the MFCC features
        features = np.mean(mfcc, axis=1)  # Calculate the mean of each feature
        # Append the features and label to the corresponding lists
        X.append(features)
        y.append(label)


# In[ ]:


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)

# Train the classifier on the training set
knn.fit(X_train, y_train)

# Save the trained model as a pickle file
model_path = r'C:\Users\Apurva\Desktop\KNNmodel\knn_model.pkl'
joblib.dump(knn, model_path)

# Load the KNN model from the pickle file
knn = joblib.load(model_path)


# In[3]:


filepath = r'C:\Users\Apurva\Downloads\alarm.wav'
y, sr = librosa.load(filepath, duration=30)  # Load the audio file and limit the duration to 30 seconds
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)  # Extract the MFCC features
features = np.mean(mfcc, axis=1)  # Calculate the mean of each feature

# Predict the genre label of the audio file
label = knn.predict([features])[0]

# Reverse the label-to-genre mapping
genres = {
    0: 'blues',
    1: 'classical',
    2: 'country',
    3: 'disco',
    4: 'hiphop',
    5: 'jazz',
    6: 'metal',
    7: 'pop',
    8: 'reggae',
    9: 'rock'
}

# Print the predicted genre of the audio file
genre = genres[label]
print('Predicted genre:', genre)


# In[7]:


def prediction(filepath):
    y, sr = librosa.load(filepath, duration=30)  # Load the audio file and limit the duration to 30 seconds
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)  # Extract the MFCC features
    features = np.mean(mfcc, axis=1)  # Calculate the mean of each feature

    # Predict the genre label of the audio file
    label = knn.predict([features])[0]
    genre = genres[label]
    print('Predicted genre:', genre)


# In[9]:


filepath = r'C:\Users\Apurva\Desktop\KNNmodel\sample.wav'
prediction(filepath)

