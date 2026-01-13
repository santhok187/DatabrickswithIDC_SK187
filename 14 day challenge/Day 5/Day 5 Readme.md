# 🚀 Day 5 – Databricks 14 Days AI Challenge  
📅 14/01/26  
⚙️ Delta Lake Advanced: Version Control & Optimization

---

## 📖 Learn
- Time travel (version history)  
- MERGE operations (upserts)  
- OPTIMIZE & ZORDER  
- VACUUM for cleanup  

---

## 🛠️ Tasks
1. Implement incremental MERGE  
2. Query historical versions  
3. Optimize tables  
4. Clean old files  

---

## 🧑‍💻 Hands-On Work
- Created new Delta datasets and applied **MERGE** for incremental upserts.  
- Queried historical versions using **time travel** (`versionAsOf`, `timestampAsOf`).  
- Applied **OPTIMIZE** to reduce 156 fragmented files down to 26 compact files.  
- Used **ZORDER** on `brand` and `user_id` to reduce query scans from 129 files → 26 → 4.  
- Ran **VACUUM** with custom retention to clean obsolete files.  

---

## 📊 Insights
- **Time travel** enables rollback and auditing.  
- **MERGE** ensures idempotent ingestion.  
- **OPTIMIZE & ZORDER** drastically improve query performance and reduce file scans.  
- **VACUUM** keeps storage lean and efficient.  

---

## 🙌 Reflection
Day 5 highlighted how Delta Lake goes beyond governance — it enables **performance tuning and lifecycle management**.  
With time travel, MERGE, OPTIMIZE, ZORDER, and VACUUM, pipelines become **auditable, efficient, and production‑ready**.

---

#DatabricksWithIDC #AIChallenge #PySpark #BigData #DeltaLake #Day5