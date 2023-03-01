import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
        
def predict(text):    
    # Load the text processing model
    with open('model/files/emotionModel.pkl', 'rb') as f:
        model = pickle.load(f)
        
    with open('model/files/tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)   
        
    with open('model/files/label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)     

    input_sequence = tokenizer.texts_to_sequences([text])
    padded_input_sequence = pad_sequences(input_sequence, maxlen=66)
    prediction = model.predict(padded_input_sequence)
    predicted_label = label_encoder.inverse_transform([np.argmax(prediction[0])])
    return predicted_label[0]