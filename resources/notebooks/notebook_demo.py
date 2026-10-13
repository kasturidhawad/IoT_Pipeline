# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
df = spark.range(10)


display(df)