def factorial_of_number(input_number):
    #base case
    if input_number == 0:
        return 1
    return input_number * factorial_of_number(input_number-1) #call the function untill it reaches the base case and return the result 
input_number = int(input("Enter the number:"))
print(factorial_of_number(input_number= input_number))



