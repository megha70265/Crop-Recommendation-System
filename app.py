import streamlit as st
import pickle 
from tensorflow import keras
from keras.models import load_model
import numpy
import joblib
import os
path=os.getcwd()
path=os.path.join(path,'model2.pkl')
# with open(path, 'rb') as file:
#     model2 = pickle.load(file)
model2=joblib.load('model2.pkl')
print(type(model2))
#model=pickle.load(r"C:\Users\anegh\OneDrive\Desktop\proj\model2.pkl")
st.header("YIELD PREDICTION SYSTEM")
pressure=st.text_input("ENTER PRESSURE VALUE:")
temp=st.text_input("ENTER TEMPERATURE VALUE:")
humid=st.text_input("ENTER HUMID VALUE:")
if (pressure is not None) and (temp is not None) and (humid is not None):
    if st.button("predict"):
        inp = numpy.array([[float(pressure), float(temp), float(humid)]])
        out = model2.predict(inp)
        st.subheader(out[0])



