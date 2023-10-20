import streamlit as st
from langchain_helper import generate_restaurant_name_and_item


st.title("Resturant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Mexican","Mars","Deep Sea"))



if cuisine :
    response = generate_restaurant_name_and_item(cuisine=cuisine)

    st.header(response['resturant_name'].strip())
    
    menu_items = response['menu_items'].strip().split(",")    
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item.strip())
