import streamlit as st
import numpy as np
import pickle as pkl
model1 = pkl.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Empolyee Attrition",
                   initial_sidebar_state="expanded", layout="wide")

def preprocess(Department, Gender, MaritalStatus, JobLevel, JobSatisfaction, SalaryHike, StockOptionLevel, OverTime, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager,	EnvironmentSatisfaction, TrainingTimesLastYear,	WorkLifeBalance, RelationshipSatisfaction):
    if Department == "Human Resources":
        Department = 0
    elif Department == "Research & Development":
        Department = 1
    else:
        Department = 2

    if Gender == "Female":
        Gender = 0
    else:
        Gender = 1
        
    if MaritalStatus == "Divorced":
        MaritalStatus = 0
    elif MaritalStatus == "Married":
        MaritalStatus = 1
    else:
        MaritalStatus = 2

    if JobLevel == "1":
        JobLevel = 0
    elif JobLevel == "2":
        JobLevel = 1
    elif JobLevel == "3":
        JobLevel = 2
    elif JobLevel == "4":
        JobLevel = 3
    else:
        JobLevel = 4

    if JobSatisfaction == "High":
        JobSatisfaction = 0
    elif JobSatisfaction == "Low":
        JobSatisfaction = 1
    elif JobSatisfaction == "Medium":
        JobSatisfaction = 2
    else:
        JobSatisfaction = 3

    if SalaryHike == "10":
        SalaryHike = 0
    elif SalaryHike == "11":
        SalaryHike = 1
    elif SalaryHike == "12":
        SalaryHike = 2
    elif SalaryHike == "13":
        SalaryHike = 3
    elif SalaryHike == "14":
        SalaryHike = 4
    elif SalaryHike == "15":
        SalaryHike = 5
    elif SalaryHike == "16":
        SalaryHike = 6
    elif SalaryHike == "17":
        SalaryHike = 7
    elif SalaryHike == "18":
        SalaryHike = 8
    elif SalaryHike == "19":
        SalaryHike = 9
    elif SalaryHike == "20":
        SalaryHike = 10
    elif SalaryHike == "21":
        SalaryHike = 11
    elif SalaryHike == "22":
        SalaryHike = 12
    elif SalaryHike == "23":
        SalaryHike = 13
    elif SalaryHike == "24":
        SalaryHike = 14
    else:
        SalaryHike = 15
        
    if StockOptionLevel == "0":
        StockOptionLevel = 0
    elif StockOptionLevel == "1":
        StockOptionLevel = 1
    elif StockOptionLevel == "2":
        StockOptionLevel = 2
    else:
        StockOptionLevel = 3
    
    if OverTime == "No":
        OverTime = 0
    else:
        OverTime = 1
    
    if YearsInCurrentRole == "0":
        YearsInCurrentRole = 0
    elif YearsInCurrentRole == "1":
        YearsInCurrentRole = 1
    elif YearsInCurrentRole == "2":
        YearsInCurrentRole = 2
    elif YearsInCurrentRole == "3":
        YearsInCurrentRole = 3
    elif YearsInCurrentRole == "4":
        YearsInCurrentRole = 4
    elif YearsInCurrentRole == "5":
        YearsInCurrentRole = 5
    elif YearsInCurrentRole == "6":
        YearsInCurrentRole = 6
    elif YearsInCurrentRole == "7":
        YearsInCurrentRole = 7
    elif YearsInCurrentRole == "8":
        YearsInCurrentRole = 8
    elif YearsInCurrentRole == "9":
        YearsInCurrentRole = 9
    elif YearsInCurrentRole == "10":
        YearsInCurrentRole = 10
    elif YearsInCurrentRole == "11":
        YearsInCurrentRole = 11
    elif YearsInCurrentRole == "12":
        YearsInCurrentRole = 12
    elif YearsInCurrentRole == "13":
        YearsInCurrentRole = 13
    elif YearsInCurrentRole == "14":
        YearsInCurrentRole = 14
    elif YearsInCurrentRole == "15":
        YearsInCurrentRole = 15
    elif YearsInCurrentRole == "16":
        YearsInCurrentRole = 16
    elif YearsInCurrentRole == "17":
        YearsInCurrentRole = 17
    else:
        YearsInCurrentRole = 18

    if YearsSinceLastPromotion == "0":
        YearsSinceLastPromotion = 0
    elif YearsSinceLastPromotion == "1":
        YearsSinceLastPromotion = 1
    elif YearsSinceLastPromotion == "2":
        YearsSinceLastPromotion = 2
    elif YearsSinceLastPromotion == "3":
        YearsSinceLastPromotion = 3
    elif YearsSinceLastPromotion == "4":
        YearsSinceLastPromotion = 4
    elif YearsSinceLastPromotion == "5":
        YearsSinceLastPromotion = 5
    elif YearsSinceLastPromotion == "6":
        YearsSinceLastPromotion = 6
    elif YearsSinceLastPromotion == "7":
        YearsSinceLastPromotion = 7
    elif YearsSinceLastPromotion == "8":
        YearsSinceLastPromotion = 8
    elif YearsSinceLastPromotion == "9":
        YearsSinceLastPromotion = 9
    elif YearsSinceLastPromotion == "10":
        YearsSinceLastPromotion = 10
    elif YearsSinceLastPromotion == "11":
        YearsSinceLastPromotion = 11
    elif YearsSinceLastPromotion == "12":
        YearsSinceLastPromotion = 12
    elif YearsSinceLastPromotion == "13":
        YearsSinceLastPromotion = 13
    elif YearsSinceLastPromotion == "14":
        YearsSinceLastPromotion = 14
    else:
        YearsSinceLastPromotion = 15
    
    if YearsWithCurrManager == "0":
        YearsWithCurrManager = 0
    elif YearsWithCurrManager == "1":
        YearsWithCurrManager = 1
    elif YearsWithCurrManager == "2":
        YearsWithCurrManager = 2
    elif YearsWithCurrManager == "3":
        YearsWithCurrManager = 3
    elif YearsWithCurrManager == "4":
        YearsWithCurrManager = 4
    elif YearsWithCurrManager == "5":
        YearsWithCurrManager = 5
    elif YearsWithCurrManager == "6":
        YearsWithCurrManager = 6
    elif YearsWithCurrManager == "7":
        YearsWithCurrManager = 7
    elif YearsWithCurrManager == "8":
        YearsWithCurrManager = 8
    elif YearsWithCurrManager == "9":
        YearsWithCurrManager = 9
    elif YearsWithCurrManager == "10":
        YearsWithCurrManager = 10
    elif YearsWithCurrManager == "11":
        YearsWithCurrManager = 11
    elif YearsWithCurrManager == "12":
        YearsWithCurrManager = 12
    elif YearsWithCurrManager == "13":
        YearsWithCurrManager = 13
    elif YearsWithCurrManager == "14":
        YearsWithCurrManager = 14
    elif YearsWithCurrManager == "15":
        YearsWithCurrManager = 15
    elif YearsWithCurrManager == "16":
        YearsWithCurrManager = 16
    else:
        YearsWithCurrManager = 17
    
    if EnvironmentSatisfaction == "High":
        EnvironmentSatisfaction = 0
    elif EnvironmentSatisfaction == "Low":
        EnvironmentSatisfaction = 1
    elif EnvironmentSatisfaction == "Medium":
        EnvironmentSatisfaction = 2
    else:
        EnvironmentSatisfaction = 3
    
    if TrainingTimesLastYear == "0":
        TrainingTimesLastYear = 0
    elif TrainingTimesLastYear == "1":
        TrainingTimesLastYear = 1
    elif TrainingTimesLastYear == "2":
        TrainingTimesLastYear = 2
    elif TrainingTimesLastYear == "3":
        TrainingTimesLastYear = 3
    elif TrainingTimesLastYear == "4":
        TrainingTimesLastYear= 4
    elif TrainingTimesLastYear == "5":
        TrainingTimesLastYear = 5
    else:
        TrainingTimesLastYear = 6
    
    if WorkLifeBalance == "Bad":
        WorkLifeBalance = 0
    elif WorkLifeBalance == "Best":
        WorkLifeBalance = 1
    elif WorkLifeBalance == "Better":
        WorkLifeBalance = 2
    else:
        WorkLifeBalance = 3
        
    if RelationshipSatisfaction == "High":
        RelationshipSatisfaction = 0
    elif RelationshipSatisfaction == "Low":
        RelationshipSatisfaction = 1
    elif RelationshipSatisfaction == "Medium":
        RelationshipSatisfaction = 2
    else:
        RelationshipSatisfaction = 3
        
    user_input = [Department, Gender, MaritalStatus, JobLevel, JobSatisfaction, SalaryHike, StockOptionLevel, OverTime, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager,	EnvironmentSatisfaction, TrainingTimesLastYear,	WorkLifeBalance, RelationshipSatisfaction]
    user_input = np.array(user_input)
    user_input = user_input.reshape(1, -1)
    prediction1 = model1.predict(user_input)

    return prediction1


# front end elements of the web page
html_temp = """ 
    <div style ="background-color:#4DB8FF; padding:13px"> 
    <h2 style ="color:black; text-align:center; font-family: calibri">Empolyee Attrition Prediction </h2> 
    </div> 
    """
st.markdown(html_temp, unsafe_allow_html=True)

st.subheader('Please fill the following form:')

col1, col2, col3 = st.columns((1, 1, 1))
with col1:
    Department = st.selectbox("Select the department name: ", ('Sales', 'Research & Development', 'Human Resources'))
    Gender = st.radio("Gender: ", ["Female", "Male"])
    JobSatisfaction = st.selectbox("Are you satisfied with your job? ", ('Very High', 'Medium', 'High', 'Low'))
    JobLevel = st.selectbox("Select Job Level ", ('2', '1', '3', '4', '5'))
    SalaryHike = st.selectbox("Select salary hike in % ", ('10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'))

with col2:
    StockOptionLevel = st.selectbox("Select stock option level ", ('0', '1', '2', '3'))
    OverTime = st.radio("Do you work over time? ", ['Yes', 'No'])
    YearsInCurrentRole = st.selectbox("Experience in years ", ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'))
    YearsSinceLastPromotion = st.selectbox("Years since last promotion ", ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'))
    YearsWithCurrManager = st.selectbox("Years workng with current manager ", ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'))

with col3:
    EnvironmentSatisfaction = st.selectbox("Are you satisfied by the environment? ", ('Very High', 'Medium', 'High', 'Low'))
    TrainingTimesLastYear = st.selectbox("Number of trainings in the last years ", ('1', '2', '3', '4', '5', '6'))
    WorkLifeBalance = st.selectbox("How is your work life balance? ", ('Very High', 'Medium', 'High', 'Low'))
    MaritalStatus = st.radio("What is your Marital Status? ", ['Single', 'Married', 'Divorced'])
    RelationshipSatisfaction = st.selectbox("How satisfied with your relationship? ", ('Very High', 'Medium', 'High', 'Low'))
    
# user_input=preprocess
pred = preprocess(Department, Gender, MaritalStatus, JobLevel, JobSatisfaction, SalaryHike, StockOptionLevel, OverTime, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager, EnvironmentSatisfaction, TrainingTimesLastYear,	WorkLifeBalance, RelationshipSatisfaction)

if st.button("Predict"):
    if pred[0]==0:
        st.write("No, the employee will not leave the job")

    else:
        st.write("Yes, the employee will leave the job")