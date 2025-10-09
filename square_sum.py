# Databricks notebook source
# MAGIC %md
# MAGIC Problem 6

# COMMAND ----------

number = int(input("Enter your number:"))
total = 0
for i in range(1, number+1): 
 total += i * i
 print(total)
