import streamlit as st
import functions as fc


st.sidebar.header("Write your request:")
req = st.sidebar.text_area("Paste your text here")
search_button = st.sidebar.button("Search")

if search_button:
    req_text = fc.call_wiki(req)
    st.title(f"{req}")
    st.write(req_text)
    
    


