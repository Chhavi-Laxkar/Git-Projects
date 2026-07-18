# Step 1 - Create functions :
def addition(num1 , num2):
    return num1 + num2
def subtraction(num1 , num2):
    return num1 - num2
def multiplication(num1 , num2):
    return num1 * num2
def division(num1 , num2):
    return num1 / num2
def average(num1 , num2):
    return (num1 + num2) / 2

# Step 2 - User input :
print("Please Select One Operations :\n"
       "1.Addition\n"
       "2.Subtraction\n"
       "3.Multiplication\n"
       "4.Division\n"
       "5.Average\n")


select = int(input("Select operations from 1,2,3,4,5 :"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Step 3 - Print result
if select == 1 :
    print("Addition =", addition(num1 , num2))
elif select == 2 :
    print("Subtraction =", subtraction(num1 , num2))    
elif select == 3 :
    print("Multiplication =", multiplication(num1 , num2))
elif select == 4 :
    print("Division =", division(num1 , num2))
elif select == 5 :
    print("Average =", average(num1 , num2))    
else :
    print("Invalid input")



