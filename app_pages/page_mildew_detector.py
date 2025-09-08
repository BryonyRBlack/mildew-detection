import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analytics import(load_model_and_predict, resize_input_image, plot_predictions_probabilities)

def page_mildew_detector_body():
    st.info(f"To answer business requirement #2:"
            f"The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.")
    st.write(f"You can download a set of leaves with both healthy and Powdery Mildew, for live predicition"
             f"This is available [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)")
    st.write("~~~")
    images_buffer = st.file_uploader("Upload images, multiple can be selected", type="png", accept_multiple_files=True)
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            img_pil = (Image.open(image))
            st.info(f"Leaf provided: {image.name}")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image size: {img_array.shape[1]}px. Width X {img_array.shape[0]}px height")
            version = "v1"
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)
            df_report = df_report._append({"Name":image.name,
                                           "Result": pred_class}, ignore_index=True)
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)