import streamlit as st
import pandas as pd

st.title('My Streamlit App')
st.subheader('My Streamlit App Data')
st.header("My header")
st.text("địt con mẹ chúng mày")
st.markdown("[**địt** con mẹ chúng mày](https://youtu.be/dQw4w9WgXcQ?si=OrhaP4-Nzhmu35HW)")
    # DataFrame
df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
})
st.write(df)
st.write("mai nghỉ học")

# streamlit run app.py
