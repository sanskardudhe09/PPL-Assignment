#try block
try:
    a = 10
    b = 0
    print("Result of Division is " +str(a/b))
except:
    print("You have divided a number by zero which is not allowed")
print("Handling ZeroDivisionError and ValueError")
#try block
try:
    a = int(input("Enter numerator number:"))
    b = int(input("Enter denominator value:"))
    print("Result of Division :" +str(a/b))
#except block handling division by zero
except(ZeroDivisionError):
    print("You have divided a number by zero which is not allowed ")
#except block to handle value error
except(ValueError):
    print("You must enter an integer value")
#using finally block
finally:
    print("Code execution is over")
print("Handling IndexError and IOError")
#try block
a = [1,2,3]
try:
    print("Second element =%d" %a[1])
    print("Fourth element =%d" %a[3])
except IndexError:
    print("An error occured")
#handling IOError
try:
    fileptr = open("file.txt", "r")
except IOError:
    print("File not found")
else:
    print("File opened successfully")
    fileptr.close()


#Program to raise exceptions
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise