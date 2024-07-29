from function import manage_csv
import streamlit as st
import time


    
with st.form("my_form"):
    st.title("Assi shop app")

    st.text_input(label="",placeholder="Add meter..",
                key="meter")
    st.text_input(label="",placeholder="Add price..",
                key="price")
    st.text_input(label="",placeholder="Add type..",
                key="type")

    submitted = st.form_submit_button("Submit")
    if submitted:
        meter = st.session_state["meter"]
        price = st.session_state["price"]
        type_sold = st.session_state["type"]
        time_sold = time.strftime("%d-%m-%Y")
        mylist = [meter,price,type_sold,time_sold]
        manage_csv.add_toCSV(mylist,"assi_shop.csv")

