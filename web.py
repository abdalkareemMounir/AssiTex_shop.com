from function import manage_csv
import streamlit as st
import time
#from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Main menu",
        options = ["Home","Documentation","Dashbord"]
    )

#page = st_navbar(["Home", "Documentation","Dashbord"])
st.write(selected)
if selected == "Home":
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
            st.write("meter",meter,"price",price,"type",type_sold,"time",time_sold)

elif selected == "Documentation":
    st.write("data")
    df1 = manage_csv.show_csv("assi_shop.csv")
    st.dataframe(df1)
