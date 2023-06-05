
import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("C:/Users/HP/Desktop/VIT - 2/EDAI - 2/Credit_Score_Classification/trained_model.sav","rb"))

def credit_score(input_data):
    features = np.array(input_data)
    prediction = loaded_model.predict(features.reshape(1,-1))
    print(prediction)
    return prediction[0]

def main():
    st.title("Credit Score Classification")
    a = st.number_input("Annual Income: ")*0.012
    b = st.number_input("Monthly Inhand Salary: ")*0.012
    c = st.number_input("Number of Bank Accounts: ")
    d = st.number_input("Number of Credit cards: ")
    e = st.number_input("Interest rate: ")
    f = st.number_input("Number of Loans: ")
    g = st.number_input("Average number of days delayed by the person: ")
    h = st.number_input("Number of delayed payments: ")
    i = st.number_input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
    j = st.number_input("Outstanding Debt: ")*0.012
    k = st.number_input("Credit History Age: ")
    l = st.number_input("Monthly Balance: ")*0.012
    score = ''
    if st.button("PREDICT CREDIT SCORE"):
        score = credit_score([a,b,c,d,e,f,g,h,i,j,k,l])
    st.success(score)

if __name__ == '__main__' :
    main()    
    
    
    