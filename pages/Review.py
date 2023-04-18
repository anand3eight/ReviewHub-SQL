import streamlit as st
from DBOperations import DBUserOperationsSQL as DB
from streamlit_star_rating import st_star_rating

def reviewCompany(dbObj) :
    y = st.empty()
    names = tuple(dbObj.fetchCompanyNames(''))
    companyReview = dict()
    prev_users = dbObj.searchUsernames()
    with st.form('review_company') :
        user = st.text_input('Username')
        company = st.selectbox('Choose a Company', names)
        review = st.text_area('Review')
        rating = st_star_rating(label="Rate", maxValue=5, defaultValue=0, key="rating",
                                 dark_theme=True)
        publish = st.form_submit_button('Publish Review', use_container_width=True)
        if publish :
            if user not in prev_users :
                st.error('Username Not Found, Signup')
            else :
                companyReview['User'] = user
                companyReview['Name'] = company
                companyReview['Review'] = review
                companyReview['Rating'] = rating
                dbObj.insertCompanyReview(companyReview)
                st.error('Review Published')

def reviewPlace(dbObj):
    y = st.empty()
    names = tuple(dbObj.fetchPlaceNames(''))
    placeReview = dict()
    prev_users = dbObj.searchUsernames()
    with st.form('review_place') :
        user = st.text_input('Username')
        company = st.selectbox('Choose a Place', names)
        review = st.text_area('Review')
        rating = st_star_rating(label="Rate", maxValue=5, defaultValue=0, key="rating",
                                 dark_theme=True)
        publish = st.form_submit_button('Publish Review', use_container_width=True)
        if publish :
            if user not in prev_users :
                st.error('Username Not Found, Signup')
            else :
                placeReview['User'] = user
                placeReview['Name'] = company
                placeReview['Review'] = review
                placeReview['Rating'] = rating
                dbObj.insertPlaceReview(placeReview)
                st.error('Review Published')

if __name__ == '__main__':
    dbObj = DB.DBSQLUser()
    x = st.empty()
    st.title('Review')
    option = st.selectbox('Choose an Option', ('Company', 'Place'))
    if option == 'Company':
        reviewCompany(dbObj)
    elif option == 'Place':
        reviewPlace(dbObj)