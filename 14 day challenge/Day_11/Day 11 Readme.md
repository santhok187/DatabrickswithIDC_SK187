# 🚀 Day 11 – Databricks 14 Days AI Challenge  
📅 19/01/26  
📊 Statistical Analysis & ML Prep

---

## 📖 Learn
- Descriptive statistics  
- Hypothesis testing  
- A/B test design  
- Feature engineering  

---

## 🛠️ Tasks
1. Calculate statistical summaries  
2. Test hypotheses (weekday vs weekend)  
3. Identify correlations  
4. Engineer features for ML  

---

## 🧑‍💻 Hands-On Work
- Loaded October events dataset into Spark.  
- Computed **descriptive statistics** (mean, stddev, min, max, mode) for each brand.  
- Added **weekday vs weekend flag** and calculated conversion ratios.  
- Engineered brand-level features:  
  - Total views, carts, purchases  
  - View→purchase and cart→purchase conversion rates  
  - Weekly purchase ratios  
- Calculated **overall sales per brand** and joined with conversion metrics.  
- Added descriptive stats to derived features.  
- Performed **correlation analysis**:  
  - Total price vs conversion rates  
  - Cart→purchase vs view→purchase rates  
- Saved results into **Gold Delta table: `ecom.gold.Derived_Features`**.  
- Visualized top brands by conversion and sales across weekday vs weekend.  

---

## 📊 Insights
- **Descriptive statistics** summarize brand-level behavior.  
- **Hypothesis testing** validates weekday vs weekend conversion differences.  
- **A/B test design** principles applied to event data.  
- **Feature engineering** transforms raw events into ML-ready features.  
- **Correlation analysis** reveals relationships between sales and conversion rates.  

---

## 🙌 Reflection
Day 11 showed how **statistics and hypothesis testing** bridge raw event data with ML pipelines.  
By engineering features and validating correlations, we ensure models are trained on **meaningful, business-relevant signals**.

---

#DatabricksWithIDC #AIChallenge #Day11 #StatisticalAnalysis #HypothesisTesting #ABTesting #FeatureEngineering #MLPrep #DeltaLake #BigData