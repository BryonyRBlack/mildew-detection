# ![Header image saying Powdery Mildew Detector](/assests/images/Brown%20Aesthetic%20Email%20header.png)

## Project Overview

[Powdery Mildew Detector](https://mildew-detection-xff2.onrender.com/) is a machine-learning project. This is to assess if a cherry leaf is infected with Powdery Mildew or not. The dataset used is from Kaggle.

## Table of Contents

- [](#)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
    - [Hypothesis](#hypothesis)
    - [Validation](#validation)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design](#dashboard-design)
    - [Quick Project Summary](#quick-project-summary)
    - [Project Hypothesis](#project-hypothesis)
    - [Leaf Visualizer](#leaf-visualizer)
    - [Mildew Detection](#mildew-detection)
  - [Model Performance Metrics](#model-performance-metrics)
  - [Epic and User Stories](#epic-and-user-stories)
    - [Epic 1 - Data Collection and preparation](#epic-1---data-collection-and-preparation)
    - [Epic 2 - Data Visualization and Exloratory Analysis](#epic-2---data-visualization-and-exloratory-analysis)
    - [Epic 3 - Model Development and Optimization](#epic-3---model-development-and-optimization)
    - [Epic 4 -- Dashboard Development](#epic-4----dashboard-development)
    - [Epic 5 - Model Evaluation and Deployment](#epic-5---model-evaluation-and-deployment)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
    - [Render](#render)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Testing](#testing)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
- The dataset contains 4,208 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

### Hypothesis

- That cherry leaves infexted with powdery mildew have a different apperance than healthy cherry leaves.
- Healthy cherry leaves have mire green visable as proven by their average and variability images.
- That using Machine Learning, costs can be saved on health checks.

### Validation

**Dataset**

- A visual analysis was completeld on the data to see if there was any notable differences. As such, it was possible to note that there was a powdery substance on the leaves infected with Powdery Mildew.

A healthy leaf looks like:

![Image of a healthy leaf.](/outputs/v1/healthy%20leaves.png)

Whilst a leaf with Powdery Mildew:

![Image of a leaf that is infected with Powdery Mildew](/outputs/v1/powdery%20mildew%20leaves.png)

- To further analyse this, average and variability images were created

![Average and variability images for an infected leaf](/outputs/v1/avg_var_powdery_mildew.png)
![Average and variability images for an infected leaf](/outputs/v1/avg_var_healthy.png)

This showed a clear visual difference between the healthy and infected leaves and confirms the first hypothesis, it also confirms the second, and that more green is visable.

**Model Development**

- To train a model to be able to differentiate between a healthy and infected leaf. This was then evaluated to check it's accuracy.

![Image showing the accuracy after model training](/outputs/v1/model_training_acc.png)
![Image showing the losses after model training](/outputs/v1/model_training_losses.png)

**Costs**
Though this would not be proven until taken into practice. Whilst each tree would need leaves taken and photographed, there us ability to upload multiple images at the same time this would save time. This cannot be fully validated at this point.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- Business Requirement #1 - Data Visualization
  - average images and variability images for each class (healthy or powdery mildew),
  - the differences between average healthy and average powdery mildew cherry leaves,
  - an image montage for each class.
- Business Requirement #2
  - Build a ML system that is capable of predicting whether a cherry leaf is healthy or contains powdery mildew.

## ML Business Case

- We want a ML model that can quickly identify if a cherry leafe is infected with Powdery Mildew.
- This should also show the difference between infected and non-infectead leaves
- The model success metrics are at least 75% recall.
- The model output is definited as a flag, indicating if the leaf has Powdery Mildew.
- The training set comes from Kaggle, and contains over 4,000 images.

## Dashboard Design

### Quick Project Summary

- Provides an explanation about what Powdery Mildew is.
- Provides a link to Kaggle dataset that has been used.
- Advises that further information is in the ReadMe
- Confirms the Business Requirements

### Project Hypothesis

- Advises what the hypothesis is
- Using the data analysis, is able to validate.

### Leaf Visualizer

- Shows images of leaves with Powdery Mildew, and healthy leaves.
- A montage is available for the user to view.
- -Checkboxes used for ease to the user.

### Mildew Detection

- Allows for an image to be uploaded to predict if Powdery Mildew is present. Alternativly, an image can be downloaded from the dataset.
- Multiple images can be uploaded for a prediction.
- An analysis report is provided, this can be downloaded.

## Model Performance Metrics

- Bar chart showing the distribution.
- Training accuracy and loss
- Test set performance metrics

## Epic and User Stories

### Epic 1 - Data Collection and preparation

As a data analyst, I need to collect and prepare the data in order to train the model.

User Stories:

- As a data analyst, I am able to import the dataset. I am anle to load it within the project to gain further insights.
- I am able to analyse the data in order to distribute it fairly for a model training purpose.

### Epic 2 - Data Visualization and Exloratory Analysis

As a data analyst, I need to visually analyse and explore the date to understand key differences.

User Stories:

- I can genrate average and variabilitiy images, which can be used to display visual differences.
- I can create an image montage, that can be used to see both healthy or infected leaves.
- I have generated bar charts to show the dataset distribution of sets. This is to ensure that the data is split evenly accross Training, Validation and Test sets.

### Epic 3 - Model Development and Optimization

As a machine learning engineer I need to train a ML model to predict if a leaf is healthy or infected.

User Stories:

- I can fit a ML pipeline, with the data to train the ML model.
- I can analysie which is the best algorithm.
- I can carry out oprimisations to ensure the ML gives accurate results.

### Epic 4 -- Dashboard Development

As a product owner, I need a dashboard which can predict from user uploaded images, and is user-friendly.

User Stories:

- As a user, I can see the project summary page to understand the purpse.
- As a user I can see visualizations to understand and verify the outcomes.
- As a user, I can upload my own images of cherry leaves to check if healthy or infected.
- As a user I can download a report of my images.

### Epic 5 - Model Evaluation and Deployment

As a machine learning engineer, I need to test and deploy the model to ensure it works in a real world setting.

- I want to deploy the model, so that users can interact with it.
- I can test the system with unseen images.
- As a user, I want a simple interface.

## Unfixed Bugs

- There are currently no unfixed bugs.

## Bugs

- During deployment, the slug size was too large for Heroku. I moved as much as possible to .slugignore however this was still too large. After speaking with my mentor, this was then uploaded to render.com which worked.

## Deployment

### Render

- The App live link is: [here](https://mildew-detection-xff2.onrender.com/)
- The project was deployed to Render using the following steps.

1. Log in to Render and create a Web Service
2. At the Soure Code, select GitHub as the deployment method.
3. Input the html code, and click connect.
4. Name the Web Page, and confirm the coding language as Python, and the branch.
5. Set the Build Command as: pip install -r requirements.txt && ./setup.sh
6. Set the Start Command as: streamlit run app.py
7. Build the app.
8. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.

## Main Data Analysis and Machine Learning Libraries

- numpy - to convert information into arrays
- pandas - for creating and saving dataframes
- matplotlib - for plotting the datasets distribution
- plotly - for plotting the ML learning curve
- streamlit - for creating the dashboard
- joblib - for running tasks
- scikit-learn - for model evaluation
- tensorflow-cpu - for model creation
- keras>=3.0.0 - for model hyperparameters
- render - for hosting the dashboard
- git/github - for writing and storing the code
- kaggle - for the data used in the project

## Testing

All code in the app_pages, src directories, and notebooks have been run through PEP8 and passed. The exceptions are:

- Some code was "line too long". This was in importing documentation, or to set up graphs.
- In pip installation, PEP8 suggested symbols would need to have whitespace. Howevever this would then not work

## Credits

- Whilst creating this project, I used Code Institute's Malaria testing walkthrough project videos as a guide.
- The template used, is the one provided by Code Institute

### Content

- The information about Powdery Mildew was taken from [treefruit](https://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/)

### Media

- The image for the ReadMe header came from [canva](https://www.canva.com/templates/EAFw8hKewR4-brown-aesthetic-email-header/)

## Acknowledgements

- I would like to thank my mentor Mo Shami for his support and guidance during this project.
