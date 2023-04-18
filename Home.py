import streamlit as st

if __name__ == "__main__" :
    x = st.empty()
    st.markdown("<h1 style='text-align: center;'>Welcome to Google Reviews⭐️</h1>", unsafe_allow_html=True)
    st.write("<h3>About</h3>", unsafe_allow_html=True)
    st.write("The goal of our project is to provide proper information about companies and places. This app contains reviews of companies and places that are enrolled in it with average rating. By using this app, the user can have a clear idea about both the positive and negative aspects/feedback of the places and companies enrolled. The user have the access share their experience about the companies and places they had experienced. By using this app the company can improve themselves by the reviews they have got.")