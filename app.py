import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(  page_title="CNN Plant Detection Results App", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp {
        background-color: #27ae60;
    }
    .stMetric {
        background-color: #dcfce7;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #27ae60;
    }
    h1, h2, h3 {
        color: #1e3a1f;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("CNN Plant Detection Results Website by the glorious Alex and Sam")

cross_v = pd.read_csv("Cross Validation results on 5 folds.csv")
p1 = pd.read_csv("Predictions for 1 fold.csv")
p2 = pd.read_csv("Predictions for 2 fold.csv")
p3 = pd.read_csv("Predictions for 3 fold.csv")
p4 = pd.read_csv("Predictions for 4 fold.csv")
p5 = pd.read_csv("Predictions for 5 fold.csv")
predictions = pd.concat([p1, p2, p3, p4, p5], ignore_index=True)


tab1, tab2 = st.tabs(["Landing page", "Interactive visualization"])
with tab1:
    st.header("Plant Disease Detection by Alex Vuong and Samantha Sobhian ")
    st.write("""
             
    We made a Plant Disease Detection model using CNN binary classification and Bayesian optimization.

    The model was trained on a dataset of plant images.

    Here in this page, you will interact with the CNN's predictions and performance metrics.

    🌱 🌿 🪴 Enjoy 🌱 🌿 🪴   

    """)


    st.markdown("<br>" * 16, unsafe_allow_html=True)
    st.markdown("2$%$ extra credit here I come 😋")


with tab2:


    dropdown = st.selectbox(
        "Select Fold(s) to see their results:",
        ["All Folds"] + sorted(predictions['Fold'].unique().tolist())
    )

    if dropdown == "All Folds":
        df = predictions.copy()
    else:
        df = predictions[predictions['Fold'] == dropdown]

    
    correct = (df["Correct Classification Or Not"] == 1).sum()
    incorrect = (df["Correct Classification Or Not"] == 0).sum()
    accuracy = correct / len(df) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy:", f"{accuracy}%")
    with col2:
        st.metric("Correct Predictions:", correct)
    with col3:
        st.metric("Incorrect Predictions:", incorrect)

    st.dataframe(df, use_container_width=True)


    st.header("Cross Validation Output of Each Fold and its Predictions")

    st.subheader("Cross Validation Accuracy of each Fold/Model")

    chart = alt.Chart(cross_v).mark_bar().encode(
        x='Fold:O',
        y='Test Accuracy:Q',
        tooltip=['Fold', 'Test Accuracy']
    ).interactive()

    st.altair_chart(chart, use_container_width=True)