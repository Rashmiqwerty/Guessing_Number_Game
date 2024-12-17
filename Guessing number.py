import random
rd=random.randint(7,9)
guess=0
c=0
count=1

while guess!=rd and guess!='exit' and count<=8:
    guess=input("Enter a guess number: ")
    if count==1:
        print("You have only 8 tries.....")
    if guess=='exit':
        break
    
    guess=int(guess)
    c+=1

    if guess<rd:
        print("Two low")
    elif guess>rd:
        print("Two high")
    else:
        print("Right")
        print("You took only ",c,"tries!")
    count+=1
    print("You have done your ",count,"tries..")
    
    if count==9:
        print("Sorry your tries are over")
input()
