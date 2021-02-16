from PIL import Image
import numpy as np
import joblib
def predict(image): 
    model = joblib.load("model.pkl")
    img = np.array(Image.open(image))[:,:,:1].reshape(1,784)
    return model.predict(img)
    