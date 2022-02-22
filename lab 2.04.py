'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction: a and d                                           
    actual: a and d

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction:b
    actual: c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: e
    actual: e

Example 4
    a  =['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: a  =['a', 'b', 'c', 'haha', 'e']
    actual: a  =['a', 'b', 'c', 'haha', 'e']

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.

3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a? print(a[0],[0])
'''
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','bagles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1


user_input = input('Do you like sweet foods? ')
if user_input == 'y':
    score[1] = score[1] + 1
    score[3] = score[3] + 1
    score[0] += 1


user_input = input('Do you like animal products? ')
if user_input == 'y':
    score[2] += 1
    score[4] += 1


user_input =input('Do you like food made with batter? ')
if user_input == 'y':
    score[1] += 1
    score[5] += 1


user_input = input("Do you like food normally served with syrup? ")
if user_input == 'y':
    score[1] += 1
    score[3] += 1


user_input = input('Do you like foods that came from chickens? ')
if user_input == 'y':
    score[4] += 1


user_input = input('Do you like meat for breakfast? ')
if user_input == 'y':
    score[2] += 1


user_input = input('Do you like foods that can be served with sprinkles on top? ')
if user_input == 'y':
    score[0] += 1
    score[1] += 1


    
fav_food_index = score.index(max(score))
print(f"Your favorite food was: {food[fav_food_index]}")

food.pop(fav_food_index)
score.pop(fav_food_index)

fav_food_index = score.index(max(score))
print(f"Your second favorite food was: {food[fav_food_index]}")