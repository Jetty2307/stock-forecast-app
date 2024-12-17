import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Test Streamlit App")

# Header
st.header("Welcome to the Test App")

# Subheader
st.subheader("Interact with the Widgets Below")

# Text Input
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)

# Button
if st.button("Submit"):
    st.write(f"Hello,{name}! Your age {age} years old.")

# Generate Random Data for Visualization

data = pd.DataFrame(
    np.random.randn(10,3),
    columns=["Column A", "Column B", "Column C"]
)

# Display DataFrame
st.write("Here is a random DataFrame:")
st.dataframe(data)

# Line Chart
st.write("Line Chart of Random Data:")
st.line_chart(data)

import plotly.express as px

# Dropdowm for Chart Selection
chart_type = st.selectbox(
    "Select a Chart Type:",
    ["Line Chart","Scatter Plot","Bar Chart"]
)

# Render Interactive Charts Using Plotly
if chart_type == "Line Chart":
    fig = px.line(data, x=data.index, y="Column A", title="Interactive Line Chart")
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Scatter Plot":
    fig = px.scatter(
        data,
        x="Column A",
        y="Column B",
        size=np.abs(data["Column C"]), # Bubble size based on Column C
        color="Column C",
        title="Interactive Scatter Plot"
    )
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Bar Chart":
    fig = px.bar(
        data,
        x=data.index,
        y="Column A",
        title="Interactive Bar Chart"
    )
    st.plotly_chart(fig, use_container_width=True)