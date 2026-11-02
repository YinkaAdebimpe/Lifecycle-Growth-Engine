# Customer Retention & Growth Analytics — Executive Summary

**Client:** UK Online Retailer *(simulated via public data)*  
**Prepared by:** Yinka Adebimpe, Data Scientist  
**Date:** November 2026

---

## 1. The Business Problem
Customer acquisition costs are rising, making retention the most profitable lever for growth. Our analysis of 397,885 transactions found that **33.4% of our customer base has churned** (no purchase in 90 days). This represents **1,449 lost customers** and a projected **£2.97M in lost revenue**. 

Alarmingly, churned customers spent a median of £349 before leaving, compared to £987 for active customers. This suggests we are losing high-potential buyers before they reach full lifetime value.

## 2. The Solution: Predictive Analytics
We built a Machine Learning model (Random Forest) to identify active customers at high risk of churning, based on their purchase frequency and spend. 
- **Model Accuracy:** ROC-AUC 0.785
- **Recall:** The model successfully identifies **81% of all customers who are about to churn**.

Additionally, we ran statistical A/B tests (T-tests) to validate segment differences, mapped the basket-size funnel, and built a Holt-Winters forecasting model to project future revenue.

## 3. Financial Impact
Rather than a blanket discount, this model allows for targeted retention campaigns. 
**Scenario:** Sending a £10 discount to customers flagged as high-risk.
- **Cost:** Targeting 460 high-risk customers costs **£4,600**.
- **Return:** Assuming a conservative 15% campaign success rate, we save 236 customers from churning. At an average value of £2,054, this protects **£72,721 in revenue**.
- **Net Result:** A **£68,121 net profit** from a single campaign (15x ROI).

**Forecasting:** Our time-series model forecasts revenue approaching **£1M per month** for Q1 2012, allowing for proactive budgeting.

## 4. Recommendations
1. **Deploy the Model:** Use the Random Forest model to flag churn risks weekly and trigger £10 discounts.
2. **Focus on the First 30 Days:** Cohort analysis shows that if a customer makes a second purchase, retention stabilizes. Introduce a "second purchase" incentive for new customers.
3. **Upsell the Funnel:** The basket-size funnel shows most customers buy only 1 item. Implement "frequently bought together" recommendations to increase basket size.
