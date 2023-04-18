import streamlit as st
import time
from DBOperations import DBUserOperationsSQL as DB


def signupWindow(dbObj) :
    x = st.empty()
    prev_users = dbObj.searchUsernames()
    with x.form('signup_page'):
        st.write("<h2 align = center>SIGN UP</h2>", unsafe_allow_html=True)
        name = st.text_input("Name : ")
        country = st.text_input("Country : ")
        username = st.text_input("Username : ")
        password = st.text_input("Password : ", type="password")
        confirm_password = st.text_input("Confirm Password : ", type="password")
        signUp = st.form_submit_button(label='Sign Up', use_container_width=True)

    if signUp :
        if name == "" :
            st.error("Invalid Name")
        elif country == "" :
            st.error("Invalid Country")
        elif username == "" :
            st.error("Invalid Username")
        elif username in prev_users:
            st.error("Username already Taken")
        elif len(password) < 8 or password != confirm_password :
            st.error("Re-Enter Password")
        else :
            x.empty()
            user = dict()
            user["Name"] = name
            user["Country"] = country
            user["Username"] = username
            user["Password"] = password
            dbObj.insertUser(user)
            x.error("Signup Successful, Go to Login")
            time.sleep(1)
            x.empty()


if __name__ == "__main__" :
    dbObj = DB.DBSQLUser()
    signupWindow(dbObj)