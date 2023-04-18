import streamlit as st
import re
from DBOperations import DBUserOperationsSQL as DB


def emailCheck(email) :
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if re.fullmatch(pattern, email) :
        return True
    return False

def phoneCheck(phoneNo) :
    pattern = re.compile('[0-9]{10}')
    if re.fullmatch(pattern, phoneNo) :
        return True
    return False

def publishCompany(dbObj) :
    x = st.empty()
    companyDetails = dict()
    prev_users = dbObj.searchUsernames()
    with x.form(key='company_review') :
        userName = st.text_input('Username')
        companyName = st.text_input('Company Name')
        companyAddress = st.text_input('Address')
        companyLocation = st.text_input('Country')
        companyContact = st.text_input('Contact')
        companyEmail = st.text_input('Email')
        publish = st.form_submit_button(label='Publish', use_container_width=True)
        if publish :
            if userName not in prev_users :
                st.error('Username Not Found, Signup')
            else :
                if companyName == "" :
                    st.error('Enter Company Name')
                else :
                    companyDetails['Name'] = companyName
                    if companyAddress == "":
                        st.error('Enter Company Address')
                    else :
                        companyDetails['Address'] = companyAddress
                        if companyLocation == "":
                            st.error('Enter Company Location')
                        else :
                            companyDetails['Country'] = companyLocation
                            if phoneCheck(companyContact) == False :
                                st.error('Enter Valid Contact')
                            else :
                                companyDetails['Phone'] = companyContact
                                if emailCheck(companyEmail) == False :
                                    st.error('Enter Valid Email')
                                else :
                                    companyDetails['Email'] = companyEmail
                                    companyDetails['Publisher'] = userName
                                    dbObj.insertCompany(companyDetails)
                                    st.error('Company Published!')


def publishPlace(dbObj):
    placeDetails = dict()
    x = st.empty()
    prev_users = dbObj.searchUsernames()
    with x.form(key='place_review'):
        userName = st.text_input('Username')
        placeName = st.text_input('Place')
        placeAddress = st.text_input('Address')
        placeLocation = st.text_input('Country')
        publish = st.form_submit_button(label='Publish', use_container_width=True)
        if publish :
            if userName not in prev_users :
                st.error('Username Not Found, Signup')
            else :
                if placeName == "" :
                    st.error('Enter Place')
                else :
                    placeDetails['Name'] = placeName
                    if placeAddress == "":
                        st.error('Enter Address')
                    else :
                        placeDetails['Address'] = placeAddress
                        if placeLocation == "":
                            st.error('Enter Location')
                        else :
                            placeDetails['Country'] = placeLocation
                            placeDetails['Publisher'] = userName
                            dbObj.insertPlace(placeDetails)
                            st.error('Place Published!')


if __name__ == '__main__' :
    dbObj = DB.DBSQLUser()
    x = st.empty()
    st.title('Publish')
    option = st.selectbox('Choose an Option', ('Company', 'Place'))
    if option == 'Company' :
        publishCompany(dbObj)
    elif option == 'Place' :
        publishPlace(dbObj)