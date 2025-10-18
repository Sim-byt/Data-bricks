# Databricks notebook source
# MAGIC %md
# MAGIC Problem 7

# COMMAND ----------

books_list = ['Harry Potter', '1984' , 'The Fault in Our Stars' , 'The Mom Test', 'Life in Code']
books_list.insert(5, 'Pachinko')
books_list.remove('The Fault in Our Stars')
books_list.pop(1)
print(books_list)


# COMMAND ----------

# MAGIC %md
# MAGIC Problem 8

# COMMAND ----------

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']
item_to_find = ('CGA')
item_found = False
for item in dna_sequence:

  if item == item_to_find:
    item_found = True
    break
if item_found:
    print('item_found')
else:
  print('item_not_found')

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 9

# COMMAND ----------

import random
fortune = ""
random_number = random. randint (1, 8)
# print (random number)
if random_number == 1:
 fortune = "Don't pursue happiness - create it."
elif random_number == 2:
 fortune = "All things are difficult before they are easy."
elif random_number == 3:
 fortune = "The early bird gets the worm, but the second mouse gets the cheese."
elif random_number == 4: 
 fortune = "Someone in your life needs a letter from you." 
elif random_number == 5:
 fortune = "Don't just think."
elif random_number == 6:
 fortune = "Act! Your heart will skip a beat."
elif random_number == 7:
 fortune = "The fortune you search for is in another cookie."
elif random_number == 8:
 fortune = "Help! I'm being held prisoner in a Chinese bakery!"
else :
 fortune = "glitch"
print ("fortune cookie says :" , fortune)

# COMMAND ----------

import random 
fortunes = ["Don't pursue happiness - create it.",
"All things are difficult before they are easy.",
"The early bird gets the worm, but the second mouse gets the cheese.",
"Someone in your life needs a letter from you.",
"Don't just think.",
"Act! Your heart will skip a beat.",
"The fortune you search for is in another cookie.",
"Help! I'm being held prisoner in a Chinese bakery!"]
print(random.choice(fortunes))  

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 10

# COMMAND ----------

distance = int(input("Enter distance in kilometers: "))
distance_to_miles = distance / 1.609
print(distance_to_miles)

# COMMAND ----------

kilometers = 10000
distance_to_miles = kilometers / 1.609
print(distance_to_miles)

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 11

# COMMAND ----------

a = 100
b = 25
def add(a, b):
 answer = a+b
 print(answer)
def subtract(a, b):
 answer = a-b
 print(answer)
def multiply(a, b):
 answer = a*b
 print(answer)
def divide(a, b):
 answer = a/b
 print(answer)
def exp(a, b):
 answer = a**b
 print(answer)
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
exp(a, b)

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 12

# COMMAND ----------

x = 34.68
def price_at(x):
    print(x)
price_at(x)

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def max_price(a, b):
 max_price = max(stock_prices)
 print(max_price)
def min_price(a, b):
 min_price = min(stock_prices)
 print(min_price)
def max_day(a, b):
 max_day = days[stock_prices.index(max(stock_prices))]
max_price(a, b)
min_price(a, b)

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 13

# COMMAND ----------

items = {
    1: '🍔 Cheeseburger',
    2: '🍟 Fries',
    3: '🥤 Soda',
    4: '🍦 Ice Cream',
    5: '🍪 Cookie'
}

def get_item(number):
    return items.get(number)

welcome = "Welcome to the Mcdonalds!"
print(welcome)
item_number = int(input("Enter a number between 1 and 5: "))
item = get_item(item_number)
if item:
    print(item)
else:
    print('Invalid input')