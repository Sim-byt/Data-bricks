# Databricks notebook source
# MAGIC %md
# MAGIC Problem 5

# COMMAND ----------

import pandas as pd

output = []

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        output.append("FIZZBUZZ")
    elif number % 3 == 0:
        output.append("FIZZ")
    elif number % 5 == 0:
        output.append("BUZZ")
    else:
        output.append(str(number))

# Display results in a table in Databricks
df = pd.DataFrame({
    "Number": list(range(1, 101)),
    "Output": output
})

display(df)
