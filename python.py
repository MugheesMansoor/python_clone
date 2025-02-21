#palindrome  code 
"""def is_palindrome_number(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10  # Get the last digit
        reverse = reverse * 10 + digit  # Build the reversed number
        n = n // 10  # Remove the last digit

    return original == reverse

# Test examples
user=int(input("enter a no. "))
print(is_palindrome_number(user))  
"""
#  inheritance 
"""
# Parent class
class janwar:
    def __init__(self, name):
        self.name = name  # Set the name of the animal

    def speak(self):
        print("janwar makes a sound")  # Generic sound for any animal

# Child class that inherits from Animal
class Dog(janwar):
    def speak(self):
        print(f"{self.name} says Woof!")  # Specific sound for a dog

# Create an object of the Dog class
my_dog = Dog("Buddy")
my_dog.speak()  # This will call the speak method of the Dog class
"""
#code  of  shollow copy & deep copy ...
"""
import copy

# Original list with nested list
original_list = [1, 2, [3, 4]]

# Creating a shallow copy
shallow_copy = copy.copy(original_list)

# Creating a deep copy
deep_copy = copy.deepcopy(original_list)

# Modifying the nested list in the shallow copy
shallow_copy[2][0] = 99

# Modifying the nested list in the deep copy
deep_copy[2][1] = 77

# Print all three lists
print("Original List:", original_list)
print("Shallow Copy: ", shallow_copy)
print("Deep Copy:   ", deep_copy)

"""