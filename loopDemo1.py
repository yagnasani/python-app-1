def displayNumbers1():
    n=1
    while n<=10:
        print(n)
        n=n+1

#displayNumbers1()

def displayNumbers2():
    n=1
    while True:
        print(n)
        n=n+1
        if n>10:
            break
    
#displayNumbers2()

def reverseNumber():
    n=int(input("Enter no "))
    s=0
    while(n>0):
       r=n%10
       s=s*10+ r     
       n=n//10
        
    print(s)
    

#reverseNumber()

def palindrome():
    n=int(input("Enter no "))
    m=n
    s=0
    while(n>0):
       r=n%10
       s=s*10+ r     
       n=n//10
        
    if m==s:
        print("palindrome")
    else:
        print("Not")

#palindrome()

def factorialNumber():
    n=int(input("Enter a number:"))
    fact=1
    while n>0:
        fact=fact*n
        n-=1

    print(fact)

factorialNumber()
        
        


