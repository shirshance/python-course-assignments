# Lung Cancer Prediction with Machine Learning

## Project description

In this project, I used a lung cancer dataset from Kaggle to build a simple machine learning model.

The goal was to predict whether a patient has lung cancer based on clinical and lifestyle features such as age, gender, smoking, coughing, wheezing, fatigue, chest pain, and other symptoms.

This is a beginner machine learning project, so I used Logistic Regression.

## Dataset

Dataset name: Lung Cancer Prediction Dataset
Source: Kaggle

The dataset contains 284 samples and 16 attributes.

The target column is:

* `LUNG_CANCER`

The model tries to predict:

* `YES`
* `NO`

## Features

The input features include:

* Gender
* Age
* Smoking
* Yellow fingers
* Anxiety
* Peer pressure
* Chronic disease
* Fatigue
* Allergy
* Wheezing
* Alcohol
* Coughing
* Shortness of breath
* Swallowing difficulty
* Chest pain

## How to download the data

1. Go to Kaggle.
2. Search for: `Lung Cancer Prediction Dataset`
3. Download the CSV file.
4. Put the CSV file in the same folder as the Python script.
5. Make sure the file is named:

```bash
survey lung cancer.csv
```

## How to run

Install the required packages:

```bash
pip install pandas scikit-learn
```

Run the script:

```bash
python3 lungcancer.py
```

## What the script does

The script:

1. Loads the CSV file.
2. Converts text values to numbers.
3. Splits the data into training and testing sets.
4. Trains a Logistic Regression model.
5. Predicts lung cancer status.
6. Prints the accuracy, confusion matrix, classification report, and most important features.

## Machine learning method

I used Logistic Regression.

Logistic Regression is a simple classification model. It learns how different features are associated with the probability of lung cancer.

## Prompts used with ChatGPT

I found a lung cancer dataset on Kaggle and want to use it for a machine learning project in Python. Can you help me write the code? Please keep it beginner-friendly. I would like to predict whether a patient has lung cancer based on the provided clinical and lifestyle features, using Logistic Regression. Also explain each step of the process.
