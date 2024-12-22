import os
import sys
import streamlit as st

sys.path.insert(0, './dashboard')

from multiapp import MultiApp


st.set_page_config(page_title="Telecom User Data Visualization", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# Telecom User Data Analysis
""")


# The main app
app.run()