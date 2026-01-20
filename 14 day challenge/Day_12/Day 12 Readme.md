# 🚀 Day 12 – Databricks 14 Days AI Challenge  
📅 20/01/26  
📊 Product-Level Analysis & ML Prediction

---

## 📖 Learn
- Product-level conversion analysis  
- Outlier detection & thresholds  
- Feature engineering for ML  
- ML model training & evaluation  
- MLflow logging & Unity Catalog registration  

---

## 🛠️ Tasks
1. Aggregate product-level conversion metrics  
2. Engineer features (conversion rates, price stats)  
3. Handle outliers & label top sellers  
4. Build ML pipeline (Vector Assembler + GBT Classifier)  
5. Log & register model with MLflow + Unity Catalog  
6. Generate Rising Stars report  

---

## 🧑‍💻 Hands-On Work
- Created **product_features** table with conversion metrics & price stats.  
- Applied thresholds: views > 100, carts > 5, conversion rate filters.  
- Detected outliers using Z‑score and top 10% revenue threshold.  
- Labeled products as **Top Sellers (1) vs Others (0)**.  
- Built ML features with **VectorAssembler**.  
- Trained **GBT Classifier** to predict elite products.  
- Logged parameters, metrics, and feature importances with **MLflow**.  
- Registered model in **Unity Catalog** for governance.  
- Generated **Rising Stars report** → products with >80% success probability but not yet top sellers.  

---

## 📊 Insights
- Product-level ML prep requires stricter filters for high-quality signals.  
- Outlier handling improves robustness of features.  
- MLflow ensures reproducibility and governance.  
- Rising Stars report provides actionable insights for business teams.  

---

## 🙌 Reflection
Day 12 marked the transition from **analysis to prediction**.  
By combining product-level features, ML pipelines, and MLflow governance, I built a system that not only identifies **current top sellers** but also predicts **future rising stars**.

---

#DatabricksWithIDC #AIChallenge #Day12 #MLPrep #FeatureEngineering #GBTClassifier #MLflow #UnityCatalog #DeltaLake #BigData