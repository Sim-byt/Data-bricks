# Databricks notebook source
# MAGIC %md
# MAGIC Problem 3

# COMMAND ----------

Height = int(input('Enter your height in cms:'))
Credits = int(input('Enter your number of credits:'))
if Height >= 137 and Credits >= 10:
    print('Enjoy the ride!')
elif Height < 137 and Credits >= 10:
    print ('You are not tall enough to ride.')
elif Height >= 137 and Credits < 10:
    print('You do not have enough Credits.')
else:
    print('You have not met either requirement.')