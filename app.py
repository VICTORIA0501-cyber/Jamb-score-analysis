import streamlit as st
from main import data_pel, grouped_data, df_jamb , grp_lbl
import plotly.figure_factory as ff


st.title("Welcome to ILARA/AKAKA")

st.bar_chart(data_pel)

st.bar_chart(grouped_data)

fig = ff.create_distplot(df_jamb, grp_lbl)

st.plotly_chart(fig, use_container_width=True)


