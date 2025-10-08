# Databricks notebook source
# MAGIC %md
# MAGIC Problem 1

# COMMAND ----------

Ph = int(input('Enter a Ph value between 0 and 14:'))
if Ph > 7:
    print('Basic')
elif Ph < 7:
    print('Acidic')
else:
    print('Neutral')