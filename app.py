import numpy as np  
import pickle  
import streamlit as st  
from PIL import Image  

# Load the trained classifier model  
pickle_in = open("fertilizer_classifier.pkl", "rb")  
classifier = pickle.load(pickle_in) 


st.set_page_config(
    page_title="Fertilizer Prediction",
    page_icon="🪴",
)

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
@media only screen and (max-width: 768px) {
    footer {
        display: none;
    }
    .st-logo {
        display: none;
    }
}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

def predict_note_authentication(Temperature, Humidity, Moisture, Soil_Type, Crop_Type, Nitrogen, Potassium, Phosphorous):  
    try: 
        inputs = np.array([[float(Temperature), float(Humidity), float(Moisture),    float(Soil_Type), float(Crop_Type), float(Nitrogen), float(Potassium), float(Phosphorous)]])  
        
        prediction = classifier.predict(inputs)  
        predicted_value = prediction[0]  
        
        if predicted_value == 6:  
            return 'Urea\n\n\nUrea is a common type of fertilizer used to provide nitrogen, a vital nutrient for plant growth. It Is a white, crystalline substance that dissolves easily in water.\n' 
        elif predicted_value == 5:  
            return 'DAP\n\n\nDAP has two main nutrients: nitrogen and phosphorus. Nitrogen helps plants grow leaves and stems, while phosphorus helps them develop roots and flowers. So, DAP is a great way to give your plants a boost.\n'  
        elif predicted_value == 4:  
            return 'Gromor 28-28\n\n\nGromor 28-28 is a fertilizer that gives plants a quick boost of energy. It is like a multivitamin for your crops! It has two main nutrients: Nitrogen (N) Helps plants grow leaves and stems and  Phosphorus (P) Helps plants develop strong roots and flowers\n'
        elif predicted_value == 3:  
            return 'Gromor 20-20\n\n\nGromor 20-20 is typically used for crops that require a balanced supply of nutrients, such as wheat, paddy, sugarcane, and oilseeds.It is also beneficial for improving soil fertility and increasing crop yields.\n'
        elif predicted_value == 2:  
            return 'Gromor 17-17-17\n\n\nGromor 17-17-17 is a balanced fertilizer that provides essential nutrients to plants in equal amounts.It contains 17% Nitrogen (N), 17% Phosphorus (P), and 17% Potassium (K). These nutrients are crucial for plant growth, development, and overall health.\n'
        elif predicted_value == 1:  
            return 'Gromor 14-35-14\n\n\nIt is suitable for most crops, especially those that require high levels of phosphorus, such as rice, cotton, groundnut, chillies, soybean, and potato. However, it is not recommended for chlorine-sensitive crops like tobacco and grapes.\n'
        elif predicted_value == 0:  
            return 'Gromor 10-26-26\n\n\nGromor 10-26-26 is a balanced fertilizer with high levels of phosphorus and potassium, making it ideal for crops like sugarcane and potatoes. It is  best used during the early growth stages of plants when they need extra nutrients to develop strong roots and shoots.\n'  
        else:  
            return f'Predicted value is {predicted_value}'  
    except ValueError:  
        return "Invalid input! Please ensure all fields are filled with numeric values."  

def main():  
   
     
    #st.title("Fertilizer Prediction")  
    html_temp = """ 
    
    <h1 style="color:green;text-align:center;padding:0px;margin:0px">Fertilizer Prediction</h1>  
  
    """  
    st.markdown(html_temp, unsafe_allow_html=True)   
    
    # User input fields  
    Temperature = st.text_input("Enter degree of Temperature", "")  

    Humidity = st.text_input("Enter percentage of Humidity", "")    
    Moisture = st.text_input("Enter level of Moisture", "")  
    
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

    Nitrogen = st.text_input("Enter amount of Nitrogen", "")  
    Potassium = st.text_input("Enter amount of  Potassium", "")  
    Phosphorous = st.text_input("Enter amount of Phosphorous", "")  
    
    result = ""  
    if st.button("Predict"):  
        result = predict_note_authentication(Temperature, Humidity, Moisture, Soil_Type_value, Crop_Type, Nitrogen , Potassium, Phosphorous)  
    
    st.success('The fertilizer needed is : {}'.format(result))  
    
   if st.button("About"):
       st.markdown("Fertilizers are substances added to the soil to enhance plant growth by providing essential nutrients. Fertilizer prediction uses machine learning models like logistic regression to analyze data on soil conditions, crop types, and historical yields to predict the optimal fertilizer type  for a specific agricultural field. This helps farmers maximize crop productivity and reduce fertilizer waste.")
       # Load the image
       image = Image.open("fertilizers bg.jpg")

# Display the image
        st.image(image,width=200)
        st.text("Built with Streamlit")
        st.text("By 10320 Shama Khan")  

if __name__ == '__main__':  
    main()
    
