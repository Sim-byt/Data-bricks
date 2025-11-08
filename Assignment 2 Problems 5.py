# Databricks notebook source
# MAGIC %md
# MAGIC Assignment 2 (Problem 1)

# COMMAND ----------

import numpy as np
arr = np.array([1,2,3,5,0])
print(arr)
if np.all(arr > 0):
    print("All elements are non zero")
else :
    print("All elements are not non zero")

# COMMAND ----------

import numpy as np
arr = np.array([0,0,0,0])
print("Array:", arr)
print("any element is non zero")

# COMMAND ----------

import numpy as np
arr = np.array([56, -2, 7])
print("Array:", arr)
print("Bytes:", arr.nbytes)
print("item size:", arr.itemsize)
print("size:", arr.shape)

# COMMAND ----------

import numpy as np
arr = np.zeros(10)
print(arr)

# COMMAND ----------

import numpy as np
arr = np.ones(6)
print(arr)

# COMMAND ----------

import numpy as np
arr = np.full(12, 3)
print(arr)

# COMMAND ----------

import numpy as np
arr = np.arange(8, 21)
print(arr)

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 2

# COMMAND ----------

import numpy as np

egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])

egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])

egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])
avg1 = np.average(egg_carton1)
avg2 = np.average(egg_carton2)
avg3 = np.average(egg_carton3)
print("Average fresh carton 1: ", avg1)
print("Average fresh carton 2: ", avg2)
print("Average fresh carton 3: ", avg3)
cartons = (avg1, avg2, avg3)
most_fresh = np.argmax(cartons) + 1
least_fresh = np.argmin(cartons) + 1
print("carton {} is the most fresh".format(most_fresh))
print("carton {} is the least fresh".format(least_fresh))

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 3

# COMMAND ----------

import numpy as np

comet_visible_from_Earth = 75
last_seen = 1986
next_seen = last_seen + 75
print("Next time comet will be visible from Earth: ", next_seen)
comet = np.arange(1986, 3000, 75)
print("Comet will be visible from Earth in these years: ", comet)

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 4

# COMMAND ----------

import numpy as np
import pandas as pd

passengers = np.array([
 [1, 0, 3, 22],
 [2, 1, 1, 38],
 [3, 1, 3, 26],
 [4, 1, 1, 35],
 [5, 0, 3, 35],
 [6, 0, 3, 18],
 [7, 0, 1, 54],
 [8, 0, 3, 2],
 [9, 1, 3, 27],
[10, 1, 2, 14],
[11, 1, 3, 4],
[12, 1, 1, 58],
[13, 0, 3, 20],
[14, 0, 3, 39],
[15, 0, 3, 14],
[16, 1, 2, 55],
[17, 0, 3, 2],
[18, 1, 2, 12],
[19, 0, 3, 31],
[20, 1, 3, 8],
[21, 0, 2, 35],
[22, 1, 2, 34],
[23, 1, 3, 15],
[24, 1, 1, 28],
[25, 0, 3, 8],
[26, 1, 3, 38],
[27, 0, 3, 2],
[28, 0, 1, 1],
[29, 1, 3, 5],
[30, 0, 3, 18],
[31, 0, 1, 40],
[32, 1, 1, 70],
[33, 1, 3, 33],
[34, 0, 2, 66],
[35, 0, 1, 28],
[36, 0, 1, 42],
[37, 1, 3, 5],
[38, 0, 3, 18],
[39, 0, 3, 18],
[40, 1, 3, 14],
[41, 0, 3, 40],
[42, 0, 2, 27],
[43, 0, 3, 29],
[44, 1, 2, 0],
[45, 1, 3, 19],
[46, 0, 3, 33],
[47, 0, 3, 14],
[48, 1, 3, 22],
[49, 0, 3, 41],
[50, 0, 3, 18]
])
df = pd.DataFrame(passengers, columns=['PassengerId', 'Survived', 'Passenger class', 'Age'])
print(df)
print("size:", df.shape)
avg_age = np.average(df['Age'])
print("Average age:", avg_age)
oldest_passenger_number = df.loc[df['Age'].idxmax(), 'PassengerId']
youngest_passenger_number = df.loc[df['Age'].idxmin(), 'PassengerId']
print("Oldest passenger number:", oldest_passenger_number)
print("Youngest passenger number:", youngest_passenger_number)
survival_rate = df['Survived'].mean() * 100
print("Survival rate:", survival_rate)
survival_by_class = df.groupby('Passenger class')['Survived'].mean() * 100
print("Survival rate by class:")
print(survival_by_class)


# COMMAND ----------

# MAGIC %md
# MAGIC Problem 5
# MAGIC Data Dictionary method

# COMMAND ----------

import pandas as pd
Method = "Data_Dictionary_Method: Data by coloumn"
print(Method)
Contacts_data = {"name": ["John", "Jane", "Bob", "Alice"],
                 "age": [25, 30, 35, 40],
                 "phone": ["123-456-7890", "987-654-3210", "555-555-5555", "111-222-3333"],
                 "astrological_sign": ["Aquarius", "Pisces", "Aries", "Taurus"]}
contacts = pd.DataFrame(Contacts_data)
display(contacts)

