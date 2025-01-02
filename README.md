# **INCOME Prediction** - YASHASWINI
### **Introduction About the Data**:
**Introduction: Adult Income Prediction Project**  
The **Adult Income Prediction project** aims to predict whether an individual earns more or less than **$50,000** per year based on demographic and work-related attributes. This project provides insights into income distribution patterns and helps build predictive models using machine learning techniques. It also serves as a practical application for data preprocessing, feature engineering, and classification algorithms, making it a valuable learning experience in the field of data science.

---

### **Dataset Description: Adult Income Prediction (Census Income Data)**

**Goal:** The goal of this dataset is to predict the income of individuals, specifically whether they earn more than $50,000 per year (binary classification).

---

#### **Independent Variables:**

1. **age**: Age of the individual.
2. **workclass**: Type of employment (e.g., Private, Self-emp-not-inc, Government).
3. **fnlwgt**: Final weight, representing the number of people the census results are weighted to represent.
4. **education**: Highest level of education attained (e.g., Bachelors, Masters, Doctorate).
5. **education-num**: Number of years of education (numeric representation).
6. **marital-status**: Marital status (e.g., Married-civ-spouse, Divorced, Never-married).
7. **occupation**: Occupation of the individual (e.g., Tech-support, Sales, Executive).
8. **relationship**: Relationship status (e.g., Husband, Wife, Own-child).
9. **race**: Racial group (e.g., White, Black, Asian-Pac-Islander).
10. **sex**: Gender of the individual (Male/Female).
11. **capital-gain**: Capital gains earned (numeric value).
12. **capital-loss**: Capital losses (numeric value).
13. **hours-per-week**: Number of hours worked per week (numeric value).
14. **native-country**: Country of origin (e.g., United-States, Mexico, India).

---

#### **Target Variable:**

1. **income**: The target variable that indicates whether an individual earns more than $50K per year (binary classification: ">50K" or "<=50K").
---

Dataset Source Link:  https://www.kaggle.com/datasets/wenruliu/adult-income-dataset

- **continuous variables** ('age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week') 

- **categorical variables** ('workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country') 
categorical variables are encoded using target encoding 

--- 

### Deployment Link: http://127.0.0.1:5001
#### Screen shot of UI:
![alt text](<Screenshots/Screenshot (3).png>)

---




### *POSTMAN TESTING OF API*:
![alt text](Screenshots/Screenshot(1).jpeg)

---
### *APPROACH FOR THE PROJECT*
#### **Data Ingestion**:
   In the Data Ingestion phase, the dataset is read from a CSV.
   It is then inspected for missing values and duplicates.
   Missing values in categorical variables such as workclass, occupation, and native.country are imputed using the most frequent values (mode).
   The dataset is split into training and testing sets using train_test_split from sklearn.

#### **Data Transformation**:
 In the Data Transformation phase, the data is processed using the following steps:

#### **Target Encoding**:
The categorical columns (workclass, education, marital.status, occupation, relationship, race, sex, native.country) are encoded using TargetEncoder, where the categories are replaced by the average target value for each category.
SMOTE: Synthetic Minority Over-sampling Technique (SMOTE) is applied to handle class imbalance by generating synthetic samples.
Standard Scaling: All numerical features are scaled using StandardScaler, ensuring that they have zero mean and unit variance.
A pipeline is created with the following stages:

- Target Encoding of categorical features

- SMOTE for handling class imbalance

- Standard Scaling of numerical features

- Logistic Regression as the model

#### **Model Training**:
In the Model Training phase, the pipeline is fitted on the training data, where it applies encoding, scaling, and training the LogisticRegression model. The LogisticRegression model is set with C=0.5 and max_iter=500 to optimize the results. The model's performance is evaluated using the accuracy score on the test data.

The pipeline, which includes all preprocessing steps and the trained model, is saved as a .pkl file using joblib. This allows for easy loading and reusability in the future.

#### **Prediction Pipeline**:
In the Prediction Pipeline, a function is created to load the saved pipeline (logistic_pipeline.pkl) and use it for predictions on new data. The pipeline can take in user data, preprocess it, and output the predicted income class (<=50K or >50K).

#### **Flask App Creation**:
A Flask web application is developed with a user interface where users can input their data to predict whether their income is greater than $50K or not. The Flask app integrates the prediction pipeline and displays the prediction result.

---

### Notebook for Adult Income Prediction Model:
Link : [NoteBook](Notebook.ipynb)

---
### TECH STACK
| **Technology**            | **Purpose**                               |
|---------------------------|-------------------------------------------|
| **Flask**                  | Backend Framework                        |
| **HTML**                   | Frontend Development (Website Structure) |
| **CSS**                    | Styling the Website                      |
| **JavaScript**             | Frontend Interactivity (optional)        |
| **Python (pandas, openpyxl)** | Data Processing, Storing Predictions and Form Inputs in Excel |
| **Pickle**                 | Model Serialization (logistic_reg.pkl)    |
| **Postman**                | API Testing                              |
| **OS Module**              | Handling file operations (e.g., loading model, reading/writing Excel) |


