import streamlit as st
import matplotlib.pyplot as plt

def page_project_hypothesis_body():
    st.write(f"Project Hypothesis and Validation")
    st.info(
        f"Cherry leaves infexted with powdery mildew have a different apperance than healthy cherry leaves.\n"
        f"Typically, this is white spots on an infected leaf."
    )
    st.success(
        f"This was shown by:\n"
        f"* The Image Montage showed that the infected leaves had white spots on them.\n"
        f"* The average and varibility images showed a difference between the healthy and infected leaves."
    )