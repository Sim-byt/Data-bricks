# Databricks notebook source
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
