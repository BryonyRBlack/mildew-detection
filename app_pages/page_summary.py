import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():
    st.write(f"Quick Prokect Summary")
    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is caused by Podosphaera clandestina, "
        f"an obligate biotrophic fungus. "
        f"Mid- and late-season sweet cherry (Prunus avium) cultivars "
        f"are commonly affected, rendering them unmarketable due to the "
        f"covering of white fungal growth on the cherry surface. "
        f"Season long disease control of both leaves and fruit is critical "
        f"to minimize overall disease pressure in the orchard and consequently "
        f"to protect developing fruit from accumulating spores "
        f"on their surfaces."
    )
    st.write(
        f"Dataset\n\n"
        f"The dataset contains 4,208 images of cherry leaves. "
        f"Half of these are healthy leaves, the other have Powdery Mildew "
        f"The dataset is availble from Kaggle "
        f"[here](https://www.kaggle.com/codeinstitute/cherry-leaves)"
    )
    st.success(
        f"Buisness Requirements\n\n"
        f"Currently, the way to identify this is to manually "
        f"look at the leaves. "
        f"As an alternative, using photographs would save time and money.\n"
        f"As such, the requirements are:\n"
        f"* The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that "
        f"contains powdery mildew.\n"
        f"* The client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew."
    )
