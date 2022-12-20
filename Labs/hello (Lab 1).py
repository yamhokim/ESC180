# Problem 1: Your First Python Program
print("Hello, Python") # Prints "Hello, Python"

# Problem 2: Greetings
greeting = "Hello, "
name = "Yoonho Kim" # The name is stored in a variable
greeting = greeting + name
print(greeting) # Prints out hello and the name

# Problem 3: Variables
# The two name values are stored as variables which are then used in the print statement
name1 = "Hermione Granger"
name2 = "Harry Potter"
print("Hello, " + name1 + " and " + name2 + ". Your names are " + name1 + " and " + name2 + ". Hi there. Your names are still " + name1 + " and " + name2 + ".")

# Problem 4: Tracing
name1 = "Hermione Granger"
name2 = "Harry Potter"
print("Hello, " + name1 + " and " + name2 + ". Your names are " + name1 + " and " + name2 + ". Hi there. Your names are still " + name1 + " and " + name2 + ".")

# Changes the values of the two name variables to these two new names
name1 = "Prof. Cluett"
name2 = "Prof. Thywissen"

# Problem 5: More Greetigns
greetee = input() # Asks for user input
# Using if/else statements, if the name is "Lord Voldemort", the program returns "I'm not talking to you"
if greetee == " Lord Voldemort":
    print("I'm not talking to you.")
# Any other name will return the normal greeting
else:
    print("Hello", greetee, sep=", ")