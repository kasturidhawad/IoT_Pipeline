# Databricks notebook source
# /// script
# [tool.databricks.environment]
# base_environment = "databricks_ai_v5"
# environment_version = "5"
# ///
data = [
    (101, 1, "Completed", 2500.0),
    (102, 2, "Pending", 1500.0),
    (103, 1, "Completed", 3200.0),
    (104, 3, "Cancelled", 800.0),
    (105, 2, "Completed", 2100.0)
]

columns = ["order_key", "customer_id", "status", "amount"]

df = spark.createDataFrame(data, columns)

display(df)

# COMMAND ----------

from pyspark.sql.functions import count, sum

summary_df = (
    df.groupBy("customer_id")
      .agg(
          count("order_key").alias("total_orders"),
          sum("amount").alias("total_amount")
      )
)

display(summary_df)