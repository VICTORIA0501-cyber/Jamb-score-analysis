import streamlit as st
from main import data_pel, grouped_data


st.title("Welcome to ILARA/AKAKA")

st.bar_chart(data_pel)

st.hist(grouped_data)
