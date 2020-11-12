#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from PIL import Image
import streamlit as st
import pickle


# In[5]:


loaded_model = pickle.load(open('gbc_model.sav', 'rb'))


# In[6]:


def predict(local_model, local_input_df):
    predictions_df = local_model.predict(local_input_df)
    predictions = predictions_df
    return predictions 


# In[12]:


def run():
    
    from PIL import Image
    image = Image.open('churn.png')
    image_com = Image.open('com.jpg')
    
    st.image(image, use_column_width=True)
    
    add_selectbox = st.sidebar.selectbox("Are you currently employed?", ("Yes", "No"))
    
    
    st.sidebar.info('This app is created to predict employee churn')
    st.sidebar.success('https://www.linkedin.com/in/kristofcsaba')
    
    st.sidebar.image(image_com)
    
    st.title("Employee Churn Prediction App")





    if add_selectbox == "Yes":
    
        satisfaction = st.selectbox('Job Satisfaction', [1,2,3,4,5,6,7,8,9,10]) #min_value=1, max_value=10, value=5)
        evaluation = st.selectbox('Job Evaluation', [1,2,3,4,5,6,7,8,9,10]) #min_value=1, max_value=10, value=5)
        number_of_projects = st.number_input('Number of Projects', min_value=0, max_value=7, value=1)
        average_monthly_hours = st.number_input('Average Montly Hours', min_value=0, max_value=310, value=160)
        time_spend_company = st.selectbox('Years Spent at Company', [0,1,2,3,4,5,6,7])
    
        if st.checkbox('Suffered Work Accident'):
            work_accident = 1
        else:
            work_accident = 0
        if st.checkbox('Earned promotion'):
            promotion = 1
        else:
            promotion = 0

        churn_or_not=""

        input_dict = {'satisfaction' : satisfaction, 'evaluation' : evaluation, 'number_of_projects' :                     number_of_projects,
             'average_monthly_hours' : average_monthly_hours, 'time_spend_company' : time_spend_company,
              'work_accident' : work_accident, 'promotion' : promotion}

        input_df = pd.DataFrame([input_dict])

        if st.button('Predict'):
            output = predict(local_model=loaded_model, local_input_df=input_df);
            if(output == [0]):
                churn_or_not = " not churn"
            elif(output == [1]):
                churn_or_not = 'churn'
        
            quitOrNot = str(churn_or_not)
    
        st.success('We predict that the person will {}'.format(churn_or_not))
    
    if add_selectbox == 'No':
        return None

if __name__ == '__main__':
    run()

# In[ ]:




