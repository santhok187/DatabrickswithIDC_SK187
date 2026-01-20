# 🚀 Day 10 – Databricks 14 Days AI Challenge  
📅 18/01/26  
⚡ Performance Optimization

---

## 📖 Learn
1. Query execution plans  
   - Parsed Logical plan  
   - Analyzed Logical plan  
   - Optimized Logical plan  
   - Physical plan  
2. Partitioning strategies  
3. OPTIMIZE & Z‑ORDER  
4. Caching techniques  

---

## 🛠️ Tasks
1. Analyze query plans  
2. Partition large tables  
3. Apply Z‑ORDER  
4. Benchmark improvements  

---

## 🧑‍💻 Hands-On Work
- Created two versions of tables: partitioned vs non‑partitioned.  
- Benchmarked queries:
  - Non‑partitioned → scanned all files.  
  - Partitioned → reduced file scans by ~90%.  
- Applied **Z‑ORDER** on `user_id`:
  - Before → 38+ files read.  
  - After → only 1 file read (98% filtered).  
- Demonstrated caching techniques (conceptual, limited by free compute).  

---

## 📊 Insights
- **Partitioning** improves query efficiency by pruning irrelevant data.  
- **Z‑ORDER** optimizes data layout for high‑cardinality queries.  
- **Caching** accelerates repeated queries by storing results in memory.  
- **Execution plans** provide transparency into Spark’s optimization process.  

---

## 🙌 Reflection
Day 10 highlighted how **performance optimization** is critical for production workloads.  
By combining partitioning, Z‑ORDER, and caching, queries become **faster, cheaper, and more scalable**.

---

#DatabricksWithIDC #AIChallenge #Day10 #PerformanceOptimization #DeltaLake #BigData