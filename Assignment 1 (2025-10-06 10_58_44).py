# Databricks notebook source
# MAGIC %md
# MAGIC Problem 1

# COMMAND ----------

Ph = 7
if Ph > 7:
    print('Basic')
elif Ph < 7:
    print('Acidic')
else:
    print('Neutral')

# COMMAND ----------

Ph = int(input('Enter a Ph value between 0 and 14:'))
if Ph > 7:
    print('Basic')
elif Ph < 7:
    print('Acidic')
else:
    print('Neutral')

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 2

# COMMAND ----------

import random
question = "Will I become a millionaire?"
answer = ""
random_number = random. randint (1, 9)
# print (random number)
if random_number == 1:
 answer = "Yes - definitely"
elif random_number == 2:
 answer = "It is decidedly so"
elif random_number == 3:
 answer = "Without a doubt"
elif random_number == 4: 
 answer = "Reply hazy, try again" 
elif random_number == 5:
 answer = "Ask again later"
elif random_number == 6:
 answer = "Better not tell you now"
elif random_number == 7:
 answer = "My sources say no"
elif random_number == 8:
 answer = "Outlook not so good"
elif random_number == 9:
 answer = "Very doubtful"
else :
 answer = "glitch"
print ("God :" , question)
print("Magic Ball:" , answer)


# COMMAND ----------

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
          

# COMMAND ----------

# MAGIC %md
# MAGIC Problem 4

# COMMAND ----------

House1 = 'Gryffindor'
House2 = 'Ravenclaw'
House3 = 'Hufflepuff'
House4 = 'Slytherin'

house_points = {
    House1: 0,
    House2: 0,
    House3: 0,
    House4: 0
}

choice = input('Do you like Dawn (1) or Dusk (2)? ')
if choice == '1':
    house_points[House1] += 1
    house_points[House2] += 1
elif choice == '2':
    house_points[House3] += 1
    house_points[House4] += 1
else:
    print('Wrong input')

choice = input('When I am dead, I want people to remember me as The Good (1) The Great (2) The Wise (3) or The Bad (4)? ')
if choice == '1':
    house_points[House1] += 2
elif choice == '2':
    house_points[House2] += 2
elif choice == '3':
    house_points[House3] += 2
elif choice == '3':
    house_points[House4] += 2
else:
    print('Wrong input')


choice = input('Which kind of instrument most pleases your ear? The violin (1) the trumpet (2) the piano (3) or the drum (4)? ')
if choice == '1':
    house_points[House1] += 4
elif choice == '2':
    house_points[House2] += 4
elif choice == '3':
    house_points[House3] += 4
elif choice == '4':
        house_points[House4] += 4
else:
        print('Wrong input')
print(house_points)
house = max(house_points, key=house_points.get)
print('You are in ' + house)




# COMMAND ----------

# MAGIC %md
# MAGIC Problem 5

# COMMAND ----------

number = int(
    input("Enter a number between 1 and 100:")
    )

if number * 3 == 0 and number * 5 == 0:
    print ("FizzBuzz")
elif number * 3 == 0:
    print ("Fizz")
elif number * 5 == 0:
    print ("Buzz")
else:
    print("Number")