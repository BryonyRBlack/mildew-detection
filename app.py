import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_leaf_visualizer import page_leaf_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_ml_performance import page_ml_performance_metrics
from app_pages.page_project_hypothesis import page_project_hypothesis_body

app = MultiPage(app_name="Powedery Mildew Detector")

app.add_page("Project Summary", page_summary_body)
app.add_page("Leaf Visualizer", page_leaf_visualizer_body)
app.add_page("Powdery Mildew Detector", page_mildew_detector_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)
app.add_page("Project Hypothesis", page_project_hypothesis_body)

app.run()