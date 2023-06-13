import streamlit as st
import functions as fc


st.sidebar.header("Let's look for the info you need")
req = st.sidebar.text_area("Write your request below:")
search_button = st.sidebar.button("Search")

if search_button:
    try:
        req_text = fc.call_wiki(req.strip())
        st.title(f"{req}")
        st.write(req_text)
    except:
        st.title(f"{req}")
        st.header("Sorry!")
        st.write(f"I don't have any information about {req}")
else:
    st.title(f"Ooops...")
    st.header("Sorry!")
    st.write("You have to provide a request!")
    
    

#col1, col2 = st.columns(2)
#col1.header("")
#col1.expander("")
    
    


