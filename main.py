# Ethan lawrence
# September 11 2024
# String Manipulation

# Part 1
# Define a variable and assign it the string that is your last name
# Then tell Python to print the value assigned to the variable

lastName = 'Lawrence'
print(len(lastName))


# Part 2
# Use the len( ) function to get the number of characters in your first name
# Assign the length of your first name to a variable named num_characters
# Have Python print the value stored in the num_characters variable

firstName = 'Ethan'
num_characters = len(firstName)
print(num_characters)



# Part 3
# Use the input( ) and len( ) functions to prompt (ask) the user to enter their last name
# Then have Python print the length (number of characters) in the last name

userLastName = input('Enter your last name:     ')
print(len(userLastName))


# Part 4
# Assign the name of the city you live in to a variable called city
# Use square bracket notation to extract (grab) and print the THIRD character in the name of your city

city = 'Traverce City'
print(city[2])



# Part 5
# Assign the string 'Career Tech' to a variable called school
# Use square brackets and a starting and ending index number to print (display) only the characters 'Tec' on your screen when you run your script

school = 'Career Tech'
print(school[7:10])



# Part 6
# Assign the name of your favorite superhero or movie character to a variable
# Use the Python upper( ) string method to print the name of your superhero/movie character in uppercase 
# Also use the Python lower( ) string method to print the name of your superhero/movie character in lowercase 

superhero = 'hero'
print(superhero.lower())
print(superhero.upper())



# Part 7
# Assign this quote to a variable named message: 'One of Elizabeth's favorite desserts is blueberry cobbler.'
# Use the escape character to tell Python to ignore the apostrophe after Elizabeth and continue reading until it reaches the end of the string
# Then print the string stored in the message variable

message = 'One of Elizabeth\'s favorite desserts is blueberry cobbler.'
print(message)