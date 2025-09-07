# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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

### Validation

### Dataset

- A visual analysis was completeld on the data to see if there was any notable differences. As such, it was possible to note that there was a powdery substance on the leaves infected with Powdery Mildew.

A healthy leaf looks like:

![Image of a healthy leaf.](/outputs/v1/healthy%20leaves.png)

Whilst a leaf with Powdery Mildew:

![Image of a leaf that is infected with Powdery Mildew](/outputs/v1/powdery%20mildew%20leaves.png)

- To further analyse this, average and variability images were created

![Average and variability images for an infected leaf](/outputs/v1/avg_var_powdery_mildew.png)
![Average and variability images for an infected leaf](/outputs/v1/avg_var_healthy.png)

This showed a clear visual difference between the healthy and infected leaves.

### Model Development

- To train a model to be able to differentiate between a healthy and infected leaf. This was then evaluated to check it's accuracy.

![Image showing the accuracy after model training](/outputs/v1/model_training_acc.png)
![Image showing the losses after model training](/outputs/v1/model_training_losses.png)

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- Business Requirement #1
  - average images and variability images for each class (healthy or powdery mildew),
  - the differences between average healthy and average powdery mildew cherry leaves,
  - an image montage for each class.
- Business Requirement #2
  - You may deliver an ML system that is capable of predicting whether a cherry leaf is healthy or contains powdery mildew. In this case, we suggest to use Neural Networks to map the relationships between the features and the labels.

## ML Business Case

- We want a ML model that can quickly identify if a cherry leafe is infected with Powdery Mildew.
- This should also show the difference between infected and non-infectead leaves

## Dashboard Design

### Quick Project Summary

- Provides an explanation about what Powdery Mildew is.
- Provides a link to Kaggle dataset that has been used.
- Advises that further information is in the ReadMe
- Confirms the Business Requirements

### Project Hypothesis

- Advises that the hypothesis is that it is possible to distinguish leaves with Powdery Mildew, from healthy leaves.
- Using the data analysis, is able to validate.

### Leaf Visualizer

- Shows images of leaves with Powdery Mildew, and healthy leaves.
- A montage is available for the user to view.

### Mildew Detection

- Allows for an image to be uploaded to predict if Powdery Mildew is present. Alternativly, an image can be downloaded from the dataset.
- Multiple images can be uploaded for a prediction.
- An analysis report is provided, this can be downloaded.

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.
- There are currently no unfixed bugs.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

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

## Credits

- Whilst creating this project, I used Code Institute's Malaria testing walkthrough project videos as a guide.
- The template used, is the one provided by Code Institute

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
