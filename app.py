import numpy as np
import pickle
import streamlit as st


# Load the trained classifier model
pickle_in = open("fertilizer_classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

def predict_note_authentication(Temparature, Humidity, Moisture, Soil_Type, Crop_Type, Nitrogen, Potassium, Phosphorous):
    try:
        # Convert input values to numerical data
        Temparature = float(Temparature)
        Humidity = float(Humidity)
        Moisture = float(Moisture)
        Nitrogen = float(Nitrogen)
        Potassium = float(Potassium)
        Phosphorous = float(Phosphorous)

        # Create input array
        inputs = np.array([[Temparature, Humidity, Moisture, Soil_Type, Crop_Type, Nitrogen, Potassium, Phosphorous]])

        # Make prediction
        prediction = classifier.predict(inputs)
        predicted_value = prediction[0]

        # Map predicted value to fertilizer name
        fertilizer_mapping = {
            6: "Urea",
            5: "DAP",
            4: "Gromor 28-28",
            3: "Gromor 20-20",
            2: "Gromor 17-17-17",
            1: "Gromor 14-35-14",
            0: "Gromor 10-26-26"
        }
        result = fertilizer_mapping.get(predicted_value, f"Predicted value is {predicted_value}")
        return result

    except ValueError:
        return "Invalid input! Please ensure all fields are filled with numeric values."

def main():  
   
     
    #st.title("Fertilizer Prediction")  
    html_temp = """ 
    <div style="background-color: rgba(144, 238, 144, 0.7); padding:10px">  <!-- Light green with 70% opacity -->  
    <div style="background-color:#004d00;padding:10px">  <!-- Dark green color -->  
    <h2 style="color:white;text-align:center;">Fertilizer Prediction</h2>  
    </div>  
    </div> 
    <br> 
    """  
    st.markdown(html_temp, unsafe_allow_html=True)   
    
    # User input fields  
    Temparature = st.text_input("Enter percentage of Temparature", "")  
    Humidity = st.text_input("Enter percentage of Humidity ", "")  
    Moisture = st.text_input("Enter Moisture", "")  
    
    Soil_Type = { 
        'Black': 0, 
        'Clayey': 1,  
        'Loamy': 2,  
        'Red': 3 ,
        'Sandy': 4, 
    }  
    Soil_Type_label = st.selectbox("Select Soil Type", list(Soil_Type.keys()))  
    Soil_Type_value = Soil_Type[Soil_Type_label]  

    Crop_Type_options = {  
        'Barley': 0, 
        'Loamy': 1,  
        'Ground Nuts': 2,  
        'Maize': 3 ,
        'Millets': 4,
        'Oil seeds': 5,
        'Paddy': 6, 
        'Pulses': 7,   
        'Sugarcane': 8,
        'Tobacco' : 9 ,
        'Wheat' : 10 
    }  
    Crop_Type_label = st.selectbox("Select Crop Type", list(Crop_Type_options.keys()))  
    Crop_Type = Crop_Type_options[Crop_Type_label]  

    Nitrogen = st.text_input("Enter amount of  Nitrogen", "")  
    Potassium = st.text_input("Enter amount of Potassium", "")  
    Phosphorous = st.text_input("Enter amount of  Phosphorous", "")  
    
    result = ""  
    if st.button("Predict"):  
        result = predict_note_authentication(Temparature, Humidity, Moisture, Soil_Type_value, Crop_Type, Nitrogen , Potassium, Phosphorous)  
    
    st.success('The output is: {}'.format(result))  
    
    if st.button("About"):  
        st.text("ML modle biuld using Logistic regression")  
        st.text("By 10320 Shama Khan")  


if __name__ == '__main__':  
    main()
    