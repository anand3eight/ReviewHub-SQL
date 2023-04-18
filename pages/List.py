import streamlit as st
from DBOperations import DBUserOperationsSQL as DB
from streamlit_star_rating import st_star_rating

def viewCompany(dbObj) :
    y = st.empty()
    st.write('Search Company Reviews')
    option = st.selectbox('Search by', ('Name', 'Location'))
    if option == 'Name':
        companyName = st.text_input('Name : ')
        search = st.button('Search')
        if search :
            companyDetails = dbObj.fetchCompanyByName(companyName)
            if len(companyDetails) == 0:
                st.write('No Results Found')
            else :
                st.write('<h2>Results<h2>', unsafe_allow_html=True)
                count = 1
                for x in companyDetails:
                    for i in x :
                        st.text_input(label=i, value=x[i], key=str(count) + "_" + i)
                    rating = dbObj.getAverageCompanyRating(option, x['Name'])
                    stars = st_star_rating(label="Rating", maxValue=5, defaultValue=rating, key="rating"+x[i],
                                            read_only=True, dark_theme=True)
                    st.markdown("""---""")
                    count += 1

    elif option == 'Location':
        companyLocation = st.text_input('Location : ')
        search = st.button('Search')
        if search :
            companyDetails = dbObj.fetchCompanyByLocation(companyLocation)
            if len(companyDetails) == 0 :
                st.write('No Results Found')
            else :
                st.write('<h2>Results<h2>', unsafe_allow_html=True)
                count = 1
                for x in companyDetails :
                    for i in x :
                        st.text_input(label=i, value=x[i], key=str(count) + "_" + i)
                    rating = dbObj.getAverageCompanyRating(option, x['Address'])
                    stars = st_star_rating(label="Rating", maxValue=5, defaultValue=rating, key="rating"+x[i],
                                            read_only=True, dark_theme=True)
                    st.markdown("""---""")
                    count += 1


def viewPlace(dbObj) :
    y = st.empty()
    st.write('Search Place Reviews')
    option = st.selectbox('Search by', ('Name', 'Location'))
    if option == 'Name':
        placeName = st.text_input('Name : ')
        search = st.button('Search')
        if search :
            placeDetails = dbObj.fetchPlaceByName(placeName)
            if len(placeDetails) == 0:
                st.write('No Results Found')
            else :
                st.write('<h2>Results<h2>', unsafe_allow_html=True)
                count = 1
                for x in placeDetails :
                    for i in x :
                        st.text_input(label=i, value=x[i], key=str(count) + "_" + i)
                    rating = dbObj.getAveragePlaceRating(option, x['Name'])
                    stars = st_star_rating(label="Rating", maxValue=5, defaultValue=rating, key="rating"+x[i],
                                            read_only=True, dark_theme=True)
                    st.markdown("""---""")
                    count += 1

    elif option == 'Location':
        placeLocation = st.text_input('Location : ')
        search = st.button('Search')
        if search :
            placeDetails = dbObj.fetchPlaceByLocation(placeLocation)
            if len(placeDetails) == 0 :
                st.write('No Results Found')
            else :
                st.write('<h2>Results<h2>', unsafe_allow_html=True)
                count = 1
                for x in placeDetails:
                    for i in x:
                        st.text_input(label=i, value=x[i], key=str(count) + "_" + i)
                    rating = dbObj.getAveragePlaceRating(option, x['Address'])
                    stars = st_star_rating(label="Rating", maxValue=5, defaultValue=rating, key="rating"+x[i],
                                            read_only=True, dark_theme=True)
                    st.markdown("""---""")
                    count += 1

if __name__ == '__main__' :
    dbObj = DB.DBSQLUser()
    x = st.empty()
    st.title('View Details')
    option = st.selectbox('Choose an Option', ('Company', 'Place'))
    if option == 'Company' :
        viewCompany(dbObj)
    elif option == 'Place' :
        viewPlace(dbObj)