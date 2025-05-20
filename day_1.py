
# 1. Write a program to accept 5 numbers from user and display the largest and smallest
#    number using while loop.

'''count = 1

largest = None
smallest = None

while count <= 5:

    num = int(input("Enter a number:"))

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num


    count+=1

print("Largest Number is ",largest)
print("Smallest Number is ",smallest) '''
    

# Similar practice program

'''count = 1


num_list = []

while count <= 6:
    num = int(input("Enter a number:"))
    num_list.append(num)

    count+=1

    num_list.sort()

print("Numbers list ",num_list)
print("Second largest number:",num_list[-2])
print("Second smallest number:",num_list[1])'''

# 2. Write a Python program that determines the largest of
# three numbers using if-else statements.

'''n1 = int(input("Enter a number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))

if n1 > n2 and n1 > n3:
    print(n1,"is largest.")

elif n2 > n1 and n2 > n3:
    print(n2,"is largest.")

else:
    print(n3,"is largest")'''


# 3. Write a Python function to find the maximum of three numbers.

def max_num(a,b,c):

     if a > b and a > c:
         return a

     elif b > a and b > c:
         return b

     else :
         return c


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

large_num = max_num(a,b,c)
print("Maximum number is ",large_num)


    
