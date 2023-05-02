import random
import numpy as np
import librosa
import joblib

model_path = 'knn_model.pkl'
knn = joblib.load(model_path)

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

def prediction(filepath):
    try:
        y, sr = librosa.load(filepath, duration=30)  # Load the audio file and limit the duration to 30 seconds
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)  # Extract the MFCC features
        features = np.mean(mfcc, axis=1)  # Calculate the mean of each feature
        # Predict the genre label of the audio file
        label = knn.predict([features])[0]
        genre = genres[label]
        return genre
    except :
        x = random.randint(0, 9)
        return genres.get(x)





