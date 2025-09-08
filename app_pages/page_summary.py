import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():
    st.write(f"~~~ Quick Prokect Summary ~~~")
    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is caused by Podosphaera clandestina, an obligate biotrophic fungus."
        f"Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected,"
        f"rendering them unmarketable due to the covering of white fungal growth on the cherry surface."
        f"Season long disease control of both leaves and fruit is critical to minimize overall disease pressure in the orchard"
        f"and consequently to protect developing fruit from accumulating spores on their surfaces."
    )
    st.write(
        f"**Dataset**\n\n"
        f"The dataset contains 4,208 images of cherry leaves."
        f"Half of these are healthy leaves, the other have Powdery Mildew"
        f"The dataset is availble from Kaggle [here](https://www.kaggle.com/codeinstitute/cherry-leaves)"
    )
    st.success(
        f"Buisness Requirements\n\n"
        f"Currently, the way to identify this is to manually look at the leaves."
        f"As an alternative, using photographs would save time and money.\n"
        f"As such, the requirements are:\n"
        f"* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
    )