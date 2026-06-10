import streamlit as st

from src.transform import reduce_dimension

st.set_page_config(
    page_title="PCA Dimensionality Reduction"
)

st.title(
    "📉 PCA Dimensionality Reduction"
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100
)

income = st.number_input(
    "Annual Income (k$)",
    min_value=0.0,
    max_value=150.0
)

score = st.number_input(
    "Spending Score",
    min_value=0.0,
    max_value=100.0
)

if st.button(
    "Reduce Dimensions"
):

    pc = reduce_dimension(
        age,
        income,
        score
    )

    st.success(
        f"Principal Component 1: {pc[0]:.2f}"
    )

    st.success(
        f"Principal Component 2: {pc[1]:.2f}"
    )