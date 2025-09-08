import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random

def page_leaf_visualizer_body():
    st.write("~~~ Leaf Visualizer ~~~")
    st.info(
        f"This is to answer business requirement #1:\n"
        f"* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew"
    )
    version = "v1"
    if st.checkbox("Difference between average and variability image"):
        avg_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        st.warning(
            f"There is a difference between the healthy leaves and those with mildew.\n"
            f"The healthy leaves are green, whilst the Mildew shows as white dots over the leaf"
        )
        st.image(avg_mildew, caption="Powdery Mildew Infected leaf - Average and Variability")
        st.image(avg_healthy, caption="Healthy Leaf - Average and Variability")
        st.write("~~~")
        if st.checkbox("Differences between leaves"):
            diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
            st.warning(
                f"We notice that the healthy leaves are greener than the infected"
            )
            st.image(diff_between_avgs, caption="Difference between Average Images")
        if st.checkbox("Image Montage"):
            st.write("To refresh, click 'Create Montage")
            my_data_dir="inputs/datasets/cherry-leaves"
            labels = os.listdir(my_data_dir+ "/validation")
            label_to_display = st.selectbox(label="Select a label", options=labels, index=0)
            if st.button("Create Montage"):
                image_montage(dir_path=my_data_dir + "/validation",
                              label_to_display=label_to_display,
                              nrows=8,
                              ncols=3,
                              figsize=(10,25))
            st.write("~~~")

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    sns.set_style("dark")
    labels = os.listdir(dir_path)
    if label_to_display in labels:
        images_list = os.listdir(dir_path + "/" + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease rows or collums to create montage.\n"
                f"There are {len(images_list)}.\n"
                f"There are {nrows * ncols} in your request"
            )
            return
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + "/" + label_to_display + "/" + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px X Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()
        st.pyplot(fig=fig)
    else:
        print(f"The selected label doesn't exist.")
        print(f"Please select: {labels}")