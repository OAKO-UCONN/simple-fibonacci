n = input("Enter a number: ")
print("Number to calculate is " + n)
print(type(n))

#conversion to float
n = float(n)


#fibonacci calculation
def fibonacci(n):
    if n<2:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

#convert back to a string.
n = str(n)
print("n = " + n)
