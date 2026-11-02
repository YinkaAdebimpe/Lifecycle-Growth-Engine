# Customer Lifecycle & Growth Engine

**Author:** Yinka Adebimpe  
**Project:** E-commerce Customer Retention & Churn Prediction  
**Repo:** [Lifecycle-Growth-Engine](https://github.com/YinkaAdebimpe/Lifecycle-Growth-Engine)

---

## 📈 Business Context & Impact

**The Business Problem:**
For a UK-based online retailer, customer acquisition is expensive, making retention critical. Analysis of 397,885 transactions revealed a **33.4% churn rate**, representing **1,449 lost customers** and an estimated **£2.97M in lost revenue opportunity**. Furthermore, churned customers spent a median of £349, compared to £987 for active customers—meaning the business was losing its highest-potential buyers.

**The Data Solution:**
I built an RFM-based (Recency, Frequency, Monetary) churn prediction model using a Random Forest classifier. The model identifies active customers at risk of churning, allowing the marketing team to intervene with targeted retention campaigns before the customer is lost.

**The Business Impact:**
Simulating a retention campaign on a holdout test set:
- **Model Performance:** ROC-AUC 0.785 (catching 81% of actual churners).
- **Campaign Efficiency:** Targeting the predicted churners with a £10 discount would cost **£4,600**.
- **Net Profit:** With a conservative 15% retention success rate, the model saves **£72,721 in revenue**, yielding a **Net Profit of £68,121** (a 15x ROI).

---

## 🛠️ Technical Summary

### Data
- **Source:** Online Retail II dataset (UCI/Kaggle).
- **Scale:** 397,885 transactions, 4,338 unique customers.
- **Timeframe:** December 2010 – December 2011.

### Methodology
1. **Cohort Analysis** — Tracked retention by monthly cohorts; found that if a customer survives past the first 30 days, retention stabilizes.
2. **RFM Engineering** — Calculated Recency, Frequency, and Monetary value for each customer.
3. **Machine Learning** — Trained Logistic Regression and Random Forest models (ROC-AUC 0.785) to predict churn based on purchase behaviour.
4. **ROI Analysis** — Translated model predictions into a financial campaign simulation.

### Key Findings
- **The 90-Day Window:** Customers with no purchase in 90 days have effectively churned. 
- **Frequency Drives Retention:** Customers who make 10+ purchases almost never churn, whereas 1-order customers churn at a rate of 50%+.
- **Model Trade-off:** The model prioritizes *Recall* (0.81) over *Precision* (0.51) because in retention, a false alarm (wasted discount) is cheaper than a missed churner (lost LTV).

---

## 📂 Repository Structure

```text
.
├── data/                   # Raw and processed datasets
├── images/                 # Charts and heatmaps
├── models/                 # Trained .pkl files
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_cohort_and_churn.ipynb
│   ├── 03_churn_model.ipynb
│   └── 04_roi_analysis.ipynb
├── src/
│   └── config.py
├── reports/
│   ├── Executive_Summary.md
│   └── Technical_Report.md
├── README.md
└── requirements.txt
