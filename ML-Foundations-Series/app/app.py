import streamlit as st
import joblib
import numpy as np

st.title('House Price Predictor')
st.write('Enter property features to get a predicted price.')

model = joblib.load('../models/house_price_model.pkl')

area = st.number_input('Area (sq ft)', 300, 10000, 1500)
bedrooms = st.number_input('Bedrooms', 1, 10, 3)
bathrooms = st.number_input('Bathrooms', 1, 10, 2)
age = st.number_input('Age (years)', 0, 100, 10)
location_score = st.slider('Location Score (1-10)', 1.0, 10.0, 7.5)
has_garage = st.checkbox('Garage')
has_pool = st.checkbox('Pool')

if st.button('Predict Price'):
    features = np.array([[area, bedrooms, bathrooms, age, location_score, int(has_garage), int(has_pool)]])
    price = model.predict(features)[0]
    st.success(f'Estimated price: ${price:,.2f}')
