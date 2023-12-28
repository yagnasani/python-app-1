def loopExample1():
    for x in range (1,11):
       for y in range (1,(x+1)):
           print(x,end='')
       print()
         

#loopExample1()

def loopExample2():
    for x in reversed (range (0,11)):
        print(x)

#loopExample2()

def loopExample3():
    n = int(input("Enter number of rows:"))
    for i in range(1,n+1):
       print("-" * (n-i),end="") 
       print((str(i)+"-")*i)

#loopExample3()

#Write a program that will accept a range of number starting from 1. Display sum of all odd numbers
def sumOdd():
    n=int(input("Enter number range:"))
    total=0
    for x in range(1,n+1):
        if(x%2!=0):
            total=total+x

    print(total)

#sumOdd()


def multiplication_table(number):
    print(f"Multiplication Table of {number}:")
    for i in range(1, 11):  # Iterate from 1 to 10
        result = number * i
        print(f"{number} x {i} = {result}")

def main():

# Taking user input for the number
    user_number = int(input("Enter a number to print its multiplication table: "))

# Call the function with the user input number
    multiplication_table(user_number)

main()

        




    
