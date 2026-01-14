# 🚀 Day 6 – Databricks 14 Days AI Challenge  
📅 15/01/26  
⚙️ Medallion Architecture: Bronze → Silver → Gold

---

## 📖 Learn
- Bronze (raw) → Silver (cleaned) → Gold (aggregated)  
- Best practices for each layer  
- Incremental processing patterns  

---

## 🛠️ Tasks
1. Design 3‑layer architecture  
2. Build Bronze: raw ingestion  
3. Build Silver: cleaning & validation  
4. Build Gold: business aggregates  

---

## 🧑‍💻 Hands-On Work
### Batch Processing (Full Refresh)
- Ingested raw CSV files into **Bronze tables**.  
- Applied cleaning, deduplication, and validation to build **Silver tables**.  
- Built **Gold aggregates**:
  - Recent 20 products viewed per user  
  - Products in user carts  

### Stream Processing (Incremental)
- Defined schema and checkpointing for streaming ingestion.  
- Loaded streaming data into **Bronze stream tables**.  
- Applied deduplication with watermarking to build **Silver stream tables**.  
- Built **Gold aggregates**:
  - Recent views per user  
  - Cart products per user  
  - Popular products by category/brand  
  - Co‑view product pairs for recommendations  

---

## 📊 Insights
- **Bronze → Silver → Gold** ensures layered governance and clarity.  
- **Batch pipelines** provide full refresh dashboards.  
- **Streaming pipelines** enable real‑time recommendations and popularity tracking.  
- **Co‑view pairs** create the foundation for collaborative filtering recommendations.  

---

## 🙌 Reflection
Day 6 highlighted how the **Medallion Architecture** supports both **batch and streaming pipelines**. This layered approach ensures clean, reliable data at each stage and delivers **business‑ready insights** for dashboards and recommendation systems.

---

#DatabricksWithIDC #AIChallenge #PySpark #BigData #MedallionArchitecture #Day6