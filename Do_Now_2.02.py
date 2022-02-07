'''
############################
Do Now 2.02
############################
----------------------------
Part 1
----------------------------
Open up the console. Type each line of the following code into the interactive editor:
 >>> 5 < 3 
 >>> 5 > 3
 >>> type(5 < 3)
 >>> type(5 > 3)
 >>> my_favorite_animal = "cats"
 >>> user_favorite_animal = input("What is your favorite animal? ")
 >>> my_favorite_animal == user_favorite_animal
In your notebook, answer the following
What does 5 < 3 evaluate to? false  
What is the type of 5 < 3? What does that stand for (should be familiar from Snap!)? bool
What is the difference between == and = ? == compares the two and displays true or false and = just sets the input to the line of code
What data type do you think my_favorite_animal == user_favorite_animal is? bool
----------------------------
Part 2
----------------------------
Open up the console. Type the following code into the interactive editor.
 >>> months_with_driving_permit = 6
 >>> age = 16
 >>> can_get_license = months_with_driving_permit >= 6 and age >= 16
 >>> print(can_get_license)
In your Notebook, add this to your notes in your notebook
What does 'and' do here? What type do you think can_get_license is? And makes it meet two requirements to be true. bool
Update the code to fit the new driving law: If you are over the age of 18 you don't need to have a permit
----------------------------
Part 3
----------------------------
Open up the console. Type the following code into the interactive editor.
>>> animal = 'mouse' 
>>> animal == 'cat' or 'dog'
>>> animal = 'mouse'
>>> animal == 'cat' or animal == 'dog'
In your notebook, continue answers to the following
What does = and == do here?
What is the difference between the two 'or' statements?  = sets an input to something and == compares the two
'''
months_with_driving_permit = 6
age = 16
can_get_license = months_with_driving_permit >= 6 and age >= 16 or age == 18 
print(can_get_license)