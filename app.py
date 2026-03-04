import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Breast Cancer 10-Year Mortality Risk Predictor",
    page_icon="🩺",
    layout="wide"
)

pipeline = joblib.load("breast_cancer_10yr_pipeline.pkl")

# ---------------- GLOBAL STYLE ---------------- #
st.markdown("""
<style>
.stApp {
    background-color: #f4f6f9;
}

.main-header {
    text-align: center;
    padding: 25px 0 10px 0;
}

.main-header h1 {
    color: #1B3B5F;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("""
<div class="main-header">
    <h1>🩺 Breast Cancer 10-Year Mortality Risk Predictor</h1>
</div>
""", unsafe_allow_html=True)

# ---------------- INFO ---------------- #
with st.expander("ℹ Understanding the Input Features"):
    st.markdown("""
**Age at Diagnosis**  
Patient’s age when breast cancer was diagnosed.

**Type of Breast Surgery**  
- *Breast Conserving*: Only tumor and small surrounding tissue removed.  
- *Mastectomy*: Entire breast removed.

**Cancer Type Detailed**  
Histological type of breast cancer (e.g., ductal or lobular).

**Cellularity**  
How densely packed the tumor cells appear under a microscope.

**ER / PR Status**  
Estrogen and Progesterone receptor status.  
Positive means the tumor grows in response to hormones.

**HER2 Status**  
Protein affecting cancer growth. Positive HER2 cancers tend to grow faster.

**Neoplasm Histologic Grade**  
How abnormal cancer cells look:
- Grade 1 → Slow growing  
- Grade 3 → Aggressive

**Lymph Nodes Examined Positive**  
Number of lymph nodes where cancer spread.

**Tumor Size**  
Size of tumor in millimeters.

**Tumor Stage**  
Overall extent of cancer spread (Stage I = early, Stage IV = advanced).
""")

st.markdown("---")

st.subheader("Patient Clinical Information")

col1, col2 = st.columns(2)

# -------- LEFT (7) -------- #
with col1:
    age = st.number_input("Age at Diagnosis", 20, 100, 50)
    surgery = st.selectbox("Type of Breast Surgery", ["MASTECTOMY", "BREAST CONSERVING"])
    cancer_type = st.selectbox("Cancer Type Detailed",
                               ["Invasive Ductal Carcinoma",
                                "Invasive Lobular Carcinoma"])
    cellularity = st.selectbox("Cellularity", ["High", "Moderate", "Low"])
    chemo = st.selectbox("Chemotherapy", ["YES", "NO"])
    er_status = st.selectbox("ER status measured by IHC", ["Positive", "Negative"])
    pr_status = st.selectbox("PR Status", ["Positive", "Negative"])

# -------- RIGHT (7) -------- #
with col2:
    her2 = st.selectbox("HER2 Status", ["Positive", "Negative"])
    grade = st.selectbox("Neoplasm Histologic Grade", ["Grade 1", "Grade 2", "Grade 3"])
    hormone = st.selectbox("Hormone Therapy", ["YES", "NO"])
    nodes = st.number_input("Lymph nodes examined positive", 0, 50, 0)
    radio = st.selectbox("Radio Therapy", ["YES", "NO"])
    tumor_size = st.number_input("Tumor Size (mm)", 1, 200, 20)
    stage = st.selectbox("Tumor Stage", ["Stage I", "Stage II", "Stage III", "Stage IV"])

st.markdown("---")

# ---------------- PREDICTION ---------------- #
if st.button("🔍 Predict 10-Year Mortality Risk"):

    input_df = pd.DataFrame([{
        "Age at Diagnosis": age,
        "Type of Breast Surgery": surgery,
        "Cancer Type Detailed": cancer_type,
        "Cellularity": cellularity,
        "Chemotherapy": chemo,
        "ER status measured by IHC": er_status,
        "PR Status": pr_status,
        "HER2 Status": her2,
        "Neoplasm Histologic Grade": grade,
        "Hormone Therapy": hormone,
        "Lymph nodes examined positive": nodes,
        "Radio Therapy": radio,
        "Tumor Size": tumor_size,
        "Tumor Stage": stage
    }])

    prob = pipeline.predict_proba(input_df)[0][1]

    threshold_low = 0.35
    threshold_high = 0.65

    st.subheader("Prediction Result")

    if prob < threshold_low:
        risk_color = "#27AE60"
        risk_text = "LOW RISK"
    elif threshold_low <= prob < threshold_high:
        risk_color = "#F39C12"
        risk_text = "MODERATE RISK"
    else:
        risk_color = "#C0392B"
        risk_text = "HIGH RISK"

    st.markdown(f"""
    <div style="
        background-color:{risk_color};
        padding:25px;
        border-radius:10px;
        text-align:center;
        color:white;
        font-size:24px;
        font-weight:bold;">
        {risk_text}
        <br>
        Probability of 10-Year Mortality: {prob:.2%}
    </div>
    """, unsafe_allow_html=True)

    st.caption("Disclaimer: This model is for research and educational purposes only.")