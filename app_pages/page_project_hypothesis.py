import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write(f"Project Hypothesis and Validation")
    st.info(
        f"Cherry leaves infexted with powdery mildew have a different "
        f"apperance than healthy cherry leaves.\n"
        f"Typically, this is white spots on an infected leaf."
    )
    st.success(
        f"This was shown by:\n"
        f"* The Image Montage showed that the infected leaves "
        f"had white spots on them.\n"
    )
    st.info(
        f"Healthy cherry leaves have more green visable as proven by their "
        f"average and variability images."
    )
    st.success(
        f"This was shown by:\n"
        f"* The average and varibility images showed a difference between "
        f"the healthy and infected leaves.")
    st.info(
        f"That using Machine Learning, costs can be saved on health checks")
    st.success(
        f"Though this would not be proven until taken into practice. "
        f"Whilst each tree would need leaves taken and photographed, "
        f"there is the ability to upload multiple images at the same, "
        f"which would save time. This cannot be fully validated at this point."
    )