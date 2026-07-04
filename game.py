import random 
secret=random.randint(1,100)
attempt=0
max_attempts=5

while attempt<max_attempts:
    try:
        guess=int(input("enter number between 1-100: "))
        attempt+=1
        if guess<secret:
            print("very low")
        elif guess>secret:
            print("too high")
     
        else:
            print("you won buddy and the correct answer is,{attempt}")
    except ValueError:
            print("print only the numbers")
            break

if attempt == max_attempts:
    print(" OOPS! you have reached the limit") 
