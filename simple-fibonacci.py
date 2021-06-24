number = input("Enter a number: ")
print("Number to calculate is " + number)
print(type(number))

#conversion to float
n = float(number)


#fibonacci calculation
def fibonacci(n):
    if n<2:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

