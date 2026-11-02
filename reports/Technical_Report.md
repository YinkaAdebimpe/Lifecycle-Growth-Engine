# Customer Retention & Growth Analytics — Technical Report

**Prepared by:** Yinka Adebimpe  
**Date:** November 2026

---

## 1. Introduction & Objective
To build a comprehensive customer lifecycle engine that predicts churn, validates segment differences statistically, maps the purchase funnel, and forecasts future revenue to support business decision-making.

## 2. Data
- **Source:** Online Retail II (UCI).
- **Size:** 397,885 cleaned transactions across 4,338 unique customers.
- **Timeframe:** Dec 2010 – Dec 2011.
- **Cleaning:** Removed missing Customer IDs, negative quantities (returns), and zero prices.

## 3. Methodology

### 3.1 Cohort Analysis
Built monthly cohorts based on first purchase date. Findings showed a steep drop-off in Month 1 retention, but stabilization thereafter. 

### 3.2 RFM Engineering
Aggregated data by `customer_id` to calculate Recency (days), Frequency (unique invoices), and Monetary (total spend). We excluded Recency from the features to prevent target leakage, as the target (churn) is defined by Recency.

### 3.3 Modelling
- **Models:** Logistic Regression (baseline) and Random Forest.
- **Class Imbalance:** Used `class_weight='balanced'`.
- **Metric:** ROC-AUC.
- **Results:** Random Forest achieved an ROC-AUC of **0.785**. The model prioritized Recall (0.81) over Precision (0.51) to maximize the number of at-risk customers captured.

### 3.4 Advanced Analytics
- **A/B Testing:** Applied an independent T-test (`scipy.stats.ttest_ind`) comparing UK vs. International order values to validate segment spending differences.
- **Funnel Analysis:** Aggregated basket sizes to map the purchase funnel and identify drop-off rates.
- **Time-Series Forecasting:** Utilized Holt-Winters Exponential Smoothing (`statsmodels`) on monthly aggregated revenue to forecast a 3-month horizon, accounting for trend.

### 3.5 ROI Calculation
- **Targeting:** Flagged customers with `churn_prob > 0.50`.
- **Cost:** £10 discount * 460 targeted customers = £4,600.
- **Revenue Saved:** (236 true positives * 15% success rate) * £2,054 avg LTV = £72,721.
- **Net Profit:** £68,121.

## 4. Limitations & Next Steps
- **Historical Snapshot:** The dataset represents a single year. A production model would retrain monthly.
- **Seasonality:** The forecasting model used trend-only due to insufficient data for seasonality (less than 24 months).
- **Causal Inference:** The 15% retention rate is an assumption. A real business should A/B test the discount campaign to measure the true lift.

