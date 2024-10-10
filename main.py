import streamlit as st
import langchain_helper

st.title("Software Company Name Generator")

industry = st.sidebar.selectbox("Pick an Industry", ("Finance", "Healthcare", "E-commerce", "Education", "Technology"))

if industry:
    response = langchain_helper.generate_company_name_and_info(industry)
    st.header(response['company_name'].strip())
    company_info = response['company_info'].strip().split("\n")
    st.write("**Company Info**")
    for info in company_info:
        st.write("-", info)