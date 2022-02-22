'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''
name = input("Can you please tell me your name? > ")
age = int(input ("Can you please tell me your age? > "))
year_turn_100 = 2022 - age + 100
number = int(input("Please enter a number 1-100 > "))
message = f"You will turn 100 in the year {year_turn_100} \n"
print(number * message)

