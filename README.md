\# Breast Cancer 10-Year Mortality Prediction



\## 📌 Project Overview



This project predicts 10-year mortality risk in breast cancer patients using the METABRIC dataset.



The objective is to build an interpretable machine learning model that can support treatment planning and clinical decision-making by identifying high-risk patients.



---



\## 🎯 Problem Statement



Can we predict whether a breast cancer patient will die within 10 years of diagnosis using clinical and treatment-related features?



This is framed as a binary classification problem:



\- 0 → Survived beyond 10 years  

\- 1 → Died within 10 years  



---



\## 📊 Dataset



\- Source: METABRIC (Molecular Taxonomy of Breast Cancer International Consortium)

\- Survival time and vital status used to create the target variable.



Rows with missing survival time or vital status were removed instead of imputed to preserve survival integrity.



---



\## 🎯 Target Variable



`10\_year\_mortality`



Created using:

\- Overall Survival (Months)

\- Patient Vital Status



---



\## 🧹 Data Preprocessing



\- Median imputation for numerical features

\- Mode imputation for categorical features

\- Binary mapping for treatment/status variables

\- One-hot encoding for multi-category features

\- Stratified train-test split

\- Class imbalance handled using `class\_weight='balanced'`



---



\## 📈 Exploratory Data Analysis



Key insights:



\- Mortality class imbalance observed.

\- Higher tumor stage strongly associated with mortality.

\- Larger tumor size linked to increased risk.

\- ER negative patients showed higher mortality patterns.

\- Older age groups had increased mortality rates.



---



\## 🤖 Models Evaluated



\- Logistic Regression

\- Decision Tree

\- Support Vector Machine (SVM)



---



\## 🏆 Final Model Selection



Logistic Regression was selected as the final model because:



\- Lowest False Negatives (important in healthcare)

\- Higher recall for mortality class

\- Competitive ROC-AUC

\- High interpretability for clinical context



Accuracy was NOT used as the primary decision metric.



---



\## 📊 Model Performance



\- ROC-AUC: ~0.83

\- Improved mortality recall using class weighting

\- Cross-validation performed to ensure stability

\- Confusion matrix used for detailed error analysis



---



\## ⏳ Survival Analysis



Kaplan–Meier survival curves were used to visualize survival probability over time.



This complements the machine learning classification by providing time-based survival insights.



---



\## 🛠 Tech Stack



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- Matplotlib

\- Seaborn

\- Lifelines



---



\## 🚀 Future Improvements



\- Cox Proportional Hazards model

\- External dataset validation

\- Deployment as clinical decision support tool

\- Feature importance interpretation using SHAP



---



\## 👩‍💻 Author



Tabassum Shaikh  

Aspiring Data Scientist | Machine Learning \& Healthcare Analytics

