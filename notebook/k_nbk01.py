# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT "I'm running SQL!"

# COMMAND ----------

# Notebook_A has four commands:
name = "John"
print(f"Hello {name}")
%run ./k_nbk02
print(f"Welcome back {full_name})


# COMMAND ----------

name = "John"
print(f"Hello {name}")
full_name = f"{name} Doe"
print(f"Welcome back {full_name}")

# COMMAND ----------

# MAGIC %run ./ExampleSetupFolder/example-setup

# COMMAND ----------

# MAGIC %md # Header
# MAGIC   - Bullet 1
# MAGIC   - Bullet 2

# COMMAND ----------


