# 🚀 Day 3 – Databricks 14 Days AI Challenge  
📅 11/01/26  
⚙️ PySpark Transformations Deep Dive

---

## 📖 Learn
- PySpark vs Pandas → scaling from single‑node analysis to distributed big data processing  
- Joins → combining datasets with inner, left, right, and outer joins  
- Window Functions → running totals, rankings, and cumulative analytics without collapsing data  
- UDFs → extending PySpark with custom Python logic for derived features  

---

## 🛠️ Tasks
1. Load full e-commerce dataset  
2. Perform complex joins  
3. Calculate running totals with window functions  
4. Create derived features  

---

## 🧑‍💻 Hands-On Work
- Loaded October + November e-commerce datasets into Databricks.  
- Created DataFrames for **purchase**, **cart**, and **view** events.  
- Aggregated brand-level totals and applied **window functions** (`dense_rank`) for ranking.  
- Joined purchase, cart, and view DataFrames to build a consolidated view.  
- Engineered **conversion rate features**:  
  - Cart → Purchase Conversion Rate  
  - View → Purchase Conversion Rate  
- Implemented a **UDF** to classify brands into performance categories.  

---

## 📊 Insights
- Top 10 brands by purchase revenue with conversion rates.  
- Top 10 brands by cart-to-purchase conversion efficiency.  
- Top 10 brands by view-to-purchase conversion efficiency.  
- UDF-based **Performance Flag** adds recruiter-friendly business context.  

---

## 🙌 Reflection
Day 3 highlighted how PySpark transformations, window functions, and UDFs together enable scalable, customizable analytics pipelines that connect raw event logs to actionable business metrics.

---

#DatabricksWithIDC #AIChallenge #PySpark #BigData #DataEngineering #Day3