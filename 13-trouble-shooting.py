# print(the value of pi is : 3.14) syntax error

# print(25/0)          runtime error

                  #logical error 
#print ("hello name")
#print ("hello" ,name)

# table of any  no .
# a=input("enter the no.")
# b=input("enter the last value")
#i=1
# while i<=20:
 
#  print(int(a*i))
#  c+=c
 
# Function to print multiplication table
def print_table(number):
    i = 1
    print(f"Multiplication Table of {number}:")
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1

# Main program
if __name__ == "__main__":
    # Get input from the user
    while True:
        try:
            user_input = int(input("Enter a number to generate its multiplication table (0 to exit): "))
            if user_input == 0:
                print("Exiting the program.")
                break
            else:
                print_table(user_input)
        except ValueError:
            print("Please enter a valid number.")

