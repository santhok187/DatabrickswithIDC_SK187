# 🚀 Day 2 – Databricks AI Challenge  
⚙️ Spark Architecture Fundamentals

## 📖 Introduction
Apache Spark is a **distributed compute engine** designed for large-scale data processing. It operates on a **distributed processing framework**, enabling high performance and scalability.

---

## 🔄 ELT vs ETL
Spark supports **ELT (Extract, Load, Transform)** workflows.  
Instead of repeatedly transforming data during each load, Spark loads data once and performs transformations **in memory** across a distributed cluster.  
This makes it significantly **faster than traditional ETL** processes.

---

## 🧩 Core APIs
- **RDD (Resilient Distributed Dataset):** The fundamental Spark abstraction for distributed collections of raw data.  
- **DataFrame:** An evolution of RDD that combines schema information with distributed data, enabling **metadata awareness** and integration with **Spark SQL** for high-level query optimization.

---

## 🏗️ Architecture
- **Driver:** Creates the `SparkSession`, builds the execution plan, and schedules tasks.  
- **Executors (Workers):** JVM processes on worker nodes where computation occurs.  
- **Cluster Manager:** Allocates CPU and memory resources across the cluster. Spark can run on **YARN, Mesos, or Kubernetes**.  
- **DAG (Directed Acyclic Graph):** Represents the **lineage of execution**. Spark converts user operations into a DAG of stages and tasks.  
  - **Jobs:** Created by actions (e.g., `count`, `show`).  
  - **Stages:** Subdivisions of jobs based on shuffle boundaries.  
  - **Tasks:** Smallest execution units, run in parallel on executors.  
  - DAG ensures **optimization, fault tolerance, and consistency** by tracking lineage and recomputing lost partitions if failures occur.

---

## ⚡ Query Optimization
- **Adaptive Query Execution (AQE):** Dynamically optimizes query execution plans based on runtime statistics.  
- **Caching:** Stores data in memory (serialized or deserialized) for faster reuse.  
- **Locality:**  
  - **Node locality:** Data processed on the same node where it resides.  
  - **Process locality:** Data already in memory is processed directly.  

---

## 🔄 Joins
- Broadcast Join  
- Shuffle Sort-Merge Join  
- Broadcast Hash Join  

---

## 🧠 Memory Management & Execution Plans
Spark uses a multi-stage optimization pipeline:  
1. **Parsed Logical Plan (Unresolved):** Syntax validation.  
2. **Analyzed Logical Plan (Resolved):** Schema and data validation.  
3. **Optimized Logical Plan:** Reorganizes operations for efficiency.  
4. **Physical Plan:** Executes operations on actual data.  

---

## 🕒 Lazy Evaluation
- **Transformations** (e.g., `select`, `filter`, `agg`) are not executed immediately.  
- Spark waits for **actions** (e.g., `count`, `show`) to trigger execution.  
- This enables Spark to **optimize workflows before execution**.  

---

## 📓 Notebook Magic Commands
- `%sql` → Run SQL queries directly.  
- `%python` / `%pyspark` / `%scala` → Switch languages in notebooks.  
- `%fs` → Navigate the Databricks File System (DBFS).  

---

## 🙌 Reflection
Day 2 helped me understand how Spark’s **DAG-based execution, lazy evaluation, and query optimization** make it both **efficient and resilient**. These fundamentals are the backbone of scalable AI and data engineering workflows.  

#Databricks #ApacheSpark #AIChallenge #Day2 #BigData #CloudNative #DataEngineering