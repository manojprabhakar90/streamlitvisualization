import streamlit as st
import pandas as pd
import time
import plotly.express as px
import country_converter as coco
import plotly.figure_factory as ff
import plotly.graph_objects as go

data = pd.read_csv("ds_salaries.csv")

work_year = data['work_year'].value_counts()
fig = px.pie(values = work_year.values, names = work_year.index, 
            title = 'Work year distribution',color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
st.plotly_chart(fig)
