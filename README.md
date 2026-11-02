# Customer Lifecycle & Growth Engine

**Author:** Yinka Adebimpe  
**Project:** E-commerce Customer Retention, Analytics & Forecasting  
**Repo:** [Lifecycle-Growth-Engine](https://github.com/YinkaAdebimpe/Lifecycle-Growth-Engine)

---

## 📈 Business Context & Impact

**The Business Problem:**
Customer acquisition is expensive, making retention the most profitable lever for growth. Analysis of 397,885 transactions revealed a **33.4% churn rate**, representing **1,449 lost customers** and an estimated **£2.97M in lost revenue opportunity**. Alarmingly, churned customers spent a median of £349, compared to £987 for active customers, meaning the business is losing its highest-potential buyers.

**The Data Solution:**
I built an end-to-end customer lifecycle engine. It uses RFM (Recency, Frequency, Monetary) engineering to segment customers, a Random Forest classifier to predict churn, and statistical forecasting to project future revenue. 

**The Business Impact:**
- **Churn Prevention:** Simulating a retention campaign on a holdout test set (ROC-AUC 0.785, Recall 0.81) yielded a **Net Profit of £68,121** from a £4,600 discount cost (a 15x ROI).
- **Revenue Forecasting:** A Holt-Winters time-series model forecasted an upward monthly revenue trend approaching **£1M per month** for Q1 2012.
- **Strategic Insights:** T-tests validated that UK and International segments spend differently, and funnel analysis exposed upsell opportunities in basket sizes.

---

## 🛠️ Technical Summary

### Data
- **Source:** Online Retail II dataset (UCI/Kaggle).
- **Scale:** 397,885 transactions, 4,338 unique customers (Dec 2010 – Dec 2011).

### Methodology & Key Findings
1. **Cohort & Churn Analysis:** Tracked monthly cohorts and defined churn as 90+ days of inactivity. Found that frequency dictates retention: 1-order customers churn at 50%+, while 10+ order customers almost never churn.
2. **Machine Learning (Churn):** Trained a Random Forest model to predict churn based on Frequency and Monetary value. Prioritized Recall (0.81) over Precision (0.51) to capture maximum at-risk revenue.
3. **Funnel Analysis:** Mapped basket sizes (1 item vs. 10 items) to identify the drop-off in multi-item purchases, highlighting a clear upsell opportunity.
4. **A/B Testing (T-Test):** Conducted an independent T-test (`scipy.stats`) comparing the average order value of UK vs. International customers to validate segment spending differences.
5. **Forecasting:** Utilized Holt-Winters Exponential Smoothing (`statsmodels`) to forecast a 3-month revenue horizon, providing a predictive budget tool for the executive team.

---

## 📂 Repository Structure

```text
.
├── data/                   # Raw and processed datasets
├── images/                 # Charts, heatmaps, and ROI plots
├── models/                 # Trained .pkl files
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_cohort_and_churn.ipynb
│   ├── 03_churn_model.ipynb
│   ├── 04_roi_analysis.ipynb
│   └── 05_advanced_analytics.ipynb
├── src/
│   └── config.py
├── reports/
│   ├── Executive_Summary.md
│   └── Technical_Report.md
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run
1. Clone the repo and install dependencies: `pip install -r requirements.txt`
2. Run the notebooks in order (`01` → `05`).
