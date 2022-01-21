#Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.#
print('Question1')

# giving value to input_string.
input_string = 'Python is a case sensitive language'

# printing the length of input_string.
print("\nPart a ")
print(f"Length of Input String = {len(input_string)}")

# printing the input_string in reverse order.
print("\nPart b")
print(input_string[::-1])


# slicing and printing the input_string.
print("\nPart c")
sliced_string = input_string[10:26]
print(sliced_string)
print


# replacing and printing.
print("\nPart d")
new_string = input_string.replace("a case sensitive", "object oriented")
print(new_string)


# printing index of "a" from input_string.
print("\nPart e")
print(input_string.index("a"))


# replacing blank white spaces with empty string.
print("\nPart f")
print(input_string.replace(" ", ""))


####################################################################################

print("Question 2\n")

# Initializing variables.
name = "Mayank Jindal"
SID = "21105028"
department = "ECE"
CGPA = "10"

# Printing statements in the given format.
print(f"Hey, {name.title()} here! \nMy SID is {SID} \nI am from {department} and my CGPA is {CGPA}")

#####################################################################################


print("Question 3")


a = 56
b = 10

print(" a&b : ", a & b)
print(" a|b : ", a | b)
print(" a^b : ", a ^ b)

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)
# Right shift a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)


##################################################################################


print("Question 4")

# taking input of 3 numbers from the user.
a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))

#finding the highest no.
if a > b:
    if a > c:
        highest_number = a
    else:
        highest_number = c

if b > a:
    if b > c:
        highest_number = b
    else:
        highest_number = c


print(f"Highest no. = {highest_number}")


##################################################################################


print("Qustion 5")

# taking input string from the user.
input_string = input("Enter input string: ")

if "name" in input_string:
    print("Yes")
else:
    print("No")

################################################################################


print("Question 6\n")

# taking input of 3 lengths from the user.
a = int(input("Enter 1st length : ")) 
b = int(input("Enter 2nd length : "))
c = int(input("Enter 3rd length : "))

# checking condition for triangle.
if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")


#########################################################################
